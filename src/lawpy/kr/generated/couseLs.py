"""Auto-generated client stubs for target=couseLs
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class CouselsClient(KoreanBaseClient):
    """Auto-generated client for target=couseLs."""

# ── couseLs ──────────────────────────────────────
    def search_couseLss(
        self,
        vcode: str | None = None,
        lj_jo: str,
        display: int | None = None,
        page: int | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 맞춤형 법령 조문 목록 조회

        Args:
        vcode: 분류코드(필수) 법령은 L로 시작하는 14자리 코드(L0000000000001)
        lj_jo: 조문여부
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/custLsJoListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "couseLs",
            "type": "JSON",
        }
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
        # TODO: navigate to the root list object and return items
        return []
