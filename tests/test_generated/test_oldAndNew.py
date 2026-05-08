"""Auto-generated tests for target=oldAndNew."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import OldandnewDetail, OldandnewList
from lawpy.kr.generated.oldAndNew import GeneratedOldandnewClient


def _make_client() -> GeneratedOldandnewClient:
    return GeneratedOldandnewClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedOldandnewClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OldAndNewLawSearch": {"oldAndNew": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_oldAndNews()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], OldandnewList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_oldAndNews()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OldAndNewLawSearch": {"oldAndNew": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_oldAndNews(query="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OldAndNewLawSearch": {"구조문_ 기본정보": "val", "법령일련번호": "val", "법령ID": "val"}}))
        result = client.get_oldAndNew_detail()
        assert isinstance(result, OldandnewDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OldAndNewLawSearch": {"구조문_ 기본정보": "val", "법령일련번호": "val", "법령ID": "val"}}))
        client.get_oldAndNew_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
