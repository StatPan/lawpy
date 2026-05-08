"""Law reference and customized article modules for Korean law API."""

from typing import Literal, cast

from lawpy.kr.generated._models_generated import (
    CouseadmrulList,
    CouselsList,
    CouseordinList,
    DrlawList,
    EflawjosubList,
    LawjosubList,
    LnklsList,
    LnkordList,
    LsdelegatedDetail,
    OneviewDetail,
    OneviewList,
    ThdcmpDetail,
    ThdcmpList,
)
from lawpy.kr.generated.couseAdmrul import GeneratedCouseadmrulClient
from lawpy.kr.generated.couseLs import GeneratedCouselsClient
from lawpy.kr.generated.couseOrdin import GeneratedCouseordinClient
from lawpy.kr.generated.drlaw import GeneratedDrlawClient
from lawpy.kr.generated.eflawjosub import GeneratedEflawjosubClient
from lawpy.kr.generated.lawjosub import GeneratedLawjosubClient
from lawpy.kr.generated.lnkLs import GeneratedLnklsClient
from lawpy.kr.generated.lnkOrd import GeneratedLnkordClient
from lawpy.kr.generated.lsDelegated import GeneratedLsdelegatedClient
from lawpy.kr.generated.oneview import GeneratedOneviewClient
from lawpy.kr.generated.thdCmp import GeneratedThdcmpClient

CustomizedArticleSource = Literal["law", "administrative_rule", "ordinance"]
CustomizedArticleList = CouselsList | CouseadmrulList | CouseordinList


