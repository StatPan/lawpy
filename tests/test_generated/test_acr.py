"""Auto-generated tests for target=acr."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import AcrDetail, AcrList
from lawpy.kr.generated.acr import GeneratedAcrClient


def _make_client() -> GeneratedAcrClient:
    return GeneratedAcrClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedAcrClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_acrs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AcrList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_acrs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_acrs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"결정문 일련번호": "val", "기관명": "val", "회의종류": "val"}))
        result = client.get_acr_detail()
        assert isinstance(result, AcrDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"결정문 일련번호": "val", "기관명": "val", "회의종류": "val"}))
        client.get_acr_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
