"""Tests for Korean school/public rule client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient, KRClient, SchoolPublicRuleClient
from lawpy.kr.generated._models_generated import SchoolDetail, SchoolList


def _mock_response(payload: dict) -> Mock:
    response = Mock()
    response.json.return_value = payload
    return response


def test_school_public_rule_client_is_on_kr_client() -> None:
    client = KRClient(api_key="test_key")

    assert isinstance(client, SchoolPublicRuleClient)
    assert isinstance(client, KoreanLawClient)


def test_search_school_public_rules_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"school": [{"target": "school"}]}))

    result = client.search_school_public_rules(
        query="자동차",
        current=False,
        search_scope=2,
        category="5",
        revision_code="200403",
        promulgation_date=20240101,
        promulgation_date_range="20240101~20241231",
        promulgation_number=7,
        alphabetical="ga",
        popup=True,
        page=3,
        per_page=9,
        sort="ldes",
    )

    assert len(result) == 1
    assert isinstance(result[0], SchoolList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "school"
    assert params["query"] == "자동차"
    assert params["nw"] == 2
    assert params["search"] == 2
    assert params["knd"] == "5"
    assert params["rrClsCd"] == "200403"
    assert params["date"] == 20240101
    assert params["prmlYd"] == "20240101~20241231"
    assert params["nb"] == 7
    assert params["gana"] == "ga"
    assert params["popYn"] == "Y"
    assert params["page"] == 3
    assert params["display"] == 9
    assert params["sort"] == "ldes"


def test_search_school_public_rules_omits_optional_flags() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"school": [{"target": "school"}]}))

    client.search_school_public_rules()

    params = client._make_request.call_args.kwargs["params"]
    assert "nw" not in params
    assert "popYn" not in params


def test_get_school_public_rule_detail_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"행정규칙명": "한국방송통신대학교 학칙"}))

    result = client.get_school_public_rule_detail(
        rule_id="123",
        rule_lid="ABC",
        rule_name="한국방송통신대학교 학칙",
    )

    assert isinstance(result, SchoolDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "school"
    assert params["ID"] == "123"
    assert params["LID"] == "ABC"
    assert params["LM"] == "한국방송통신대학교 학칙"
