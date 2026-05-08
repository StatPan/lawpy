"""School, corporation, and public institution rule module for Korean law API."""

from lawpy.kr.generated._models_generated import SchoolDetail, SchoolList
from lawpy.kr.generated.school import GeneratedSchoolClient


class SchoolPublicRuleClient(GeneratedSchoolClient):
    """Client for school, corporation, and public institution rule APIs."""

    def search_school_public_rules(
        self,
        query: str | None = None,
        *,
        current: bool | None = None,
        search_scope: int = 1,
        category: str | None = None,
        revision_code: str | None = None,
        promulgation_date: int | None = None,
        promulgation_date_range: str | None = None,
        promulgation_number: int | None = None,
        alphabetical: str | None = None,
        popup: bool | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
    ) -> list[SchoolList]:
        """Search school, corporation, and public institution rules."""
        return self.search_schools(
            nw=self._current_flag(current),
            search=search_scope,
            query=query,
            display=per_page,
            page=page,
            knd=category,
            rrclscd=revision_code,
            date=promulgation_date,
            prmlyd=promulgation_date_range,
            nb=promulgation_number,
            gana=alphabetical,
            sort=sort,
            popyn=self._popup_flag(popup),
        )

    def get_school_public_rule_detail(
        self,
        rule_id: str | None = None,
        *,
        rule_lid: str | None = None,
        rule_name: str | None = None,
    ) -> SchoolDetail:
        """Get a school, corporation, or public institution rule detail."""
        return self.get_school_detail(id=rule_id, lid=rule_lid, lm=rule_name)

    @staticmethod
    def _current_flag(current: bool | None) -> int | None:
        if current is None:
            return None
        return 1 if current else 2

    @staticmethod
    def _popup_flag(popup: bool | None) -> str | None:
        if popup is None:
            return None
        return "Y" if popup else "N"
