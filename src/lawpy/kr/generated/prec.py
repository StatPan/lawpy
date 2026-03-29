"""Auto-generated client for target=prec
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class PrecClient(KoreanBaseClient):
    """Auto-generated client for target=prec.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── prec ──────────────────────────────────────
    def search_precs(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        org: str | None = None,
        curt: str | None = None,
        jo: str | None = None,
        gana: str | None = None,
        sort: str | None = None,
        date: int | None = None,
        prncyd: str | None = None,
        nb: int | None = None,
        datsrcnm: str | None = None,
        mobileyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 판례 목록 조회

        Args:
        search: 검색범위 (기본 : 1 판례명) 2 : 본문검색
        query: 검색범위에서 검색을 원하는 질의(검색 결과 리스트)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        org: 법원종류 (대법원:400201, 하위법원:400202)
        curt: 법원명 (대법원, 서울고등법원, 광주지법, 인천지방법원)
        jo: 참조법령명(형법, 민법 등)
        gana: 사전식 검색(ga,na,da…,etc)
        sort: 정렬옵션 lasc : 사건명 오름차순 ldes : 사건명 내림차순 dasc : 선고일자 오름차순 ddes : 선고일자 내림차순(생략시 기본) nasc : 법원명 오름차순 ndes : 법원명 내림차순
        date: 판례 선고일자
        prncyd: 선고일자 검색(20090101~20090130)
        nb: 판례 사건번호
        datsrcnm: 데이터출처명 (국세법령정보시스템, 근로복지공단산재판례, 대법원)
        mobileyn: 모바일여부

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: PrecSearch.prec
        """
        params: dict = {"target": "prec", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if org is not None:
            params["org"] = org
        if curt is not None:
            params["curt"] = curt
        if jo is not None:
            params["JO"] = jo
        if gana is not None:
            params["gana"] = gana
        if sort is not None:
            params["sort"] = sort
        if date is not None:
            params["date"] = date
        if prncyd is not None:
            params["prncYd"] = prncyd
        if nb is not None:
            params["nb"] = nb
        if datsrcnm is not None:
            params["datSrcNm"] = datsrcnm
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("PrecSearch", {})
        items = root.get("prec", [])
        if isinstance(items, dict):
            items = [items]
        return items or []

    def get_prec_detail(
        self,
        id: str | None = None,
        lm: str | None = None,
        mobileyn: str | None = None,
    ) -> dict:
        """[GENERATED] 판례 본문 조회

        Args:
        id: 판례 일련번호
        lm: 판례명
        mobileyn: 모바일여부

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: PrecSearch
        """
        params: dict = {"target": "prec", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if lm is not None:
            params["LM"] = lm
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("PrecSearch", data)

