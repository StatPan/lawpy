"""Korean law adapter."""

import httpx
import xmltodict

from lawpy.client import LawClient
from lawpy.exceptions import APIError, ParseError
from lawpy.models import Law, LawText


class KoreanLawClient(LawClient):
    """Client for Korean National Law Information Center API."""

    BASE_URL = "https://www.law.go.kr/DRF/lawSearch.do"

    def __init__(self, api_key: str, timeout: int = 30) -> None:
        """Initialize Korean law client.

        Args:
            api_key: API key from National Law Information Center
            timeout: Request timeout in seconds
        """
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
            if not data or data.get("law") is None:
                return []
            laws_data = data.get("law", {}).get("list", [])

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

    def get_law_text(self, law_id: str) -> LawText:
        """Get full text of a specific law.

        Args:
            law_id: The ID of the law (e.g., '000001')

        Returns:
            LawText object containing the full text

        Raises:
            APIError: If the API request fails
            ParseError: If the response cannot be parsed
        """
        params = {
            "OC": self.api_key,
            "target": "law",
            "type": "XML",
            "ID": law_id,
        }

        try:
            response = self._client.get(self.BASE_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                from lawpy.exceptions import NotFoundError

                raise NotFoundError(f"Law not found: {law_id}", status_code=404) from e
            raise APIError(
                f"HTTP error: {e.response.status_code}", status_code=e.response.status_code
            ) from e
        except httpx.RequestError as e:
            raise APIError(f"Request error: {e}") from e

        try:
            data = xmltodict.parse(response.content)
            law_data = data.get("law", {})

            return LawText(
                law_id=law_id,
                law_name=law_data.get("법령명한글", ""),
                articles=[],
            )

        except Exception as e:
            raise ParseError(f"Failed to parse response: {e}") from e
