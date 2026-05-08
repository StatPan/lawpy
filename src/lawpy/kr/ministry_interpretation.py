"""Ministry first-interpretation module for Korean law API."""

from collections.abc import Callable
from inspect import signature
from typing import Literal, cast

from pydantic import BaseModel

from lawpy.kr.generated.dapaCgmExpc import GeneratedDapacgmexpcClient
from lawpy.kr.generated.kcgCgmExpc import GeneratedKcgcgmexpcClient
from lawpy.kr.generated.kcsCgmExpc import GeneratedKcscgmexpcClient
from lawpy.kr.generated.kdcaCgmExpc import GeneratedKdcacgmexpcClient
from lawpy.kr.generated.kfsCgmExpc import GeneratedKfscgmexpcClient
from lawpy.kr.generated.khsCgmExpc import GeneratedKhscgmexpcClient
from lawpy.kr.generated.kipoCgmExpc import GeneratedKipocgmexpcClient
from lawpy.kr.generated.kmaCgmExpc import GeneratedKmacgmexpcClient
from lawpy.kr.generated.kostatCgmExpc import GeneratedKostatcgmexpcClient
from lawpy.kr.generated.mafraCgmExpc import GeneratedMafracgmexpcClient
from lawpy.kr.generated.mcstCgmExpc import GeneratedMcstcgmexpcClient
from lawpy.kr.generated.meCgmExpc import GeneratedMecgmexpcClient
from lawpy.kr.generated.mfdsCgmExpc import GeneratedMfdscgmexpcClient
from lawpy.kr.generated.mmaCgmExpc import GeneratedMmacgmexpcClient
from lawpy.kr.generated.mndCgmExpc import GeneratedMndcgmexpcClient
from lawpy.kr.generated.moeCgmExpc import GeneratedMoecgmexpcClient
from lawpy.kr.generated.moefCgmExpc import GeneratedMoefcgmexpcClient
from lawpy.kr.generated.moelCgmExpc import GeneratedMoelcgmexpcClient
from lawpy.kr.generated.mofaCgmExpc import GeneratedMofacgmexpcClient
from lawpy.kr.generated.mofCgmExpc import GeneratedMofcgmexpcClient
from lawpy.kr.generated.mogefCgmExpc import GeneratedMogefcgmexpcClient
from lawpy.kr.generated.mohwCgmExpc import GeneratedMohwcgmexpcClient
from lawpy.kr.generated.moisCgmExpc import GeneratedMoiscgmexpcClient
from lawpy.kr.generated.mojCgmExpc import GeneratedMojcgmexpcClient
from lawpy.kr.generated.molegCgmExpc import GeneratedMolegcgmexpcClient
from lawpy.kr.generated.molitCgmExpc import GeneratedMolitcgmexpcClient
from lawpy.kr.generated.motieCgmExpc import GeneratedMotiecgmexpcClient
from lawpy.kr.generated.mouCgmExpc import GeneratedMoucgmexpcClient
from lawpy.kr.generated.mpmCgmExpc import GeneratedMpmcgmexpcClient
from lawpy.kr.generated.mpvaCgmExpc import GeneratedMpvacgmexpcClient
from lawpy.kr.generated.msitCgmExpc import GeneratedMsitcgmexpcClient
from lawpy.kr.generated.mssCgmExpc import GeneratedMsscgmexpcClient
from lawpy.kr.generated.naaccCgmExpc import GeneratedNaacccgmexpcClient
from lawpy.kr.generated.nfaCgmExpc import GeneratedNfacgmexpcClient
from lawpy.kr.generated.npaCgmExpc import GeneratedNpacgmexpcClient
from lawpy.kr.generated.ntsCgmExpc import GeneratedNtscgmexpcClient
from lawpy.kr.generated.okaCgmExpc import GeneratedOkacgmexpcClient
from lawpy.kr.generated.ppsCgmExpc import GeneratedPpscgmexpcClient
from lawpy.kr.generated.rdaCgmExpc import GeneratedRdacgmexpcClient

