"""Installed help surface for humans and AI agents using lawpy.

This module is intentionally importable from an installed wheel. It gives a
short, stable route from `uv add lawpy` to the objects and patterns that matter.
"""

from __future__ import annotations

import argparse
import sys
import types
from textwrap import dedent

TOPICS = ("quickstart", "kr", "generated", "codegen")

QUICKSTART = dedent(
    """
    lawpy quickstart
    =================

    Main object:
        KRClient

    Meaning:
        KRClient is the ergonomic entry point for Korean law.go.kr data.
        It combines the public wrappers for law, precedent, administrative rule,
        annex/form, local ordinance, legal terminology, legal knowledge-base,
        legal interpretation, constitutional decision, administrative review
        decision, committee decision, ministry interpretation, school/public
        rule, treaty, customized article, law/ordinance link, one-view, and
        three-way comparison workflows.
        KoreanLawClient is kept as a compatibility alias.

    Basic pattern:
        from lawpy import KRClient

        client = KRClient(api_key="your-open-law-email-id")
        results = client.search_laws("민법", per_page=5)
        detail = client.get_law_detail(law_id=results[0].law_id)

    API key:
        Set LAWPY_KR_API_KEY, or pass api_key directly.
        The key is the email username registered at open.law.go.kr.

    Next:
        lawpy.help("kr")         public wrapper method map
        lawpy.help("generated")  use a generated-only target
        lawpy.help("codegen")    specs/codegen support policy
    """
).strip()

KR = dedent(
    """
    KRClient pattern
    ================

    Use KRClient first. It is the stable public surface for common datapan-data
    workflows. KoreanLawClient is a compatibility alias for existing code.

    Public wrapper methods:
        Law:
            search_laws(query, page=1, per_page=20)
            get_law_detail(law_id=None, mst=None, article_number=None)
            get_law_list(page=1, per_page=20)
            get_law_history(query=None, page=1, per_page=20)

        Precedent:
            search_precedents(query=None, page=1, per_page=20)
            get_precedent_detail(prec_id)

        Administrative rules and notices:
            search_administrative_rules(query=None, page=1, per_page=20)
            search_notices(query=None, page=1, per_page=20)
            get_administrative_rule_detail(rule_id=None, rule_name=None)

        Annexes and forms:
            search_law_annex_forms(query=None, page=1, per_page=20)
            search_administrative_rule_annex_forms(query=None, page=1, per_page=20)
            search_ordinance_annex_forms(query=None, page=1, per_page=20)

        Local ordinances and local notices:
            search_ordinances(query=None, page=1, per_page=20)
            search_local_notices(query=None, page=1, per_page=20)
            get_ordinance_detail(ordinance_id=None, mst=None)

        Legal terminology:
            search_legal_terms(query=None, page=1, per_page=20)
            get_legal_term_detail(term)

        Legal knowledge base:
            search_legal_knowledge_terms(query=None, page=1, per_page=20)
            search_daily_terms(query=None, page=1, per_page=20)
            get_legal_term_daily_term_relations(query=None, term_id=None)
            get_daily_term_legal_term_relations(query=None, term_id=None)
            get_legal_term_article_relations(query)
            get_article_legal_term_relations(query=None, law_id=None, article_number=None)
            search_related_laws(query=None, law_id=None, relation_code=None)
            search_ai_laws(query=None, page=1, per_page=20)
            search_ai_related_laws(query=None)

        Legal interpretations:
            search_legal_interpretations(query=None, page=1, per_page=20)
            get_legal_interpretation_detail(interpretation_id=None, interpretation_name=None)

        Constitutional decisions:
            search_constitutional_decisions(query=None, page=1, per_page=20)
            get_constitutional_decision_detail(decision_id=None, decision_name=None)

        Administrative review decisions:
            search_administrative_review_decisions(query=None, page=1, per_page=20)
            get_administrative_review_decision_detail(decision_id=None, decision_name=None)

        Committee decisions:
            list_committee_decision_targets()
            search_committee_decisions(committee, query=None, page=1, per_page=20)
            get_committee_decision_detail(committee, decision_id=None)

        Ministry interpretations:
            list_ministry_interpretation_targets()
            search_ministry_interpretations(ministry, query=None, page=1, per_page=20)
            get_ministry_interpretation_detail(ministry, interpretation_id=None)

        School, corporation, and public institution rules:
            search_school_public_rules(query=None, page=1, per_page=20)
            get_school_public_rule_detail(rule_id=None, rule_lid=None, rule_name=None)

        Treaties:
            search_treaties(query=None, page=1, per_page=20)
            get_treaty_detail(treaty_id)

        Customized and reference APIs:
            search_customized_articles(source, classification_code, page=1, per_page=20)
            search_law_article_units(law_id=None, mst=None, article=None)
            search_effective_law_article_units(law_id=None, mst=None, effective_date=None)
            search_ordinance_links_by_law(query=None, page=1, per_page=20)
            search_law_links_by_ordinance(query=None, page=1, per_page=20)
            search_law_ordinance_link_status(query=None, page=1, per_page=20)
            get_delegated_law_detail(law_id=None, mst=None)
            search_oneview_laws(query=None, page=1, per_page=20)
            get_oneview_law_detail(mst=None, law_name=None, article_number=None)
            search_three_way_comparisons(query=None, page=1, per_page=20)
            get_three_way_comparison_detail(comparison_kind=None, law_id=None, mst=None)

    One pattern teaches the rest:
        items = client.search_ordinances("서울", per_page=10)
        first = items[0]
        detail = client.get_ordinance_detail(ordinance_id=first.자치법규ID)

    Response pattern:
        Public wrappers return typed Python objects or generated Pydantic models.
        For generated Pydantic models, use model_dump(by_alias=True) when storing
        the original Korean API field names.

    Collector metadata:
        KRClient.get_method_specs()
        KRClient.describe_methods()
        KRClient.describe_method("get_law_detail")

        These return installed, JSON-serializable metadata for target builders:
        kind, required params, alternative seed params, seed_source, fixed params,
        allowed values, and upstream target names where known.
    """
).strip()

