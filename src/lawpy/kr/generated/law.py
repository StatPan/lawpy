"""Auto-generated client for target=law
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LawClient(KoreanBaseClient):
    """Auto-generated client for target=law.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── law ──────────────────────────────────────
    def search_laws(
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
        mobileyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 법령 목록 조회

        Args:
        search: 검색범위 (기본 : 1 법령명) 2 : 본문검색
        query: 법령명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션 (기본 : lasc 법령오름차순) ldes : 법령내림차순 dasc : 공포일자 오름차순 ddes : 공포일자 내림차순 nasc : 공포번호 오름차순 ndes : 공포번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        date: 법령의 공포일자 검색
        efyd: 시행일자 범위 검색(20090101~20090130)
        ancyd: 공포일자 범위 검색(20090101~20090130)
        ancno: 공포번호 범위 검색(306~400)
        rrclscd: 법령 제개정 종류 (300201-제정 / 300202-일부개정 / 300203-전부개정 300204-폐지 / 300205-폐지제정 / 300206-일괄개정 300207-일괄폐지 / 300209-타법개정 / 300210-타법폐지 300208-기타)
        nb: 법령의 공포번호 검색
        org: 소관부처별 검색(소관부처코드 제공)
        knd: 법령종류(코드제공)
        gana: 사전식 검색 (ga,na,da…,etc)
        mobileyn: 모바일여부

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: LawSearch.law
        """
        params: dict = {"target": "law", "type": "JSON"}
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
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("LawSearch", {})
        items = root.get("law", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_law_detail(
        self,
        id: str | None = None,
        mst: str | None = None,
        lm: str | None = None,
        ld: int | None = None,
        ln: int | None = None,
        jo: int | None = None,
        pd: str | None = None,
        pn: int | None = None,
        bd: str | None = None,
        bt: int | None = None,
        bn: int | None = None,
        bg: int | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 법령 본문 조회

        Args:
        id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력)
        mst: 법령 마스터 번호 법령테이블의 lsi_seq 값을 의미함
        lm: 법령의 법령명(법령명 입력시 해당 법령 링크)
        ld: 법령의 공포일자
        ln: 법령의 공포번호
        jo: 조번호 생략(기본값) : 모든 조를 표시함 6자리숫자 : 조번호(4자리)+조가지번호(2자리) (000200 : 2조, 001002 : 10조의 2)
        pd: 부칙표시 ON일 경우 부칙 목록만 출력 생략할 경우 법령 + 부칙 표시
        pn: 부칙번호 해당 부칙번호에 해당하는 부칙 보기
        bd: 별표표시 생략(기본값) : 법령+별표 ON : 모든 별표 표시
        bt: 별표구분 별표표시가 on일 경우 값을 읽어들임 (별표=1/서식=2/별지=3/별도=4/부록=5)
        bn: 별표번호 별표표시가 on일 경우 값을 읽어들임
        bg: 별표가지번호 별표표시가 on일 경우 값을 읽어들임
        mobileyn: 모바일여부

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: LawSearch
        """
        params: dict = {"target": "law", "type": "JSON"}
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
        if jo is not None:
            params["JO"] = jo
        if pd is not None:
            params["PD"] = pd
        if pn is not None:
            params["PN"] = pn
        if bd is not None:
            params["BD"] = bd
        if bt is not None:
            params["BT"] = bt
        if bn is not None:
            params["BN"] = bn
        if bg is not None:
            params["BG"] = bg
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("LawSearch", data)

