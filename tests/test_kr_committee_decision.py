"""Tests for Korean committee decision client."""

from unittest.mock import Mock

import pytest

from lawpy.kr import CommitteeDecisionClient, KoreanLawClient, KRClient
from lawpy.kr.committee_decision import COMMITTEE_DECISION_TARGETS, CommitteeDecisionTarget
from lawpy.kr.generated._models_generated import AcrDetail, AcrList, BaipvcsList


def _mock_response(payload: dict) -> Mock:
    response = Mock()
    response.json.return_value = payload
    return response


@pytest.mark.parametrize("committee", list(COMMITTEE_DECISION_TARGETS))
def test_committee_decision_targets_map_search_params(
    committee: CommitteeDecisionTarget,
) -> None:
    client = KRClient(api_key="test_key")
    payload = {"BaiPvcs": [{"target": committee}]} if committee == "baiPvcs" else {"result": [{"target": committee}]}
    client._make_request = Mock(return_value=_mock_response(payload))

    result = client.search_committee_decisions(
        committee,
        "영업정지",
        search_scope=2,
        page=3,
        per_page=9,
        sort="ldes",
        alphabetical="ga",
        popup=True,
    )

    assert len(result) == 1
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == committee
    assert params["query"] == "영업정지"
    assert params["search"] == 2
    assert params["page"] == 3
    assert params["display"] == 9
    assert params["sort"] == "ldes"
    assert params["gana"] == "ga"
    assert params["popYn"] == "Y"


def test_committee_decision_client_is_on_kr_client() -> None:
    client = KRClient(api_key="test_key")

    assert isinstance(client, CommitteeDecisionClient)
    assert isinstance(client, KoreanLawClient)
    assert client.list_committee_decision_targets()["ftc"] == "공정거래위원회 결정문"


def test_search_committee_decisions_returns_generated_model() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"result": [{"target": "acr"}]}))

    result = client.search_committee_decisions("acr")

    assert isinstance(result[0], AcrList)


def test_search_committee_decisions_maps_bai_response_date() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"BaiPvcs": [{"target": "baiPvcs"}]}))

    result = client.search_committee_decisions("baiPvcs", response_date=20240101)

    assert isinstance(result[0], BaipvcsList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "baiPvcs"
    assert params["date"] == 20240101


def test_search_committee_decisions_rejects_bai_only_response_date_for_others() -> None:
    client = KRClient(api_key="test_key")

    with pytest.raises(ValueError, match="response_date is only supported"):
        client.search_committee_decisions("ftc", response_date=20240101)


def test_get_committee_decision_detail_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"제목": "결정문"}))

    result = client.get_committee_decision_detail("acr", decision_id="123")

    assert isinstance(result, AcrDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "acr"
    assert params["ID"] == "123"
