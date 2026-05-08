"""Auto-generated client for target=eflawjosub
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import EflawjosubList


class GeneratedEflawjosubClient(KoreanBaseClient):
    """Auto-generated client for target=eflawjosub.

    All methods return Pydantic models parsed from the API response.
    """

# ── eflawjosub ──────────────────────────────────────
    def search_eflawjosubs(
        self,
        id: str | None = None,
        mst: str | None = None,
        efyd: int | None = None,
        jo: str | None = None,
        hang: str | None = None,
        ho: str | None = None,
        mok: str | None = None,
    ) -> list[EflawjosubList]:
        """[GENERATED] 현행법령(시행일) 본문 조항호목 조회 (국가법령정보센터 기준)

        Args:
        id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력)
        mst: 법령 마스터 번호 - 법령테이블의 lsi_seq 값을 의미함
        efyd: 법령의 시행일자 (ID 입력시에는 무시하는 값으로 입력하지 않음)
        jo: 조 번호 6자리숫자 예) 제2조 : 000200, 제10조의2 : 001002
        hang: 항 번호 6자리숫자 예) 제2항 : 000200
        ho: 호 번호 6자리숫자 예) 제2호 : 000200, 제10호의2 : 001002
        mok: 목 한자리 문자 예) 가,나,다,라, … 카,타,파,하 한글은 인코딩 하여 사용하여야 정상적으로 사용이가능 URLDecoder.decode('다', 'UTF-8')

        Returns:
            List of EflawjosubList instances.
            Response path: 법령.법령키
        """
        params: dict = {"target": "eflawjosub", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if mst is not None:
            params["MST"] = mst
        if efyd is not None:
            params["efYd"] = efyd
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
        root = data.get("법령", {})
        if isinstance(root, dict):
            items = root.get("법령키", [])
        else:
            items = root if isinstance(root, list) else []
        if isinstance(items, dict):
            items = [items]
        return [EflawjosubList.model_validate(item) for item in items]

