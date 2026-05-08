"""Auto-generated client for target=aiSearch
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import AisearchList


class GeneratedAisearchClient(KoreanBaseClient):
    """Auto-generated client for target=aiSearch.

    All methods return Pydantic models parsed from the API response.
    """

# ── aiSearch ──────────────────────────────────────
    def search_aiSearchs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
    ) -> list[AisearchList]:
        """[GENERATED] 지능형 법령검색 시스템 검색 API 조회

        Args:
        search: 검색범위 법령분류 (0:법령조문, 1:법령 별표·서식, 2:행정규칙 조문, 3:행정규칙 별표·서식)
        query: 법령명에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='뺑소니')
        display: 검색된 결과 개수 (default=20)
        page: 검색 결과 페이지 (default=1)

        Returns:
            List of AisearchList instances.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "aiSearch", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        if isinstance(data, list):
            raw = data
        else:
            raw = []
            for v in data.values():
                if isinstance(v, list):
                    raw = v
                    break
                if isinstance(v, dict):
                    for _ik, _iv in v.items():
                        if _ik in ("resultMsg", "resultCode", "page", "totalCnt", "target", "키워드", "section", "numOfRows", "display", "query"):
                            continue
                        if isinstance(_iv, list) and _iv:
                            raw = _iv
                            break
                    if not raw:
                        raw = [v]
                    break
        return [AisearchList.model_validate(item) for item in raw]

