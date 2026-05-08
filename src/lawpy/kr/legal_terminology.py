"""Legal terminology (법령용어) module for Korean law API."""

from lawpy.kr.generated._models_generated import LstrmDetail, LstrmList
from lawpy.kr.generated.lstrm import GeneratedLstrmClient


class LegalTerminologyClient(GeneratedLstrmClient):
    """Client for legal terminology (법령용어) APIs."""

    def search_legal_terms(
        self,
        query: str | None = None,
        *,
        law_kind_code: int | None = None,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        alphabetical: str | None = None,
    ) -> list[LstrmList]:
        """Search legal terms (법령용어 목록 조회).

        Args:
            query: Legal term search query.
            law_kind_code: Legal dictionary kind code. 010101=법령, 010102=행정규칙.
            page: Page number.
            per_page: Results per page, max 100.
            sort: Sort option accepted by law.go.kr.
            alphabetical: Korean dictionary prefix search code, passed as ``gana``.

        Returns:
            List of generated :class:`LstrmList` models.
        """
        return self.search_lstrms(
            query=query,
            dickndcd=law_kind_code,
            display=per_page,
            page=page,
            sort=sort,
            gana=alphabetical,
        )

    def get_legal_term_detail(self, term: str) -> LstrmDetail:
        """Get legal term detail (법령용어 본문 조회)."""
        return self.get_lstrm_detail(query=term)
