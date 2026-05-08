"""Tests for Korean law reference and customized article client."""

from unittest.mock import Mock

import pytest

from lawpy.kr import KRClient, LawReferenceClient
from lawpy.kr.generated._models_generated import (
    CouselsList,
    DrlawList,
    EflawjosubList,
    LawjosubList,
    LnklsList,
    LnkordList,
    LsdelegatedDetail,
    OneviewDetail,
    OneviewList,
    ThdcmpDetail,
    ThdcmpList,
)


def _mock_response(payload: dict) -> Mock:
    response = Mock()
    response.json.return_value = payload
    return response


def test_law_reference_client_is_on_kr_client() -> None:
    client = KRClient(api_key="test_key")

    assert isinstance(client, LawReferenceClient)


def test_search_customized_articles_maps_law_target() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"items": [{"target": "couseLs"}]}))

    result = client.search_customized_articles(
        "law",
        "L0000000000001",
        article_only=True,
        page=2,
        per_page=5,
        popup=True,
    )

    assert isinstance(result[0], CouselsList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "couseLs"
    assert params["vcode"] == "L0000000000001"
    assert params["lj=jo"] == "Y"
    assert params["display"] == 5
    assert params["page"] == 2
    assert params["popYn"] == "Y"


def test_search_customized_articles_defaults_to_article_mode() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"items": [{"target": "couseLs"}]}))

    client.search_customized_articles("law", "L0000000000001")

    params = client._make_request.call_args.kwargs["params"]
    assert params["vcode"] == "L0000000000001"
    assert params["lj=jo"] == "Y"


def test_search_customized_articles_requires_classification_code_before_request() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock()

    with pytest.raises(ValueError, match="vcode is required"):
        client.search_customized_articles("law", None)  # type: ignore[arg-type]

    client._make_request.assert_not_called()


def test_search_law_article_units_maps_service_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"법령": {"법령키": [{}]}}))

    result = client.search_law_article_units(
        law_id="009682",
        article="000200",
        paragraph="000100",
        subparagraph="000300",
        item="가",
    )

    assert isinstance(result[0], LawjosubList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lawjosub"
    assert params["ID"] == "009682"
    assert params["JO"] == "000200"
    assert params["HANG"] == "000100"
    assert params["HO"] == "000300"
    assert params["MOK"] == "가"


def test_search_effective_law_article_units_maps_service_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"법령": {"법령키": [{}]}}))

    result = client.search_effective_law_article_units(
        law_id="009682",
        effective_date=20240101,
        article="000200",
    )

    assert isinstance(result[0], EflawjosubList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "eflawjosub"
    assert params["ID"] == "009682"
    assert params["efYd"] == 20240101
    assert params["JO"] == "000200"


def test_search_ordinance_links_by_law_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"LawSearch": {"target": "lnkLs"}}))

    result = client.search_ordinance_links_by_law("민법", page=3, per_page=7, sort="ldes")

    assert isinstance(result[0], LnklsList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lnkLs"
    assert params["query"] == "민법"
    assert params["display"] == 7
    assert params["page"] == 3
    assert params["sort"] == "ldes"


def test_search_law_links_by_ordinance_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"target": "lnkOrd"}}))

    result = client.search_law_links_by_ordinance("서울", popup=False)

    assert isinstance(result[0], LnkordList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lnkOrd"
    assert params["query"] == "서울"
    assert params["popYn"] == "N"


def test_search_law_ordinance_link_status_uses_xml_target() -> None:
    client = KRClient(api_key="test_key")
    client._make_xml_request = Mock(return_value={"law": {"target": "drlaw"}})

    result = client.search_law_ordinance_link_status("민법", page=4, per_page=8)

    assert isinstance(result[0], DrlawList)
    params = client._make_xml_request.call_args.kwargs["params"]
    assert params["target"] == "drlaw"
    assert params["query"] == "민법"
    assert params["display"] == 8
    assert params["page"] == 4


def test_get_delegated_law_detail_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"lsDelegated": {"법령": {}}}))

    result = client.get_delegated_law_detail(law_id="009682")

    assert isinstance(result, LsdelegatedDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lsDelegated"
    assert params["ID"] == "009682"


def test_get_delegated_law_detail_requires_seed_before_request() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock()

    with pytest.raises(ValueError, match="Either law_id or mst must be provided"):
        client.get_delegated_law_detail()

    client._make_request.assert_not_called()


def test_oneview_methods_map_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"items": [{}]}))

    result = client.search_oneview_laws("민법", page=2, per_page=6)

    assert isinstance(result[0], OneviewList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "oneview"
    assert params["query"] == "민법"
    assert params["display"] == 6
    assert params["page"] == 2

    client._make_request = Mock(return_value=_mock_response({"items": {}}))
    detail = client.get_oneview_law_detail(mst="123", article_number=2)

    assert isinstance(detail, OneviewDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "oneview"
    assert params["MST"] == "123"
    assert params["JO"] == "000200"


def test_three_way_comparison_methods_map_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": {"thdCmp": [{}]}}))

    result = client.search_three_way_comparisons(
        "민법",
        page=2,
        per_page=6,
        enforcement_date_range="20240101~20241231",
        promulgation_date=20240101,
        popup=True,
    )

    assert isinstance(result[0], ThdcmpList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "thdCmp"
    assert params["query"] == "민법"
    assert params["display"] == 6
    assert params["page"] == 2
    assert params["efYd"] == "20240101~20241231"
    assert params["date"] == 20240101
    assert params["popYn"] == "Y"

    client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": {}}))
    detail = client.get_three_way_comparison_detail(1, law_id="009682")

    assert isinstance(detail, ThdcmpDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "thdCmp"
    assert params["knd"] == 1
    assert params["ID"] == "009682"


def test_get_three_way_comparison_detail_requires_kind_before_request() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock()

    with pytest.raises(ValueError, match="comparison_kind must be provided"):
        client.get_three_way_comparison_detail(law_id="009682")

    client._make_request.assert_not_called()


def test_get_three_way_comparison_detail_requires_seed_before_request() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock()

    with pytest.raises(ValueError, match="Either law_id or mst must be provided"):
        client.get_three_way_comparison_detail(1)

    client._make_request.assert_not_called()
