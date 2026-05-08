"""Auto-generated tests for target=lsJoHstInf."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LsjohstinfList
from lawpy.kr.generated.lsJoHstInf import GeneratedLsjohstinfClient


def _make_client() -> GeneratedLsjohstinfClient:
    return GeneratedLsjohstinfClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLsjohstinfClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": [{"법령ID": "val", "법령명한글": "val", "법령일련번호": "val"}]}))
        result = client.search_lsJoHstInfs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LsjohstinfList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_lsJoHstInfs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"LawSearch": [{"법령ID": "val", "법령명한글": "val", "법령일련번호": "val"}]}))
        client.search_lsJoHstInfs(id="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
