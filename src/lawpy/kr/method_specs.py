"""Collector-oriented metadata for KRClient public methods."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

KR_METHOD_SPECS: dict[str, dict[str, Any]] = {
    "search_laws": {
        "kind": "search",
        "required": ["query"],
        "seed_source": None,
        "target": "law",
    },
    "get_law_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "law_search_results",
        "target": "law",
    },
    "get_law_list": {
        "kind": "search",
        "required": [],
        "target": "eflaw",
    },
    "get_law_history": {
        "kind": "search",
        "required": [],
        "target": "lsHistory",
    },
    "get_law_history_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["law_id"], ["mst"], ["law_name", "promulgation_date", "promulgation_number"]],
        "seed_source": "law_history_results",
        "target": "lsHistory",
    },
    "search_english_laws": {
        "kind": "search",
        "required": [],
        "target": "elaw",
    },
    "get_english_law_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "english_law_search_results",
        "target": "elaw",
    },
    "search_law_old_and_new": {
        "kind": "search",
        "required": [],
        "target": "oldAndNew",
    },
    "get_law_old_and_new_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "law_old_and_new_search_results",
        "target": "oldAndNew",
    },
    "search_law_abbreviations": {
        "kind": "search",
        "required": [],
        "target": "lsAbrv",
    },
    "search_law_change_history": {
        "kind": "search",
        "required": [],
        "target": "lsHstInf",
    },
    "search_law_article_change_history": {
        "kind": "search",
        "required": ["law_id", "article_number"],
        "seed_source": "law_article_units",
        "target": "lsJoHstInf",
    },
    "search_precedents": {
        "kind": "search",
        "required": [],
        "target": "prec",
    },
    "get_precedent_detail": {
        "kind": "detail",
        "required": ["prec_id"],
        "seed_source": "precedent_search_results",
        "target": "prec",
    },
    "search_administrative_rules": {
        "kind": "search",
        "required": [],
        "target": "admrul",
    },
    "search_notices": {
        "kind": "search",
        "required": [],
        "target": "admrul",
        "fixed_params": {"knd": 3},
    },
    "get_administrative_rule_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["rule_id"], ["rule_name"]],
        "seed_source": "administrative_rule_search_results",
        "target": "admrul",
    },
    "search_law_annex_forms": {
        "kind": "search",
        "required": [],
        "target": "admbyl",
    },
    "search_administrative_rule_annex_forms": {
        "kind": "search",
        "required": [],
        "target": "admrulbyl",
    },
    "search_ordinance_annex_forms": {
        "kind": "search",
        "required": [],
        "target": "ordinbyl",
    },
    "search_ordinances": {
        "kind": "search",
        "required": [],
        "target": "ordin",
    },
    "search_local_notices": {
        "kind": "search",
        "required": [],
        "target": "ordin",
        "fixed_params": {"knd": 30010},
    },
    "get_ordinance_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["ordinance_id"], ["mst"]],
        "seed_source": "ordinance_search_results",
        "target": "ordin",
    },
    "search_legal_terms": {
        "kind": "search",
        "required": [],
        "target": "lstrm",
    },
    "get_legal_term_detail": {
        "kind": "detail",
        "required": ["term"],
        "seed_source": "legal_term_search_results",
        "target": "lstrm",
    },
    "search_legal_knowledge_terms": {
        "kind": "search",
        "required": [],
        "target": "lsTrm",
    },
    "search_daily_terms": {
        "kind": "search",
        "required": [],
        "target": "dlyTrm",
    },
    "get_legal_term_daily_term_relations": {
        "kind": "detail",
        "required": [],
        "alternatives": [["query"], ["term_id"]],
        "seed_source": "legal_knowledge_terms",
        "target": "lstrmRlt",
    },
    "get_daily_term_legal_term_relations": {
        "kind": "detail",
        "required": [],
        "alternatives": [["query"], ["term_id"]],
        "seed_source": "daily_terms",
        "target": "dlytrmRlt",
    },
    "get_legal_term_article_relations": {
        "kind": "detail",
        "required": ["query"],
        "seed_source": "legal_knowledge_terms",
        "target": "lstrmRltJo",
    },
    "get_article_legal_term_relations": {
        "kind": "detail",
        "required": [],
        "alternatives": [["query"], ["law_id", "article_number"]],
        "seed_source": "law_article_units",
        "target": "joRltLstrm",
    },
    "search_related_laws": {
        "kind": "search",
        "required": [],
        "target": "lsRlt",
    },
    "search_ai_laws": {
        "kind": "search",
        "required": [],
        "target": "aiSearch",
    },
    "search_ai_related_laws": {
        "kind": "search",
        "required": [],
        "target": "aiRltLs",
    },
    "search_legal_interpretations": {
        "kind": "search",
        "required": [],
        "target": "expc",
    },
    "get_legal_interpretation_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["interpretation_id"], ["interpretation_name"]],
        "seed_source": "legal_interpretation_search_results",
        "target": "expc",
    },
    "search_constitutional_decisions": {
        "kind": "search",
        "required": [],
        "target": "detc",
    },
    "get_constitutional_decision_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["decision_id"], ["decision_name"]],
        "seed_source": "constitutional_decision_search_results",
        "target": "detc",
    },
    "search_administrative_review_decisions": {
        "kind": "search",
        "required": [],
        "target": "decc",
    },
    "get_administrative_review_decision_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["decision_id"], ["decision_name"]],
        "seed_source": "administrative_review_decision_search_results",
        "target": "decc",
    },
    "list_committee_decision_targets": {
        "kind": "catalog",
        "required": [],
        "catalog": "committee_decision_targets",
    },
    "search_committee_decisions": {
        "kind": "search",
        "required": ["committee"],
        "seed_source": "committee_decision_targets",
        "target": "committee_decision",
    },
    "get_committee_decision_detail": {
        "kind": "detail",
        "required": ["committee", "decision_id"],
        "seed_source": "committee_decision_search_results",
        "target": "committee_decision",
    },
    "list_ministry_interpretation_targets": {
        "kind": "catalog",
        "required": [],
        "catalog": "ministry_interpretation_targets",
    },
    "search_ministry_interpretations": {
        "kind": "search",
        "required": ["ministry"],
        "seed_source": "ministry_interpretation_targets",
        "target": "ministry_interpretation",
    },
    "get_ministry_interpretation_detail": {
        "kind": "detail",
        "required": ["ministry", "interpretation_id"],
        "seed_source": "ministry_interpretation_search_results",
        "target": "ministry_interpretation",
    },
    "search_school_public_rules": {
        "kind": "search",
        "required": [],
        "target": "school",
    },
    "get_school_public_rule_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["rule_id"], ["rule_lid"], ["rule_name"]],
        "seed_source": "school_public_rule_search_results",
        "target": "school",
    },
    "search_treaties": {
        "kind": "search",
        "required": [],
        "target": "trty",
    },
    "get_treaty_detail": {
        "kind": "detail",
        "required": ["treaty_id"],
        "seed_source": "treaty_search_results",
        "target": "trty",
    },
    "search_customized_articles": {
        "kind": "search",
        "required": ["source", "classification_code"],
        "seed_source": "customized_article_classification_codes",
        "target_by_source": {
            "law": "couseLs",
            "administrative_rule": "couseAdmrul",
            "ordinance": "couseOrdin",
        },
        "allowed_values": {
            "source": ["law", "administrative_rule", "ordinance"],
            "classification_code_prefix": {
                "law": "L",
                "administrative_rule": "A",
                "ordinance": "O",
            },
        },
    },
    "search_law_article_units": {
        "kind": "search",
        "required": [],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "law_search_results",
        "target": "lawjosub",
    },
    "search_effective_law_article_units": {
        "kind": "search",
        "required": [],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "law_search_results",
        "target": "eflawjosub",
    },
    "search_ordinance_links_by_law": {
        "kind": "search",
        "required": [],
        "target": "lnkLs",
    },
    "search_law_links_by_ordinance": {
        "kind": "search",
        "required": [],
        "target": "lnkOrd",
    },
    "search_law_ordinance_link_status": {
        "kind": "search",
        "required": [],
        "target": "drlaw",
    },
    "get_delegated_law_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "law_search_results",
        "target": "lsDelegated",
    },
    "search_oneview_laws": {
        "kind": "search",
        "required": [],
        "target": "oneview",
    },
    "get_oneview_law_detail": {
        "kind": "detail",
        "required": [],
        "alternatives": [["mst"], ["law_name", "promulgation_date", "promulgation_number"]],
        "seed_source": "oneview_law_search_results",
        "target": "oneview",
    },
    "search_three_way_comparisons": {
        "kind": "search",
        "required": [],
        "target": "thdCmp",
    },
    "get_three_way_comparison_detail": {
        "kind": "detail",
        "required": ["comparison_kind"],
        "alternatives": [["law_id"], ["mst"]],
        "seed_source": "three_way_comparison_search_results",
        "target": "thdCmp",
        "allowed_values": {
            "comparison_kind": [1, 2],
        },
    },
    "search_couseLss": {
        "kind": "search",
        "required": ["vcode", "lj_jo"],
        "seed_source": "customized_article_classification_codes",
        "target": "couseLs",
        "allowed_values": {"vcode_prefix": "L", "lj_jo": ["Y", "N"]},
    },
    "search_couseAdmruls": {
        "kind": "search",
        "required": ["vcode", "lj_jo"],
        "seed_source": "customized_article_classification_codes",
        "target": "couseAdmrul",
        "allowed_values": {"vcode_prefix": "A", "lj_jo": ["Y", "N"]},
    },
    "search_couseOrdins": {
        "kind": "search",
        "required": ["vcode", "lj_jo"],
        "seed_source": "customized_article_classification_codes",
        "target": "couseOrdin",
        "allowed_values": {"vcode_prefix": "O", "lj_jo": ["Y", "N"]},
    },
}


def get_kr_method_specs() -> dict[str, dict[str, Any]]:
    """Return a defensive copy of KRClient public method metadata."""
    return deepcopy(KR_METHOD_SPECS)

