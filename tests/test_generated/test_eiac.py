"""Auto-generated tests for target=eiac."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import EiacDetail, EiacList
from lawpy.kr.generated.eiac import GeneratedEiacClient


def _make_client() -> GeneratedEiacClient:
    return GeneratedEiacClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedEiacClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_eiacs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], EiacList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_eiacs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_eiacs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"결정문 일련번호": "val", "사건의분류": "val", "의결서종류": "val"}))
        result = client.get_eiac_detail()
        assert isinstance(result, EiacDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"결정문 일련번호": "val", "사건의분류": "val", "의결서종류": "val"}))
        client.get_eiac_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