class LawReferenceClient(
    GeneratedCouselsClient,
    GeneratedCouseadmrulClient,
    GeneratedCouseordinClient,
    GeneratedLawjosubClient,
    GeneratedEflawjosubClient,
    GeneratedLnklsClient,
    GeneratedLnkordClient,
    GeneratedDrlawClient,
    GeneratedLsdelegatedClient,
    GeneratedOneviewClient,
    GeneratedThdcmpClient,
):
    """Client for customized article, link, and comparative law reference APIs."""

    def search_customized_articles(
        self,
        source: CustomizedArticleSource,
        classification_code: str,
        *,
        article_only: bool | None = None,
        page: int = 1,
        per_page: int = 20,
        popup: bool | None = None,
    ) -> list[CustomizedArticleList]:
        """Search customized article lists by law, administrative rule, or ordinance code."""
        lj_jo = self._yn_flag(article_only)
        popyn = self._yn_flag(popup)
        if source == "law":
            return cast(
                list[CustomizedArticleList],
                self.search_couseLss(
                    vcode=classification_code,
                    lj_jo=lj_jo,
                    display=per_page,
                    page=page,
                    popyn=popyn,
                ),
            )
        if source == "administrative_rule":
            return cast(
                list[CustomizedArticleList],
                self.search_couseAdmruls(
                    vcode=classification_code,
                    lj_jo=lj_jo,
                    display=per_page,
                    page=page,
                    popyn=popyn,
                ),
            )
        if source == "ordinance":
            return cast(
                list[CustomizedArticleList],
                self.search_couseOrdins(
                    vcode=classification_code,
                    lj_jo=lj_jo,
                    display=per_page,
                    page=page,
                    popyn=popyn,
                ),
            )
        msg = f"Unsupported customized article source: {source}"
        raise ValueError(msg)

    def search_law_article_units(
        self,
        law_id: str | None = None,
        *,
        mst: str | None = None,
        article: str | None = None,
        paragraph: str | None = None,
        subparagraph: str | None = None,
        item: str | None = None,
    ) -> list[LawjosubList]:
        """Search current-law article/paragraph/subparagraph/item units."""
        return self.search_lawjosubs(
            id=law_id,
            mst=mst,
            jo=article,
            hang=paragraph,
            ho=subparagraph,
            mok=item,
        )

    def search_effective_law_article_units(
        self,
        law_id: str | None = None,
        *,
        mst: str | None = None,
        effective_date: int | None = None,
        article: str | None = None,
        paragraph: str | None = None,
        subparagraph: str | None = None,
        item: str | None = None,
    ) -> list[EflawjosubList]:
        """Search effective-date law article/paragraph/subparagraph/item units."""
        return self.search_eflawjosubs(
            id=law_id,
            mst=mst,
            efyd=effective_date,
            jo=article,
            hang=paragraph,
            ho=subparagraph,
            mok=item,
        )

    def search_ordinance_links_by_law(
        self,
        query: str | None = None,
        *,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        popup: bool | None = None,
    ) -> list[LnklsList]:
        """Search local ordinance links from a law-oriented query."""
        return self.search_lnkLss(
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            popyn=self._yn_flag(popup),
        )

    def search_law_links_by_ordinance(
        self,
        query: str | None = None,
        *,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        popup: bool | None = None,
    ) -> list[LnkordList]:
        """Search law links from an ordinance-oriented query."""
        return self.search_lnkOrds(
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            popyn=self._yn_flag(popup),
        )

    def search_law_ordinance_link_status(
        self,
        query: str | None = None,
        *,
        page: int = 1,
        per_page: int = 20,
    ) -> list[DrlawList]:
        """Search law-local ordinance linkage status."""
        return self.search_drlaws(query=query, display=per_page, page=page)

    def get_delegated_law_detail(
        self,
        law_id: str | None = None,
        *,
        mst: str | None = None,
    ) -> LsdelegatedDetail:
        """Get delegated-law detail for a law ID or master sequence."""
        return self.get_lsDelegated_detail(id=law_id, mst=mst)

    def search_oneview_laws(
        self,
        query: str | None = None,
        *,
        page: int = 1,
        per_page: int = 20,
    ) -> list[OneviewList]:
        """Search one-view law summaries."""
        return self.search_oneviews(query=query, display=per_page, page=page)

    def get_oneview_law_detail(
        self,
        mst: str | None = None,
        *,
        law_name: str | None = None,
        promulgation_date: int | None = None,
        promulgation_number: int | None = None,
        article_number: int | None = None,
    ) -> OneviewDetail:
        """Get one-view law detail."""
        article_code = f"{article_number:04d}00" if article_number is not None else None
        return self.get_oneview_detail(
            mst=mst,
            lm=law_name,
            ld=promulgation_date,
            ln=promulgation_number,
            jo=cast(int | None, article_code),
        )

    def search_three_way_comparisons(
        self,
        query: str | None = None,
        *,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        enforcement_date_range: str | None = None,
        promulgation_date_range: str | None = None,
        promulgation_date: int | None = None,
        promulgation_number: int | None = None,
        promulgation_number_range: str | None = None,
        revision_type: str | None = None,
        org_code: str | None = None,
        law_kind: str | None = None,
        alphabetical: str | None = None,
        popup: bool | None = None,
    ) -> list[ThdcmpList]:
        """Search three-way law comparison records."""
        return self.search_thdCmps(
            query=query,
            display=per_page,
            page=page,
            sort=sort,
            efyd=enforcement_date_range,
            ancyd=promulgation_date_range,
            date=promulgation_date,
            nb=promulgation_number,
            ancno=promulgation_number_range,
            rrclscd=revision_type,
            org=org_code,
            knd=law_kind,
            gana=alphabetical,
            popyn=self._yn_flag(popup),
        )

    def get_three_way_comparison_detail(
        self,
        comparison_kind: int | None = None,
        *,
        law_id: str | None = None,
        mst: str | None = None,
        law_name: str | None = None,
        promulgation_date: int | None = None,
        promulgation_number: int | None = None,
    ) -> ThdcmpDetail:
        """Get three-way law comparison detail."""
        return self.get_thdCmp_detail(
            knd=comparison_kind,
            id=law_id,
            mst=mst,
            lm=law_name,
            ld=promulgation_date,
            ln=promulgation_number,
        )

    @staticmethod
    def _yn_flag(value: bool | None) -> str | None:
        if value is None:
            return None
        return "Y" if value else "N"
