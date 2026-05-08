"""Universal law information API client library.

Installed quickstart:
    import lawpy
    print(lawpy.help())

Main Korean API object:
    from lawpy import KRClient

    client = KRClient(api_key="your-open-law-email-id")
    laws = client.search_laws("민법", per_page=5)

Use lawpy.help("kr") for public wrapper methods and
lawpy.help("generated") for generated-only KR targets.
"""

from lawpy.kr import (
    AdministrativeRuleClient,
    CommitteeDecisionClient,
    KoreanLawClient,
    KRClient,
    LawReferenceClient,
    MinistryInterpretationClient,
    OrdinanceClient,
    PrecedentClient,
)
from lawpy.kr.generated._models_generated import AdmrulDetail, AdmrulList, OrdinDetail, OrdinList
from lawpy.models import (
    Article,
    Item,
    Law,
    LawDetail,
    Paragraph,
    Precedent,
    PrecedentDetail,
    SubItem,
)

__version__ = "0.2.1"


def help(topic: str = "quickstart") -> str:
    """Return installed lawpy usage guidance."""
    from lawpy.help import guide

    return guide(topic)


def print_guide(topic: str = "quickstart") -> None:
    """Print installed lawpy usage guidance."""
    from lawpy.help import print_guide as _print_guide

    _print_guide(topic)


__all__ = [
    "AdministrativeRuleClient",
    "AdmrulDetail",
    "AdmrulList",
    "CommitteeDecisionClient",
    "KRClient",
    "KoreanLawClient",
    "LawReferenceClient",
    "MinistryInterpretationClient",
    "OrdinanceClient",
    "OrdinDetail",
    "OrdinList",
    "PrecedentClient",
    "Article",
    "Item",
    "Law",
    "LawDetail",
    "Paragraph",
    "Precedent",
    "PrecedentDetail",
    "SubItem",
    "help",
    "print_guide",
    "__version__",
]
