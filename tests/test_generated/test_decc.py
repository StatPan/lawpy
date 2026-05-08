"""Auto-generated tests for target=decc."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import DeccDetail, DeccList
from lawpy.kr.generated.decc import GeneratedDeccClient


def _make_client() -> GeneratedDeccClient:
    return GeneratedDeccClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedDeccClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": [{"target": "val", "키워드": "val", "section": "val", "의결일자": "20240131"}]}))
        result = client.search_deccs()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], DeccList)
            assert result[0].의결일자 == "20240131"

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_deccs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": [{"target": "val", "키워드": "val", "section": "val", "의결일자": "20240131"}]}))
        client.search_deccs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_passes_popyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": [{"target": "val", "키워드": "val", "section": "val", "의결일자": "20240131"}]}))
        client.search_deccs(popyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["popYn"] == "Y"
        assert "mobileYn" not in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": {"행정심판례일련번호": "val", "사건명": "val", "사건번호": "val", "주문": "val"}}))
        result = client.get_decc_detail()
        assert isinstance(result, DeccDetail)
        assert result.사건명 == "val"
        assert result.주문 == "val"

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"Decc": {"행정심판례일련번호": "val", "사건명": "val", "사건번호": "val", "주문": "val"}}))
        client.get_decc_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
