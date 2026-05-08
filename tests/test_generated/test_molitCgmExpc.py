"""Auto-generated tests for target=molitCgmExpc."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import MolitcgmexpcDetail, MolitcgmexpcList
from lawpy.kr.generated.molitCgmExpc import GeneratedMolitcgmexpcClient


def _make_client() -> GeneratedMolitcgmexpcClient:
    return GeneratedMolitcgmexpcClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedMolitcgmexpcClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_molitCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MolitcgmexpcList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_molitCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_molitCgmExpcs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_molitCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MolitcgmexpcList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"법령해석일련번호": "val", "대분류": "val", "중분류": "val"}}))
        result = client.get_molitCgmExpc_detail()
        assert isinstance(result, MolitcgmexpcDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"법령해석일련번호": "val", "대분류": "val", "중분류": "val"}}))
        client.get_molitCgmExpc_detail(id=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
