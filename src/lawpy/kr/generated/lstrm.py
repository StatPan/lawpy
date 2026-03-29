"""Auto-generated client stubs for target=lstrm
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LstrmClient(KoreanBaseClient):
    """Auto-generated client for target=lstrm."""

# ── lstrm ──────────────────────────────────────
    def search_lstrms(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        gana: str | None = None,
        dickndcd: int | None = None,
        mobileyn: str,
    ) -> list[dict]:
        """[GENERATED] 법령 용어 목록 조회

        Args:
        query: 법령용어명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: 정렬옵션(기본 : lasc 법령용어명 오름차순) ldes : 법령용어명 내림차순
        gana: 사전식 검색 (ga,na,da…,etc)
        dickndcd: 법령 종류 코드 (법령 : 010101, 행정규칙 : 010102)
        mobileyn: 모바일여부

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/mobLsTrmListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "lstrm",
            "type": "JSON",
        }
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if gana is not None:
            params["gana"] = gana
        if dickndcd is not None:
            params["dicKndCd"] = dickndcd
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
    def get_lstrm_detail(
        self,
        query: str | None = None,
    ) -> dict:
        """[GENERATED] 법령 용어 본문 조회

        Args:
        query: 상세조회하고자 하는 법령용어 명

        Returns:
            Detail dict.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/lsTrmInfoGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "lstrm",
            "type": "JSON",
        }
        if query is not None:
            params["query"] = query
        response = self._make_request(self.SERVICE_URL, params=params)
        return response.json()
