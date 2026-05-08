"""Auto-generated tests for target=ordinbyl."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import OrdinbylList
from lawpy.kr.generated.ordinbyl import GeneratedOrdinbylClient


def _make_client() -> GeneratedOrdinbylClient:
    return GeneratedOrdinbylClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedOrdinbylClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"OC": "val", "target": "val", "search": "val"}]}))
        result = client.search_ordinbyls()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], OrdinbylList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_ordinbyls()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"OC": "val", "target": "val", "search": "val"}]}))
        client.search_ordinbyls(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params
