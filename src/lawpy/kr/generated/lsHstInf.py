"""Auto-generated client stubs for target=lsHstInf
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LshstinfClient(KoreanBaseClient):
    """Auto-generated client for target=lsHstInf."""

# ── lsHstInf ──────────────────────────────────────
    def search_lsHstInfs(
        self,
        regdt: str,
        org: str | None = None,
        display: int | None = None,
        page: int | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 법령 변경이력 목록 조회

        Args:
        regdt: 법령 변경일 검색(20150101)
        org: 소관부처별 검색(소관부처코드 제공)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/lsChgListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "lsHstInf",
            "type": "JSON",
        }
        if regdt is not None:
            params["regDt"] = regdt
        if org is not None:
            params["org"] = org
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
