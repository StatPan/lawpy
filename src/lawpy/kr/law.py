"""Law (법령) module for Korean law API."""

import xmltodict

from lawpy.exceptions import ParseError
from lawpy.kr.generated.elaw import ElawClient
from lawpy.kr.generated.lsAbrv import LsabrvClient
from lawpy.kr.generated.lsHstInf import LshstinfClient
from lawpy.kr.generated.lsJoHstInf import LsjohstinfClient
from lawpy.kr.generated.oldAndNew import OldandnewClient
from lawpy.models import (
    Article,
    Item,
    Law,
    LawAbbreviation,
    LawArticleChangeHistoryEntry,
    LawChangeHistoryEntry,
    LawDetail,
    LawOldAndNewDetail,
    LawOldAndNewSummary,
    Paragraph,
    SubItem,
)


class LawClient(ElawClient, OldandnewClient, LsabrvClient, LshstinfClient, LsjohstinfClient):
    """Client for Law (법령) APIs."""

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
            APIError: If API request fails
            ParseError: If response cannot be parsed
        """
        params = {
            "OC": str(self.api_key),
            "target": target,
            "type": type,
            "query": query,
            "exact": "Y" if exact_match else "N",
            "display": per_page,
            "page": page,
        }

        response = self._make_request(self.BASE_URL, params)
        return self._parse_law_list(response.content)

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
            law_id: The ID of law (e.g., '009682'). Either law_id or mst must be provided.
            mst: The master number of law (lsi_seq value). Either law_id or mst must be provided.
            article_number: Specific article number to retrieve (default: all articles)
            language: Language type ('KO' for Korean, 'ORI' for original)
            output_type: Output type ('HTML', 'XML', or 'JSON')

        Returns:
            LawDetail object containing detailed law information and full text

        Raises:
            ValueError: If neither law_id nor mst is provided
            APIError: If API request fails
            ParseError: If response cannot be parsed
        """
        if law_id is None and mst is None:
            msg = "Either law_id or mst must be provided"
            raise ValueError(msg)

        params: dict[str, str | int] = {
            "OC": str(self.api_key),
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

        response = self._make_request(self.SERVICE_URL, params, raise_404=True)
        return self._parse_law_detail(response.content, law_id, mst, language)

    def get_law_list(
        self,
        query: str | None = None,
        law_id: str | None = None,
        org_code: str | None = None,
        date: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        output_type: str = "XML",
    ) -> list[Law]:
        """Get list of current laws (based on effective date).

        Args:
            query: Law name search query
            law_id: Law ID (LID, e.g., '830')
            org_code: Ministry code (e.g., '1613000' for Ministry of Economy and Finance)
            date: Effective date search (20090101~20091231)
            page: Page number (default: 1)
            per_page: Number of results per page (default: 20, max: 100)
            sort: Sort option (default: lasc)
                   lasc: Effective date descending
                   ldes: Effective date ascending
                   ddas: Proclamation date descending
                   ddes: Proclamation date ascending
                   nasc: Proclamation number ascending
                   ndes: Proclamation number descending
                   efasc: Effective date ascending
                   efdes: Effective date descending
            output_type: Output type ('HTML', 'XML', or 'JSON')

        Returns:
            List of Law objects

        Raises:
            APIError: If API request fails
            ParseError: If response cannot be parsed
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "eflaw",
            "type": output_type,
            "display": per_page,
            "page": page,
            "sort": sort or "lasc",
        }

        if query is not None:
            params["query"] = query
        if law_id is not None:
            params["LID"] = law_id
        if org_code is not None:
            params["org"] = org_code
        if date is not None:
            params["date"] = date

        response = self._make_request(self.BASE_URL, params)
        return self._parse_law_list(response.content)

    def get_law_history(
        self,
        query: str | None = None,
        law_id: str | None = None,
        org_code: str | None = None,
        knd: str | None = None,
        rr_cls_cd: str | None = None,
        ls_chap_no: str | None = None,
        gana: str | None = None,
        date: str | None = None,
        anc_yd: str | None = None,
        anc_no: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        output_type: str = "XML",
    ) -> list[Law]:
        """Get law amendment history list.

        Args:
            query: Law name search query
            law_id: Law ID (e.g., '009682')
            org_code: Ministry code (e.g., '1613000')
            knd: Law kind code (001: Laws, 002: Presidential Decrees, 003: Prime Ministerial Ordinances, 004: Ministry Ordinances)
            rr_cls_cd: Related regulatory classification code
            ls_chap_no: Law section number
            gana: Amendment version letter (가, 나, 다, etc.)
            date: Proclamation date search (e.g., '20090101')
            anc_yd: Amendment year date
            anc_no: Amendment number
            page: Page number (default: 1)
            per_page: Number of results per page (default: 20, max: 100)
            sort: Sort option (default: ldes)
                   ldes: Effective date descending
                   lasc: Effective date ascending
                   ddas: Proclamation date descending
                   ddes: Proclamation date ascending
                   nasc: Proclamation number ascending
                   ndes: Proclamation number descending
            output_type: Output type ('HTML', 'XML', or 'JSON')

        Returns:
            List of Law objects

        Raises:
            APIError: If API request fails
            ParseError: If response cannot be parsed
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "lsHistory",
            "type": output_type,
            "display": per_page,
            "page": page,
            "sort": sort or "ldes",
        }

        if query is not None:
            params["query"] = query
        if law_id is not None:
            params["LID"] = law_id
        if org_code is not None:
            params["org"] = org_code
        if knd is not None:
            params["knd"] = knd
        if rr_cls_cd is not None:
            params["rrClsCd"] = rr_cls_cd
        if ls_chap_no is not None:
            params["lsChapNo"] = ls_chap_no
        if gana is not None:
            params["gana"] = gana
        if date is not None:
            params["date"] = date
        if anc_yd is not None:
            params["ancYd"] = anc_yd
        if anc_no is not None:
            params["ancNo"] = anc_no

        response = self._make_request(self.BASE_URL, params)
        return self._parse_law_list(response.content)

    def get_law_history_detail(
        self,
        law_id: str | None = None,
        mst: int | None = None,
        law_name: str | None = None,
        promulgation_date: str | None = None,
        promulgation_number: int | None = None,
        output_type: str = "HTML",
        character_type: str | None = None,
    ) -> str:
        """Get detailed law history text (HTML).

        Args:
            law_id: Law ID (e.g., '009682'). Either law_id or mst must be provided.
            mst: The master number of law (lsi_seq value). Either law_id or mst must be provided.
            law_name: Law name (LM)
            promulgation_date: Promulgation date (LD), e.g., '20240101'
            promulgation_number: Promulgation number (LN)
            output_type: Output type ('HTML', 'XML', or 'JSON', default: 'HTML')
            character_type: Character type ('010202' for Korean, '010201' for original text)

        Returns:
            HTML text content

        Raises:
            ValueError: If neither law_id nor mst is provided
            APIError: If API request fails
        """
        if law_id is None and mst is None:
            msg = "Either law_id or mst must be provided"
            raise ValueError(msg)

        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "lsHistory",
            "type": output_type,
        }

        if law_id is not None:
            params["ID"] = law_id
        if mst is not None:
            params["MST"] = mst
        if law_name is not None:
            params["LM"] = law_name
        if promulgation_date is not None:
            params["LD"] = promulgation_date
        if promulgation_number is not None:
            params["LN"] = promulgation_number
        if character_type is not None:
            params["chrClsCd"] = character_type

        response = self._make_request(self.SERVICE_URL, params)
        return response.text

    def get_law_old_new(
        self,
        query: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        promulgation_date: int | None = None,
        promulgation_number: int | None = None,
        output_type: str = "JSON",
    ) -> list[dict]:
        """Get old/new law comparison list (신구법 목록).

        Args:
            query: Law name search query
            page: Page number (default: 1)
            per_page: Number of results per page (default: 20, max: 100)
            sort: Sort option (default: lasc)
            promulgation_date: Promulgation date (YYYYMMDD)
            promulgation_number: Promulgation number
            output_type: Output type ('JSON' recommended)

        Returns:
            List of old/new comparison metadata dictionaries
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "oldAndNew",
            "type": output_type,
            "display": per_page,
            "page": page,
            "sort": sort or "lasc",
        }

        if query is not None:
            params["query"] = query
        if promulgation_date is not None:
            params["date"] = promulgation_date
        if promulgation_number is not None:
            params["nb"] = promulgation_number

        response = self._make_request(self.BASE_URL, params)
        data = response.json()
        root = data.get("OldAndNewLawSearch", {})
        items = root.get("oldAndNew", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_law_old_new_detail(
        self,
        law_id: str | None = None,
        mst: int | None = None,
        law_name: str | None = None,
        promulgation_date: int | None = None,
        promulgation_number: int | None = None,
        output_type: str = "JSON",
    ) -> dict:
        """Get old/new law comparison detail (신구법 본문).

        Args:
            law_id: Law ID (ID)
            mst: Law master sequence (MST)
            law_name: Law name (LM)
            promulgation_date: Promulgation date (LD)
            promulgation_number: Promulgation number (LN)
            output_type: Output type ('JSON' recommended)

        Returns:
            Detail dictionary from ``OldAndNewLawSearch`` root
        """
        if law_id is None and mst is None:
            msg = "Either law_id or mst must be provided"
            raise ValueError(msg)

        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "oldAndNew",
            "type": output_type,
        }

        if law_id is not None:
            params["ID"] = law_id
        if mst is not None:
            params["MST"] = mst
        if law_name is not None:
            params["LM"] = law_name
        if promulgation_date is not None:
            params["LD"] = promulgation_date
        if promulgation_number is not None:
            params["LN"] = promulgation_number

        response = self._make_request(self.SERVICE_URL, params)
        data = response.json()
        root = data.get("OldAndNewLawSearch", data)
        if isinstance(root, dict):
            return root
        return {}

    def get_law_abbreviations(
        self,
        start_date: int | None = None,
        end_date: int | None = None,
        output_type: str = "JSON",
    ) -> list[dict]:
        """Get law abbreviations (법령명 약칭)."""
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "lsAbrv",
            "type": output_type,
        }

        if start_date is not None:
            params["stdDt"] = start_date
        if end_date is not None:
            params["endDt"] = end_date

        response = self._make_request(self.BASE_URL, params)
        data = response.json()
        root = data.get("LawSearch", {})
        items = root.get("law", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_law_change_history(
        self,
        registered_date: int | None = None,
        org_code: str | None = None,
        page: int = 1,
        per_page: int = 20,
        output_type: str = "JSON",
    ) -> list[dict]:
        """Get law-level change history feed (법령 변경이력 목록)."""
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "lsHstInf",
            "type": output_type,
            "display": per_page,
            "page": page,
        }

        if registered_date is not None:
            params["regDt"] = registered_date
        if org_code is not None:
            params["org"] = org_code

        response = self._make_request(self.BASE_URL, params)
        data = response.json()
        root = data.get("LawSearch", {})
        if isinstance(root, list):
            return root
        if isinstance(root, dict) and root:
            return [root]
        return []

    def get_law_article_change_history(
        self,
        law_id: str,
        article_code: int | None = None,
        page: int = 1,
        per_page: int = 20,
        output_type: str = "JSON",
    ) -> list[dict]:
        """Get article-level change history (조문별 변경 이력 목록)."""
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "lsJoHstInf",
            "type": output_type,
            "ID": law_id,
            "display": per_page,
            "page": page,
        }

        if article_code is not None:
            params["JO"] = article_code

        response = self._make_request(self.SERVICE_URL, params)
        data = response.json()
        root = data.get("LawSearch", {})
        if isinstance(root, list):
            return root
        if isinstance(root, dict) and root:
            return [root]
        return []

    def search_english_laws(
        self,
        query: str,
        page: int = 1,
        per_page: int = 20,
        sort: str = "lasc",
    ) -> list[Law]:
        """Search English laws via generated ``elaw.search_elaws`` wrapper."""
        rows = self.search_elaws(query=query, page=page, display=per_page, sort=sort)
        return [self._law_from_generated_dict(row) for row in rows]

    def get_english_law_detail(
        self,
        law_id: str | None = None,
        mst: str | None = None,
    ) -> LawDetail:
        """Get English law detail via generated ``elaw.get_elaw_detail`` wrapper."""
        if law_id is None and mst is None:
            msg = "Either law_id or mst must be provided"
            raise ValueError(msg)
        detail = self.get_elaw_detail(id=law_id, mst=mst)
        return self._law_detail_from_generated_dict(detail, law_id=law_id, mst=mst, language="EN")

    def search_law_old_and_new(
        self,
        query: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str = "lasc",
    ) -> list[LawOldAndNewSummary]:
        """Search old/new law list via generated ``oldAndNew.search_oldAndNews`` wrapper."""
        rows = self.search_oldAndNews(query=query, page=page, display=per_page, sort=sort)
        return [
            LawOldAndNewSummary(
                law_id=row.get("법령ID") or row.get("ID"),
                law_name=row.get("법령명한글") or row.get("법령명"),
                promulgation_date=row.get("공포일자") or row.get("LD"),
                promulgation_number=str(row.get("공포번호") or row.get("LN") or "") or None,
                raw=row,
            )
            for row in rows
        ]

    def get_law_old_and_new_detail(
        self,
        law_id: str | None = None,
        mst: str | None = None,
    ) -> LawOldAndNewDetail:
        """Get old/new law detail via generated ``oldAndNew.get_oldAndNew_detail`` wrapper."""
        if law_id is None and mst is None:
            msg = "Either law_id or mst must be provided"
            raise ValueError(msg)
        row = self.get_oldAndNew_detail(id=law_id, mst=mst)
        return LawOldAndNewDetail(
            law_id=row.get("법령ID") or row.get("ID"),
            law_name=row.get("법령명한글") or row.get("법령명"),
            comparison_text=row.get("신구법비교") or row.get("비교내용") or row.get("contents"),
            raw=row,
        )

    def search_law_abbreviations(
        self,
        start_date: int | None = None,
        end_date: int | None = None,
    ) -> list[LawAbbreviation]:
        """Search law abbreviations via generated ``lsAbrv.search_lsAbrvs`` wrapper."""
        rows = self.search_lsAbrvs(stddt=start_date, enddt=end_date)
        return [
            LawAbbreviation(
                law_id=row.get("법령ID") or row.get("ID"),
                law_name=row.get("법령명한글") or row.get("법령명"),
                abbreviation=row.get("약칭명") or row.get("abbreviation"),
                raw=row,
            )
            for row in rows
        ]

    def search_law_change_history(
        self,
        registered_date: int | None = None,
        org_code: str | None = None,
        page: int = 1,
        per_page: int = 20,
    ) -> list[LawChangeHistoryEntry]:
        """Search law-level change history via generated ``lsHstInf.search_lsHstInfs`` wrapper."""
        rows = self.search_lsHstInfs(
            regdt=registered_date,
            org=org_code,
            page=page,
            display=per_page,
        )
        return [
            LawChangeHistoryEntry(
                law_id=row.get("법령ID") or row.get("ID"),
                law_name=row.get("법령명한글") or row.get("법령명"),
                change_date=row.get("변경일자") or row.get("regDt"),
                raw=row,
            )
            for row in rows
        ]

    def search_law_article_change_history(
        self,
        law_id: str,
        article_number: int,
        page: int = 1,
        per_page: int = 20,
    ) -> list[LawArticleChangeHistoryEntry]:
        """Search article-level change history via generated ``lsJoHstInf.search_lsJoHstInfs`` wrapper."""
        if not law_id:
            msg = "law_id is required"
            raise ValueError(msg)
        jo = int(f"{article_number:04d}00")
        rows = self.search_lsJoHstInfs(id=law_id, jo=jo, page=page, display=per_page)
        return [
            LawArticleChangeHistoryEntry(
                law_id=row.get("법령ID") or row.get("ID"),
                article_code=str(row.get("조문번호") or row.get("JO") or jo),
                change_date=row.get("변경일자") or row.get("regDt"),
                raw=row,
            )
            for row in rows
        ]

    def _law_from_generated_dict(self, row: dict) -> Law:
        return Law(
            law_id=row.get("법령ID") or row.get("lawId") or row.get("ID") or "",
            law_name=row.get("법령명한글") or row.get("법령명영문") or row.get("법령명") or row.get("lawName") or "",
            law_no=str(row.get("공포번호") or row.get("lawNo") or ""),
            promulgation_date=row.get("공포일자") or row.get("promulgationDate"),
            enforcement_date=row.get("시행일자") or row.get("enforcementDate"),
        )

    def _law_detail_from_generated_dict(
        self,
        detail: dict,
        law_id: str | None,
        mst: str | None,
        language: str,
    ) -> LawDetail:
        base = detail.get("기본정보") if isinstance(detail, dict) else None
        if not isinstance(base, dict):
            base = detail if isinstance(detail, dict) else {}
        promulgation_number = base.get("공포번호") or base.get("promulgationNumber")
        try:
            pn = int(promulgation_number) if promulgation_number else None
        except (TypeError, ValueError):
            pn = None

        return LawDetail(
            law_id=base.get("법령ID") or base.get("lawId") or law_id or str(mst or ""),
            law_name_korean=base.get("법령명_한글") or base.get("법령명한글") or base.get("법령명영문") or base.get("lawName") or "",
            law_name_chinese=base.get("법령명_한자") or base.get("lawNameChinese"),
            law_name_abbr=base.get("법령명약칭") or base.get("lawNameAbbr"),
            promulgation_date=base.get("공포일자") or base.get("promulgationDate"),
            promulgation_number=pn,
            enforcement_date=base.get("시행일자") or base.get("enforcementDate"),
            law_type=base.get("법종구분") or base.get("lawType"),
            ministry=base.get("소관부처") or base.get("ministry"),
            articles=[],
            language=language,
        )

    def _parse_law_list(self, content: bytes) -> list[Law]:
        """Parse law list from XML response.

        Args:
            content: XML response content

        Returns:
            List of Law objects

        Raises:
            ParseError: If parsing fails
        """
        try:
            data = xmltodict.parse(content)
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

    def _parse_law_detail(
        self, content: bytes, law_id: str | None, mst: int | None, language: str
    ) -> LawDetail:
        """Parse law detail from XML response.

        Args:
            content: XML response content
            law_id: Law ID
            mst: Master number
            language: Language code

        Returns:
            LawDetail object

        Raises:
            ParseError: If parsing fails
        """
        try:
            data = xmltodict.parse(content)
            law_data = data.get("법령", {})

            basic_info = law_data.get("기본정보", {})
            article_data = law_data.get("조문", {})
            article_list = article_data.get("조문단위", [])

            articles = []
            if article_list and not isinstance(article_list, list):
                article_list = [article_list]

            for article in article_list:
                article_no = int(article.get("조문번호", 0))
                article_title = article.get("조문제목", "")
                article_content = article.get("조문내용", "")
                changed = article.get("조문변경여부") == "Y"
                effective_date = article.get("조문시행일자")

                paragraphs = []
                paragraph_list = article.get("항", [])
                if paragraph_list and not isinstance(paragraph_list, list):
                    paragraph_list = [paragraph_list]

                for paragraph in paragraph_list:
                    paragraph_no = paragraph.get("항번호", "")
                    paragraph_content = paragraph.get("항내용", "")

                    items = []
                    item_list = paragraph.get("호", [])
                    if item_list and not isinstance(item_list, list):
                        item_list = [item_list]

                    for item in item_list:
                        item_no_str = item.get("호번호", "0")
                        item_no_str_clean = item_no_str.rstrip(".")
                        item_no = int(item_no_str_clean) if item_no_str_clean.isdigit() else 0
                        item_content = item.get("호내용", "")

                        sub_items = []
                        sub_item_list = item.get("목", [])
                        if sub_item_list and not isinstance(sub_item_list, list):
                            sub_item_list = [sub_item_list]

                        for sub_item in sub_item_list:
                            sub_item_no = sub_item.get("목번호", "")
                            sub_item_content = sub_item.get("목내용", "")
                            sub_items.append(SubItem(number=sub_item_no, content=sub_item_content))

                        items.append(Item(number=item_no, content=item_content, sub_items=sub_items))

                    paragraphs.append(Paragraph(number=paragraph_no, content=paragraph_content, items=items))

                articles.append(
                    Article(
                        number=article_no,
                        title=article_title,
                        content=article_content,
                        paragraphs=paragraphs,
                        changed=changed,
                        effective_date=effective_date,
                    )
                )

            law_type = basic_info.get("법종구분")
            if isinstance(law_type, dict):
                law_type = law_type.get("#text", "")

            ministry = basic_info.get("소관부처")
            if isinstance(ministry, dict):
                ministry = ministry.get("#text", "")

            promulgation_number = basic_info.get("공포번호")
            if promulgation_number and isinstance(promulgation_number, str) and promulgation_number.isdigit():
                prom_no = int(promulgation_number)
            else:
                prom_no = None

            return LawDetail(
                law_id=law_id or str(mst),
                law_name_korean=basic_info.get("법령명_한글", ""),
                law_name_chinese=basic_info.get("법령명_한자"),
                law_name_abbr=basic_info.get("법령명약칭"),
                promulgation_date=basic_info.get("공포일자"),
                promulgation_number=prom_no,
                enforcement_date=basic_info.get("시행일자"),
                law_type=law_type,
                ministry=ministry,
                articles=articles,
                language=language,
            )

        except Exception as e:
            raise ParseError(f"Failed to parse response: {e}") from e
