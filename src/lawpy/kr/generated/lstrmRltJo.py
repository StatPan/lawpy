"""Auto-generated client for target=lstrmRltJo
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LstrmrltjoDetail


class GeneratedLstrmrltjoClient(KoreanBaseClient):
    """Auto-generated client for target=lstrmRltJo.

    All methods return Pydantic models parsed from the API response.
    """

# ── lstrmRltJo ──────────────────────────────────────
    def get_lstrmRltJo_detail(
        self,
        query: str | None = None,
    ) -> LstrmrltjoDetail:
        """[GENERATED] 법령용어-조문 연계 조회

        Args:
        query: 법령용어명에서 검색을 원하는 질의

        Returns:
            LstrmrltjoDetail instance.
            Root key not discovered — returning raw response
        """
        params: dict = {"target": "lstrmRltJo", "type": "JSON"}
        if query is not None:
            params["query"] = query
        response = self._make_request(self.SERVICE_URL, params=params)
        return LstrmrltjoDetail.model_validate(response.json())

