"""Auto-generated tests for target=admbyl."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import AdmbylList
from lawpy.kr.generated.admbyl import GeneratedAdmbylClient


def _make_client() -> GeneratedAdmbylClient:
    return GeneratedAdmbylClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedAdmbylClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"admRulBylSearch": {"admrulbyl": [{"OC": "val", "target": "val", "search": "val"}]}}))
        result = client.search_admbyls()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AdmbylList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_admbyls()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"admRulBylSearch": {"admrulbyl": [{"OC": "val", "target": "val", "search": "val"}]}}))
        client.search_admbyls(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"admRulBylSearch": [{"OC": "val", "target": "val", "search": "val"}]}))
        result = client.search_admbyls()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AdmbylList)
