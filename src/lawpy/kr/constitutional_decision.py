"""Constitutional Court decision (헌재결정례) module for Korean law API."""

import xmltodict

from lawpy.exceptions import NotFoundError, ParseError
from lawpy.kr.base import KoreanBaseClient
from lawpy.models import ConstitutionalDecision, ConstitutionalDecisionDetail


class ConstitutionalDecisionClient(KoreanBaseClient):
    """Client for Constitutional Court Decision (헌재결정례) APIs.

    Wraps the National Law Information Center's Constitutional Court decision
    search and content-retrieval endpoints:
      - List:   GET http://www.law.go.kr/DRF/lawSearch.do?target=detc
      - Detail: GET http://www.law.go.kr/DRF/lawService.do?target=detc&ID=<id>
    """

    # ------------------------------------------------------------------ #
    #  Public API                                                          #
    # ------------------------------------------------------------------ #

    def search_decisions(
        self,
        query: str | None = None,
        search_scope: int = 1,
        sort: str = "ddes",
        page: int = 1,
        per_page: int = 20,
        case_gana: str | None = None,
        final_date: str | None = None,
        case_number: str | None = None,
        output_type: str = "XML",
    ) -> list[ConstitutionalDecision]:
        """Search Constitutional Court decisions (헌재결정례 목록 조회).

        Args:
            query: Search keyword. When *search_scope=2* performs full-text search.
            search_scope: 1 = decision name (default), 2 = full-text.
            sort: Sort order.
                'lasc'  사건명 오름차순
                'ldes'  사건명 내림차순
                'dasc'  종국일자 오름차순
                'ddes'  종국일자 내림차순 (default)
                'nasc'  사건번호 오름차순
                'ndes'  사건번호 내림차순
                'efasc' 종국일자 오름차순
                'efdes' 종국일자 내림차순
            page: Page number (default 1).
            per_page: Results per page (default 20, max 100).
            case_gana: Alphabetical case prefix (사전식 검색, e.g. 'ga').
            final_date: Final decision date filter (종국일자, YYYYMMDD).
            case_number: Case number filter (사건번호).
            output_type: 'XML' or 'JSON'.

        Returns:
            List of :class:`ConstitutionalDecision` objects.

        Raises:
            APIError: If the HTTP request fails.
            ParseError: If the response cannot be parsed.
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "detc",
            "type": output_type,
            "search": search_scope,
            "sort": sort,
            "display": per_page,
            "page": page,
        }

        if query is not None:
            params["query"] = query
        if case_gana is not None:
            params["gana"] = case_gana
        if final_date is not None:
            params["date"] = final_date
        if case_number is not None:
            params["nb"] = case_number

        response = self._make_request(self.BASE_URL, params)
        return self._parse_decision_list(response.content)

    def get_decision_detail(
        self,
        decision_id: str,
        output_type: str = "XML",
    ) -> ConstitutionalDecisionDetail:
        """Get full text of a Constitutional Court decision (헌재결정례 본문 조회).

        Args:
            decision_id: Decision serial number (헌재결정례일련번호) from
                :meth:`search_decisions`.
            output_type: 'XML' or 'JSON'.

        Returns:
            :class:`ConstitutionalDecisionDetail` with full decision text.

        Raises:
            NotFoundError: If the decision is not found.
            APIError: If the HTTP request fails.
            ParseError: If the response cannot be parsed.
        """
        params: dict[str, str | int] = {
            "OC": str(self.api_key),
            "target": "detc",
            "type": output_type,
            "ID": decision_id,
        }

        response = self._make_request(self.SERVICE_URL, params, raise_404=True)
        return self._parse_decision_detail(response.content, decision_id)

    # ------------------------------------------------------------------ #
    #  Private helpers                                                     #
    # ------------------------------------------------------------------ #

    def _parse_decision_list(self, content: bytes) -> list[ConstitutionalDecision]:
        """Parse decision list from XML response.

        Args:
            content: Raw XML bytes from ``lawSearch.do?target=detc``.

        Returns:
            List of :class:`ConstitutionalDecision` objects.

        Raises:
            ParseError: If parsing fails.
        """
        try:
            data = xmltodict.parse(content)
        except Exception as e:
            raise ParseError(f"Failed to parse XML: {e}") from e

        detc_search = data.get("DetcSearch") or data.get("LawSearch")
        if not detc_search:
            return []

        items = detc_search.get("detc", [])
        if items is None:
            return []
        if not isinstance(items, list):
            items = [items]

        decisions: list[ConstitutionalDecision] = []
        for item in items:
            try:
                decisions.append(
                    ConstitutionalDecision(
                        decision_id=str(item.get("헌재결정례일련번호", "")),
                        case_name=item.get("사건명", ""),
                        case_number=item.get("사건번호", ""),
                        final_date=item.get("종국일자"),
                        # The spec lists this field as '헌재결정례 상세링크';
                        # XML tags cannot contain spaces so we also try the
                        # concatenated form used by similar endpoints.
                        detail_link=(
                            item.get("헌재결정례상세링크")
                            or item.get("헌재결정례 상세링크")
                        ),
                    )
                )
            except Exception as e:
                raise ParseError(f"Failed to parse decision item: {e}") from e

        return decisions

    def _parse_decision_detail(
        self, content: bytes, decision_id: str
    ) -> ConstitutionalDecisionDetail:
        """Parse decision detail from XML response.

        Args:
            content: Raw XML bytes from ``lawService.do?target=detc``.
            decision_id: The requested decision ID (used as fallback).

        Returns:
            :class:`ConstitutionalDecisionDetail` object.

        Raises:
            NotFoundError: If the API signals the record was not found.
            ParseError: If parsing fails.
        """
        try:
            data = xmltodict.parse(content)
        except Exception as e:
            raise ParseError(f"Failed to parse XML: {e}") from e

        detc_data: dict = (
            data.get("DetcService")
            or data.get("헌재결정례")
            or {}
        )

        if not detc_data:
            raise NotFoundError(
                f"Constitutional Court decision not found: {decision_id}",
                status_code=404,
            )

        return ConstitutionalDecisionDetail(
            decision_id=str(detc_data.get("헌재결정례일련번호") or decision_id),
            case_name=detc_data.get("사건명", ""),
            case_number=detc_data.get("사건번호", ""),
            final_date=detc_data.get("종국일자"),
            case_type=detc_data.get("사건종류"),
            decision_type=detc_data.get("결정유형"),
            ref_statutes=detc_data.get("참조조문"),
            ruling_summary=detc_data.get("판시사항"),
            decision_gist=detc_data.get("결정요지"),
            full_text=detc_data.get("결정내용"),
        )
