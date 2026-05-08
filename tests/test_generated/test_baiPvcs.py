"""Auto-generated tests for target=baiPvcs."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import BaipvcsDetail, BaipvcsList
from lawpy.kr.generated.baiPvcs import GeneratedBaipvcsClient


def _make_client() -> GeneratedBaipvcsClient:
    return GeneratedBaipvcsClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedBaipvcsClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"BaiPvcs": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_baiPvcss()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], BaipvcsList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_baiPvcss()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"BaiPvcs": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_baiPvcss(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"BaiPvcs": {"감사원사전컨설팅의견서일련번호": "val", "의견서명": "val", "회신일자": "val"}}))
        result = client.get_baiPvcs_detail()
        assert isinstance(result, BaipvcsDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"BaiPvcs": {"감사원사전컨설팅의견서일련번호": "val", "의견서명": "val", "회신일자": "val"}}))
        client.get_baiPvcs_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
