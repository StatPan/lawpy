"""Auto-generated client stubs for target=nlrc
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class NlrcClient(KoreanBaseClient):
    """Auto-generated client for target=nlrc."""

# ── nlrc ──────────────────────────────────────
    def search_nlrcs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        gana: str | None = None,
        sort: str | None = None,
        popyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 노동위원회 결정문 목록 조회

        Args:
        search: 검색범위 1 : 제목 (default) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (IE 조회시 UTF-8 인코딩 필수)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        gana: 사전식 검색 (ga,na,da…,etc)
        sort: 정렬옵션 lasc : 제목 오름차순 (default) ldes : 제목 내림차순 dasc : 등록일 오름차순 ddes : 등록일 내림차순 nasc : 사건번호 오름차순 ndes : 사건번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/nlrcListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "nlrc",
            "type": "JSON",
        }
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
        if popyn is not None:
            params["popYn"] = popyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
    def get_nlrc_detail(
        self,
        id: str | None = None,
    ) -> dict:
        """[GENERATED] 노동위원회 결정문 본문 조회

        Args:
        id: 결정문 일련번호

        Returns:
            Detail dict.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/nlrcInfoGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "nlrc",
            "type": "JSON",
        }
        if id is not None:
            params["ID"] = id
        response = self._make_request(self.SERVICE_URL, params=params)
        return response.json()
