"""Auto-generated client for target=lsJoHstInf
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LsjohstinfClient(KoreanBaseClient):
    """Auto-generated client for target=lsJoHstInf.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── lsJoHstInf ──────────────────────────────────────
    def search_lsJoHstInfs(
        self,
        id: str | None = None,
        jo: int | None = None,
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
            List of result dicts. Fields match the API response schema.
            Response path: LawSearch (item key not discovered)
        """
        params: dict = {"target": "lsJoHstInf", "type": "JSON"}
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
        root = data.get("LawSearch", {})
        # item key unknown — return raw root
        return root if isinstance(root, list) else [root] if root else []

