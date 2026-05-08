"""Auto-generated tests for target=oneview."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import OneviewDetail, OneviewList
from lawpy.kr.generated.oneview import GeneratedOneviewClient


def _make_client() -> GeneratedOneviewClient:
    return GeneratedOneviewClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedOneviewClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"items": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_oneviews()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OneviewList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_oneviews()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"items": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_oneviews(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"items": {"패턴일련번호": "val", "법령일련번호": "val", "법령명": "val"}}))
        result = client.get_oneview_detail()
        assert isinstance(result, OneviewDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"items": {"패턴일련번호": "val", "법령일련번호": "val", "법령명": "val"}}))
        client.get_oneview_detail(mst="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "MST" in call_params
