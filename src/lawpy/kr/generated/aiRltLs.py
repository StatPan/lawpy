"""Auto-generated client for target=aiRltLs
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import AirltlsList


class GeneratedAirltlsClient(KoreanBaseClient):
    """Auto-generated client for target=aiRltLs.

    All methods return Pydantic models parsed from the API response.
    """

# ── aiRltLs ──────────────────────────────────────
    def search_aiRltLss(
        self,
        search: int | None = None,
        query: str | None = None,
    ) -> list[AirltlsList]:
        """[GENERATED] 지능형 법령검색 시스템 연관법령 API 조회

        Args:
        search: 검색범위 법령분류(0:법령조문, 1:행정규칙조문)
        query: 법령명에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='뺑소니')

        Returns:
            List of AirltlsList instances.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "aiRltLs", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        response = self._make_request(self.BASE_URL, params=params)
        data = self._parse_json_response(response, target="aiRltLs")
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
        return [AirltlsList.model_validate(item) for item in raw]

