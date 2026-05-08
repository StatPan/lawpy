"""Auto-generated tests for target=lsDelegated."""

from unittest.mock import Mock

from lawpy.kr.generated._models_generated import LsdelegatedDetail
from lawpy.kr.generated.lsDelegated import GeneratedLsdelegatedClient


def _make_client() -> GeneratedLsdelegatedClient:
    return GeneratedLsdelegatedClient(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGeneratedLsdelegatedClient:
    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "lsDelegated": {
                        "법령": {
                            "법령정보": {"법령ID": "val", "법령일련번호": "val", "법령명": "val"},
                            "위임조문정보": [],
                        }
                    }
                }
            )
        )

        result = client.get_lsDelegated_detail(id="1")

        assert isinstance(result, LsdelegatedDetail)

    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(
            return_value=_mock_response(
                {
                    "lsDelegated": {
                        "법령": {
                            "법령정보": {"법령ID": "val", "법령일련번호": "val", "법령명": "val"},
                            "위임조문정보": [],
                        }
                    }
                }
            )
        )

        client.get_lsDelegated_detail(id="1")

        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {}))
        assert "ID" in call_params
