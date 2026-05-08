"""Client for target=drlaw (법령-자치법규 연계현황).
This target only supports XML output, not JSON.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import DrlawList


class GeneratedDrlawClient(KoreanBaseClient):
    """Client for target=drlaw (법령-자치법규 연계현황 조회).

    Uses XML parsing since this target does not support JSON output.
    """

    def search_drlaws(
        self,
        query: str | None = None,
        display: int | None = None,
        page: int | None = None,
    ) -> list[DrlawList]:
        """법령-자치법규 연계현황 목록 조회.

        Args:
            query: 검색어
            display: 검색결과 개수 (default=20, max=100)
            page: 검색 결과 페이지 (default=1)

        Returns:
            List of DrlawList instances parsed from XML response.
        """
        params: dict = {"target": "drlaw"}
        if query is not None:
            params["query"] = query
        if display is not None:
            params["display"] = display
        if page is not None:
            params["page"] = page
        data = self._make_xml_request(self.BASE_URL, params=params)
        law_data = data.get("law")
        if law_data is None:
            return []
        items = law_data if isinstance(law_data, list) else [law_data]
        return [DrlawList.model_validate(item) for item in items]


__all__ = ["GeneratedDrlawClient"]
