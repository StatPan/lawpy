"""Tests for Korean ministry interpretation client."""

from unittest.mock import Mock

import pytest
from pydantic import BaseModel

from lawpy.kr import KoreanLawClient, KRClient, MinistryInterpretationClient
from lawpy.kr.generated._models_generated import MojcgmexpcDetail, MojcgmexpcList, NtscgmexpcList
from lawpy.kr.ministry_interpretation import (
    MINISTRY_INTERPRETATION_TARGETS,
    MinistryInterpretationTarget,
)


def _mock_response(payload: dict) -> Mock:
    response = Mock()
    response.json.return_value = payload
    return response


@pytest.mark.parametrize("ministry", list(MINISTRY_INTERPRETATION_TARGETS))
def test_ministry_interpretation_targets_map_search_params(
    ministry: MinistryInterpretationTarget,
) -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(
        return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": ministry}]}})
    )

    result = client.search_ministry_interpretations(
        ministry,
        "과태료",
        search_scope=2,
        page=3,
        per_page=9,
        question_agency_code=10,
        interpretation_agency_code=20,
        agenda_number=30,
        interpretation_date_range="20240101~20241231",
        sort="ldes",
        alphabetical="ga",
        popup=True,
        fields="안건명,안건번호",
    )

    assert len(result) == 1
    assert isinstance(result[0], BaseModel)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == ministry
    assert params["query"] == "과태료"
    assert params["search"] == 2
    assert params["page"] == 3
    assert params["display"] == 9
    assert params["sort"] == "ldes"
    assert params["gana"] == "ga"
    assert params["popYn"] == "Y"
    assert params["fields"] == "안건명,안건번호"


def test_ministry_interpretation_client_is_on_kr_client() -> None:
    client = KRClient(api_key="test_key")

    assert isinstance(client, MinistryInterpretationClient)
    assert isinstance(client, KoreanLawClient)
    assert client.list_ministry_interpretation_targets()["mojCgmExpc"] == "법무부 법령해석"


def test_search_ministry_interpretations_returns_generated_model() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(
        return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "mojCgmExpc"}]}})
    )

    result = client.search_ministry_interpretations("mojCgmExpc")

    assert isinstance(result[0], MojcgmexpcList)


def test_search_ministry_interpretations_maps_extended_params_when_supported() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(
        return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "mojCgmExpc"}]}})
    )

    client.search_ministry_interpretations(
        "mojCgmExpc",
        question_agency_code=10,
        interpretation_agency_code=20,
        agenda_number=30,
        interpretation_date_range="20240101~20241231",
    )

    params = client._make_request.call_args.kwargs["params"]
    assert params["inq"] == 10
    assert params["rpl"] == 20
    assert params["itmno"] == 30
    assert params["explYd"] == "20240101~20241231"


def test_search_ministry_interpretations_supports_list_only_targets() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(
        return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "ntsCgmExpc"}]}})
    )

    result = client.search_ministry_interpretations("ntsCgmExpc")

    assert isinstance(result[0], NtscgmexpcList)


def test_get_ministry_interpretation_detail_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"안건명": "과태료"}))

    result = client.get_ministry_interpretation_detail(
        "mojCgmExpc",
        interpretation_id=123,
        interpretation_name="과태료",
        fields="안건명",
    )

    assert isinstance(result, MojcgmexpcDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "mojCgmExpc"
    assert params["ID"] == 123
    assert params["LM"] == "과태료"
    assert params["fields"] == "안건명"


@pytest.mark.parametrize("ministry", ["moefCgmExpc", "ntsCgmExpc"])
def test_get_ministry_interpretation_detail_rejects_list_only_targets(
    ministry: MinistryInterpretationTarget,
) -> None:
    client = KRClient(api_key="test_key")

    with pytest.raises(ValueError, match="list search only"):
        client.get_ministry_interpretation_detail(ministry, interpretation_id=123)
