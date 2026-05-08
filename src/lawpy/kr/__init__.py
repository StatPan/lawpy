"""Korean law API modules.

Start with KoreanLawClient for normal use:

    from lawpy import KoreanLawClient

    client = KoreanLawClient(api_key="your-open-law-email-id")
    laws = client.search_laws("민법", per_page=5)

For installed guidance, run:

    import lawpy
    print(lawpy.help("kr"))
"""

from lawpy.kr.administrative_rule import AdministrativeRuleClient
from lawpy.kr.client import KoreanLawClient
from lawpy.kr.law import LawClient
from lawpy.kr.ordinance import OrdinanceClient
from lawpy.kr.precedent import PrecedentClient

__all__ = ["AdministrativeRuleClient", "KoreanLawClient", "LawClient", "OrdinanceClient", "PrecedentClient"]
