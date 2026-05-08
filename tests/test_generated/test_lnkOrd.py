"""Auto-generated tests for target=lnkOrd."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LnkordList
from lawpy.kr.generated.lnkOrd import GeneratedLnkordClient


def _make_client() -> GeneratedLnkordClient:
    return GeneratedLnkordClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLnkordClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_lnkOrds()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], LnkordList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lnkOrds()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_lnkOrds(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params
