"""Auto-generated client for target=detc
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import DetcDetail, DetcList


class GeneratedDetcClient(KoreanBaseClient):
    """Auto-generated client for target=detc.

    All methods return Pydantic models parsed from the API response.
    """

# ── detc ──────────────────────────────────────
    def search_detcs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        gana: str | None = None,
        sort: str | None = None,
        date: int | None = None,
        edyd: str | None = None,
        nb: int | None = None,
        popyn: str | None = None,
        mobileyn: str | None = None,
    ) -> list[DetcList]:
        """[GENERATED] 헌재결정례 목록 조회

        Args:
        search: 검색범위 (기본 : 1 헌재결정례명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='자동차')
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        gana: 사전식 검색(ga,na,da…,etc)
        sort: 정렬옵션 (기본 : lasc 사건명 오름차순) ldes 사건명 내림차순 dasc : 선고일자 오름차순 ddes : 선고일자 내림차순 nasc : 사건번호 오름차순 ndes : 사건번호 내림차순 efasc : 종국일자 오름차순 efdes : 종국일자 내림차순
        date: 종국일자
        edyd: 종국일자 기간 검색
        nb: 사건번호
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')
        mobileyn: 모바일여부

        Returns:
            List of DetcList instances.
            Response path: DetcSearch.Detc
        """
        params: dict = {"target": "detc", "type": "JSON"}
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
        if date is not None:
            params["date"] = date
        if edyd is not None:
            params["edYd"] = edyd
        if nb is not None:
            params["nb"] = nb
        if popyn is not None:
            params["popYn"] = popyn
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("DetcSearch", {})
        if isinstance(root, dict):
            items = root.get("Detc", [])
        else:
            items = root if isinstance(root, list) else []
        if isinstance(items, dict):
            items = [items]
        return [DetcList.model_validate(item) for item in items]

    def get_detc_detail(
        self,
        id: str | None = None,
        lm: str | None = None,
        mobileyn: str | None = None,
    ) -> DetcDetail:
        """[GENERATED] 헌재결정례 본문 조회

        Args:
        id: 헌재결정례 일련번호
        lm: 헌재결정례명
        mobileyn: 모바일여부

        Returns:
            DetcDetail instance.
            Response path: DetcSearch
        """
        params: dict = {"target": "detc", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lm is not None:
            params["LM"] = lm
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        raw = data.get("DetcSearch", data)
        return DetcDetail.model_validate(raw)

