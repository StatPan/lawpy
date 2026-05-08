"""Tests for Korean annex and form (별표·서식) client."""

from unittest.mock import Mock

from lawpy.kr import AnnexFormClient, KoreanLawClient, KRClient
from lawpy.kr.generated._models_generated import AdmbylList, LicbylList, OrdinbylList


def _mock_response(payload: dict) -> Mock:
    response = Mock()
    response.json.return_value = payload
    return response


def test_annex_form_client_is_on_kr_client() -> None:
    client = KRClient(api_key="test_key")

    assert isinstance(client, AnnexFormClient)
    assert isinstance(client, KoreanLawClient)


def test_search_law_annex_forms_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"target": "licbyl"}]}))

    result = client.search_law_annex_forms(
        query="민법",
        search_scope=2,
        annex_type="1",
        org_code="1170000",
        alphabetical="ga",
        mobile=True,
        page=3,
        per_page=7,
        sort="ldes",
    )

    assert len(result) == 1
    assert isinstance(result[0], LicbylList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "licbyl"
    assert params["query"] == "민법"
    assert params["search"] == 2
    assert params["knd"] == "1"
    assert params["org"] == "1170000"
    assert params["gana"] == "ga"
    assert params["mobileYn"] == "Y"
    assert params["page"] == 3
    assert params["display"] == 7
    assert params["sort"] == "ldes"


def test_search_administrative_rule_annex_forms_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(
        return_value=_mock_response({"admRulBylSearch": {"admrulbyl": [{"target": "admbyl"}]}})
    )

    result = client.search_administrative_rule_annex_forms(query="고시", annex_type="2", mobile=False)

    assert len(result) == 1
    assert isinstance(result[0], AdmbylList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "admbyl"
    assert params["query"] == "고시"
    assert params["knd"] == "2"
    assert params["mobileYn"] == "N"


def test_search_ordinance_annex_forms_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"target": "ordinbyl"}]}))

    result = client.search_ordinance_annex_forms(query="서울", annex_type="3")

    assert len(result) == 1
    assert isinstance(result[0], OrdinbylList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "ordinbyl"
    assert params["query"] == "서울"
    assert params["knd"] == "3"
    assert "mobileYn" not in params
