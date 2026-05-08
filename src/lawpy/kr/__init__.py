"""Korean law API modules.

Start with KRClient for normal use:

    from lawpy import KRClient

    client = KRClient(api_key="your-open-law-email-id")
    laws = client.search_laws("민법", per_page=5)

KoreanLawClient is kept as a compatibility alias.

For installed guidance, run:

    import lawpy
    print(lawpy.help("kr"))
"""

from lawpy.kr.administrative_rule import AdministrativeRuleClient
from lawpy.kr.client import KoreanLawClient, KRClient
from lawpy.kr.law import LawClient
from lawpy.kr.legal_interpretation import LegalInterpretationClient
from lawpy.kr.legal_terminology import LegalTerminologyClient
from lawpy.kr.ordinance import OrdinanceClient
from lawpy.kr.precedent import PrecedentClient
from lawpy.kr.treaty import TreatyClient

__all__ = [
    "AdministrativeRuleClient",
    "KRClient",
    "KoreanLawClient",
    "LawClient",
    "LegalInterpretationClient",
    "LegalTerminologyClient",
    "OrdinanceClient",
    "PrecedentClient",
    "TreatyClient",
]
