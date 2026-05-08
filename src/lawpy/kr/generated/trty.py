"""Auto-generated client for target=trty
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import TrtyDetail, TrtyList


class GeneratedTrtyClient(KoreanBaseClient):
    """Auto-generated client for target=trty.

    All methods return Pydantic models parsed from the API response.
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
        natcd: int | None = None,
        sort: str | None = None,
        popyn: str | None = None,
        mobileyn: str | None = None,
    ) -> list[TrtyList]:
        """[GENERATED] 조약 목록 조회

        Args:
        search: 검색범위 (기본 : 1 조약명) 2 : 조약본문
        query: 검색범위에서 검색을 원하는 질의 (검색 결과 리스트)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        gana: 사전식 검색 (ga,na,da…,etc)
        eftyd: 발효일자 검색(20090101~20090130)
        concyd: 체결일자 검색(20090101~20090130)
        cls: 1 : 양자조약 2 : 다자조약
        natcd: 국가코드
        sort: 정렬옵션 (기본 : lasc 조약명오름차순) ldes 조약명내림차순 dasc : 발효일자 오름차순 ddes : 발효일자 내림차순 nasc : 조약번호 오름차순 ndes : 조약번호 내림차순 rasc : 관보게재일 오름차순 rdes : 관보게재일 내림차순
        popyn: 상세화면 팝업창 여부(팝업창으로 띄우고 싶을 때만 'popYn=Y')
        mobileyn: 모바일여부

        Returns:
            List of TrtyList instances.
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
        if natcd is not None:
            params["natCd"] = natcd
        if sort is not None:
            params["sort"] = sort
        if popyn is not None:
            params["popYn"] = popyn
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = self._parse_json_response(response, target="trty")
        root = data.get("TrtySearch", {})
        if isinstance(root, dict):
            items = root.get("Trty", [])
        else:
            items = root if isinstance(root, list) else []
        if isinstance(items, dict):
            items = [items]
        return [TrtyList.model_validate(item) for item in items]

    def get_trty_detail(
        self,
        id: str | None = None,
        chrclscd: str | None = None,
        mobileyn: str | None = None,
    ) -> TrtyDetail:
        """[GENERATED] 조약 본문 조회

        Args:
        id: 조약 ID
        chrclscd: 한글/영문 : 010202(한글)/ 010203(영문) (default = 010202)
        mobileyn: 모바일여부

        Returns:
            TrtyDetail instance.
            Response path: TrtySearch
        """
        params: dict = {"target": "trty", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if chrclscd is not None:
            params["chrClsCd"] = chrclscd
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        data = self._parse_json_response(response, target="trty")
        raw = data.get("TrtySearch", data)
        return TrtyDetail.model_validate(raw)

