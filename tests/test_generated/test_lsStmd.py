"""Auto-generated tests for target=lsStmd."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LsstmdDetail, LsstmdList
from lawpy.kr.generated.lsStmd import GeneratedLsstmdClient


def _make_client() -> GeneratedLsstmdClient:
    return GeneratedLsstmdClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLsstmdClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsStmdSearch": {"law": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_lsStmds()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LsstmdList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lsStmds()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsStmdSearch": {"law": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_lsStmds(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsStmdSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_lsStmds()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LsstmdList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsStmdSearch": {"기본정보": "val", "법령ID": "val", "법령일련번호": "val"}}))
        result = client.get_lsStmd_detail()
        assert isinstance(result, LsstmdDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsStmdSearch": {"기본정보": "val", "법령ID": "val", "법령일련번호": "val"}}))
        client.get_lsStmd_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
