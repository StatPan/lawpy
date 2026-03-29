"""Auto-generated client stubs for target=decc
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class DeccClient(KoreanBaseClient):
    """Auto-generated client for target=decc."""

# ── decc ──────────────────────────────────────
    def search_deccs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        cls: str | None = None,
        gana: str | None = None,
        date: int | None = None,
        dpayd: str | None = None,
        rslyd: str | None = None,
        sort: str | None = None,
        mobileyn: str,
    ) -> list[dict]:
        """[GENERATED] 행정심판례 목록 조회

        Args:
        search: 검색범위 (기본 : 1 행정심판례명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의(검색 결과 리스트)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        cls: 재결례유형 (출력 결과 필드에 있는 재결구분코드)
        gana: 사전식 검색(ga,na,da…,etc)
        date: 의결일자
        dpayd: 처분일자 검색(20090101~20090130)
        rslyd: 의결일자 검색(20090101~20090130)
        sort: 정렬옵션 (기본 : lasc 재결례명 오름차순) ldes 재결례명 내림차순 dasc : 의결일자 오름차순 ddes : 의결일자 내림차순 nasc : 사건번호 오름차순 ndes : 사건번호 내림차순
        mobileyn: 모바일여부

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/mobDeccListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "decc",
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
        if cls is not None:
            params["cls"] = cls
        if gana is not None:
            params["gana"] = gana
        if date is not None:
            params["date"] = date
        if dpayd is not None:
            params["dpaYd"] = dpayd
        if rslyd is not None:
            params["rslYd"] = rslyd
        if sort is not None:
            params["sort"] = sort
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
    def get_decc_detail(
        self,
        id: str | None = None,
        lm: str | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 행정심판례 본문 조회

        Args:
        id: 행정심판례 일련번호
        lm: 행정심판례명
        mobileyn: 모바일여부

        Returns:
            Detail dict.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/mobDeccInfoGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "decc",
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
