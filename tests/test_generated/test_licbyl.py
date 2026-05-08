"""Auto-generated tests for target=licbyl."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LicbylList
from lawpy.kr.generated.licbyl import GeneratedLicbylClient


def _make_client() -> GeneratedLicbylClient:
    return GeneratedLicbylClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLicbylClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_licbyls()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LicbylList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_licbyls()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_licbyls(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"licBylSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_licbyls(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"

    def test_search_nested_empty_list_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"licBylSearch": {"items": []}}))
        result = client.search_licbyls()
        assert isinstance(result, list)
        assert len(result) == 0
