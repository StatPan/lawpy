"""Auto-generated client for target=lnkLs
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LnklsList


class GeneratedLnklsClient(KoreanBaseClient):
    """Auto-generated client for target=lnkLs.

    All methods return Pydantic models parsed from the API response.
    """

# ── lnkLs ──────────────────────────────────────
    def search_lnkLss(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[LnklsList]:
        """[GENERATED] 법령 기준 자치법규 연계 관련 목록 조회

        Args:
        query: 법령명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션(기본 : lasc 법령오름차순) ldes : 법령내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of LnklsList instances.
            Response path: LawSearch (item key not discovered)
        """
        params: dict = {"target": "lnkLs", "type": "JSON"}
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
        root = data.get("LawSearch", {})
        if isinstance(root, list):
            items = root
        elif isinstance(root, dict):
            items = []
            found_items = False
            for value in root.values():
                if isinstance(value, list):
                    items = value
                    found_items = True
                    break
            if not found_items and root:
                items = [root]
        else:
            items = []
        if isinstance(items, dict):
            items = [items]
        return [LnklsList.model_validate(item) for item in items]

