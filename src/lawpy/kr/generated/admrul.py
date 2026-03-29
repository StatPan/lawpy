"""Auto-generated client stubs for target=admrul
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class AdmrulClient(KoreanBaseClient):
    """Auto-generated client for target=admrul."""

# ── admrul ──────────────────────────────────────
    def search_admruls(
        self,
        nw: int | None = None,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        org: str | None = None,
        knd: str | None = None,
        gana: str | None = None,
        sort: str | None = None,
        date: int | None = None,
        prmlyd: str | None = None,
        modyd: str | None = None,
        nb: int | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 행정규칙 목록 조회

        Args:
        nw: (1: 현행, 2: 연혁, 기본값: 현행)
        search: 검색범위 (기본 : 1 행정규칙명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query="자동차")
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        org: 소관부처별 검색(코드별도제공)
        knd: 행정규칙 종류별 검색 (1=훈령/2=예규/3=고시 /4=공고/5=지침/6=기타)
        gana: 사전식 검색 (ga,na,da…,etc)
        sort: 정렬옵션 (기본 : lasc 행정규칙명 오른차순) ldes 행정규칙명 내림차순 dasc : 발령일자 오름차순 ddes : 발령일자 내림차순 nasc : 발령번호 오름차순 ndes : 발령번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        date: 행정규칙 발령일자
        prmlyd: 발령일자 기간검색(20090101~20090130)
        modyd: 수정일자 기간검색(20090101~20090130)
        nb: 행정규칙 발령번호 ex)제2023-8호 검색을 원할시 nb=20238
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/admrulListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "admrul",
            "type": "JSON",
        }
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
        if org is not None:
            params["org"] = org
        if knd is not None:
            params["knd"] = knd
        if gana is not None:
            params["gana"] = gana
        if sort is not None:
            params["sort"] = sort
        if date is not None:
            params["date"] = date
        if prmlyd is not None:
            params["prmlYd"] = prmlyd
        if modyd is not None:
            params["modYd"] = modyd
        if nb is not None:
            params["nb"] = nb
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
    def get_admrul_detail(
        self,
        id: str | None = None,
        lm: str | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 행정규칙 본문 조회

        Args:
        id: 행정규칙 일련번호
        lm: 행정규칙명 조회하고자 하는 정확한 행정규칙명을 입력
        mobileyn: 모바일여부

        Returns:
            Detail dict.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/mobAdmrulInfoGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "admrul",
            "type": "JSON",
        }
        if id is not None:
            params["ID"] = id
        if lm is not None:
            params["LM"] = lm
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        return response.json()
