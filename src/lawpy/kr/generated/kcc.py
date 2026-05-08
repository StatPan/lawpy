"""Auto-generated client for target=kcc
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import KccDetail, KccList


class GeneratedKccClient(KoreanBaseClient):
    """Auto-generated client for target=kcc.

    All methods return Pydantic models parsed from the API response.
    """

# ── kcc ──────────────────────────────────────
    def search_kccs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        gana: str | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[KccList]:
        """[GENERATED] 방송미디어통신위원회 결정문 목록 조회

        Args:
        search: 검색범위 1 : 안건명 (default) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (IE 조회시 UTF-8 인코딩 필수)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        gana: 사전식 검색 (ga,na,da…,etc)
        sort: 정렬옵션 lasc : 안건명 오름차순 (default) ldes : 안건명 내림차순 dasc : 의결연월일 오름차순 ddes : 의결연월일 내림차순 nasc : 안건번호 오름차순 ndes : 안건번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of KccList instances.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "kcc", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if gana is not None:
            params["gana"] = gana
        if sort is not None:
            params["sort"] = sort
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
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
        return [KccList.model_validate(item) for item in raw]

    def get_kcc_detail(
        self,
        id: str | None = None,
    ) -> KccDetail:
        """[GENERATED] 방송미디어통신위원회 결정문 본문 조회

        Args:
        id: 결정문 일련번호

        Returns:
            KccDetail instance.
            Root key not discovered — returning raw response
        """
        params: dict = {"target": "kcc", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        response = self._make_request(self.SERVICE_URL, params=params)
        return KccDetail.model_validate(response.json())

