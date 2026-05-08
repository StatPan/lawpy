"""Auto-generated client for target=decc
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import DeccDetail, DeccList


class GeneratedDeccClient(KoreanBaseClient):
    """Auto-generated client for target=decc.

    All methods return Pydantic models parsed from the API response.
    """

# ── decc ──────────────────────────────────────
    def search_deccs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        cls: str | None = None,
        gana: str | None = None,
        date: int | None = None,
        dpayd: str | None = None,
        rslyd: str | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[DeccList]:
        """[GENERATED] 행정심판례 목록 조회

        Args:
        search: 검색범위 (기본 : 1 행정심판례명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='자동차')
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        cls: 재결례유형 (출력 결과 필드에 있는 재결구분코드)
        gana: 사전식 검색(ga,na,da…,etc)
        date: 의결일자
        dpayd: 처분일자 검색(20090101~20090130)
        rslyd: 의결일자 검색(20090101~20090130)
        sort: 정렬옵션 (기본 : lasc 재결례명 오름차순) ldes 재결례명 내림차순 dasc : 의결일자 오름차순 ddes : 의결일자 내림차순 nasc : 사건번호 오름차순 ndes : 사건번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of DeccList instances.
            Response path: Decc.decc
        """
        params: dict = {"target": "decc", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if cls is not None:
            params["cls"] = cls
        if gana is not None:
            params["gana"] = gana
        if date is not None:
            params["date"] = date
        if dpayd is not None:
            params["dpaYd"] = dpayd
        if rslyd is not None:
            params["rslYd"] = rslyd
        if sort is not None:
            params["sort"] = sort
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("Decc", {})
        if isinstance(root, dict):
            items = root.get("decc", [])
        else:
            items = root if isinstance(root, list) else []
        if isinstance(items, dict):
            items = [items]
        return [DeccList.model_validate(item) for item in items]

    def get_decc_detail(
        self,
        id: str | None = None,
        lm: str | None = None,
    ) -> DeccDetail:
        """[GENERATED] 행정심판례 본문 조회

        Args:
        id: 행정심판례 일련번호
        lm: 행정심판례명

        Returns:
            DeccDetail instance.
            Response path: Decc
        """
        params: dict = {"target": "decc", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lm is not None:
            params["LM"] = lm
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        raw = data.get("Decc", data)
        return DeccDetail.model_validate(raw)

