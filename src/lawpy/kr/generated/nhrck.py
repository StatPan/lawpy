"""Auto-generated client for target=nhrck
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class NhrckClient(KoreanBaseClient):
    """Auto-generated client for target=nhrck.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── nhrck ──────────────────────────────────────
    def search_nhrcks(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        gana: str | None = None,
        sort: str | None = None,
        popyn: str | None = None,
        fields: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 국가인권위원회 결정문 목록 조회

        Args:
        search: 검색범위 1 : 사건명 (default) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의 (IE 조회시 UTF-8 인코딩 필수)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        gana: 사전식 검색 (ga,na,da…,etc)
        sort: 정렬옵션 lasc : 사건명 오름차순 (default) ldes : 사건명 내림차순 nasc : 의결번호 오름차순 ndes : 의결번호 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')
        fields: 응답항목 옵션(사건명, 사건번호, ...) * 빈 값일 경우 전체 항목 표출 * 출력 형태 HTML일 경우 적용 불가능

        Returns:
            List of result dicts. Fields match the API response schema.
            Root key not discovered — using best-effort extraction
        """
        params: dict = {"target": "nhrck", "type": "JSON"}
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
        if fields is not None:
            params["fields"] = fields
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        # root key not discovered — returning raw response
        if isinstance(data, list):
            return data
        for v in data.values():
            if isinstance(v, list): return v
            if isinstance(v, dict): return [v]
        return []

    def get_nhrck_detail(
        self,
        id: str | None = None,
        lm: str | None = None,
        fields: str | None = None,
    ) -> dict:
        """[GENERATED] 국가인권위원회 결정문 본문 조회

        Args:
        id: 결정문 일련번호
        lm: 결정문명
        fields: 응답항목 옵션(사건명, 사건번호, ...) * 빈 값일 경우 전체 항목 표출 * 출력 형태 HTML일 경우 적용 불가능

        Returns:
            Detail dict. Fields match the API response schema.
            Root key not discovered — returning raw response
        """
        params: dict = {"target": "nhrck", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lm is not None:
            params["LM"] = lm
        if fields is not None:
            params["fields"] = fields
        response = self._make_request(self.SERVICE_URL, params=params)
        return response.json()

