# KR Generated API Coverage

> Last updated: 2026-05-08

This document is the source of truth for Korean law.go.kr spec-generated API coverage in `lawpy`.

## v1 Gate

- Spec files tracked in `specs/kr`: 195
- Generated client modules in `src/lawpy/kr/generated`: 98
- Generated tests in `tests/test_generated`: 98
- Missing generated tests: 0

`scripts/codegen.py` handles 96 generic targets, including standard
`ListGuide` / `InfoGuide` targets and the suffix-less 법령정보지식베이스 guides.
It keeps special generated model support for `drlaw` and `lsDelegated`, whose
responses do not fit the generic JSON list/detail pattern.

For v1, "generated coverage" means every generated KR module has:

- a generated client module
- typed Pydantic models where the endpoint response is modeled
- at least one generated test file covering search/detail behavior available for that target

Public wrappers are tracked separately. They are the ergonomic API layer intended for `KRClient` and `datapan-data` workflows.
`KoreanLawClient` is kept as a compatibility alias for existing code.
See [KR Generated Client to Public Wrapper Policy](public-wrapper-policy.md) for wrapper promotion rules.

## Public Wrapper Status

| Target | Public surface | Status |
| --- | --- | --- |
| `law` | `LawClient`, `KRClient` | implemented |
| `prec` | `PrecedentClient`, `KRClient` | implemented |
| `admrul` | `AdministrativeRuleClient`, `KRClient` | implemented |
| `licbyl` | `AnnexFormClient`, `KRClient` | implemented as annex/form wrapper |
| `admbyl` | `AnnexFormClient`, `KRClient` | implemented as annex/form wrapper |
| `ordinbyl` | `AnnexFormClient`, `KRClient` | implemented as annex/form wrapper |
| `ordin` | `OrdinanceClient`, `KRClient` | implemented |
| `lstrm` | `LegalTerminologyClient`, `KRClient` | implemented |
| `expc` | `LegalInterpretationClient`, `KRClient` | implemented |
| `detc` | `ConstitutionalDecisionClient`, `KRClient` | implemented |
| `decc` | `AdministrativeReviewDecisionClient`, `KRClient` | implemented |
| `trty` | `TreatyClient`, `KRClient` | implemented |
| `elaw` | `LawClient`, `KRClient` | implemented as law-family wrapper |
| `oldAndNew` | `LawClient`, `KRClient` | implemented as law-family wrapper |
| `lsAbrv` | `LawClient`, `KRClient` | implemented as law-family wrapper |
| `lsHstInf` | `LawClient`, `KRClient` | implemented as law-family wrapper |
| `lsJoHstInf` | `LawClient`, `KRClient` | implemented as law-family wrapper |
| `lstrmAI` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `dlytrm` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `lstrmRlt` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `dlytrmRlt` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `lstrmRltJo` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `joRltLstrm` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `lsRlt` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `aiSearch` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `aiRltLs` | `LegalKnowledgeBaseClient`, `KRClient` | implemented as legal knowledge-base wrapper |
| `acr` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `baiPvcs` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `ecc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `eiac` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `fsc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `ftc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `iaciac` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `kcc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `nhrck` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `nlrc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `oclt` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `ppc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `sfc` | `CommitteeDecisionClient`, `KRClient` | implemented as committee decision wrapper |
| `dapaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kcgCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kcsCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kdcaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kfsCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `khsCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kipoCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kmaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `kostatCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mafraCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mcstCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `meCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mfdsCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mmaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mndCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `moeCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `moefCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `moelCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mofCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mofaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mogefCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mohwCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `moisCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mojCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `molegCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `molitCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `motieCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mouCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mpmCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mpvaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `msitCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `mssCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `naaccCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `nfaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `npaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `ntsCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `okaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `ppsCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |
| `rdaCgmExpc` | `MinistryInterpretationClient`, `KRClient` | implemented as ministry interpretation wrapper |

## Generated Matrix

| Target | Generated client | Methods | Models | Generated tests | Public wrapper |
| --- | --- | --- | --- | --- | --- |
| `acr` | `GeneratedAcrClient` | `search_acrs`, `get_acr_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `acrSpecialDecc` | `GeneratedAcrspecialdeccClient` | `search_acrSpecialDeccs`, `get_acrSpecialDecc_detail` | yes | yes | generated only |
| `adapSpecialDecc` | `GeneratedAdapspecialdeccClient` | `search_adapSpecialDeccs`, `get_adapSpecialDecc_detail` | yes | yes | generated only |
| `admbyl` | `GeneratedAdmbylClient` | `search_admbyls` | yes | yes | `AnnexFormClient`, `KRClient` |
| `admrul` | `GeneratedAdmrulClient` | `search_admruls`, `get_admrul_detail` | yes | yes | `AdministrativeRuleClient`, `KRClient` |
| `admrulOldAndNew` | `GeneratedAdmruloldandnewClient` | `search_admrulOldAndNews`, `get_admrulOldAndNew_detail` | yes | yes | generated only |
| `aiRltLs` | `GeneratedAirltlsClient` | `search_aiRltLss` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `aiSearch` | `GeneratedAisearchClient` | `search_aiSearchs` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `baiPvcs` | `GeneratedBaipvcsClient` | `search_baiPvcss`, `get_baiPvcs_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `couseAdmrul` | `GeneratedCouseadmrulClient` | `search_couseAdmruls` | yes | yes | generated only |
| `couseLs` | `GeneratedCouselsClient` | `search_couseLss` | yes | yes | generated only |
| `couseOrdin` | `GeneratedCouseordinClient` | `search_couseOrdins` | yes | yes | generated only |
| `dapaCgmExpc` | `GeneratedDapacgmexpcClient` | `search_dapaCgmExpcs`, `get_dapaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `decc` | `GeneratedDeccClient` | `search_deccs`, `get_decc_detail` | yes | yes | `AdministrativeReviewDecisionClient`, `KRClient` |
| `detc` | `GeneratedDetcClient` | `search_detcs`, `get_detc_detail` | yes | yes | `ConstitutionalDecisionClient`, `KRClient` |
| `drlaw` | `GeneratedDrlawClient` | `search_drlaws` | yes | yes | generated only |
| `dlytrm` | `GeneratedDlytrmClient` | `search_dlytrms` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `dlytrmRlt` | `GeneratedDlytrmrltClient` | `get_dlytrmRlt_detail` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `ecc` | `GeneratedEccClient` | `search_eccs`, `get_ecc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `eflaw` | `GeneratedEflawClient` | `search_eflaws`, `get_eflaw_detail` | yes | yes | generated only |
| `eflawjosub` | `GeneratedEflawjosubClient` | `search_eflawjosubs` | yes | yes | generated only |
| `eiac` | `GeneratedEiacClient` | `search_eiacs`, `get_eiac_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `elaw` | `GeneratedElawClient` | `search_elaws`, `get_elaw_detail` | yes | yes | `LawClient`, `KRClient` |
| `expc` | `GeneratedExpcClient` | `search_expcs`, `get_expc_detail` | yes | yes | `LegalInterpretationClient`, `KRClient` |
| `fsc` | `GeneratedFscClient` | `search_fscs`, `get_fsc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `ftc` | `GeneratedFtcClient` | `search_ftcs`, `get_ftc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `iaciac` | `GeneratedIaciacClient` | `search_iaciacs`, `get_iaciac_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `joRltLstrm` | `GeneratedJorltlstrmClient` | `get_joRltLstrm_detail` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `kcc` | `GeneratedKccClient` | `search_kccs`, `get_kcc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `kcgCgmExpc` | `GeneratedKcgcgmexpcClient` | `search_kcgCgmExpcs`, `get_kcgCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `kcsCgmExpc` | `GeneratedKcscgmexpcClient` | `search_kcsCgmExpcs`, `get_kcsCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `kdcaCgmExpc` | `GeneratedKdcacgmexpcClient` | `search_kdcaCgmExpcs`, `get_kdcaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `kfsCgmExpc` | `GeneratedKfscgmexpcClient` | `search_kfsCgmExpcs`, `get_kfsCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `khsCgmExpc` | `GeneratedKhscgmexpcClient` | `search_khsCgmExpcs`, `get_khsCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `kipoCgmExpc` | `GeneratedKipocgmexpcClient` | `search_kipoCgmExpcs`, `get_kipoCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `kmaCgmExpc` | `GeneratedKmacgmexpcClient` | `search_kmaCgmExpcs`, `get_kmaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `kmstSpecialDecc` | `GeneratedKmstspecialdeccClient` | `search_kmstSpecialDeccs`, `get_kmstSpecialDecc_detail` | yes | yes | generated only |
| `kostatCgmExpc` | `GeneratedKostatcgmexpcClient` | `search_kostatCgmExpcs`, `get_kostatCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `law` | `GeneratedLawClient` | `search_laws`, `get_law_detail` | yes | yes | `LawClient`, `KRClient` |
| `lawjosub` | `GeneratedLawjosubClient` | `search_lawjosubs` | yes | yes | generated only |
| `licbyl` | `GeneratedLicbylClient` | `search_licbyls` | yes | yes | `AnnexFormClient`, `KRClient` |
| `lnkLs` | `GeneratedLnklsClient` | `search_lnkLss` | yes | yes | generated only |
| `lnkOrd` | `GeneratedLnkordClient` | `search_lnkOrds` | yes | yes | generated only |
| `lsAbrv` | `GeneratedLsabrvClient` | `search_lsAbrvs` | yes | yes | `LawClient`, `KRClient` |
| `lsDelegated` | `GeneratedLsdelegatedClient` | `get_lsDelegated_detail` | yes | yes | generated only |
| `lsHistory` | `GeneratedLshistoryClient` | `search_lsHistorys`, `get_lsHistory_detail` | yes | yes | generated only |
| `lsHstInf` | `GeneratedLshstinfClient` | `search_lsHstInfs` | yes | yes | `LawClient`, `KRClient` |
| `lsJoHstInf` | `GeneratedLsjohstinfClient` | `search_lsJoHstInfs` | yes | yes | `LawClient`, `KRClient` |
| `lsRlt` | `GeneratedLsrltClient` | `search_lsRlts` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `lsStmd` | `GeneratedLsstmdClient` | `search_lsStmds`, `get_lsStmd_detail` | yes | yes | generated only |
| `lstrm` | `GeneratedLstrmClient` | `search_lstrms`, `get_lstrm_detail` | yes | yes | `LegalTerminologyClient`, `KRClient` |
| `lstrmAI` | `GeneratedLstrmaiClient` | `search_lstrmAIs` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `lstrmRlt` | `GeneratedLstrmrltClient` | `get_lstrmRlt_detail` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `lstrmRltJo` | `GeneratedLstrmrltjoClient` | `get_lstrmRltJo_detail` | yes | yes | `LegalKnowledgeBaseClient`, `KRClient` |
| `mafraCgmExpc` | `GeneratedMafracgmexpcClient` | `search_mafraCgmExpcs`, `get_mafraCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mcstCgmExpc` | `GeneratedMcstcgmexpcClient` | `search_mcstCgmExpcs`, `get_mcstCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `meCgmExpc` | `GeneratedMecgmexpcClient` | `search_meCgmExpcs`, `get_meCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mfdsCgmExpc` | `GeneratedMfdscgmexpcClient` | `search_mfdsCgmExpcs`, `get_mfdsCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mmaCgmExpc` | `GeneratedMmacgmexpcClient` | `search_mmaCgmExpcs`, `get_mmaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mndCgmExpc` | `GeneratedMndcgmexpcClient` | `search_mndCgmExpcs`, `get_mndCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `moeCgmExpc` | `GeneratedMoecgmexpcClient` | `search_moeCgmExpcs`, `get_moeCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `moefCgmExpc` | `GeneratedMoefcgmexpcClient` | `search_moefCgmExpcs` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `moelCgmExpc` | `GeneratedMoelcgmexpcClient` | `search_moelCgmExpcs`, `get_moelCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mofaCgmExpc` | `GeneratedMofacgmexpcClient` | `search_mofaCgmExpcs`, `get_mofaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mofCgmExpc` | `GeneratedMofcgmexpcClient` | `search_mofCgmExpcs`, `get_mofCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mogefCgmExpc` | `GeneratedMogefcgmexpcClient` | `search_mogefCgmExpcs`, `get_mogefCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mohwCgmExpc` | `GeneratedMohwcgmexpcClient` | `search_mohwCgmExpcs`, `get_mohwCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `moisCgmExpc` | `GeneratedMoiscgmexpcClient` | `search_moisCgmExpcs`, `get_moisCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mojCgmExpc` | `GeneratedMojcgmexpcClient` | `search_mojCgmExpcs`, `get_mojCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `molegCgmExpc` | `GeneratedMolegcgmexpcClient` | `search_molegCgmExpcs`, `get_molegCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `molitCgmExpc` | `GeneratedMolitcgmexpcClient` | `search_molitCgmExpcs`, `get_molitCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `motieCgmExpc` | `GeneratedMotiecgmexpcClient` | `search_motieCgmExpcs`, `get_motieCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mouCgmExpc` | `GeneratedMoucgmexpcClient` | `search_mouCgmExpcs`, `get_mouCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mpmCgmExpc` | `GeneratedMpmcgmexpcClient` | `search_mpmCgmExpcs`, `get_mpmCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mpvaCgmExpc` | `GeneratedMpvacgmexpcClient` | `search_mpvaCgmExpcs`, `get_mpvaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `msitCgmExpc` | `GeneratedMsitcgmexpcClient` | `search_msitCgmExpcs`, `get_msitCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `mssCgmExpc` | `GeneratedMsscgmexpcClient` | `search_mssCgmExpcs`, `get_mssCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `naaccCgmExpc` | `GeneratedNaacccgmexpcClient` | `search_naaccCgmExpcs`, `get_naaccCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `nfaCgmExpc` | `GeneratedNfacgmexpcClient` | `search_nfaCgmExpcs`, `get_nfaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `nhrck` | `GeneratedNhrckClient` | `search_nhrcks`, `get_nhrck_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `nlrc` | `GeneratedNlrcClient` | `search_nlrcs`, `get_nlrc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `npaCgmExpc` | `GeneratedNpacgmexpcClient` | `search_npaCgmExpcs`, `get_npaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `ntsCgmExpc` | `GeneratedNtscgmexpcClient` | `search_ntsCgmExpcs` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `oclt` | `GeneratedOcltClient` | `search_oclts`, `get_oclt_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `okaCgmExpc` | `GeneratedOkacgmexpcClient` | `search_okaCgmExpcs`, `get_okaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `oldAndNew` | `GeneratedOldandnewClient` | `search_oldAndNews`, `get_oldAndNew_detail` | yes | yes | `LawClient`, `KRClient` |
| `oneview` | `GeneratedOneviewClient` | `search_oneviews`, `get_oneview_detail` | yes | yes | generated only |
| `ordin` | `GeneratedOrdinClient` | `search_ordins`, `get_ordin_detail` | yes | yes | `OrdinanceClient`, `KRClient` |
| `ordinbyl` | `GeneratedOrdinbylClient` | `search_ordinbyls` | yes | yes | `AnnexFormClient`, `KRClient` |
| `ppc` | `GeneratedPpcClient` | `search_ppcs`, `get_ppc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `ppsCgmExpc` | `GeneratedPpscgmexpcClient` | `search_ppsCgmExpcs`, `get_ppsCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `prec` | `GeneratedPrecClient` | `search_precs`, `get_prec_detail` | yes | yes | `PrecedentClient`, `KRClient` |
| `rdaCgmExpc` | `GeneratedRdacgmexpcClient` | `search_rdaCgmExpcs`, `get_rdaCgmExpc_detail` | yes | yes | `MinistryInterpretationClient`, `KRClient` |
| `school` | `GeneratedSchoolClient` | `search_schools`, `get_school_detail` | yes | yes | `SchoolPublicRuleClient`, `KRClient` |
| `sfc` | `GeneratedSfcClient` | `search_sfcs`, `get_sfc_detail` | yes | yes | `CommitteeDecisionClient`, `KRClient` |
| `thdCmp` | `GeneratedThdcmpClient` | `search_thdCmps`, `get_thdCmp_detail` | yes | yes | generated only |
| `trty` | `GeneratedTrtyClient` | `search_trtys`, `get_trty_detail` | yes | yes | `TreatyClient`, `KRClient` |
| `ttSpecialDecc` | `GeneratedTtspecialdeccClient` | `search_ttSpecialDeccs`, `get_ttSpecialDecc_detail` | yes | yes | generated only |

## Verification

Run these before marking v1 generated coverage as complete:

```bash
uv run pytest tests/test_generated
uv run pytest
uv run ruff check src/lawpy tests
uv run mypy src/lawpy
```
