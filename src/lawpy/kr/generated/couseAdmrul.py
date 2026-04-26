"""Auto-generated client for target=couseAdmrul
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class CouseadmrulClient(KoreanBaseClient):
    """Auto-generated client for target=couseAdmrul.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── couseAdmrul ──────────────────────────────────────
    def search_couseAdmruls(
        self,
        vcode: str | None = None,
        lj_jo: str | None = None,
        display: int | None = None,
        page: int | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 맞춤형 행정규칙 조문 목록 조회

        Args:
        vcode: 분류코드 행정규칙은 A로 시작하는 14자리 코드(A0000000000001)
        lj_jo: 조문여부
        display: 검색된 결과 개 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts. Fields match the API response schema.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "couseAdmrul", "type": "JSON"}
        if vcode is not None:
            params["vcode"] = vcode
        if lj_jo is not None:
            params["lj=jo"] = lj_jo
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        if isinstance(data, list):
            return data
        for v in data.values():
            if isinstance(v, list):
                return v
            if isinstance(v, dict):
                return [v]
        return []

