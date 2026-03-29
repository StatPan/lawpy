"""Auto-generated client for target=eflaw
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class EflawClient(KoreanBaseClient):
    """Auto-generated client for target=eflaw.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── eflaw ──────────────────────────────────────
    def search_eflaws(
        self,
        search: int | None = None,
        query: str | None = None,
        nw: int | None = None,
        lid: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        efyd: str | None = None,
        date: str | None = None,
        ancyd: str | None = None,
        ancno: str | None = None,
        rrclscd: str | None = None,
        nb: int | None = None,
        org: str | None = None,
        knd: str | None = None,
        gana: str | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 현행법령(시행일) 목록 조회 (국가법령정보센터 기준)

        Args:
        search: 검색범위 (기본 : 1 법령명) 2 : 본문검색
        query: 법령명에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='자동차')
        nw: 1: 연혁, 2: 시행예정, 3: 현행 (기본값: 전체) 연혁+예정 : nw=1,2 예정+현행 : nw=2,3 연혁+현행 : nw=1,3 연혁+예정+현행 : nw=1,2,3
        lid: 법령ID (LID=830)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션(기본 : lasc 법령오름차순) ldes : 법령내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        efyd: 시행일자 범위 검색(20090101~20090130)
        date: 공포일자 검색
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
        params: dict = {"target": "eflaw", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if nw is not None:
            params["nw"] = nw
        if lid is not None:
            params["LID"] = lid
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if efyd is not None:
            params["efYd"] = efyd
        if date is not None:
            params["date"] = date
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

    def get_eflaw_detail(
        self,
        id: str | None = None,
        mst: str | None = None,
        efyd: int | None = None,
        jo: int | None = None,
        chrclscd: str | None = None,
    ) -> dict:
        """[GENERATED] 현행법령(시행일) 본문 조회 (국가법령정보센터 기준)

        Args:
        id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력, ID로 검색하면 그 법령의 현행 법령 본문 조회)
        mst: 법령 마스터 번호 - 법령테이블의 lsi_seq 값을 의미함
        efyd: 법령의 시행일자 (ID 입력시에는 무시하는 값으로 입력하지 않음)
        jo: 조번호 생략(기본값) : 모든 조를 표시함 6자리숫자 : 조번호(4자리)+조가지번호(2자리) (000200 : 2조, 001002 : 10조의 2)
        chrclscd: 원문/한글 여부 생략(기본값) : 한글 (010202 : 한글, 010201 : 원문)

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: LawSearch
        """
        params: dict = {"target": "eflaw", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if mst is not None:
            params["MST"] = mst
        if efyd is not None:
            params["efYd"] = efyd
        if jo is not None:
            params["JO"] = jo
        if chrclscd is not None:
            params["chrClsCd"] = chrclscd
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("LawSearch", data)

