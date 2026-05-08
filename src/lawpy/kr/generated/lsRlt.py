"""Auto-generated client for target=lsRlt
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LsrltList


class GeneratedLsrltClient(KoreanBaseClient):
    """Auto-generated client for target=lsRlt.

    All methods return Pydantic models parsed from the API response.
    """

# ── lsRlt ──────────────────────────────────────
    def search_lsRlts(
        self,
        query: str | None = None,
        id: int | None = None,
        rltclscd: int | None = None,
    ) -> list[LsrltList]:
        """[GENERATED] 관련법령 조회

        Args:
        query: 기준법령명에서 검색을 원하는 정확한 법령명
        id: 법령 ID
        rltclscd: 법령 간 관계 코드

        Returns:
            List of LsrltList instances.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "lsRlt", "type": "JSON"}
        if query is not None:
            params["query"] = query
        if id is not None:
            params["ID"] = id
        if rltclscd is not None:
            params["rltClsCd"] = rltclscd
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
        return [LsrltList.model_validate(item) for item in raw]

