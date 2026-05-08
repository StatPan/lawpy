"""Auto-generated tests for target=lstrmAI."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LstrmaiList
from lawpy.kr.generated.lstrmAI import GeneratedLstrmaiClient


def _make_client() -> GeneratedLstrmaiClient:
    return GeneratedLstrmaiClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLstrmaiClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "검색결과개수": "val"}]}))
        result = client.search_lstrmAIs()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], LstrmaiList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lstrmAIs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "검색결과개수": "val"}]}))
        client.search_lstrmAIs(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params
