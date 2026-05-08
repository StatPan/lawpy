"""Auto-generated tests for target=lnkLs."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LnklsList
from lawpy.kr.generated.lnkLs import GeneratedLnklsClient


def _make_client() -> GeneratedLnklsClient:
    return GeneratedLnklsClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLnklsClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_lnkLss()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], LnklsList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lnkLss()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_lnkLss(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params
