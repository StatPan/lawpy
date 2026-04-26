"""Auto-generated client for target=lnkOrd
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LnkordClient(KoreanBaseClient):
    """Auto-generated client for target=lnkOrd.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── lnkOrd ──────────────────────────────────────
    def search_lnkOrds(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 자치법규 기준 법령 연계 관련 목록 조회

        Args:
        query: 법규명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션 (기본 : lasc 자치법규오름차순) ldes 자치법규 내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: OrdinSearch (item key not discovered)
        """
        params: dict = {"target": "lnkOrd", "type": "JSON"}
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
        root = data.get("OrdinSearch", {})
        result = root if isinstance(root, list) else [root] if root else []
        return result

