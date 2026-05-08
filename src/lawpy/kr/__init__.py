"""Korean law API modules."""

from lawpy.kr.administrative_rule import AdministrativeRuleClient
from lawpy.kr.client import KoreanLawClient
from lawpy.kr.law import LawClient
from lawpy.kr.ordinance import OrdinanceClient
from lawpy.kr.precedent import PrecedentClient

__all__ = ["AdministrativeRuleClient", "KoreanLawClient", "LawClient", "OrdinanceClient", "PrecedentClient"]
