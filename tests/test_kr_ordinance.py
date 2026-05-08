"""Tests for Korean local ordinance (자치법규) client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient
from lawpy.kr.generated._models_generated import OrdinDetail, OrdinList


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestOrdinanceClient:
    def test_search_ordinances(self) -> None:
        client = KoreanLawClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "OrdinSearch": {
                        "law": [
                            {
                                "자치법규일련번호": "123",
                                "자치법규명": "서울특별시 테스트 고시",
                                "자치법규종류": "고시",
                            }
                        ]
                    }
                }
            )
        )

        result = client.search_ordinances(query="테스트", ordinance_type="30010")

        assert len(result) == 1
        assert isinstance(result[0], OrdinList)
        assert result[0].자치법규명 == "서울특별시 테스트 고시"

        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "ordin"
        assert params["query"] == "테스트"
        assert params["knd"] == "30010"
        assert params["nw"] == 1

    def test_search_local_notices_uses_ordinance_notice_type(self) -> None:
        client = KoreanLawClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"law": []}}))

        result = client.search_local_notices(query="고시")

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "ordin"
        assert params["knd"] == "30010"
        assert params["query"] == "고시"

    def test_get_ordinance_detail(self) -> None:
        client = KoreanLawClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"OrdinSearch": {"ID": "123", "MST": "456"}}))

        detail = client.get_ordinance_detail(ordinance_id="123")

        assert isinstance(detail, OrdinDetail)
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "ordin"
        assert params["ID"] == "123"

