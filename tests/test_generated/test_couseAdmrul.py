"""Auto-generated tests for target=couseAdmrul."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import CouseadmrulList
from lawpy.kr.generated.couseAdmrul import GeneratedCouseadmrulClient


def _make_client() -> GeneratedCouseadmrulClient:
    return GeneratedCouseadmrulClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedCouseadmrulClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "vcode": "val", "section": "val"}]}))
        result = client.search_couseAdmruls(vcode="test", lj_jo="test")
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CouseadmrulList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_couseAdmruls(vcode="test", lj_jo="test")
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"result": [{"target": "val", "vcode": "val", "section": "val"}]}))
        client.search_couseAdmruls(lj_jo="test", vcode="test")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "vcode" in call_params
