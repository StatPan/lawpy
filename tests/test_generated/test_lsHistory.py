"""Auto-generated tests for target=lsHistory."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LshistoryDetail, LshistoryList
from lawpy.kr.generated.lsHistory import GeneratedLshistoryClient


def _make_client() -> GeneratedLshistoryClient:
    return GeneratedLshistoryClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLshistoryClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"OC": "val", "target": "val", "type": "val"}]}))
        result = client.search_lsHistorys()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LshistoryList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lsHistorys()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"OC": "val", "target": "val", "type": "val"}]}))
        client.search_lsHistorys(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OC": "val", "target": "val", "type": "val"}))
        result = client.get_lsHistory_detail()
        assert isinstance(result, LshistoryDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OC": "val", "target": "val", "type": "val"}))
        client.get_lsHistory_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
