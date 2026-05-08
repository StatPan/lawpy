"""Committee decision module for Korean law API."""

from typing import Literal, TypeAlias, cast

from lawpy.kr.generated._models_generated import (
    AcrDetail,
    AcrList,
    BaipvcsDetail,
    BaipvcsList,
    EccDetail,
    EccList,
    EiacDetail,
    EiacList,
    FscDetail,
    FscList,
    FtcDetail,
    FtcList,
    IaciacDetail,
    IaciacList,
    KccDetail,
    KccList,
    NhrckDetail,
    NhrckList,
    NlrcDetail,
    NlrcList,
    OcltDetail,
    OcltList,
    PpcDetail,
    PpcList,
    SfcDetail,
    SfcList,
)
from lawpy.kr.generated.acr import GeneratedAcrClient
from lawpy.kr.generated.baiPvcs import GeneratedBaipvcsClient
from lawpy.kr.generated.ecc import GeneratedEccClient
from lawpy.kr.generated.eiac import GeneratedEiacClient
from lawpy.kr.generated.fsc import GeneratedFscClient
from lawpy.kr.generated.ftc import GeneratedFtcClient
from lawpy.kr.generated.iaciac import GeneratedIaciacClient
from lawpy.kr.generated.kcc import GeneratedKccClient
from lawpy.kr.generated.nhrck import GeneratedNhrckClient
from lawpy.kr.generated.nlrc import GeneratedNlrcClient
from lawpy.kr.generated.oclt import GeneratedOcltClient
from lawpy.kr.generated.ppc import GeneratedPpcClient
from lawpy.kr.generated.sfc import GeneratedSfcClient

CommitteeDecisionTarget = Literal[
    "acr",
    "baiPvcs",
    "ecc",
    "eiac",
    "fsc",
    "ftc",
    "iaciac",
    "kcc",
    "nhrck",
    "nlrc",
    "oclt",
    "ppc",
    "sfc",
]

CommitteeDecisionList: TypeAlias = (
    AcrList
    | BaipvcsList
    | EccList
    | EiacList
    | FscList
    | FtcList
    | IaciacList
    | KccList
    | NhrckList
    | NlrcList
    | OcltList
    | PpcList
    | SfcList
)

CommitteeDecisionDetail: TypeAlias = (
    AcrDetail
    | BaipvcsDetail
    | EccDetail
    | EiacDetail
    | FscDetail
    | FtcDetail
    | IaciacDetail
    | KccDetail
    | NhrckDetail
    | NlrcDetail
    | OcltDetail
    | PpcDetail
    | SfcDetail
)

COMMITTEE_DECISION_TARGETS: dict[CommitteeDecisionTarget, str] = {
    "acr": "국민권익위원회 결정문",
    "baiPvcs": "감사원 사전컨설팅 의견서",
    "ecc": "중앙환경분쟁조정위원회 결정문",
    "eiac": "고용보험심사위원회 결정문",
    "fsc": "금융위원회 결정문",
    "ftc": "공정거래위원회 결정문",
    "iaciac": "산업재해보상보험재심사위원회 결정문",
    "kcc": "방송미디어통신위원회 결정문",
    "nhrck": "국가인권위원회 결정문",
    "nlrc": "노동위원회 결정문",
    "oclt": "중앙토지수용위원회 결정문",
    "ppc": "개인정보보호위원회 결정문",
    "sfc": "증권선물위원회 결정문",
}


