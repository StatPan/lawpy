"""Constitutional decision (헌재결정례) module for Korean law API."""

from lawpy.kr.generated._models_generated import DetcDetail, DetcList
from lawpy.kr.generated.detc import GeneratedDetcClient


class ConstitutionalDecisionClient(GeneratedDetcClient):
    """Client for constitutional decision (헌재결정례) APIs.

    This is a thin public wrapper over the generated ``detc`` target. It returns
    generated Pydantic models directly.
    """

    def search_constitutional_decisions(
        self,
        query: str | None = None,
        *,
        search_scope: int = 1,
        decision_date: int | None = None,
        case_number: int | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        alphabetical: str | None = None,
    ) -> list[DetcList]:
        """Search constitutional decisions (헌재결정례 목록 조회)."""
        return self.search_detcs(
            search=search_scope,
            query=query,
            date=decision_date,
            nb=case_number,
            display=per_page,
            page=page,
            sort=sort,
            gana=alphabetical,
        )

    def get_constitutional_decision_detail(
        self,
        decision_id: str | None = None,
        decision_name: str | None = None,
    ) -> DetcDetail:
        """Get constitutional decision detail (헌재결정례 본문 조회)."""
        return self.get_detc_detail(id=decision_id, lm=decision_name)
