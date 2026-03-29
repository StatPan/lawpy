"""Auto-generated client for target=elaw
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class ElawClient(KoreanBaseClient):
    """Auto-generated client for target=elaw.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── elaw ──────────────────────────────────────
    def search_elaws(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        date: int | None = None,
        efyd: str | None = None,
        ancyd: str | None = None,
        ancno: str | None = None,
        rrclscd: str | None = None,
        nb: int | None = None,
        org: str | None = None,
        knd: str | None = None,
        gana: str | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 영문 법령 목록 조회

        Args:
        search: 검색범위 (기본 : 1 법령명) 2 : 본문검색
        query: 법령명에서 검색을 원하는 질의(default=*)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션(기본 : lasc 법령오름차순) ldes : 법령내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        date: 법령의 공포일자 검색
        efyd: 시행일자 범위 검색(20090101~20090130)
        ancyd: 공포일자 범위 검색(20090101~20090130)
        ancno: 공포번호 범위 검색(306~400)
        rrclscd: 법령 제개정 종류 (300201-제정 / 300202-일부개정 / 300203-전부개정 300204-폐지 / 300205-폐지제정 / 300206-일괄개정 300207-일괄폐지 / 300209-타법개정 / 300210-타법폐지 300208-기타)
        nb: 법령의 공포번호 검색
        org: 소관부처별 검색(소관부처코드 제공)
        knd: 법령종류(코드제공)
        gana: 사전식 검색 (ga,na,da…,etc)
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: LawSearch.law
        """
        params: dict = {"target": "elaw", "type": "JSON"}
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
        if rrclscd is not None:
            params["rrClsCd"] = rrclscd
        if nb is not None:
            params["nb"] = nb
        if org is not None:
            params["org"] = org
        if knd is not None:
            params["knd"] = knd
        if gana is not None:
            params["gana"] = gana
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("LawSearch", {})
        items = root.get("law", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_elaw_detail(
        self,
        id: str | None = None,
        mst: str | None = None,
        lm: str | None = None,
        ld: int | None = None,
        ln: int | None = None,
    ) -> dict:
        """[GENERATED] 영문 법령 본문 조회

        Args:
        id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력)
        mst: 법령 마스터 번호 법령테이블의 lsi_seq 값을 의미함
        lm: 법령의 법령명(법령명 입력시 해당 법령 링크)
        ld: 법령의 공포일자
        ln: 법령의 공포번호

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: LawSearch
        """
        params: dict = {"target": "elaw", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if mst is not None:
            params["MST"] = mst
        if lm is not None:
            params["LM"] = lm
        if ld is not None:
            params["LD"] = ld
        if ln is not None:
            params["LN"] = ln
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("LawSearch", data)

