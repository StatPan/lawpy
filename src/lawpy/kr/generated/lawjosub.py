"""Auto-generated client stubs for target=lawjosub
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LawjosubClient(KoreanBaseClient):
    """Auto-generated client for target=lawjosub."""

# ── lawjosub ──────────────────────────────────────
    def search_lawjosubs(
        self,
        id: str | None = None,
        mst: str | None = None,
        jo: str,
        hang: str | None = None,
        ho: str | None = None,
        mok: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 현행법령(공포일) 본문 조항호목 조회

        Args:
        id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력) (ID로 검색하면 그 법령의 현행 법령 본문 조회)
        mst: 법령 마스터 번호 - 법령테이블의 lsi_seq 값을 의미함
        jo: 조 번호 6자리숫자 예) 제2조 : 000200, 제10조의2 : 001002
        hang: 항 번호 6자리숫자 예) 제2항 : 000200
        ho: 호 번호 6자리숫자 예) 제2호 : 000200, 제10호의2 : 001002
        mok: 목 한자리 문자 예) 가,나,다,라, … 카,타,파,하 한글은 인코딩 하여 사용하여야 정상적으로 사용이가능 URLDecoder.decode("다", "UTF-8")

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/lsNwJoListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "lawjosub",
            "type": "JSON",
        }
        if id is not None:
            params["ID"] = id
        if mst is not None:
            params["MST"] = mst
        if jo is not None:
            params["JO"] = jo
        if hang is not None:
            params["HANG"] = hang
        if ho is not None:
            params["HO"] = ho
        if mok is not None:
            params["MOK"] = mok
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
