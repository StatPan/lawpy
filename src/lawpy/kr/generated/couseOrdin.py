"""Auto-generated client for target=couseOrdin
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import CouseordinList


class GeneratedCouseordinClient(KoreanBaseClient):
    """Auto-generated client for target=couseOrdin.

    All methods return Pydantic models parsed from the API response.
    """

# ── couseOrdin ──────────────────────────────────────
    def search_couseOrdins(
        self,
        vcode: str | None = None,
        lj_jo: str | None = None,
        display: int | None = None,
        page: int | None = None,
        popyn: str | None = None,
    ) -> list[CouseordinList]:
        """[GENERATED] 맞춤형 자치법규 조문 목록 조회

        Args:
        vcode: 분류코드(필수) 자치법규는 O로 시작하는 14자리 코드(O0000000000001)
        lj_jo: 조문여부
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of CouseordinList instances.
            Root key not discovered — using best-effort extraction
        """
        if vcode is None:
            msg = "vcode is required for target vcode"
            raise ValueError(msg)
        if lj_jo is None:
            msg = "lj_jo is required for target lj=jo"
            raise ValueError(msg)
        params: dict = {"target": "couseOrdin", "type": "JSON"}
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
        data = self._parse_json_response(response, target="couseOrdin")
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
        return [CouseordinList.model_validate(item) for item in raw]

