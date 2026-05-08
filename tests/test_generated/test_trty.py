"""Auto-generated tests for target=trty."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import TrtyDetail, TrtyList
from lawpy.kr.generated.trty import GeneratedTrtyClient


def _make_client() -> GeneratedTrtyClient:
    return GeneratedTrtyClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedTrtyClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"Trty": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_trtys()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TrtyList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_trtys()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"Trty": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_trtys(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"Trty": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_trtys(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_trtys()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TrtyList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"조약일련번호": "val", "조약명_한글": "val", "조약명_영문": "val"}}))
        result = client.get_trty_detail()
        assert isinstance(result, TrtyDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"조약일련번호": "val", "조약명_한글": "val", "조약명_영문": "val"}}))
        client.get_trty_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params

    def test_detail_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"조약일련번호": "val", "조약명_한글": "val", "조약명_영문": "val"}}))
        client.get_trty_detail(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"
