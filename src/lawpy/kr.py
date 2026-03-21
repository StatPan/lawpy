"""Korean law adapter."""

import os

import httpx
import xmltodict

from lawpy.client import LawClient
from lawpy.exceptions import APIError, NotFoundError, ParseError
from lawpy.models import Article, Item, Law, LawDetail, Paragraph, SubItem


class KoreanLawClient(LawClient):
    """Client for Korean National Law Information Center API."""

    BASE_URL = "https://www.law.go.kr/DRF/lawSearch.do"

    def __init__(self, api_key: str | None = None, timeout: int = 30) -> None:
        """Initialize Korean law client.

        Args:
            api_key: API key from National Law Information Center (email ID).
                     If not provided, reads from LAWPY_API_KEY environment variable.
            timeout: Request timeout in seconds

        Raises:
            ValueError: If api_key is not provided and LAWPY_API_KEY env var is not set
        """
        if api_key is None:
            api_key = os.environ.get("LAWPY_API_KEY")
            if api_key is None:
                msg = "api_key must be provided or set LAWPY_API_KEY environment variable"
                raise ValueError(msg)

        super().__init__(
            api_key=api_key,
            base_url=self.BASE_URL,
            timeout=timeout,
        )

    def search_laws(
        self,
        query: str,
        target: str = "law",
        exact_match: bool = False,
        type: str = "XML",
        page: int = 1,
        per_page: int = 100,
    ) -> list[Law]:
        """Search for Korean laws.

        Args:
            query: Search query
            target: Search target ('law' for laws, 'prec' for precedents)
            exact_match: Whether to match exact phrase
            type: Response type ('XML' or 'JSON')
            page: Page number (starts from 1)
            per_page: Number of results per page

        Returns:
            List of Law objects

        Raises:
            APIError: If the API request fails
            ParseError: If the response cannot be parsed
        """
        params = {
            "OC": self.api_key,
            "target": target,
            "type": type,
            "query": query,
            "exact": "Y" if exact_match else "N",
            "display": per_page,
            "page": page,
        }

        try:
            response = self._client.get(self.BASE_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise APIError(
                f"HTTP error: {e.response.status_code}", status_code=e.response.status_code
            ) from e
        except httpx.RequestError as e:
            raise APIError(f"Request error: {e}") from e

        try:
            data = xmltodict.parse(response.content)
            if not data or data.get("LawSearch") is None:
                return []

            law_search_data = data.get("LawSearch", {})
            laws_data = law_search_data.get("law", [])

            if laws_data is None:
                return []

            if not isinstance(laws_data, list):
                laws_data = [laws_data]

            laws = []
            for law_data in laws_data:
                law = Law(
                    law_id=law_data.get("법령ID", ""),
                    law_name=law_data.get("법령명한글", ""),
                    law_no=law_data.get("법령일련번호", ""),
                    promulgation_date=law_data.get("공포일자"),
                    enforcement_date=law_data.get("시행일자"),
                )
                laws.append(law)

            return laws

        except Exception as e:
            raise ParseError(f"Failed to parse response: {e}") from e

    def get_law_detail(
        self,
        law_id: str | None = None,
        mst: int | None = None,
        article_number: int | None = None,
        language: str = "KO",
        output_type: str = "XML",
    ) -> LawDetail:
        """Get detailed information and full text of a specific law.

        Args:
            law_id: The ID of the law (e.g., '009682'). Either law_id or mst must be provided.
            mst: The master number of the law (lsi_seq value). Either law_id or mst must be provided.
            article_number: Specific article number to retrieve (default: all articles)
            language: Language type ('KO' for Korean, 'ORI' for original)
            output_type: Output type ('HTML', 'XML', or 'JSON')

        Returns:
            LawDetail object containing detailed law information and full text

        Raises:
            ValueError: If neither law_id nor mst is provided
            APIError: If the API request fails
            ParseError: If the response cannot be parsed
        """
        if law_id is None and mst is None:
            msg = "Either law_id or mst must be provided"
            raise ValueError(msg)

        params: dict[str, str | int | None] = {
            "OC": self.api_key,
            "target": "law",
            "type": output_type,
            "LANG": language,
        }

        if law_id is not None:
            params["ID"] = law_id
        if mst is not None:
            params["MST"] = mst
        if article_number is not None:
            jo_str = f"{article_number:04d}00"
            params["JO"] = jo_str

        url = "http://www.law.go.kr/DRF/lawService.do"

        try:
            response = self._client.get(url, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise NotFoundError("Law not found", status_code=404) from e
            raise APIError(
                f"HTTP error: {e.response.status_code}", status_code=e.response.status_code
            ) from e
        except httpx.RequestError as e:
            raise APIError(f"Request error: {e}") from e

        try:
            data = xmltodict.parse(response.content)
            법령_data = data.get("법령", {})  # noqa: N806

            기본정보 = 법령_data.get("기본정보", {})  # noqa: N806
            조문_data = 법령_data.get("조문", {})  # noqa: N806
            조문_list = 조문_data.get("조문단위", [])  # noqa: N806

            articles = []
            if 조문_list and not isinstance(조문_list, list):  # noqa: N806
                조문_list = [조문_list]  # noqa: N806

            for 조문 in 조문_list:  # noqa: N806
                조문번호 = int(조문.get("조문번호", 0))  # noqa: N806
                조문제목 = 조문.get("조문제목", "")  # noqa: N806
                조문내용 = 조문.get("조문내용", "")  # noqa: N806
                변경여부 = 조문.get("조문변경여부") == "Y"  # noqa: N806
                시행일자 = 조문.get("조문시행일자")  # noqa: N806

                paragraphs = []
                항_list = 조문.get("항", [])  # noqa: N806
                if 항_list and not isinstance(항_list, list):  # noqa: N806
                    항_list = [항_list]  # noqa: N806

                for 항 in 항_list:  # noqa: N806
                    항번호 = 항.get("항번호", "")  # noqa: N806
                    항내용 = 항.get("항내용", "")  # noqa: N806

                    items = []
                    호_list = 항.get("호", [])  # noqa: N806
                    if 호_list and not isinstance(호_list, list):  # noqa: N806
                        호_list = [호_list]  # noqa: N806

                    for 호 in 호_list:  # noqa: N806
                        호번호_str = 호.get("호번호", "0")  # noqa: N806
                        호번호 = (
                            int(호번호_str.rstrip(".")) if 호번호_str.rstrip(".").isdigit() else 0
                        )  # noqa: N806
                        호내용 = 호.get("호내용", "")  # noqa: N806

                        sub_items = []
                        목_list = 호.get("목", [])  # noqa: N806
                        if 목_list and not isinstance(목_list, list):  # noqa: N806
                            목_list = [목_list]  # noqa: N806

                        for 목 in 목_list:  # noqa: N806
                            목번호 = 목.get("목번호", "")  # noqa: N806
                            목내용 = 목.get("목내용", "")  # noqa: N806
                            sub_items.append(SubItem(목번호, 목내용))

                        items.append(Item(호번호, 호내용, sub_items))

                    paragraphs.append(Paragraph(항번호, 항내용, items))

                articles.append(
                    Article(조문번호, 조문제목, 조문내용, paragraphs, 변경여부, 시행일자)
                )

            법종구분 = 기본정보.get("법종구분")  # noqa: N806
            if isinstance(법종구분, dict):  # noqa: N806
                법종구분 = 법종구분.get("#text", "")  # noqa: N806

            소관부처 = 기본정보.get("소관부처")  # noqa: N806
            if isinstance(소관부처, dict):  # noqa: N806
                소관부처 = 소관부처.get("#text", "")  # noqa: N806

            return LawDetail(
                law_id=law_id or str(mst),
                law_name_korean=기본정보.get("법령명_한글", ""),  # noqa: N806
                law_name_chinese=기본정보.get("법령명_한자"),  # noqa: N806
                law_name_abbr=기본정보.get("법령명약칭"),  # noqa: N806
                promulgation_date=기본정보.get("공포일자"),  # noqa: N806
                promulgation_number=int(기본정보.get("공포번호", 0))  # noqa: N806
                if 기본정보.get("공포번호")  # noqa: N806
                else None,
                enforcement_date=기본정보.get("시행일자"),  # noqa: N806
                law_type=법종구분,  # noqa: N806
                ministry=소관부처,  # noqa: N806
                articles=articles,
                language=language,
            )

        except Exception as e:
            raise ParseError(f"Failed to parse response: {e}") from e
