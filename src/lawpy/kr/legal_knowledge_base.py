"""Legal knowledge-base module for Korean law API."""

from lawpy.kr.generated._models_generated import (
    AirltlsList,
    AisearchList,
    DlytrmList,
    DlytrmrltDetail,
    JorltlstrmDetail,
    LsrltList,
    LstrmaiList,
    LstrmrltDetail,
    LstrmrltjoDetail,
)
from lawpy.kr.generated.aiRltLs import GeneratedAirltlsClient
from lawpy.kr.generated.aiSearch import GeneratedAisearchClient
from lawpy.kr.generated.dlytrm import GeneratedDlytrmClient
from lawpy.kr.generated.dlytrmRlt import GeneratedDlytrmrltClient
from lawpy.kr.generated.joRltLstrm import GeneratedJorltlstrmClient
from lawpy.kr.generated.lsRlt import GeneratedLsrltClient
from lawpy.kr.generated.lstrmAI import GeneratedLstrmaiClient
from lawpy.kr.generated.lstrmRlt import GeneratedLstrmrltClient
from lawpy.kr.generated.lstrmRltJo import GeneratedLstrmrltjoClient


class LegalKnowledgeBaseClient(
    GeneratedLstrmaiClient,
    GeneratedDlytrmClient,
    GeneratedLstrmrltClient,
    GeneratedDlytrmrltClient,
    GeneratedLstrmrltjoClient,
    GeneratedJorltlstrmClient,
    GeneratedLsrltClient,
    GeneratedAisearchClient,
    GeneratedAirltlsClient,
):
    """Client for legal knowledge-base APIs."""

    def search_legal_knowledge_terms(
        self,
        query: str | None = None,
        *,
        homonym: bool | None = None,
        page: int = 1,
        per_page: int = 20,
    ) -> list[LstrmaiList]:
        """Search knowledge-base legal terms."""
        return self.search_lstrmAIs(
            query=query,
            homonymyn=self._yn_flag(homonym),
            display=per_page,
            page=page,
        )

    def search_daily_terms(
        self,
        query: str | None = None,
        *,
        page: int = 1,
        per_page: int = 20,
    ) -> list[DlytrmList]:
        """Search daily-language terms in the legal knowledge base."""
        return self.search_dlytrms(query=query, display=per_page, page=page)

    def get_legal_term_daily_term_relations(
        self,
        query: str | None = None,
        *,
        term_id: str | None = None,
        relation_code: int | None = None,
    ) -> LstrmrltDetail:
        """Get legal-term to daily-term relation data."""
        return self.get_lstrmRlt_detail(query=query, mst=term_id, trmrltcd=relation_code)

    def get_daily_term_legal_term_relations(
        self,
        query: str | None = None,
        *,
        term_id: str | None = None,
        relation_code: int | None = None,
    ) -> DlytrmrltDetail:
        """Get daily-term to legal-term relation data."""
        return self.get_dlytrmRlt_detail(query=query, mst=term_id, trmrltcd=relation_code)

    def get_legal_term_article_relations(self, query: str) -> LstrmrltjoDetail:
        """Get legal-term to article relation data."""
        return self.get_lstrmRltJo_detail(query=query)

    def get_article_legal_term_relations(
        self,
        query: str | None = None,
        *,
        law_id: int | None = None,
        article_number: int | None = None,
    ) -> JorltlstrmDetail:
        """Get article to legal-term relation data."""
        return self.get_joRltLstrm_detail(query=query, id=law_id, jo=article_number)

    def search_related_laws(
        self,
        query: str | None = None,
        *,
        law_id: int | None = None,
        relation_code: int | None = None,
    ) -> list[LsrltList]:
        """Search related laws."""
        return self.search_lsRlts(query=query, id=law_id, rltclscd=relation_code)

    def search_ai_laws(
        self,
        query: str | None = None,
        *,
        search_scope: int | None = None,
        page: int = 1,
        per_page: int = 20,
    ) -> list[AisearchList]:
        """Search laws through the intelligent law-search API."""
        return self.search_aiSearchs(search=search_scope, query=query, display=per_page, page=page)

    def search_ai_related_laws(
        self,
        query: str | None = None,
        *,
        search_scope: int | None = None,
    ) -> list[AirltlsList]:
        """Search AI-related law recommendations."""
        return self.search_aiRltLss(search=search_scope, query=query)

    @staticmethod
    def _yn_flag(value: bool | None) -> str | None:
        if value is None:
            return None
        return "Y" if value else "N"
