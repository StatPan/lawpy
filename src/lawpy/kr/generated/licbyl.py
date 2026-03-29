"""Auto-generated client for target=licbyl
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class LicbylClient(KoreanBaseClient):
    """Auto-generated client for target=licbyl.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── licbyl ──────────────────────────────────────
    def search_licbyls(
        self,
        search: int | None = None,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        org: str | None = None,
        knd: str | None = None,
        gana: str | None = None,
        mobileyn: str | None = None,
    ) -> list[dict]:
        """[GENERATED] 법령 별표ㆍ서식 목록 조회

        Args:
        search: '검색범위 (기본 : 1 별표서식명) 2 : 해당법령검색 3 : 별표본문검색'
        query: 법령명에서 검색을 원하는 질의(default=*)
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)
        sort: '정렬옵션 (기본 : lasc 별표서식명 오름차순) ldes 별표서식명 내림차순'
        org: 소관부처별 검색(소관부처코드 제공)
        knd: 별표종류 1 : 별표 2 : 서식 3 : 별지 4 : 별도 5 : 부록
        gana: 사전식 검색(ga,na,da…,etc)
        mobileyn: 모바일여부

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: licBylSearch (item key not discovered)
        """
        params: dict = {"target": "licbyl", "type": "JSON"}
        if search is not None:
            params["search"] = search
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if org is not None:
            params["org"] = org
        if knd is not None:
            params["knd"] = knd
        if gana is not None:
            params["gana"] = gana
        if mobileyn is not None:
            params["mobileYn"] = mobileyn
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("licBylSearch", {})
        # item key unknown — return raw root
        return root if isinstance(root, list) else [root] if root else []

