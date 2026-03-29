"""Auto-generated client for target=admrulOldAndNew
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class AdmruloldandnewClient(KoreanBaseClient):
    """Auto-generated client for target=admrulOldAndNew.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── admrulOldAndNew ──────────────────────────────────────
    def search_admrulOldAndNews(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        org: str | None = None,
        knd: str | None = None,
        gana: str | None = None,
        sort: str | None = None,
        date: str | None = None,
        prmlyd: str | None = None,
        nb: int | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 행정규칙 신구법 비교 목록 조회

        Args:
        query: 법령명에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='자동차')
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        org: 소관부처별 검색(소관부처코드 제공)
        knd: 행정규칙 종류별 검색 (1=훈령/2=예규/3=고시 /4=공고/5=지침/6=기타)
        gana: 사전식 검색 (ga,na,da…,etc)
        sort: 정렬옵션(기본 : lasc 법령오름차순) ldes : 법령내림차순 dasc : 발령일자 오름차순 ddes : 발령일자 내림차순 nasc : 발령번호 오름차순 ndes : 발령번호 내림차순 efasc : 시행일자 오름차순 efdes : 시행일자 내림차순
        date: 행정규칙 발령일자
        prmlyd: 발령일자 기간검색(20090101~20090130)
        nb: 행정규칙 발령번호 ex)제2023-8호 검색을 원할시 nb=20238
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: OldAndNewLawSearch.oldAndNew
        """
        params: dict = {"target": "admrulOldAndNew", "type": "JSON"}
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
        if nb is not None:
            params["nb"] = nb
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("OldAndNewLawSearch", {})
        items = root.get("oldAndNew", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_admrulOldAndNew_detail(
        self,
        id: str | None = None,
        lid: str | None = None,
        lm: str | None = None,
    ) -> dict:
        """[GENERATED] 행정규칙 신구법 비교 본문 조회

        Args:
        id: 행정규칙 일련번호 (ID 또는 LID 중 하나는 반드시 입력)
        lid: 행정규칙 ID (ID 또는 LID 중 하나는 반드시 입력)
        lm: 행정규칙명 조회하고자 하는 정확한 행정규칙명을 입력

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: OldAndNewLawSearch
        """
        params: dict = {"target": "admrulOldAndNew", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lid is not None:
            params["LID"] = lid
        if lm is not None:
            params["LM"] = lm
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("OldAndNewLawSearch", data)

