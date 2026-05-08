"""Local ordinance (자치법규) module for Korean law API."""

from lawpy.kr.generated._models_generated import OrdinDetail, OrdinList
from lawpy.kr.generated.ordin import GeneratedOrdinClient


class OrdinanceClient(GeneratedOrdinClient):
    """Client for Local Ordinance (자치법규) APIs.

    The law.go.kr ``ordin`` target covers local ordinances including:
    30001=조례, 30002=규칙, 30003=훈령, 30004=예규, 30006=기타,
    30010=고시, 30011=의회규칙.
    """

    def search_ordinances(
        self,
        query: str | None = None,
        *,
        ordinance_type: str | None = None,
        current: bool = True,
        search_scope: int = 1,
        org_code: str | None = None,
        sub_org_code: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        promulgation_date: int | None = None,
        enforcement_date_range: str | None = None,
        promulgation_date_range: str | None = None,
        promulgation_number_range: str | None = None,
        promulgation_number: int | None = None,
        revision_type: str | None = None,
        field_code: int | None = None,
        chapter_code: str | None = None,
        alphabetical: str | None = None,
    ) -> list[OrdinList]:
        """Search local ordinances (자치법규 목록 조회).

        Args:
            query: Search query.
            ordinance_type: Ordinance type code. 30001=조례, 30002=규칙, 30010=고시.
            current: True for current ordinances (nw=1), False for historical ordinances (nw=2).
            search_scope: 1=ordinance name, 2=full text.
            org_code: Province/metropolitan government code.
            sub_org_code: City/county/district code. Requires ``org_code``.
            page: Page number.
            per_page: Results per page, max 100.
            sort: Sort option accepted by law.go.kr.
            promulgation_date: Promulgation date as YYYYMMDD.
            enforcement_date_range: Enforcement date range, e.g. "20090101~20090130".
            promulgation_date_range: Promulgation date range, e.g. "20090101~20090130".
            promulgation_number_range: Promulgation number range, e.g. "306~400".
            promulgation_number: Promulgation number search value.
            revision_type: Revision type code.
            field_code: Local ordinance field code.
            chapter_code: Law field chapter code.
            alphabetical: Korean alphabetical search key accepted by law.go.kr.

        Returns:
            List of generated :class:`OrdinList` models.
        """
        return self.search_ordins(
            nw=1 if current else 2,
            search=search_scope,
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            date=promulgation_date,
            efyd=enforcement_date_range,
            ancyd=promulgation_date_range,
            ancno=promulgation_number_range,
            nb=promulgation_number,
            org=org_code,
            sborg=sub_org_code,
            knd=ordinance_type,
            rrclscd=revision_type,
            ordinfd=field_code,
            lschapno=chapter_code,
            gana=alphabetical,
        )

    def search_local_notices(
        self,
        query: str | None = None,
        *,
        current: bool = True,
        search_scope: int = 1,
        org_code: str | None = None,
        sub_org_code: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        promulgation_date: int | None = None,
        enforcement_date_range: str | None = None,
        promulgation_date_range: str | None = None,
        promulgation_number_range: str | None = None,
        promulgation_number: int | None = None,
        revision_type: str | None = None,
        field_code: int | None = None,
        chapter_code: str | None = None,
        alphabetical: str | None = None,
    ) -> list[OrdinList]:
        """Search local notices (자치법규 고시).

        law.go.kr exposes local notices as local ordinances with ``knd=30010``.
        """
        return self.search_ordinances(
            query=query,
            ordinance_type="30010",
            current=current,
            search_scope=search_scope,
            org_code=org_code,
            sub_org_code=sub_org_code,
            page=page,
            per_page=per_page,
            sort=sort,
            promulgation_date=promulgation_date,
            enforcement_date_range=enforcement_date_range,
            promulgation_date_range=promulgation_date_range,
            promulgation_number_range=promulgation_number_range,
            promulgation_number=promulgation_number,
            revision_type=revision_type,
            field_code=field_code,
            chapter_code=chapter_code,
            alphabetical=alphabetical,
        )

    def get_ordinance_detail(
        self,
        ordinance_id: str | None = None,
        mst: str | None = None,
    ) -> OrdinDetail:
        """Get local ordinance detail (자치법규 본문 조회)."""
        return self.get_ordin_detail(id=ordinance_id, mst=mst)

