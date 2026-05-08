"""Tests for Korean administrative review decision (행정심판례) client."""

from unittest.mock import Mock

from lawpy.kr import AdministrativeReviewDecisionClient, KoreanLawClient, KRClient
from lawpy.kr.generated._models_generated import DeccDetail, DeccList


def _mock_response(json_data: dict) -> Mock:
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestAdministrativeReviewDecisionClient:
    def test_search_returns_generated_models_from_root_list(self) -> None:
        client = AdministrativeReviewDecisionClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "Decc": [
                        {
                            "행정심판재결례일련번호": "123",
                            "사건명": "테스트 행정심판례",
                            "사건번호": "2024-12345",
                        }
                    ]
                }
            )
        )

        result = client.search_administrative_review_decisions(query="테스트")

        assert len(result) == 1
        assert isinstance(result[0], DeccList)
        assert result[0].행정심판재결례일련번호 == "123"
        assert result[0].사건명 == "테스트 행정심판례"

    def test_search_translates_public_parameters(self) -> None:
        client = AdministrativeReviewDecisionClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"Decc": []}))

        result = client.search_administrative_review_decisions(
            query="영업정지",
            search_scope=2,
            decision_type_code="010",
            decision_date=20240131,
            disposition_date_range="20240101~20240131",
            resolution_date_range="20240201~20240229",
            page=3,
            per_page=50,
            sort="ddes",
            alphabetical="ga",
        )

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "decc"
        assert params["query"] == "영업정지"
        assert params["search"] == 2
        assert params["cls"] == "010"
        assert params["date"] == 20240131
        assert params["dpaYd"] == "20240101~20240131"
        assert params["rslYd"] == "20240201~20240229"
        assert params["page"] == 3
        assert params["display"] == 50
        assert params["sort"] == "ddes"
        assert params["gana"] == "ga"

    def test_empty_search_uses_defaults(self) -> None:
        client = AdministrativeReviewDecisionClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"Decc": []}))

        result = client.search_administrative_review_decisions()

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "decc"
        assert params["type"] == "JSON"
        assert params["search"] == 1
        assert params["page"] == 1
        assert params["display"] == 20
        assert "query" not in params

    def test_detail_id_mapping(self) -> None:
        client = AdministrativeReviewDecisionClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response({"Decc": {"행정심판례일련번호": "123"}})
        )

        detail = client.get_administrative_review_decision_detail(decision_id="123")

        assert isinstance(detail, DeccDetail)
        assert detail.행정심판례일련번호 == "123"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "decc"
        assert params["ID"] == "123"
        assert "LM" not in params

    def test_detail_name_mapping(self) -> None:
        client = AdministrativeReviewDecisionClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response({"Decc": {"사건명": "테스트 행정심판례"}})
        )

        detail = client.get_administrative_review_decision_detail(
            decision_name="테스트 행정심판례"
        )

        assert isinstance(detail, DeccDetail)
        assert detail.사건명 == "테스트 행정심판례"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "decc"
        assert params["LM"] == "테스트 행정심판례"
        assert "ID" not in params

    def test_kr_client_exposes_methods(self) -> None:
        client = KRClient(api_key="test_key")

        assert isinstance(client, AdministrativeReviewDecisionClient)
        assert hasattr(client, "search_administrative_review_decisions")
        assert hasattr(client, "get_administrative_review_decision_detail")

    def test_korean_law_client_alias_exposes_methods(self) -> None:
        client = KoreanLawClient(api_key="test_key")

        assert isinstance(client, KRClient)
        assert hasattr(client, "search_administrative_review_decisions")
        assert hasattr(client, "get_administrative_review_decision_detail")
