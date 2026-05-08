"""Auto-generated tests for target=acrSpecialDecc."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import AcrspecialdeccDetail, AcrspecialdeccList
from lawpy.kr.generated.acrSpecialDecc import GeneratedAcrspecialdeccClient


def _make_client() -> GeneratedAcrspecialdeccClient:
    return GeneratedAcrspecialdeccClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedAcrspecialdeccClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_acrSpecialDeccs()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], AcrspecialdeccList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_acrSpecialDeccs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_acrSpecialDeccs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": {"특별행정심판재결례일련번호": "val", "사건명": "val", "사건번호": "val"}}))
        result = client.get_acrSpecialDecc_detail()
        assert isinstance(result, AcrspecialdeccDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": {"특별행정심판재결례일련번호": "val", "사건명": "val", "사건번호": "val"}}))
        client.get_acrSpecialDecc_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
