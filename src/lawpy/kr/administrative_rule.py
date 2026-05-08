"""Administrative rule (행정규칙) module for Korean law API."""

from lawpy.kr.generated._models_generated import AdmrulDetail, AdmrulList
from lawpy.kr.generated.admrul import GeneratedAdmrulClient


class AdministrativeRuleClient(GeneratedAdmrulClient):
    """Client for Administrative Rule (행정규칙) APIs.

    The law.go.kr ``admrul`` target covers administrative rules including:
    1=훈령, 2=예규, 3=고시, 4=공고, 5=지침, 6=기타.
    """

    def search_administrative_rules(
        self,
        query: str | None = None,
        *,
        rule_type: str | None = None,
        current: bool = True,
        search_scope: int = 1,
        org_code: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        issued_date: int | None = None,
        issued_date_range: str | None = None,
        modified_date_range: str | None = None,
        issue_number: int | None = None,
    ) -> list[AdmrulList]:
        """Search administrative rules (행정규칙 목록 조회).

        Args:
            query: Search query.
            rule_type: Rule type code. 1=훈령, 2=예규, 3=고시, 4=공고, 5=지침, 6=기타.
            current: True for current rules (nw=1), False for historical rules (nw=2).
            search_scope: 1=rule name, 2=full text.
            org_code: Ministry/agency code.
            page: Page number.
            per_page: Results per page, max 100.
            sort: Sort option accepted by law.go.kr.
            issued_date: Issued date as YYYYMMDD.
            issued_date_range: Issued date range, e.g. "20090101~20090130".
            modified_date_range: Modified date range, e.g. "20090101~20090130".
            issue_number: Issuance number search value.

        Returns:
            List of generated :class:`AdmrulList` models.
        """
        return self.search_admruls(
            nw=1 if current else 2,
            search=search_scope,
            query=query,
            display=per_page,
            page=page,
            org=org_code,
            knd=rule_type,
            sort=sort,
            date=issued_date,
            prmlyd=issued_date_range,
            modyd=modified_date_range,
            nb=issue_number,
        )

    def search_notices(
        self,
        query: str | None = None,
        *,
        current: bool = True,
        search_scope: int = 1,
        org_code: str | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        issued_date: int | None = None,
        issued_date_range: str | None = None,
        modified_date_range: str | None = None,
        issue_number: int | None = None,
    ) -> list[AdmrulList]:
        """Search notices (고시).

        law.go.kr exposes notices as administrative rules with ``knd=3``.
        """
        return self.search_administrative_rules(
            query=query,
            rule_type="3",
            current=current,
            search_scope=search_scope,
            org_code=org_code,
            page=page,
            per_page=per_page,
            sort=sort,
            issued_date=issued_date,
            issued_date_range=issued_date_range,
            modified_date_range=modified_date_range,
            issue_number=issue_number,
        )

    def get_administrative_rule_detail(
        self,
        rule_id: str | None = None,
        rule_name: str | None = None,
    ) -> AdmrulDetail:
        """Get administrative rule detail (행정규칙 본문 조회)."""
        return self.get_admrul_detail(id=rule_id, lm=rule_name)