MinistryInterpretationTarget = Literal[
    "dapaCgmExpc",
    "kcgCgmExpc",
    "kcsCgmExpc",
    "kdcaCgmExpc",
    "kfsCgmExpc",
    "khsCgmExpc",
    "kipoCgmExpc",
    "kmaCgmExpc",
    "kostatCgmExpc",
    "mafraCgmExpc",
    "mcstCgmExpc",
    "meCgmExpc",
    "mfdsCgmExpc",
    "mmaCgmExpc",
    "mndCgmExpc",
    "moeCgmExpc",
    "moefCgmExpc",
    "moelCgmExpc",
    "mofCgmExpc",
    "mofaCgmExpc",
    "mogefCgmExpc",
    "mohwCgmExpc",
    "moisCgmExpc",
    "mojCgmExpc",
    "molegCgmExpc",
    "molitCgmExpc",
    "motieCgmExpc",
    "mouCgmExpc",
    "mpmCgmExpc",
    "mpvaCgmExpc",
    "msitCgmExpc",
    "mssCgmExpc",
    "naaccCgmExpc",
    "nfaCgmExpc",
    "npaCgmExpc",
    "ntsCgmExpc",
    "okaCgmExpc",
    "ppsCgmExpc",
    "rdaCgmExpc",
]

MINISTRY_INTERPRETATION_TARGETS: dict[MinistryInterpretationTarget, str] = {
    "dapaCgmExpc": "방위사업청 법령해석",
    "kcgCgmExpc": "해양경찰청 법령해석",
    "kcsCgmExpc": "관세청 법령해석",
    "kdcaCgmExpc": "질병관리청 법령해석",
    "kfsCgmExpc": "산림청 법령해석",
    "khsCgmExpc": "국가유산청 법령해석",
    "kipoCgmExpc": "지식재산처 법령해석",
    "kmaCgmExpc": "기상청 법령해석",
    "kostatCgmExpc": "국가데이터처 법령해석",
    "mafraCgmExpc": "농림축산식품부 법령해석",
    "mcstCgmExpc": "문화체육관광부 법령해석",
    "meCgmExpc": "기후에너지환경부 법령해석",
    "mfdsCgmExpc": "식품의약품안전처 법령해석",
    "mmaCgmExpc": "병무청 법령해석",
    "mndCgmExpc": "국방부 법령해석",
    "moeCgmExpc": "교육부 법령해석",
    "moefCgmExpc": "재정경제부 법령해석",
    "moelCgmExpc": "고용노동부 법령해석",
    "mofCgmExpc": "해양수산부 법령해석",
    "mofaCgmExpc": "외교부 법령해석",
    "mogefCgmExpc": "여성가족부 법령해석",
    "mohwCgmExpc": "보건복지부 법령해석",
    "moisCgmExpc": "행정안전부 법령해석",
    "mojCgmExpc": "법무부 법령해석",
    "molegCgmExpc": "법제처 법령해석",
    "molitCgmExpc": "국토교통부 법령해석",
    "motieCgmExpc": "산업통상부 법령해석",
    "mouCgmExpc": "통일부 법령해석",
    "mpmCgmExpc": "인사혁신처 법령해석",
    "mpvaCgmExpc": "국가보훈부 법령해석",
    "msitCgmExpc": "과학기술정보통신부 법령해석",
    "mssCgmExpc": "중소벤처기업부 법령해석",
    "naaccCgmExpc": "행정중심복합도시건설청 법령해석",
    "nfaCgmExpc": "소방청 법령해석",
    "npaCgmExpc": "경찰청 법령해석",
    "ntsCgmExpc": "국세청 법령해석",
    "okaCgmExpc": "재외동포청 법령해석",
    "ppsCgmExpc": "조달청 법령해석",
    "rdaCgmExpc": "농촌진흥청 법령해석",
}

_LIST_ONLY_TARGETS: frozenset[MinistryInterpretationTarget] = frozenset(
    {"moefCgmExpc", "ntsCgmExpc"}
)


