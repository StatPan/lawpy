"""Auto-generated client for target=joRltLstrm
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import JorltlstrmDetail


class GeneratedJorltlstrmClient(KoreanBaseClient):
    """Auto-generated client for target=joRltLstrm.

    All methods return Pydantic models parsed from the API response.
    """

# ── joRltLstrm ──────────────────────────────────────
    def get_joRltLstrm_detail(
        self,
        query: str | None = None,
        id: int | None = None,
        jo: int | None = None,
    ) -> JorltlstrmDetail:
        """[GENERATED] 조문-법령용어 연계 조회

        Args:
        query: 법령명에서 검색을 원하는 질의 (query 또는 ID 중 하나는 반드시 입력)
        id: 법령 ID
        jo: 조번호 조번호 4자리 + 조가지번호 2자리 (000200 : 2조, 000202 : 제2조의2)

        Returns:
            JorltlstrmDetail instance.
            Root key not discovered — returning raw response
        """
        params: dict = {"target": "joRltLstrm", "type": "JSON"}
        if query is not None:
            params["query"] = query
        if id is not None:
            params["ID"] = id
        if jo is not None:
            params["JO"] = jo
        response = self._make_request(self.SERVICE_URL, params=params)
        return JorltlstrmDetail.model_validate(self._parse_json_response(response, target="joRltLstrm"))

