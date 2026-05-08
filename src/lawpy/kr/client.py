"""Integrated client for Korean law APIs."""

from lawpy.kr.administrative_rule import AdministrativeRuleClient
from lawpy.kr.law import LawClient
from lawpy.kr.legal_interpretation import LegalInterpretationClient
from lawpy.kr.legal_terminology import LegalTerminologyClient
from lawpy.kr.ordinance import OrdinanceClient
from lawpy.kr.precedent import PrecedentClient
from lawpy.kr.treaty import TreatyClient


class KRClient(
    LawClient,
    PrecedentClient,
    AdministrativeRuleClient,
    OrdinanceClient,
    LegalTerminologyClient,
    LegalInterpretationClient,
    TreatyClient,
):
    """Integrated client for Korean National Law Information Center API.

    Provides a single entry-point for all implemented Korean law open-data APIs.
    This is the primary object most users and AI agents should try first.

    Basic pattern:
      >>> from lawpy import KRClient
      >>> client = KRClient(api_key="your-open-law-email-id")
      >>> laws = client.search_laws("민법", per_page=5)
      >>> detail = client.get_law_detail(law_id=laws[0].law_id)

    ``KoreanLawClient`` remains available as a compatibility alias. New code
    should prefer ``KRClient`` so future country/region modules can follow the
    same pattern, such as ``USClient`` or ``EUClient``.

    If a target is not exposed here yet, use the generated client under
    ``lawpy.kr.generated.<target>``. Run ``import lawpy; print(lawpy.help())``
    for installed guidance.

    **법령 (Law) — implemented**:
      - :meth:`search_laws`            법령명/전문 검색
      - :meth:`get_law_detail`         법령 본문 조회 (by ID or MST)
      - :meth:`get_law_list`           현행법령 목록 조회
      - :meth:`get_law_history`        연혁법령 목록 조회
      - :meth:`get_law_history_detail` 연혁법령 상세 조회

    **판례 (Precedent) — implemented**:
      - :meth:`search_precedents`      판례 목록 조회
      - :meth:`get_precedent_detail`   판례 본문 조회

    **행정규칙 (Administrative Rule) — implemented**:
      - :meth:`search_administrative_rules` 행정규칙 목록 조회
      - :meth:`search_notices`              고시 목록 조회 (행정규칙 knd=3)
      - :meth:`get_administrative_rule_detail` 행정규칙 본문 조회

    **자치법규 (Local Ordinance) — implemented**:
      - :meth:`search_ordinances`      자치법규 목록 조회
      - :meth:`search_local_notices`   자치법규 고시 목록 조회 (자치법규 knd=30010)
      - :meth:`get_ordinance_detail`   자치법규 본문 조회

    **법령용어 (Legal Terminology) — implemented**:
      - :meth:`search_legal_terms`      법령용어 목록 조회
      - :meth:`get_legal_term_detail`   법령용어 본문 조회

    **법령해석례 (Legal Interpretation) — implemented**:
      - :meth:`search_legal_interpretations`      법령해석례 목록 조회
      - :meth:`get_legal_interpretation_detail`   법령해석례 본문 조회

    **조약 (Treaty) — implemented**:
      - :meth:`search_treaties`         조약 목록 조회
      - :meth:`get_treaty_detail`       조약 본문 조회

    **향후 구현 예정**:
      - 헌재결정례 (Constitutional Court Decisions)
      - 행정심판례 (Administrative Review Cases)
      - 위원회결정문 (Committee Decisions)
      - 별표·서식 (Annexes and Forms)
    """

    pass


KoreanLawClient = KRClient
