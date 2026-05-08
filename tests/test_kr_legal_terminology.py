"""Tests for Korean legal terminology (법령용어) client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient, KRClient, LegalTerminologyClient
from lawpy.kr.generated._models_generated import LstrmDetail, LstrmList


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestLegalTerminologyClient:
    def test_search_legal_terms_returns_generated_models(self) -> None:
        client = LegalTerminologyClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "LsTrmSearch": {
                        "lstrm": [
                            {
                                "법령용어ID": "123",
                                "법령용어명": "과태료",
                                "사전구분코드": "010101",
                            }
                        ]
                    }
                }
            )
        )

        result = client.search_legal_terms(query="과태료")

        assert len(result) == 1
        assert isinstance(result[0], LstrmList)
        assert result[0].법령용어명 == "과태료"

    def test_search_legal_terms_translates_public_parameters(self) -> None:
        client = LegalTerminologyClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": {"lstrm": []}}))

        result = client.search_legal_terms(
            query="과태료",
            law_kind_code=10101,
            page=3,
            per_page=7,
            sort="ldes",
            alphabetical="ga",
        )

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "lstrm"
        assert params["query"] == "과태료"
        assert params["dicKndCd"] == 10101
        assert params["display"] == 7
        assert params["page"] == 3
        assert params["sort"] == "ldes"
        assert params["gana"] == "ga"

    def test_empty_search_returns_empty_list(self) -> None:
        client = LegalTerminologyClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"LsTrmSearch": {"lstrm": []}}))

        result = client.search_legal_terms()

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert "query" not in params
        assert params["display"] == 20
        assert params["page"] == 1

    def test_get_legal_term_detail_maps_term_to_query(self) -> None:
        client = LegalTerminologyClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "LsTrmSearch": {
                        "법령용어 일련번호": "123",
                        "법령용어명_한글": "과태료",
                        "법령용어정의": "행정질서벌",
                    }
                }
            )
        )

        detail = client.get_legal_term_detail("과태료")

        assert isinstance(detail, LstrmDetail)
        assert detail.법령용어명_한글 == "과태료"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "lstrm"
        assert params["query"] == "과태료"

    def test_integrated_clients_expose_legal_terminology_methods(self) -> None:
        kr_client = KRClient(api_key="test_key")
        compatibility_client = KoreanLawClient(api_key="test_key")

        assert callable(kr_client.search_legal_terms)
        assert callable(kr_client.get_legal_term_detail)
        assert callable(compatibility_client.search_legal_terms)
        assert callable(compatibility_client.get_legal_term_detail)