class CommitteeDecisionClient(
    GeneratedAcrClient,
    GeneratedBaipvcsClient,
    GeneratedEccClient,
    GeneratedEiacClient,
    GeneratedFscClient,
    GeneratedFtcClient,
    GeneratedIaciacClient,
    GeneratedKccClient,
    GeneratedNhrckClient,
    GeneratedNlrcClient,
    GeneratedOcltClient,
    GeneratedPpcClient,
    GeneratedSfcClient,
):
    """Client for committee decision APIs.

    This wrapper uses one stable pattern across committee-like generated
    targets. Pass the target code as ``committee`` and use the same search/detail
    method shape for all supported agencies.
    """

    def list_committee_decision_targets(self) -> dict[CommitteeDecisionTarget, str]:
        """Return supported committee decision target codes and labels."""
        return dict(COMMITTEE_DECISION_TARGETS)

    def search_committee_decisions(
        self,
        committee: CommitteeDecisionTarget,
        query: str | None = None,
        *,
        search_scope: int = 1,
        page: int = 1,
        per_page: int = 20,
        sort: str | None = None,
        alphabetical: str | None = None,
        popup: bool | None = None,
        response_date: int | None = None,
    ) -> list[CommitteeDecisionList]:
        """Search committee decisions or audit consultation opinions."""
        popup_flag = self._yn_flag(popup)
        if committee != "baiPvcs" and response_date is not None:
            msg = "response_date is only supported for committee='baiPvcs'."
            raise ValueError(msg)

        if committee == "acr":
            return cast(
                list[CommitteeDecisionList],
                self.search_acrs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "baiPvcs":
            return cast(
                list[CommitteeDecisionList],
                self.search_baiPvcss(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    date=response_date,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "ecc":
            return cast(
                list[CommitteeDecisionList],
                self.search_eccs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "eiac":
            return cast(
                list[CommitteeDecisionList],
                self.search_eiacs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "fsc":
            return cast(
                list[CommitteeDecisionList],
                self.search_fscs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "ftc":
            return cast(
                list[CommitteeDecisionList],
                self.search_ftcs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "iaciac":
            return cast(
                list[CommitteeDecisionList],
                self.search_iaciacs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "kcc":
            return cast(
                list[CommitteeDecisionList],
                self.search_kccs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "nhrck":
            return cast(
                list[CommitteeDecisionList],
                self.search_nhrcks(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "nlrc":
            return cast(
                list[CommitteeDecisionList],
                self.search_nlrcs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "oclt":
            return cast(
                list[CommitteeDecisionList],
                self.search_oclts(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "ppc":
            return cast(
                list[CommitteeDecisionList],
                self.search_ppcs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        if committee == "sfc":
            return cast(
                list[CommitteeDecisionList],
                self.search_sfcs(
                    search=search_scope,
                    query=query,
                    display=per_page,
                    page=page,
                    gana=alphabetical,
                    sort=sort,
                    popyn=popup_flag,
                ),
            )
        raise ValueError(self._unsupported_committee_message(committee))

    def get_committee_decision_detail(
        self,
        committee: CommitteeDecisionTarget,
        decision_id: str | None = None,
    ) -> CommitteeDecisionDetail:
        """Get committee decision or audit consultation opinion detail."""
        if committee == "acr":
            return cast(CommitteeDecisionDetail, self.get_acr_detail(id=decision_id))
        if committee == "baiPvcs":
            return cast(CommitteeDecisionDetail, self.get_baiPvcs_detail(id=decision_id))
        if committee == "ecc":
            return cast(CommitteeDecisionDetail, self.get_ecc_detail(id=decision_id))
        if committee == "eiac":
            return cast(CommitteeDecisionDetail, self.get_eiac_detail(id=decision_id))
        if committee == "fsc":
            return cast(CommitteeDecisionDetail, self.get_fsc_detail(id=decision_id))
        if committee == "ftc":
            return cast(CommitteeDecisionDetail, self.get_ftc_detail(id=decision_id))
        if committee == "iaciac":
            return cast(CommitteeDecisionDetail, self.get_iaciac_detail(id=decision_id))
        if committee == "kcc":
            return cast(CommitteeDecisionDetail, self.get_kcc_detail(id=decision_id))
        if committee == "nhrck":
            return cast(CommitteeDecisionDetail, self.get_nhrck_detail(id=decision_id))
        if committee == "nlrc":
            return cast(CommitteeDecisionDetail, self.get_nlrc_detail(id=decision_id))
        if committee == "oclt":
            return cast(CommitteeDecisionDetail, self.get_oclt_detail(id=decision_id))
        if committee == "ppc":
            return cast(CommitteeDecisionDetail, self.get_ppc_detail(id=decision_id))
        if committee == "sfc":
            return cast(CommitteeDecisionDetail, self.get_sfc_detail(id=decision_id))
        raise ValueError(self._unsupported_committee_message(committee))

    @staticmethod
    def _yn_flag(value: bool | None) -> str | None:
        if value is None:
            return None
        return "Y" if value else "N"

    @staticmethod
    def _unsupported_committee_message(committee: str) -> str:
        targets = ", ".join(COMMITTEE_DECISION_TARGETS)
        return f"Unsupported committee decision target {committee!r}. Expected one of: {targets}."
