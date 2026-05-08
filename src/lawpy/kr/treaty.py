"""Treaty (조약) module for Korean law API."""

from lawpy.kr.generated._models_generated import TrtyDetail, TrtyList
from lawpy.kr.generated.trty import GeneratedTrtyClient


class TreatyClient(GeneratedTrtyClient):
    """Client for Treaty (조약) APIs."""

    def search_treaties(
        self,
        query: str | None = None,
        *,
        search_scope: int | None = None,
        treaty_class: int | None = None,
        effective_date_range: str | None = None,
        conclusion_date_range: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        alphabetical: str | None = None,
    ) -> list[TrtyList]:
        """Search treaties (조약 목록 조회).

        Args:
            query: Treaty search query.
            search_scope: 1=treaty name, 2=full text.
            treaty_class: 1=bilateral treaty, 2=multilateral treaty.
            effective_date_range: Effective date range, e.g. "20090101~20090130".
            conclusion_date_range: Conclusion date range, e.g. "20090101~20090130".
            page: Page number.
            per_page: Results per page, max 100.
            sort: Sort option accepted by law.go.kr.
            alphabetical: Korean dictionary prefix search code, passed as ``gana``.

        Returns:
            List of generated :class:`TrtyList` models.
        """
        return self.search_trtys(
            search=search_scope,
            query=query,
            cls=treaty_class,
            eftyd=effective_date_range,
            concyd=conclusion_date_range,
            page=page,
            display=per_page,
            sort=sort,
            gana=alphabetical,
        )

    def get_treaty_detail(self, treaty_id: str) -> TrtyDetail:
        """Get treaty detail (조약 본문 조회)."""
        return self.get_trty_detail(id=treaty_id)
