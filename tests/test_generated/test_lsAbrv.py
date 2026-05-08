"""Auto-generated tests for target=lsAbrv."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LsabrvList
from lawpy.kr.generated.lsAbrv import GeneratedLsabrvClient


def _make_client() -> GeneratedLsabrvClient:
    return GeneratedLsabrvClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLsabrvClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": {"law": [{"target": "val", "totalCnt": "val", "law id": "val"}]}}))
        result = client.search_lsAbrvs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LsabrvList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lsAbrvs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": {"law": [{"target": "val", "totalCnt": "val", "law id": "val"}]}}))
        client.search_lsAbrvs(stddt=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "stdDt" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": [{"target": "val", "totalCnt": "val", "law id": "val"}]}))
        result = client.search_lsAbrvs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LsabrvList)
