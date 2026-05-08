"""Auto-generated client for target=lstrmRlt
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LstrmrltDetail


class GeneratedLstrmrltClient(KoreanBaseClient):
    """Auto-generated client for target=lstrmRlt.

    All methods return Pydantic models parsed from the API response.
    """

# ── lstrmRlt ──────────────────────────────────────
    def get_lstrmRlt_detail(
        self,
        query: str | None = None,
        mst: str | None = None,
        trmrltcd: int | None = None,
    ) -> LstrmrltDetail:
        """[GENERATED] 법령용어-일상용어 연계 조회

        Args:
        query: 법령용어명에서 검색을 원하는 질의 (query 또는 MST 중 하나는 반드시 입력)
        mst: 법령용어명 일련번호
        trmrltcd: 용어관계 동의어 : 140301 반의어 : 140302 상위어 : 140303 하위어 : 140304 연관어 : 140305

        Returns:
            LstrmrltDetail instance.
            Root key not discovered — returning raw response
        """
        params: dict = {"target": "lstrmRlt", "type": "JSON"}
        if query is not None:
            params["query"] = query
        if mst is not None:
            params["MST"] = mst
        if trmrltcd is not None:
            params["trmRltCd"] = trmrltcd
        response = self._make_request(self.SERVICE_URL, params=params)
        return LstrmrltDetail.model_validate(response.json())

