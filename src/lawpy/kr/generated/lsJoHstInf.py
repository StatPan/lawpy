"""Auto-generated client stubs for target=lsJoHstInf
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LsjohstinfClient(KoreanBaseClient):
    """Auto-generated client for target=lsJoHstInf."""

# ── lsJoHstInf ──────────────────────────────────────
    def search_lsJoHstInfs(
        self,
        id: str,
        jo: str,
        display: int | None = None,
        page: int | None = None,
    ) -> list[dict]:
        """[GENERATED] 조문별 변경 이력 목록 조회

        Args:
        id: 법령 ID
        jo: 조번호 6자리숫자 : 조번호(4자리)+조가지번호(2자리) (000200 : 2조, 001002 : 10조의 2)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/lsJoChgListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "lsJoHstInf",
            "type": "JSON",
        }
        if id is not None:
            params["ID"] = id
        if jo is not None:
            params["JO"] = jo
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
