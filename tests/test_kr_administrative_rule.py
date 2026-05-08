"""Tests for Korean administrative rule (행정규칙) client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient
from lawpy.kr.generated._models_generated import AdmrulDetail, AdmrulList


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestAdministrativeRuleClient:
    def test_search_administrative_rules(self) -> None:
        client = KoreanLawClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "AdmRulSearch": {
                        "admrul": [
                            {
                                "행정규칙 일련번호": "123",
                                "행정규칙명": "테스트 고시",
                                "행정규칙종류": "고시",
                            }
                        ]
                    }
                }
            )
        )

        result = client.search_administrative_rules(query="테스트", rule_type="3")

        assert len(result) == 1
        assert isinstance(result[0], AdmrulList)
        assert result[0].행정규칙명 == "테스트 고시"

        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "admrul"
        assert params["query"] == "테스트"
        assert params["knd"] == "3"
        assert params["nw"] == 1

    def test_search_notices_uses_administrative_rule_notice_type(self) -> None:
        client = KoreanLawClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"AdmRulSearch": {"admrul": []}}))

        result = client.search_notices(query="고시")

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "admrul"
        assert params["knd"] == "3"
        assert params["query"] == "고시"

    def test_get_administrative_rule_detail(self) -> None:
        client = KoreanLawClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response({"AdmRulSearch": {"ID": "123", "LM": "테스트 고시"}})
        )

        detail = client.get_administrative_rule_detail(rule_id="123")

        assert isinstance(detail, AdmrulDetail)
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "admrul"
        assert params["ID"] == "123"
