"""Auto-generated client for target=trty
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class TrtyClient(KoreanBaseClient):
    """Auto-generated client for target=trty.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── trty ──────────────────────────────────────
    def search_trtys(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        gana: str | None = None,
        eftyd: str | None = None,
        concyd: str | None = None,
        cls: int | None = None,
        sort: str | None = None,
        mobileyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 조약 목록 조회

        Args:
        search: 검색범위 (기본 : 1 조약명 ) 2 : 조약본문
        query: 검색범위에서 검색을 원하는 질의(검색 결과 리스트)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        gana: 사전식 검색(ga,na,da…,etc)
        eftyd: 발효일자 검색(20090101~20090130)
        concyd: 체결일자 검색(20090101~20090130)
        cls: 1 : 양자조약 2 : 다자조약
        sort: 정렬옵션 (기본 : lasc 조약명오름차순) ldes 조약명내림차순 dasc : 발효일자 오름차순 ddes : 발효일자 내림차순 nasc : 조약번호 오름차순 ndes : 조약번호 내림차순 rasc : 관보게재일 오름차순 rdes : 관보게재일 내림차순
        mobileyn: 모바일여부

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: TrtySearch.Trty
        """
        params: dict = {"target": "trty", "type": "JSON"}
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
        if eftyd is not None:
            params["eftYd"] = eftyd
        if concyd is not None:
            params["concYd"] = concyd
        if cls is not None:
            params["cls"] = cls
        if sort is not None:
            params["sort"] = sort
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("TrtySearch", {})
        items = root.get("Trty", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_trty_detail(
        self,
        id: str | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 조약 본문 조회

        Args:
        id: 조약 ID
        mobileyn: 모바일여부

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: TrtySearch
        """
        params: dict = {"target": "trty", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("TrtySearch", data)

