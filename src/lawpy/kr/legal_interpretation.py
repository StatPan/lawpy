"""Legal interpretation (법령해석례) module for Korean law API."""

from lawpy.kr.generated._models_generated import ExpcDetail, ExpcList
from lawpy.kr.generated.expc import GeneratedExpcClient


class LegalInterpretationClient(GeneratedExpcClient):
    """Client for Legal Interpretation (법령해석례) APIs.

    This is a thin public wrapper over the generated ``expc`` target. It returns
    generated Pydantic models directly.
    """

    def search_legal_interpretations(
        self,
        query: str | None = None,
        *,
        search_scope: int = 1,
        inquiry_agency: str | None = None,
        reply_agency_code: int | None = None,
        item_number: int | None = None,
        registered_date_range: str | None = None,
        interpretation_date_range: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        alphabetical: str | None = None,
    ) -> list[ExpcList]:
        """Search legal interpretation cases (법령해석례 목록 조회)."""
        return self.search_expcs(
            search=search_scope,
            query=query,
            inq=inquiry_agency,
            rpl=reply_agency_code,
            itmno=item_number,
            regyd=registered_date_range,
            explyd=interpretation_date_range,
            display=per_page,
            page=page,
            sort=sort,
            gana=alphabetical,
        )

    def get_legal_interpretation_detail(
        self,
        interpretation_id: int | None = None,
        interpretation_name: str | None = None,
    ) -> ExpcDetail:
        """Get legal interpretation detail (법령해석례 본문 조회)."""
        return self.get_expc_detail(id=interpretation_id, lm=interpretation_name)
