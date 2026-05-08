"""Auto-generated tests for target=eflawjosub."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import EflawjosubList
from lawpy.kr.generated.eflawjosub import GeneratedEflawjosubClient


def _make_client() -> GeneratedEflawjosubClient:
    return GeneratedEflawjosubClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedEflawjosubClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"법령": {"법령키": [{"법령키": "val", "법령ID": "val", "공포일자": "val"}]}}))
        result = client.search_eflawjosubs()
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], EflawjosubList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_eflawjosubs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"법령": {"법령키": [{"법령키": "val", "법령ID": "val", "공포일자": "val"}]}}))
        client.search_eflawjosubs(id="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
