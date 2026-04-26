"""Korean law API modules."""

from lawpy.kr.client import KoreanLawClient
from lawpy.kr.constitutional_decision import ConstitutionalDecisionClient
from lawpy.kr.law import LawClient
from lawpy.kr.precedent import PrecedentClient

__all__ = ["KoreanLawClient", "LawClient", "PrecedentClient", "ConstitutionalDecisionClient"]