GENERATED = dedent(
    """
    Generated-only target pattern
    =============================

    If KRClient does not expose a public wrapper yet, import the generated
    client directly from lawpy.kr.generated.<target>.

    Example:
        from lawpy.kr.generated.decc import GeneratedDeccClient

        client = GeneratedDeccClient(api_key="your-open-law-email-id")
        decisions = client.search_deccs(query="영업정지", display=10, page=1)

        row = decisions[0]
        data = row.model_dump(by_alias=True)

    Naming pattern:
        target file:      src/lawpy/kr/generated/{target}.py
        client class:     Generated{Target.capitalize()}Client
        search method:    search_{target}s(...)
        detail method:    get_{target}_detail(...)

    Coverage:
        KR v1 generated coverage includes 195 spec files, 98 generated modules,
        98 generated tests, and 90 public wrapper targets. See
        docs/kr/generated-coverage.md in the source repository for the full
        target/method matrix.
    """
).strip()

CODEGEN = dedent(
    """
    Specs and codegen policy
    ========================

    lawpy keeps the Korean specs, code generator, generated clients, generated
    models, and generated tests public.

    Support contract:
        - Prefer KRClient for stable public workflows.
        - Use generated clients for covered targets without a wrapper.
        - Generated code is reviewed through deterministic diffs, coverage docs,
          and CI tests.
        - Raw scraped specs may reflect upstream documentation quirks; generated
          tests and live drift checks are the guardrails.

    Contributor rule:
        Change specs/codegen/generated output together. A generated target is not
        complete unless its client, model surface, and generated test are aligned.
    """
).strip()

_GUIDES = {
    "quickstart": QUICKSTART,
    "kr": KR,
    "generated": GENERATED,
    "codegen": CODEGEN,
}


def guide(topic: str = "quickstart") -> str:
    """Return an installed lawpy usage guide.

    Args:
        topic: One of "quickstart", "kr", "generated", or "codegen".

    Returns:
        A plain-text guide suitable for `print()`, `help(lawpy)`, or AI agents.
    """
    normalized = topic.strip().lower()
    if normalized not in _GUIDES:
        choices = ", ".join(TOPICS)
        msg = f"Unknown lawpy help topic {topic!r}. Expected one of: {choices}."
        raise ValueError(msg)
    return _GUIDES[normalized]


def print_guide(topic: str = "quickstart") -> None:
    """Print an installed lawpy usage guide."""
    print(guide(topic))


def main() -> None:
    """CLI entry point for `python -m lawpy.help`."""
    parser = argparse.ArgumentParser(description="Show installed lawpy usage guidance.")
    parser.add_argument(
        "topic",
        nargs="?",
        default="quickstart",
        choices=TOPICS,
        help="Guide topic to print.",
    )
    args = parser.parse_args()
    print_guide(args.topic)


class _HelpModule(types.ModuleType):
    def __call__(self, topic: str = "quickstart") -> str:
        return guide(topic)


sys.modules[__name__].__class__ = _HelpModule


if __name__ == "__main__":
    main()
