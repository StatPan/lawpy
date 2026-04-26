"""Auto-generated client for target=lsAbrv
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LsabrvClient(KoreanBaseClient):
    """Auto-generated client for target=lsAbrv.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── lsAbrv ──────────────────────────────────────
    def search_lsAbrvs(
        self,
        stddt: int | None = None,
        enddt: int | None = None,
    ) -> list[dict]:
        """[GENERATED] 법률명 약칭 조회

        Args:
        stddt: 등록일(검색시작날짜)
        enddt: 등록일(검색종료날짜)

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: LawSearch.law
        """
        params: dict = {"target": "lsAbrv", "type": "JSON"}
        if stddt is not None:
            params["stdDt"] = stddt
        if enddt is not None:
            params["endDt"] = enddt
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("LawSearch", {})
        items = root.get("law", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

