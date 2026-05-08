"""Auto-generated tests for target=thdCmp."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import ThdcmpDetail, ThdcmpList
from lawpy.kr.generated.thdCmp import GeneratedThdcmpClient


def _make_client() -> GeneratedThdcmpClient:
    return GeneratedThdcmpClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedThdcmpClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": {"thdCmp": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_thdCmps()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ThdcmpList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_thdCmps()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": {"thdCmp": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_thdCmps(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_thdCmps()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ThdcmpList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": {"기본정보": "val", "법령ID": "val", "시행령ID": "val"}}))
        result = client.get_thdCmp_detail()
        assert isinstance(result, ThdcmpDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"thdCmpLawSearch": {"기본정보": "val", "법령ID": "val", "시행령ID": "val"}}))
        client.get_thdCmp_detail(knd=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "knd" in call_params
