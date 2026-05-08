"""Auto-generated tests for target=joRltLstrm."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import JorltlstrmDetail
from lawpy.kr.generated.joRltLstrm import GeneratedJorltlstrmClient


def _make_client() -> GeneratedJorltlstrmClient:
    return GeneratedJorltlstrmClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedJorltlstrmClient:
    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"target": "val", "키워드": "val", "검색결과개수": "val"}))
        result = client.get_joRltLstrm_detail()
        assert isinstance(result, JorltlstrmDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"target": "val", "키워드": "val", "검색결과개수": "val"}))
        client.get_joRltLstrm_detail(query="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params
