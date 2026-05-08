"""Auto-generated client for target=lstrmAI
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LstrmaiList


class GeneratedLstrmaiClient(KoreanBaseClient):
    """Auto-generated client for target=lstrmAI.

    All methods return Pydantic models parsed from the API response.
    """

# ── lstrmAI ──────────────────────────────────────
    def search_lstrmAIs(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        homonymyn: str | None = None,
    ) -> list[LstrmaiList]:
        """[GENERATED] 법령용어 조회

        Args:
        query: 법령용어명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        homonymyn: 동음이의어 존재여부 (Y/N)

        Returns:
            List of LstrmaiList instances.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "lstrmAI", "type": "JSON"}
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if homonymyn is not None:
            params["homonymYn"] = homonymyn
        response = self._make_request(self.BASE_URL, params=params)
        data = self._parse_json_response(response, target="lstrmAI")
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
        return [LstrmaiList.model_validate(item) for item in raw]