class MinistryInterpretationClient(
    GeneratedDapacgmexpcClient,
    GeneratedKcgcgmexpcClient,
    GeneratedKcscgmexpcClient,
    GeneratedKdcacgmexpcClient,
    GeneratedKfscgmexpcClient,
    GeneratedKhscgmexpcClient,
    GeneratedKipocgmexpcClient,
    GeneratedKmacgmexpcClient,
    GeneratedKostatcgmexpcClient,
    GeneratedMafracgmexpcClient,
    GeneratedMcstcgmexpcClient,
    GeneratedMecgmexpcClient,
    GeneratedMfdscgmexpcClient,
    GeneratedMmacgmexpcClient,
    GeneratedMndcgmexpcClient,
    GeneratedMoecgmexpcClient,
    GeneratedMoefcgmexpcClient,
    GeneratedMoelcgmexpcClient,
    GeneratedMofcgmexpcClient,
    GeneratedMofacgmexpcClient,
    GeneratedMogefcgmexpcClient,
    GeneratedMohwcgmexpcClient,
    GeneratedMoiscgmexpcClient,
    GeneratedMojcgmexpcClient,
    GeneratedMolegcgmexpcClient,
    GeneratedMolitcgmexpcClient,
    GeneratedMotiecgmexpcClient,
    GeneratedMoucgmexpcClient,
    GeneratedMpmcgmexpcClient,
    GeneratedMpvacgmexpcClient,
    GeneratedMsitcgmexpcClient,
    GeneratedMsscgmexpcClient,
    GeneratedNaacccgmexpcClient,
    GeneratedNfacgmexpcClient,
    GeneratedNpacgmexpcClient,
    GeneratedNtscgmexpcClient,
    GeneratedOkacgmexpcClient,
    GeneratedPpscgmexpcClient,
    GeneratedRdacgmexpcClient,
):
    """Client for ministry first-interpretation APIs."""

    def list_ministry_interpretation_targets(self) -> dict[MinistryInterpretationTarget, str]:
        """Return supported ministry interpretation target codes and labels."""
        return dict(MINISTRY_INTERPRETATION_TARGETS)

    def search_ministry_interpretations(
        self,
        ministry: MinistryInterpretationTarget,
        query: str | None = None,
        *,
        search_scope: int = 1,
        page: int = 1,
        per_page: int = 20,
        question_agency_code: int | None = None,
        interpretation_agency_code: int | None = None,
        agenda_number: int | None = None,
        interpretation_date_range: str | None = None,
        sort: str | None = None,
        alphabetical: str | None = None,
        popup: bool | None = None,
        fields: str | None = None,
    ) -> list[BaseModel]:
        """Search ministry first-interpretation records."""
        self._validate_ministry(ministry)
        method = cast(Callable[..., list[BaseModel]], getattr(self, f"search_{ministry}s"))
        params = self._supported_kwargs(
            method,
            {
                "search": search_scope,
                "query": query,
                "display": per_page,
                "page": page,
                "inq": question_agency_code,
                "rpl": interpretation_agency_code,
                "gana": alphabetical,
                "itmno": agenda_number,
                "explyd": interpretation_date_range,
                "sort": sort,
                "popyn": self._yn_flag(popup),
                "fields": fields,
            },
        )
        return method(**params)

    def get_ministry_interpretation_detail(
        self,
        ministry: MinistryInterpretationTarget,
        interpretation_id: int | None = None,
        interpretation_name: str | None = None,
        *,
        fields: str | None = None,
    ) -> BaseModel:
        """Get ministry first-interpretation detail where the target supports it."""
        self._validate_ministry(ministry)
        if ministry in _LIST_ONLY_TARGETS:
            msg = f"Target {ministry!r} exposes list search only in the generated spec."
            raise ValueError(msg)

        method = cast(Callable[..., BaseModel], getattr(self, f"get_{ministry}_detail"))
        return method(id=interpretation_id, lm=interpretation_name, fields=fields)

    @staticmethod
    def _yn_flag(value: bool | None) -> str | None:
        if value is None:
            return None
        return "Y" if value else "N"

    @staticmethod
    def _validate_ministry(ministry: str) -> None:
        if ministry in MINISTRY_INTERPRETATION_TARGETS:
            return
        targets = ", ".join(MINISTRY_INTERPRETATION_TARGETS)
        msg = f"Unsupported ministry interpretation target {ministry!r}. Expected one of: {targets}."
        raise ValueError(msg)

    @staticmethod
    def _supported_kwargs(method: Callable[..., object], params: dict[str, object]) -> dict[str, object]:
        supported = signature(method).parameters
        return {key: value for key, value in params.items() if key in supported}
