"""Auto-generated client stubs for target=lnkLs
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LnklsClient(KoreanBaseClient):
    """Auto-generated client for target=lnkLs."""

# ── lnkLs ──────────────────────────────────────
    def search_lnkLss(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 법령 기준 자치법규 연계 관련 목록 조회

        Args:
        query: 법령명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션(기본 : lasc 법령오름차순) ldes : 법령내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/lsOrdinConListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "lnkLs",
            "type": "JSON",
        }
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
