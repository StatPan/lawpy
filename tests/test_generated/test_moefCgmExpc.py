"""Auto-generated tests for target=moefCgmExpc."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import MoefcgmexpcList
from lawpy.kr.generated.moefCgmExpc import GeneratedMoefcgmexpcClient


def _make_client() -> GeneratedMoefcgmexpcClient:
    return GeneratedMoefcgmexpcClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedMoefcgmexpcClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_moefCgmExpcs()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], MoefcgmexpcList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_moefCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_moefCgmExpcs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params
