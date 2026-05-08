"""Auto-generated tests for target=lstrm."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LstrmDetail, LstrmList
from lawpy.kr.generated.lstrm import GeneratedLstrmClient


def _make_client() -> GeneratedLstrmClient:
    return GeneratedLstrmClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLstrmClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": {"lstrm": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_lstrms()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LstrmList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lstrms()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": {"lstrm": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_lstrms(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_lstrms()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LstrmList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": {"법령용어 일련번호": "val", "법령용어명_한글": "val", "법령용어명_한자": "val"}}))
        result = client.get_lstrm_detail()
        assert isinstance(result, LstrmDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": {"법령용어 일련번호": "val", "법령용어명_한글": "val", "법령용어명_한자": "val"}}))
        client.get_lstrm_detail(query="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params
