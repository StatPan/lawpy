"""Auto-generated tests for target=ordin."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import OrdinDetail, OrdinList
from lawpy.kr.generated.ordin import GeneratedOrdinClient


def _make_client() -> GeneratedOrdinClient:
    return GeneratedOrdinClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedOrdinClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"law": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_ordins()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdinList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_ordins()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"law": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_ordins(nw=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "nw" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_ordins()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdinList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"OC": "val", "target": "val", "ID": "val"}}))
        result = client.get_ordin_detail()
        assert isinstance(result, OrdinDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"OC": "val", "target": "val", "ID": "val"}}))
        client.get_ordin_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
