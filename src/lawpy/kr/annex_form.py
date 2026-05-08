"""Annex and form (별표·서식) module for Korean law API."""

from lawpy.kr.generated._models_generated import AdmbylList, LicbylList, OrdinbylList
from lawpy.kr.generated.admbyl import GeneratedAdmbylClient
from lawpy.kr.generated.licbyl import GeneratedLicbylClient
from lawpy.kr.generated.ordinbyl import GeneratedOrdinbylClient


class AnnexFormClient(GeneratedLicbylClient, GeneratedAdmbylClient, GeneratedOrdinbylClient):
    """Client for annex and form list APIs.

    This public wrapper groups the law.go.kr 별표·서식 targets:
    ``licbyl`` for laws, ``admbyl`` for administrative rules, and ``ordinbyl``
    for local ordinances.
    """

    def search_law_annex_forms(
        self,
        query: str | None = None,
        *,
        search_scope: int = 1,
        annex_type: str | None = None,
        org_code: str | None = None,
        alphabetical: str | None = None,
        mobile: bool | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
    ) -> list[LicbylList]:
        """Search law annexes and forms (법령 별표·서식 목록 조회)."""
        return self.search_licbyls(
            search=search_scope,
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            org=org_code,
            knd=annex_type,
            gana=alphabetical,
            mobileyn=self._mobile_flag(mobile),
        )

    def search_administrative_rule_annex_forms(
        self,
        query: str | None = None,
        *,
        search_scope: int = 1,
        annex_type: str | None = None,
        org_code: str | None = None,
        alphabetical: str | None = None,
        mobile: bool | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
    ) -> list[AdmbylList]:
        """Search administrative-rule annexes and forms (행정규칙 별표·서식 목록 조회)."""
        return self.search_admbyls(
            search=search_scope,
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            org=org_code,
            knd=annex_type,
            gana=alphabetical,
            mobileyn=self._mobile_flag(mobile),
        )

    def search_ordinance_annex_forms(
        self,
        query: str | None = None,
        *,
        search_scope: int = 1,
        annex_type: str | None = None,
        org_code: str | None = None,
        alphabetical: str | None = None,
        mobile: bool | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
    ) -> list[OrdinbylList]:
        """Search ordinance annexes and forms (자치법규 별표·서식 목록 조회)."""
        return self.search_ordinbyls(
            search=search_scope,
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            org=org_code,
            knd=annex_type,
            gana=alphabetical,
            mobileyn=self._mobile_flag(mobile),
        )

    @staticmethod
    def _mobile_flag(mobile: bool | None) -> str | None:
        if mobile is None:
            return None
        return "Y" if mobile else "N"
