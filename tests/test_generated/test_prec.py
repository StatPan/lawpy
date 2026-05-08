"""Auto-generated tests for target=prec."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import PrecDetail, PrecList
from lawpy.kr.generated.prec import GeneratedPrecClient


def _make_client() -> GeneratedPrecClient:
    return GeneratedPrecClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedPrecClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": {"prec": [{"target": "val", "공포번호": "val", "키워드": "val"}]}}))
        result = client.search_precs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PrecList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_precs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": {"prec": [{"target": "val", "공포번호": "val", "키워드": "val"}]}}))
        client.search_precs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": {"prec": [{"target": "val", "공포번호": "val", "키워드": "val"}]}}))
        client.search_precs(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": [{"target": "val", "공포번호": "val", "키워드": "val"}]}))
        result = client.search_precs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PrecList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": {"판례정보일련번호": "val", "사건명": "val", "사건번호": "val"}}))
        result = client.get_prec_detail()
        assert isinstance(result, PrecDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": {"판례정보일련번호": "val", "사건명": "val", "사건번호": "val"}}))
        client.get_prec_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params

    def test_detail_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"PrecSearch": {"판례정보일련번호": "val", "사건명": "val", "사건번호": "val"}}))
        client.get_prec_detail(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"
