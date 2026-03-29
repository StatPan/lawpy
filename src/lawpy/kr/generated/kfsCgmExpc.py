"""Auto-generated client for target=kfsCgmExpc
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class KfscgmexpcClient(KoreanBaseClient):
    """Auto-generated client for target=kfsCgmExpc.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── kfsCgmExpc ──────────────────────────────────────
    def search_kfsCgmExpcs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        inq: int | None = None,
        rpl: int | None = None,
        gana: str | None = None,
        itmno: int | None = None,
        explyd: str | None = None,
        sort: str | None = None,
        popyn: str | None = None,
        fields: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 산림청 법령해석 목록

        Args:
        search: 검색범위 (기본 : 1 법령해석명, 2: 본문검색)
        query: 검색범위에서 검색을 원하는 질의 (정확한 검색을 위한 문자열 검색 query='벌채')
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        inq: 질의기관코드
        rpl: 해석기관코드
        gana: 사전식 검색(ga,na,da…,etc)
        itmno: 안건번호 * 안건번호 변수 적용 시 query 요청변수는 무시됩니다.
        explyd: 해석일자 검색(20090101~20090130)
        sort: 정렬옵션 (기본 : lasc 법령해석명 오름차순) ldes 법령해석명 내림차순 dasc : 해석일자 오름차순 ddes : 해석일자 내림차순 nasc : 안건번호 오름차순 ndes : 안건번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')
        fields: 응답항목 옵션(안건명, 안건번호, ...) * 빈 값일 경우 전체 항목 표출 * 출력 형태 HTML일 경우 적용 불가능

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: CgmExpc.cgmExpc
        """
        params: dict = {"target": "kfsCgmExpc", "type": "JSON"}
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
        if explyd is not None:
            params["explYd"] = explyd
        if sort is not None:
            params["sort"] = sort
        if popyn is not None:
            params["popYn"] = popyn
        if fields is not None:
            params["fields"] = fields
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("CgmExpc", {})
        items = root.get("cgmExpc", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_kfsCgmExpc_detail(
        self,
        id: int | None = None,
        lm: str | None = None,
        fields: str | None = None,
    ) -> dict:
        """[GENERATED] 산림청 법령해석 본문

        Args:
        id: 법령해석일련번호
        lm: 법령해석명
        fields: 응답항목 옵션(안건명, 안건번호, ...) * 빈 값일 경우 전체 항목 표출 * 출력 형태 HTML일 경우 적용 불가능

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: CgmExpc
        """
        params: dict = {"target": "kfsCgmExpc", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lm is not None:
            params["LM"] = lm
        if fields is not None:
            params["fields"] = fields
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("CgmExpc", data)

