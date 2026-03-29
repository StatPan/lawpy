"""Auto-generated client for target=school
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class SchoolClient(KoreanBaseClient):
    """Auto-generated client for target=school.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── school ──────────────────────────────────────
    def search_schools(
        self,
        nw: int | None = None,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        knd: str | None = None,
        rrclscd: str | None = None,
        date: int | None = None,
        prmlyd: str | None = None,
        nb: int | None = None,
        gana: str | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 학칙ㆍ공단ㆍ공공기관 목록 조회

        Args:
        nw: (1: 현행, 2: 연혁, 기본값: 현행)
        search: 검색범위 1 : 규정명(default) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='자동차')
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        knd: 학칙공단 종류별 검색 1 : 학칙 / 2 : 학교규정 / 3 : 학교지침 / 4 : 학교시행세칙 / 5 : 공단규정, 공공기관규정
        rrclscd: 제정·개정 구분 200401 : 제정 / 200402 : 전부개정 / 200403 : 일부개정 / 200404 : 폐지 200405 : 일괄개정 / 200406 : 일괄폐지 / 200407 : 폐지제정 200408 : 정정 / 200409 : 타법개정 / 200410 : 타법폐지
        date: 발령일자 검색
        prmlyd: 발령일자 범위 검색
        nb: 발령번호 검색
        gana: 사전식 검색 (ga,na,da…,etc)
        sort: 정렬옵션 lasc : 학칙공단명 오름차순(default) ldes : 학칙공단명 내림차순 dasc : 발령일자 오름차순 ddes : 발령일자 내림차순 nasc : 발령번호 오름차순 ndes : 발령번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts. Fields match the API response schema.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "school", "type": "JSON"}
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
        if knd is not None:
            params["knd"] = knd
        if rrclscd is not None:
            params["rrClsCd"] = rrclscd
        if date is not None:
            params["date"] = date
        if prmlyd is not None:
            params["prmlYd"] = prmlyd
        if nb is not None:
            params["nb"] = nb
        if gana is not None:
            params["gana"] = gana
        if sort is not None:
            params["sort"] = sort
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # root key not discovered — returning raw response
        if isinstance(data, list):
            return data
        for v in data.values():
            if isinstance(v, list): return v
            if isinstance(v, dict): return [v]
        return []

    def get_school_detail(
        self,
        id: str | None = None,
        lid: str | None = None,
        lm: str | None = None,
    ) -> dict:
        """[GENERATED] 학칙ㆍ공단ㆍ공공기관 본문 조회

        Args:
        id: 학칙공단 일련번호
        lid: 학칙공단 ID
        lm: 학칙공단명 조회하고자 하는 정확한 학칙공단명을 입력

        Returns:
            Detail dict. Fields match the API response schema.
            Root key not discovered — returning raw response
        """
        params: dict = {"target": "school", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lid is not None:
            params["LID"] = lid
        if lm is not None:
            params["LM"] = lm
        response = self._make_request(self.SERVICE_URL, params=params)
        return response.json()

