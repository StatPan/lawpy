"""Tests for Korean Constitutional Court decision (헌재결정례) client."""

from unittest.mock import Mock, patch

import pytest

from lawpy.exceptions import APIError, NotFoundError, ParseError
from lawpy.kr import KoreanLawClient


@pytest.fixture
def client() -> KoreanLawClient:
    """Create a test client."""
    return KoreanLawClient(api_key="test_key")


# ---------------------------------------------------------------------------
# Helper XML fixtures
# ---------------------------------------------------------------------------

DETC_LIST_XML = """<?xml version="1.0" encoding="UTF-8"?>
<DetcSearch>
    <detc id="1">
        <헌재결정례일련번호>10001</헌재결정례일련번호>
        <사건명><![CDATA[위헌소원]]></사건명>
        <사건번호>2020헌바123</사건번호>
        <종국일자>20201015</종국일자>
        <헌재결정례상세링크>https://www.law.go.kr/LSW/detcInfoP.do?detcSeq=10001</헌재결정례상세링크>
    </detc>
    <detc id="2">
        <헌재결정례일련번호>10002</헌재결정례일련번호>
        <사건명><![CDATA[헌법소원심판]]></사건명>
        <사건번호>2021헌마456</사건번호>
        <종국일자>20211201</종국일자>
        <헌재결정례상세링크>https://www.law.go.kr/LSW/detcInfoP.do?detcSeq=10002</헌재결정례상세링크>
    </detc>
</DetcSearch>""".encode()

DETC_LIST_EMPTY_XML = b"""<?xml version="1.0" encoding="UTF-8"?><DetcSearch/>"""

DETC_SINGLE_LIST_XML = """<?xml version="1.0" encoding="UTF-8"?>
<DetcSearch>
    <detc id="1">
        <헌재결정례일련번호>10001</헌재결정례일련번호>
        <사건명><![CDATA[위헌소원]]></사건명>
        <사건번호>2020헌바123</사건번호>
    </detc>
</DetcSearch>""".encode()

DETC_DETAIL_XML = """<?xml version="1.0" encoding="UTF-8"?>
<DetcService>
    <헌재결정례일련번호>10001</헌재결정례일련번호>
    <사건명><![CDATA[위헌소원]]></사건명>
    <사건번호>2020헌바123</사건번호>
    <종국일자>20201015</종국일자>
    <사건종류>헌법소원</사건종류>
    <결정유형>인용</결정유형>
    <참조조문>헌법 제12조, 형사소송법 제244조</참조조문>
    <판시사항>피의자 진술거부권 고지 의무의 범위</판시사항>
    <결정요지>수사기관은 피의자에게 진술거부권을 고지할 의무가 있다.</결정요지>
    <결정내용>【주문】 이 사건 헌법소원심판 청구를 인용한다. 【이유】 살피건대...</결정내용>
</DetcService>""".encode()


# ---------------------------------------------------------------------------
# Test: search_decisions
# ---------------------------------------------------------------------------


class TestSearchDecisions:
    """Tests for ConstitutionalDecisionClient.search_decisions."""

    def test_search_returns_list(self, client: KoreanLawClient) -> None:
        """Parsing a two-item list returns two ConstitutionalDecision objects."""
        mock_resp = Mock()
        mock_resp.content = DETC_LIST_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_decisions(query="위헌")

        assert len(results) == 2

    def test_search_fields_mapped_correctly(self, client: KoreanLawClient) -> None:
        """All list fields are mapped onto the ConstitutionalDecision model."""
        mock_resp = Mock()
        mock_resp.content = DETC_LIST_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_decisions()

        first = results[0]
        assert first.decision_id == "10001"
        assert first.case_name == "위헌소원"
        assert first.case_number == "2020헌바123"
        assert first.final_date == "20201015"
        assert first.detail_link is not None and "10001" in first.detail_link

    def test_search_empty_result(self, client: KoreanLawClient) -> None:
        """Empty DetcSearch element returns an empty list."""
        mock_resp = Mock()
        mock_resp.content = DETC_LIST_EMPTY_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_decisions(query="없는결정")

        assert results == []

    def test_search_single_item_not_wrapped_in_list(self, client: KoreanLawClient) -> None:
        """xmltodict returns a dict (not list) for single items — still works."""
        mock_resp = Mock()
        mock_resp.content = DETC_SINGLE_LIST_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_decisions()

        assert len(results) == 1
        assert results[0].decision_id == "10001"

    def test_search_with_optional_params_sent(self, client: KoreanLawClient) -> None:
        """Optional filtering params are forwarded to the HTTP call."""
        mock_resp = Mock()
        mock_resp.content = DETC_LIST_EMPTY_XML
        mock_get = Mock(return_value=mock_resp)

        with patch.object(client._client, "get", mock_get):
            client.search_decisions(
                query="헌법",
                search_scope=2,
                sort="efdes",
                page=2,
                per_page=50,
                case_gana="ga",
                final_date="20201015",
                case_number="2020헌바123",
            )

        call_kwargs = mock_get.call_args
        params = call_kwargs[1]["params"] if call_kwargs[1] else call_kwargs[0][1]
        assert params["query"] == "헌법"
        assert params["search"] == 2
        assert params["sort"] == "efdes"
        assert params["page"] == 2
        assert params["display"] == 50
        assert params["gana"] == "ga"
        assert params["date"] == "20201015"
        assert params["nb"] == "2020헌바123"
        assert params["target"] == "detc"

    def test_search_api_error(self, client: KoreanLawClient) -> None:
        """HTTP 500 is wrapped in APIError."""
        from httpx import HTTPStatusError

        mock_resp = Mock()
        mock_resp.status_code = 500
        err = HTTPStatusError("Server error", request=Mock(), response=mock_resp)

        with patch.object(client._client, "get", side_effect=err):
            with pytest.raises(APIError) as exc_info:
                client.search_decisions(query="헌법")

        assert "HTTP error: 500" in str(exc_info.value)

    def test_search_invalid_xml_raises_parse_error(self, client: KoreanLawClient) -> None:
        """Malformed XML raises ParseError."""
        mock_resp = Mock()
        mock_resp.content = b"this is not xml at all <<<>>>"

        with patch.object(client._client, "get", return_value=mock_resp):
            with pytest.raises(ParseError):
                client.search_decisions()


