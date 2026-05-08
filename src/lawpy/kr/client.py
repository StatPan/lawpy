"""Integrated client for Korean law APIs."""

from lawpy.kr.administrative_rule import AdministrativeRuleClient
from lawpy.kr.law import LawClient
from lawpy.kr.ordinance import OrdinanceClient
from lawpy.kr.precedent import PrecedentClient


class KoreanLawClient(LawClient, PrecedentClient, AdministrativeRuleClient, OrdinanceClient):
    """Integrated client for Korean National Law Information Center API.

    Provides a single entry-point for all implemented Korean law open-data APIs.

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

    **향후 구현 예정**:
      - 헌재결정례 (Constitutional Court Decisions)
      - 법령해석례 (Legal Interpretation Cases)
      - 행정심판례 (Administrative Review Cases)
      - 위원회결정문 (Committee Decisions)
      - 조약 (Treaties)
      - 별표·서식 (Annexes and Forms)
      - 법령용어 (Legal Terminology)
    """

    pass
