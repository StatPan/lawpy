"""Auto-generated client for target=lawjosub
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LawjosubList


class GeneratedLawjosubClient(KoreanBaseClient):
    """Auto-generated client for target=lawjosub.

    All methods return Pydantic models parsed from the API response.
    """

# ── lawjosub ──────────────────────────────────────
    def search_lawjosubs(
        self,
        id: str | None = None,
        mst: str | None = None,
        jo: str | None = None,
        hang: str | None = None,
        ho: str | None = None,
        mok: str | None = None,
    ) -> list[LawjosubList]:
        """[GENERATED] 현행법령(공포일) 본문 조항호목 조회

        Args:
        id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력) (ID로 검색하면 그 법령의 현행 법령 본문 조회)
        mst: 법령 마스터 번호 - 법령테이블의 lsi_seq 값을 의미함
        jo: 조 번호 6자리숫자 예) 제2조 : 000200, 제10조의2 : 001002
        hang: 항 번호 6자리숫자 예) 제2항 : 000200
        ho: 호 번호 6자리숫자 예) 제2호 : 000200, 제10호의2 : 001002
        mok: 목 한자리 문자 예) 가,나,다,라, … 카,타,파,하 한글은 인코딩 하여 사용하여야 정상적으로 사용이가능 URLDecoder.decode('다', 'UTF-8')

        Returns:
            List of LawjosubList instances.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "lawjosub", "type": "JSON"}
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
        if isinstance(data, list):
            raw = data
        else:
            raw = []
            for v in data.values():
                if isinstance(v, list):
                    raw = v
                    break
                if isinstance(v, dict):
                    for _ik, _iv in v.items():
                        if _ik in ("resultMsg", "resultCode", "page", "totalCnt", "target", "키워드", "section", "numOfRows", "display", "query"):
                            continue
                        if isinstance(_iv, list) and _iv:
                            raw = _iv
                            break
                    if not raw:
                        raw = [v]
                    break
        return [LawjosubList.model_validate(item) for item in raw]

