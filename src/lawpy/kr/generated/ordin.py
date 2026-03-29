"""Auto-generated client for target=ordin
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class OrdinClient(KoreanBaseClient):
    """Auto-generated client for target=ordin.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── ordin ──────────────────────────────────────
    def search_ordins(
        self,
        nw: int | None = None,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        date: int | None = None,
        efyd: str | None = None,
        ancyd: str | None = None,
        ancno: str | None = None,
        nb: int | None = None,
        org: str | None = None,
        sborg: str | None = None,
        knd: str | None = None,
        rrclscd: str | None = None,
        ordinfd: int | None = None,
        lschapno: str | None = None,
        gana: str | None = None,
        mobileyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 자치법규 목록 조회

        Args:
        nw: (1: 현행, 2: 연혁, 기본값: 현행)
        search: 검색범위 (기본 : 1 자치법규명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의(default=*)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션 (기본 : lasc 자치법규오름차순) ldes 자치법규 내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        date: 자치법규 공포일자 검색
        efyd: 시행일자 범위 검색(20090101~20090130)
        ancyd: 공포일자 범위 검색(20090101~20090130)
        ancno: 공포번호 범위 검색(306~400)
        nb: 법령의 공포번호 검색
        org: 지자체별 도·특별시·광역시 검색(지자체코드 제공) (ex. 서울특별시에 대한 검색-> org=6110000)
        sborg: 지자체별 시·군·구 검색(지자체코드 제공) (필수값 : org, ex.서울특별시 구로구에 대한 검색-> org=6110000&sborg=3160000)
        knd: 법령종류 (30001-조례 /30002-규칙 /30003-훈령 /30004-예규/30006-기타/30010-고시 /30011-의회규칙)
        rrclscd: 법령 제개정 종류 (300201-제정 / 300202-일부개정 / 300203-전부개정 300204-폐지 / 300205-폐지제정 / 300206-일괄개정 300207-일괄폐지 / 300208-타법개정 / 300209-타법폐지 300214-기타)
        ordinfd: 분류코드별 검색. 분류코드는 지자체 분야코드 openAPI 참조
        lschapno: 법령분야별 검색(법령분야코드제공) (ex. 제1편 검색 lsChapNo=01000000 / 제1편2장,제1편2장1절 lsChapNo=01020000,01020100)
        gana: 사전식 검색 (ga,na,da…,etc)
        mobileyn: 모바일여부

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: OrdinSearch.law
        """
        params: dict = {"target": "ordin", "type": "JSON"}
        if nw is not None:
            params["nw"] = nw
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if date is not None:
            params["date"] = date
        if efyd is not None:
            params["efYd"] = efyd
        if ancyd is not None:
            params["ancYd"] = ancyd
        if ancno is not None:
            params["ancNo"] = ancno
        if nb is not None:
            params["nb"] = nb
        if org is not None:
            params["org"] = org
        if sborg is not None:
            params["sborg"] = sborg
        if knd is not None:
            params["knd"] = knd
        if rrclscd is not None:
            params["rrClsCd"] = rrclscd
        if ordinfd is not None:
            params["ordinFd"] = ordinfd
        if lschapno is not None:
            params["lsChapNo"] = lschapno
        if gana is not None:
            params["gana"] = gana
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("OrdinSearch", {})
        items = root.get("law", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_ordin_detail(
        self,
        id: str | None = None,
        mst: str | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 자치법규 본문 조회

        Args:
        id: 자치법규 ID
        mst: 자치법규 마스터 번호
        mobileyn: 모바일여부

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: OrdinSearch
        """
        params: dict = {"target": "ordin", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if mst is not None:
            params["MST"] = mst
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("OrdinSearch", data)

