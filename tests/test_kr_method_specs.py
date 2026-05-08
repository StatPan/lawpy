"""Tests for KRClient collector method metadata."""

import pytest

from lawpy.kr import KRClient


def test_get_method_specs_exposes_seed_contracts() -> None:
    specs = KRClient.get_method_specs()

    assert specs["get_delegated_law_detail"]["alternatives"] == [["law_id"], ["mst"]]
    assert specs["get_delegated_law_detail"]["seed_source"] == "law_search_results"
    assert specs["get_three_way_comparison_detail"]["required"] == ["comparison_kind"]
    assert specs["get_three_way_comparison_detail"]["allowed_values"]["comparison_kind"] == [1, 2]
    assert specs["search_customized_articles"]["required"] == ["source", "classification_code"]
    assert specs["search_customized_articles"]["seed_source"] == "customized_article_classification_codes"


def test_get_method_specs_includes_generated_required_targets() -> None:
    specs = KRClient.get_method_specs()

    assert specs["search_couseLss"]["required"] == ["vcode", "lj_jo"]
    assert specs["search_couseLss"]["allowed_values"]["vcode_prefix"] == "L"
    assert specs["search_couseAdmruls"]["allowed_values"]["vcode_prefix"] == "A"
    assert specs["search_couseOrdins"]["allowed_values"]["vcode_prefix"] == "O"


def test_describe_methods_returns_defensive_copy() -> None:
    specs = KRClient.describe_methods()
    specs["get_law_detail"]["alternatives"].append(["mutated"])

    fresh = KRClient.get_method_specs()
    assert ["mutated"] not in fresh["get_law_detail"]["alternatives"]


def test_describe_method_returns_single_spec() -> None:
    spec = KRClient(api_key="test_key").describe_method("get_english_law_detail")

    assert spec["alternatives"] == [["law_id"], ["mst"]]
    assert spec["seed_source"] == "english_law_search_results"


def test_describe_method_rejects_unknown_name() -> None:
    with pytest.raises(ValueError, match="Unknown KRClient method"):
        KRClient.describe_method("missing_method")

