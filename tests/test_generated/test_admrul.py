"""Auto-generated tests for target=admrul."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import AdmrulDetail, AdmrulList
from lawpy.kr.generated.admrul import GeneratedAdmrulClient


def _make_client() -> GeneratedAdmrulClient:
    return GeneratedAdmrulClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedAdmrulClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"admrul": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        result = client.search_admruls()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AdmrulList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({}))
        result = client.search_admruls()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"admrul": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_admruls(nw=1)
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "nw" in call_params

    def test_search_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"admrul": [{"target": "val", "키워드": "val", "section": "val"}]}}))
        client.search_admruls(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"

    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": [{"target": "val", "키워드": "val", "section": "val"}]}))
        result = client.search_admruls()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AdmrulList)

    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"행정규칙 일련번호": "val", "행정규칙명": "val", "행정규칙종류": "val"}}))
        result = client.get_admrul_detail()
        assert isinstance(result, AdmrulDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"행정규칙 일련번호": "val", "행정규칙명": "val", "행정규칙종류": "val"}}))
        client.get_admrul_detail(id="1")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params

    def test_detail_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"행정규칙 일련번호": "val", "행정규칙명": "val", "행정규칙종류": "val"}}))
        client.get_admrul_detail(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert call_params["mobileYn"] == "Y"