# ---------------------------------------------------------------------------
# Test: get_decision_detail
# ---------------------------------------------------------------------------


class TestGetDecisionDetail:
    """Tests for ConstitutionalDecisionClient.get_decision_detail."""

    def test_detail_fields_mapped_correctly(self, client: KoreanLawClient) -> None:
        """All detail fields are mapped onto ConstitutionalDecisionDetail."""
        mock_resp = Mock()
        mock_resp.content = DETC_DETAIL_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            detail = client.get_decision_detail("10001")

        assert detail.decision_id == "10001"
        assert detail.case_name == "위헌소원"
        assert detail.case_number == "2020헌바123"
        assert detail.final_date == "20201015"
        assert detail.case_type == "헌법소원"
        assert detail.decision_type == "인용"
        assert detail.ref_statutes is not None and "헌법 제12조" in detail.ref_statutes
        assert detail.ruling_summary == "피의자 진술거부권 고지 의무의 범위"
        assert detail.decision_gist is not None and "진술거부권" in detail.decision_gist
        assert detail.full_text is not None and "인용" in detail.full_text

    def test_detail_id_param_sent(self, client: KoreanLawClient) -> None:
        """The ID parameter is forwarded correctly."""
        mock_resp = Mock()
        mock_resp.content = DETC_DETAIL_XML
        mock_get = Mock(return_value=mock_resp)

        with patch.object(client._client, "get", mock_get):
            client.get_decision_detail("99999")

        call_kwargs = mock_get.call_args
        params = call_kwargs[1]["params"] if call_kwargs[1] else call_kwargs[0][1]
        assert params["ID"] == "99999"
        assert params["target"] == "detc"

    def test_detail_not_found(self, client: KoreanLawClient) -> None:
        """HTTP 404 raises NotFoundError."""
        from httpx import HTTPStatusError

        mock_resp = Mock()
        mock_resp.status_code = 404
        err = HTTPStatusError("Not found", request=Mock(), response=mock_resp)

        with patch.object(client._client, "get", side_effect=err):
            with pytest.raises(NotFoundError):
                client.get_decision_detail("000000")

    def test_detail_api_error(self, client: KoreanLawClient) -> None:
        """HTTP 500 raises APIError."""
        from httpx import HTTPStatusError

        mock_resp = Mock()
        mock_resp.status_code = 500
        err = HTTPStatusError("Server error", request=Mock(), response=mock_resp)

        with patch.object(client._client, "get", side_effect=err):
            with pytest.raises(APIError):
                client.get_decision_detail("10001")

    def test_detail_empty_root_raises_not_found(self, client: KoreanLawClient) -> None:
        """A response with an unrecognised root element raises NotFoundError."""
        mock_resp = Mock()
        mock_resp.content = b"""<?xml version="1.0"?><UnknownRoot/>"""

        with patch.object(client._client, "get", return_value=mock_resp):
            with pytest.raises(NotFoundError):
                client.get_decision_detail("99999")

    def test_detail_invalid_xml_raises_parse_error(self, client: KoreanLawClient) -> None:
        """Malformed XML raises ParseError."""
        mock_resp = Mock()
        mock_resp.content = b"<broken xml <<<"

        with patch.object(client._client, "get", return_value=mock_resp):
            with pytest.raises(ParseError):
                client.get_decision_detail("10001")
