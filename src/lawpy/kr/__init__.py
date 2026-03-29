"""Korean law API modules."""

from lawpy.kr.client import KoreanLawClient
from lawpy.kr.law import LawClient
from lawpy.kr.precedent import PrecedentClient

__all__ = ["KoreanLawClient", "LawClient", "PrecedentClient"]
