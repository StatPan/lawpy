"""Tests for Korean legal interpretation (법령해석례) client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient, KRClient, LegalInterpretationClient
from lawpy.kr.generated._models_generated import ExpcDetail, ExpcList


def _mock_response(json_data: dict) -> Mock:
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestLegalInterpretationClient:
    def test_search_returns_generated_models(self) -> None:
        client = LegalInterpretationClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "Expc": {
                        "expc": [
                            {
                                "법령해석례일련번호": "123",
                                "안건명": "테스트 해석례",
                                "안건번호": "12-3456",
                            }
                        ]
                    }
                }
            )
        )

        result = client.search_legal_interpretations(query="테스트")

        assert len(result) == 1
        assert isinstance(result[0], ExpcList)
        assert result[0].법령해석례일련번호 == "123"
        assert result[0].안건명 == "테스트 해석례"

    def test_search_translates_public_parameters(self) -> None:
        client = LegalInterpretationClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"Expc": {"expc": []}}))

        result = client.search_legal_interpretations(
            query="건축",
            search_scope=2,
            inquiry_agency="서울특별시",
            reply_agency_code=1721000,
            item_number=1234,
            registered_date_range="20240101~20240131",
            interpretation_date_range="20240201~20240229",
            page=3,
            per_page=50,
            sort="ddes",
            alphabetical="ga",
        )

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "expc"
        assert params["query"] == "건축"
        assert params["search"] == 2
        assert params["inq"] == "서울특별시"
        assert params["rpl"] == 1721000
        assert params["itmno"] == 1234
        assert params["regYd"] == "20240101~20240131"
        assert params["explYd"] == "20240201~20240229"
        assert params["page"] == 3
        assert params["display"] == 50
        assert params["sort"] == "ddes"
        assert params["gana"] == "ga"

    def test_empty_search_uses_defaults(self) -> None:
        client = LegalInterpretationClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"Expc": {"expc": []}}))

        result = client.search_legal_interpretations()

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "expc"
        assert params["type"] == "JSON"
        assert params["search"] == 1
        assert params["page"] == 1
        assert params["display"] == 20
        assert "query" not in params

    def test_detail_id_mapping(self) -> None:
        client = LegalInterpretationClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"Expc": {"ID": "123"}}))

        detail = client.get_legal_interpretation_detail(interpretation_id=123)

        assert isinstance(detail, ExpcDetail)
        assert detail.id == "123"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "expc"
        assert params["ID"] == 123
        assert "LM" not in params

    def test_detail_name_mapping(self) -> None:
        client = LegalInterpretationClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"Expc": {"LM": "테스트 해석례"}}))

        detail = client.get_legal_interpretation_detail(interpretation_name="테스트 해석례")

        assert isinstance(detail, ExpcDetail)
        assert detail.lm == "테스트 해석례"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "expc"
        assert params["LM"] == "테스트 해석례"
        assert "ID" not in params

    def test_kr_client_exposes_methods(self) -> None:
        client = KRClient(api_key="test_key")

        assert isinstance(client, LegalInterpretationClient)
        assert hasattr(client, "search_legal_interpretations")
        assert hasattr(client, "get_legal_interpretation_detail")

    def test_korean_law_client_alias_exposes_methods(self) -> None:
        client = KoreanLawClient(api_key="test_key")

        assert isinstance(client, KRClient)
        assert hasattr(client, "search_legal_interpretations")
        assert hasattr(client, "get_legal_interpretation_detail")
