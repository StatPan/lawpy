"""Auto-generated tests for target=drlaw."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import DrlawList
from lawpy.kr.generated.drlaw import GeneratedDrlawClient


def _make_client() -> GeneratedDrlawClient:
    return GeneratedDrlawClient(api_key="test_key")


class TestGeneratedDrlawClient:
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_xml_request = Mock(return_value={"law": [{"법령일련번호": "val", "법령ID": "val", "법령명한글": "val"}]})

        result = client.search_drlaws()

        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], DrlawList)

    def test_search_empty_response(self):
        client = _make_client()
        client._make_xml_request = Mock(return_value={})

        result = client.search_drlaws()

        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_passes_params(self):
        client = _make_client()
        client._make_xml_request = Mock(return_value={"law": [{"법령일련번호": "val", "법령ID": "val", "법령명한글": "val"}]})

        client.search_drlaws(query="test")

        call_params = client._make_xml_request.call_args.kwargs.get("params", client._make_xml_request.call_args[1].get("params", {}))
        assert "query" in call_params

