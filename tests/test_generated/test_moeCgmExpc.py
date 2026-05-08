"""Auto-generated tests for target=moeCgmExpc."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import MoecgmexpcDetail, MoecgmexpcList
from lawpy.kr.generated.moeCgmExpc import GeneratedMoecgmexpcClient


def _make_client() -> GeneratedMoecgmexpcClient:
    return GeneratedMoecgmexpcClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedMoecgmexpcClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_moeCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MoecgmexpcList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_moeCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"cgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_moeCgmExpcs(search=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "search" in call_params

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_moeCgmExpcs()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MoecgmexpcList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"법령해석일련번호": "val", "안건명": "val", "안건번호": "val"}}))
        result = client.get_moeCgmExpc_detail()
        assert isinstance(result, MoecgmexpcDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"CgmExpc": {"법령해석일련번호": "val", "안건명": "val", "안건번호": "val"}}))
        client.get_moeCgmExpc_detail(id=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
