"""Auto-generated client for target=lstrm
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LstrmDetail, LstrmList


class GeneratedLstrmClient(KoreanBaseClient):
    """Auto-generated client for target=lstrm.

    All methods return Pydantic models parsed from the API response.
    """

# ── lstrm ──────────────────────────────────────
    def search_lstrms(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        gana: str | None = None,
        dickndcd: int | None = None,
        mobileyn: str | None = None,
    ) -> list[LstrmList]:
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
            List of LstrmList instances.
            Response path: LsTrmSearch.lstrm
        """
        params: dict = {"target": "lstrm", "type": "JSON"}
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
        root = data.get("LsTrmSearch", {})
        if isinstance(root, dict):
            items = root.get("lstrm", [])
        else:
            items = root if isinstance(root, list) else []
        if isinstance(items, dict):
            items = [items]
        return [LstrmList.model_validate(item) for item in items]

    def get_lstrm_detail(
        self,
        query: str | None = None,
    ) -> LstrmDetail:
        """[GENERATED] 법령 용어 본문 조회

        Args:
        query: 상세조회하고자 하는 법령용어 명

        Returns:
            LstrmDetail instance.
            Response path: LsTrmSearch
        """
        params: dict = {"target": "lstrm", "type": "JSON"}
        if query is not None:
            params["query"] = query
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        raw = data.get("LsTrmSearch", data)
        return LstrmDetail.model_validate(raw)

