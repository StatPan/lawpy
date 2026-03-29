"""Precedent (판례) module for Korean law API."""

import xmltodict

from lawpy.exceptions import NotFoundError, ParseError
from lawpy.kr.base import KoreanBaseClient
from lawpy.models import Precedent, PrecedentDetail


class PrecedentClient(KoreanBaseClient):
    """Client for Precedent (판례) APIs.

    Wraps the National Law Information Center's precedent (판례) search and
    content-retrieval endpoints:
      - List:    GET http://www.law.go.kr/DRF/lawSearch.do?target=prec
      - Detail:  GET http://www.law.go.kr/DRF/lawService.do?target=prec&ID=<id>
    """

    # ------------------------------------------------------------------ #
    #  Public API                                                          #
    # ------------------------------------------------------------------ #

    def search_precedents(
        self,
        query: str | None = None,
        search_scope: int = 1,
        court_type: str | None = None,
        court_name: str | None = None,
        ref_statute: str | None = None,
        case_gana: str | None = None,
        sort: str = "ddes",
        page: int = 1,
        per_page: int = 20,
        output_type: str = "XML",
    ) -> list[Precedent]:
        """Search precedents (판례 목록 조회).

        Args:
            query: Keyword to search (검색어). When *search_scope=2* this is a
                full-text search; otherwise it matches case/ruling names.
            search_scope: Search scope.
                1 = 판례명 (default)
                2 = 전문(full-text) search
            court_type: Court type code (법원종류).
                '400201' = 대법원, '400202' = 하위법원
            court_name: Specific court name (법원명).
                e.g. '서울고등법원', '대법원'
            ref_statute: Referenced statute name (참조법령명).
                e.g. '형법', '민법'
            case_gana: Case-number prefix letter (사건식, e.g. 'ga', 'na', 'da').
            sort: Sort order.
                'lasc'  사건명 오름차순
                'ldes'  사건명 내림차순
                'dasc'  선고일자 오름차순
                'ddes'  선고일자 내림차순 (default)
                'nasc'  사건번호 오름차순
                'ndes'  사건번호 내림차순
            page: Page number (default 1).
            per_page: Results per page (default 20, max 100).
            output_type: 'XML' or 'JSON'.

        Returns:
            List of :class:`Precedent` objects.

        Raises:
            APIError: If the HTTP request fails.
            ParseError: If the response cannot be parsed.
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "prec",
            "type": output_type,
            "search": search_scope,
            "sort": sort,
            "display": per_page,
            "page": page,
        }

        if query is not None:
            params["query"] = query
        if court_type is not None:
            params["org"] = court_type
        if court_name is not None:
            params["curt"] = court_name
        if ref_statute is not None:
            params["JO"] = ref_statute
        if case_gana is not None:
            params["gana"] = case_gana

        response = self._make_request(self.BASE_URL, params)
        return self._parse_precedent_list(response.content)

    def get_precedent_detail(
        self,
        prec_id: str,
        output_type: str = "XML",
    ) -> PrecedentDetail:
        """Get full text of a specific precedent (판례 본문 조회).

        Args:
            prec_id: Precedent serial number (판례일련번호) obtained from
                :meth:`search_precedents`.
            output_type: 'XML' or 'JSON'.

        Returns:
            :class:`PrecedentDetail` with full decision text.

        Raises:
            NotFoundError: If the precedent is not found.
            APIError: If the HTTP request fails.
            ParseError: If the response cannot be parsed.
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "prec",
            "type": output_type,
            "ID": prec_id,
        }

        response = self._make_request(self.SERVICE_URL, params, raise_404=True)
        return self._parse_precedent_detail(response.content, prec_id)

    # ------------------------------------------------------------------ #
    #  Private helpers                                                     #
    # ------------------------------------------------------------------ #

    def _parse_precedent_list(self, content: bytes) -> list[Precedent]:
        """Parse precedent list from XML response.

        Args:
            content: Raw XML bytes from ``lawSearch.do``.

        Returns:
            List of :class:`Precedent` objects.

        Raises:
            ParseError: If parsing fails.
        """
        try:
            data = xmltodict.parse(content)
        except Exception as e:
            raise ParseError(f"Failed to parse XML: {e}") from e

        prec_search = data.get("PrecSearch") or data.get("LawSearch")
        if not prec_search:
            return []

        items = prec_search.get("prec", [])
        if items is None:
            return []
        if not isinstance(items, list):
            items = [items]

        precedents: list[Precedent] = []
        for item in items:
            try:
                precedents.append(
                    Precedent(
                        prec_id=str(item.get("판례일련번호", "")),
                        case_name=item.get("사건명", ""),
                        case_number=item.get("사건번호", ""),
                        decision_date=item.get("선고일자"),
                        court_name=item.get("법원명"),
                        case_type=item.get("사건분류명"),
                        judgment_type=item.get("판결유형"),
                        detail_link=item.get("판례상세링크"),
                    )
                )
            except Exception as e:
                raise ParseError(f"Failed to parse precedent item: {e}") from e

        return precedents

    def _parse_precedent_detail(self, content: bytes, prec_id: str) -> PrecedentDetail:
        """Parse precedent detail from XML response.

        Args:
            content: Raw XML bytes from ``lawService.do``.
            prec_id: The requested precedent ID (used as fallback).

        Returns:
            :class:`PrecedentDetail` object.

        Raises:
            NotFoundError: If the API signals the record was not found.
            ParseError: If parsing fails.
        """
        try:
            data = xmltodict.parse(content)
        except Exception as e:
            raise ParseError(f"Failed to parse XML: {e}") from e

        # The root element name varies across API versions; try common keys.
        prec_data: dict = (
            data.get("PrecService")
            or data.get("판례")
            or {}
        )

        if not prec_data:
            raise NotFoundError(f"Precedent not found: {prec_id}", status_code=404)

        return PrecedentDetail(
            prec_id=str(prec_data.get("판례일련번호") or prec_id),
            case_name=prec_data.get("사건명", ""),
            case_number=prec_data.get("사건번호", ""),
            decision_date=prec_data.get("선고일자"),
            court_name=prec_data.get("법원명"),
            case_type=prec_data.get("사건분류명"),
            judgment_type=prec_data.get("판결유형"),
            decision_type=prec_data.get("선고"),
            ref_statutes=prec_data.get("참조조문"),
            ref_precedents=prec_data.get("참조판례"),
            ruling_summary=prec_data.get("판시사항"),
            ruling_gist=prec_data.get("판결요지"),
            full_text=prec_data.get("판례내용"),
        )
