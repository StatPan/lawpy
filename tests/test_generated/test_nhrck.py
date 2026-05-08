"""Auto-generated tests for target=nhrck."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import NhrckDetail, NhrckList
from lawpy.kr.generated.nhrck import GeneratedNhrckClient


def _make_client() -> GeneratedNhrckClient:
    return GeneratedNhrckClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedNhrckClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_nhrcks()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], NhrckList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_nhrcks()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "키워드": "val", "section": "val"}]}))
        client.search_nhrcks(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"결정문 일련번호": "val", "기관명": "val", "위원회명": "val"}))
        result = client.get_nhrck_detail()
        assert isinstance(result, NhrckDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"결정문 일련번호": "val", "기관명": "val", "위원회명": "val"}))
        client.get_nhrck_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
