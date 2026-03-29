"""Auto-generated client for target=oneview
Source: specs/kr/ + _root_keys.json
Run scripts/codegen.py to regenerate. Do not edit.
"""
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient


class OneviewClient(KoreanBaseClient):
    """Auto-generated client for target=oneview.

    All methods return plain dicts matching the API response schema.
    See _models_generated.py for Pydantic models.
    """

# ── oneview ──────────────────────────────────────
    def search_oneviews(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
    ) -> list[dict]:
        """[GENERATED] 한눈보기 목록 조회

        Args:
        query: 법령명에서 검색을 원하는 질의
        display: 검색된 결과 개수 (default=20 max=100)
        page: 검색 결과 페이지 (default=1)

        Returns:
            List of result dicts. Fields match the API response schema.
            Response path: items (item key not discovered)
        """
        params: dict = {"target": "oneview", "type": "JSON"}
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        response = self._make_request(self.BASE_URL, params=params)
        data = response.json()
        root = data.get("items", {})
        # item key unknown — return raw root
        return root if isinstance(root, list) else [root] if root else []

    def get_oneview_detail(
        self,
        mst: str | None = None,
        lm: str | None = None,
        ld: int | None = None,
        ln: int | None = None,
        jo: int | None = None,
    ) -> dict:
        """[GENERATED] 한눈보기 본문 조회

        Args:
        mst: 법령 마스터 번호 - 법령테이블의 lsi_seq 값을 의미함
        lm: 법령의 법령명
        ld: 법령의 공포일자
        ln: 법령의 공포번호
        jo: 조번호 생략(기본값) : 모든 조를 표시함 6자리숫자 : 조번호(4자리)+조가지번호(2자리) (000200 : 2조, 001002 : 10조의 2)

        Returns:
            Detail dict. Fields match the API response schema.
            Response path: items
        """
        params: dict = {"target": "oneview", "type": "JSON"}
        if mst is not None:
            params["MST"] = mst
        if lm is not None:
            params["LM"] = lm
        if ld is not None:
            params["LD"] = ld
        if ln is not None:
            params["LN"] = ln
        if jo is not None:
            params["JO"] = jo
        response = self._make_request(self.SERVICE_URL, params=params)
        data = response.json()
        return data.get("items", data)

