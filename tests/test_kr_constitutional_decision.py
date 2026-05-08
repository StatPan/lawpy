"""Tests for Korean constitutional decision (헌재결정례) client."""

from unittest.mock import Mock

from lawpy.kr import ConstitutionalDecisionClient, KoreanLawClient, KRClient
from lawpy.kr.generated._models_generated import DetcDetail, DetcList


def _mock_response(json_data: dict) -> Mock:
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestConstitutionalDecisionClient:
    def test_search_returns_generated_models(self) -> None:
        client = ConstitutionalDecisionClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "DetcSearch": {
                        "Detc": [
                            {
                                "헌재결정례일련번호": "123",
                                "사건명": "테스트 헌재결정례",
                                "사건번호": "2024헌마123",
                            }
                        ]
                    }
                }
            )
        )

        result = client.search_constitutional_decisions(query="테스트")

        assert len(result) == 1
        assert isinstance(result[0], DetcList)
        assert result[0].헌재결정례일련번호 == "123"
        assert result[0].사건명 == "테스트 헌재결정례"

    def test_search_translates_public_parameters(self) -> None:
        client = ConstitutionalDecisionClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"DetcSearch": {"Detc": []}}))

        result = client.search_constitutional_decisions(
            query="기본권",
            search_scope=2,
            decision_date=20240131,
            case_number=20240123,
            page=3,
            per_page=50,
            sort="ddes",
            alphabetical="ga",
        )

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "detc"
        assert params["query"] == "기본권"
        assert params["search"] == 2
        assert params["date"] == 20240131
        assert params["nb"] == 20240123
        assert params["page"] == 3
        assert params["display"] == 50
        assert params["sort"] == "ddes"
        assert params["gana"] == "ga"

    def test_empty_search_uses_defaults(self) -> None:
        client = ConstitutionalDecisionClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"DetcSearch": {"Detc": []}}))

        result = client.search_constitutional_decisions()

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "detc"
        assert params["type"] == "JSON"
        assert params["search"] == 1
        assert params["page"] == 1
        assert params["display"] == 20
        assert "query" not in params

    def test_detail_id_mapping(self) -> None:
        client = ConstitutionalDecisionClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"DetcSearch": {"ID": "123"}}))

        detail = client.get_constitutional_decision_detail(decision_id="123")

        assert isinstance(detail, DetcDetail)
        assert detail.id == "123"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "detc"
        assert params["ID"] == "123"
        assert "LM" not in params

    def test_detail_name_mapping(self) -> None:
        client = ConstitutionalDecisionClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"DetcSearch": {"LM": "테스트 헌재결정례"}}))

        detail = client.get_constitutional_decision_detail(decision_name="테스트 헌재결정례")

        assert isinstance(detail, DetcDetail)
        assert detail.lm == "테스트 헌재결정례"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "detc"
        assert params["LM"] == "테스트 헌재결정례"
        assert "ID" not in params

    def test_kr_client_exposes_methods(self) -> None:
        client = KRClient(api_key="test_key")

        assert isinstance(client, ConstitutionalDecisionClient)
        assert hasattr(client, "search_constitutional_decisions")
        assert hasattr(client, "get_constitutional_decision_detail")

    def test_korean_law_client_alias_exposes_methods(self) -> None:
        client = KoreanLawClient(api_key="test_key")

        assert isinstance(client, KRClient)
        assert hasattr(client, "search_constitutional_decisions")
        assert hasattr(client, "get_constitutional_decision_detail")
