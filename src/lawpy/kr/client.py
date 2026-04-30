"""Integrated client for Korean law APIs."""

from lawpy.kr.law import LawClient
from lawpy.kr.precedent import PrecedentClient


class KoreanLawClient(LawClient, PrecedentClient):
    """Integrated client for Korean National Law Information Center API.

    Provides a single entry-point for all implemented Korean law open-data APIs.

    **법령 (Law) — implemented**:
      - :meth:`search_laws`                    법령명/전문 검색
      - :meth:`get_law_detail`                 법령 본문 조회 (by ID or MST)
      - :meth:`get_law_list`                   현행법령 목록 조회
      - :meth:`get_law_history`                연혁법령 목록 조회
      - :meth:`get_law_history_detail`         연혁법령 상세 조회
      - :meth:`get_law_old_new`                신구법 비교 목록 조회
      - :meth:`get_law_old_new_detail`         신구법 비교 본문 조회
      - :meth:`get_law_abbreviations`          법령명 약칭 조회
      - :meth:`get_law_change_history`         법령 변경이력 목록 조회
      - :meth:`get_law_article_change_history` 조문별 변경이력 목록 조회

    **판례 (Precedent) — implemented**:
      - :meth:`search_precedents`      판례 목록 조회
      - :meth:`get_precedent_detail`   판례 본문 조회

    **향후 구현 예정**:
      - 행정규칙 (Administrative Rules)
      - 자치법규 (Autonomous Ordinances)
      - 헌재결정례 (Constitutional Court Decisions)
      - 법령해석례 (Legal Interpretation Cases)
      - 행정심판례 (Administrative Review Cases)
      - 위원회결정문 (Committee Decisions)
      - 조약 (Treaties)
      - 별표·서식 (Annexes and Forms)
      - 법령용어 (Legal Terminology)
    """

    pass
