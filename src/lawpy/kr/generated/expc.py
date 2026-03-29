"""Auto-generated client stubs for target=expc
Source: specs/kr/
Do not edit by hand — regenerate with scripts/codegen.py
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class ExpcClient(KoreanBaseClient):
    """Auto-generated client for target=expc."""

# ── expc ──────────────────────────────────────
    def search_expcs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        inq: str | None = None,
        rpl: int | None = None,
        gana: str | None = None,
        itmno: int | None = None,
        regyd: str | None = None,
        explyd: str | None = None,
        sort: str | None = None,
        mobileyn: str,
    ) -> list[dict]:
        """[GENERATED] 법령해석례 목록 조회

        Args:
        search: 검색범위 (기본 : 1 법령해석례명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의(검색 결과 리스트)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        inq: 질의기관
        rpl: 회신기관
        gana: 사전식 검색(ga,na,da…,etc)
        itmno: 안건번호
        regyd: 등록일자 검색(20090101~20090130)
        explyd: 해석일자 검색(20090101~20090130)
        sort: 정렬옵션 (기본 : lasc 법령해석례명 오름차순) ldes 법령해석례명 내림차순 dasc : 해석일자 오름차순 ddes : 해석일자 내림차순 nasc : 안건번호 오름차순 ndes : 안건번호 내림차순
        mobileyn: 모바일여부

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/mobExpcListGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "expc",
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
        if inq is not None:
            params["inq"] = inq
        if rpl is not None:
            params["rpl"] = rpl
        if gana is not None:
            params["gana"] = gana
        if itmno is not None:
            params["itmno"] = itmno
        if regyd is not None:
            params["regYd"] = regyd
        if explyd is not None:
            params["explYd"] = explyd
        if sort is not None:
            params["sort"] = sort
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
    def get_expc_detail(
        self,
        id: int | None = None,
        lm: str | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 법령해석례 본문 조회

        Args:
        id: 법령해석례 일련번호
        lm: 법령해석례명
        mobileyn: 모바일여부

        Returns:
            Detail dict.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/mobExpcInfoGuide.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {
            "target": "expc",
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
