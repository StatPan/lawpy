"""Auto-generated tests for target=lstrmRltJo."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LstrmrltjoDetail
from lawpy.kr.generated.lstrmRltJo import GeneratedLstrmrltjoClient


def _make_client() -> GeneratedLstrmrltjoClient:
    return GeneratedLstrmrltjoClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLstrmrltjoClient:
    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"target": "val", "키워드": "val", "검색결과개수": "val"}))
        result = client.get_lstrmRltJo_detail()
        assert isinstance(result, LstrmrltjoDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"target": "val", "키워드": "val", "검색결과개수": "val"}))
        client.get_lstrmRltJo_detail(query="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "query" in call_params
