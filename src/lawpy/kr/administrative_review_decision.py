"""Administrative review decision (행정심판례) module for Korean law API."""

from lawpy.kr.generated._models_generated import DeccDetail, DeccList
from lawpy.kr.generated.decc import GeneratedDeccClient


class AdministrativeReviewDecisionClient(GeneratedDeccClient):
    """Client for administrative review decision (행정심판례) APIs.

    This is a thin public wrapper over the generated ``decc`` target. It returns
    generated Pydantic models directly.
    """

    def search_administrative_review_decisions(
        self,
        query: str | None = None,
        *,
        search_scope: int = 1,
        decision_type_code: str | None = None,
        decision_date: int | None = None,
        disposition_date_range: str | None = None,
        resolution_date_range: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        alphabetical: str | None = None,
    ) -> list[DeccList]:
        """Search administrative review decisions (행정심판례 목록 조회)."""
        return self.search_deccs(
            search=search_scope,
            query=query,
            cls=decision_type_code,
            date=decision_date,
            dpayd=disposition_date_range,
            rslyd=resolution_date_range,
            display=per_page,
            page=page,
            sort=sort,
            gana=alphabetical,
        )

    def get_administrative_review_decision_detail(
        self,
        decision_id: str | None = None,
        decision_name: str | None = None,
    ) -> DeccDetail:
        """Get administrative review decision detail (행정심판례 본문 조회)."""
        return self.get_decc_detail(id=decision_id, lm=decision_name)
