"""Tests for Korean treaty (조약) client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient, KRClient, TreatyClient
from lawpy.kr.generated._models_generated import TrtyDetail, TrtyList


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestTreatyClient:
    def test_search_treaties_returns_generated_models(self) -> None:
        client = TreatyClient(api_key="test_key")
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "TrtySearch": {
                        "Trty": [
                            {
                                "조약일련번호": "123",
                                "조약명": "대한민국과 테스트국 간의 조약",
                                "조약구분코드": "1",
                            }
                        ]
                    }
                }
            )
        )

        result = client.search_treaties(query="테스트")

        assert len(result) == 1
        assert isinstance(result[0], TrtyList)
        assert result[0].조약명 == "대한민국과 테스트국 간의 조약"

    def test_search_treaties_translates_public_parameters(self) -> None:
        client = TreatyClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"Trty": []}}))

        result = client.search_treaties(
            query="FTA",
            search_scope=2,
            treaty_class=1,
            effective_date_range="20200101~20201231",
            conclusion_date_range="20190101~20191231",
            page=3,
            per_page=7,
            sort="ddes",
            alphabetical="ga",
        )

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "trty"
        assert params["query"] == "FTA"
        assert params["search"] == 2
        assert params["cls"] == 1
        assert params["eftYd"] == "20200101~20201231"
        assert params["concYd"] == "20190101~20191231"
        assert params["display"] == 7
        assert params["page"] == 3
        assert params["sort"] == "ddes"
        assert params["gana"] == "ga"

    def test_empty_search_returns_empty_list(self) -> None:
        client = TreatyClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"Trty": []}}))

        result = client.search_treaties()

        assert result == []
        params = client._make_request.call_args.kwargs["params"]
        assert "query" not in params
        assert params["display"] == 20
        assert params["page"] == 1

    def test_get_treaty_detail_maps_treaty_id_to_id(self) -> None:
        client = TreatyClient(api_key="test_key")
        client._make_request = Mock(return_value=_mock_response({"TrtySearch": {"ID": "123"}}))

        detail = client.get_treaty_detail("123")

        assert isinstance(detail, TrtyDetail)
        assert detail.id == "123"
        params = client._make_request.call_args.kwargs["params"]
        assert params["target"] == "trty"
        assert params["ID"] == "123"

    def test_integrated_clients_expose_treaty_methods(self) -> None:
        kr_client = KRClient(api_key="test_key")
        compatibility_client = KoreanLawClient(api_key="test_key")

        assert callable(kr_client.search_treaties)
        assert callable(kr_client.get_treaty_detail)
        assert callable(compatibility_client.search_treaties)
        assert callable(compatibility_client.get_treaty_detail)
