"""Tests for Korean precedent (판례) client."""

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

PREC_LIST_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PrecSearch>
    <prec id="1">
        <판례일련번호>12345</판례일련번호>
        <사건명><![CDATA[손해배상(기)]]></사건명>
        <사건번호>2020다12345</사건번호>
        <선고일자>20201201</선고일자>
        <법원명>대법원</법원명>
        <사건분류명>민사</사건분류명>
        <판결유형>판결</판결유형>
        <판례상세링크>https://www.law.go.kr/LSW/precInfoP.do?precSeq=12345</판례상세링크>
    </prec>
    <prec id="2">
        <판례일련번호>67890</판례일련번호>
        <사건명><![CDATA[임금]]></사건명>
        <사건번호>2019나67890</사건번호>
        <선고일자>20190815</선고일자>
        <법원명>서울고등법원</법원명>
        <사건분류명>민사</사건분류명>
        <판결유형>판결</판결유형>
        <판례상세링크>https://www.law.go.kr/LSW/precInfoP.do?precSeq=67890</판례상세링크>
    </prec>
</PrecSearch>""".encode()

PREC_LIST_EMPTY_XML = b"""<?xml version="1.0" encoding="UTF-8"?><PrecSearch/>"""

PREC_DETAIL_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PrecService>
    <판례일련번호>12345</판례일련번호>
    <사건명><![CDATA[손해배상(기)]]></사건명>
    <사건번호>2020다12345</사건번호>
    <선고일자>20201201</선고일자>
    <법원명>대법원</법원명>
    <사건분류명>민사</사건분류명>
    <판결유형>판결</판결유형>
    <선고>선고</선고>
    <참조조문>민법 제750조</참조조문>
    <참조판례>대법원 2019. 3. 14. 선고 2018다12345 판결</참조판례>
    <판시사항>불법행위로 인한 손해배상 책임의 성립 여부</판시사항>
    <판결요지>가해자가 고의 또는 과실로 타인에게 손해를 가한 경우 손해를 배상할 책임이 있다.</판결요지>
    <판례내용>【주문】 상고를 기각한다. 【이유】 상고이유를 판단한다.</판례내용>
</PrecService>""".encode()

PREC_SINGLE_LIST_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PrecSearch>
    <prec id="1">
        <판례일련번호>12345</판례일련번호>
        <사건명><![CDATA[손해배상(기)]]></사건명>
        <사건번호>2020다12345</사건번호>
    </prec>
</PrecSearch>""".encode()


# ---------------------------------------------------------------------------
# Test: search_precedents
# ---------------------------------------------------------------------------


class TestSearchPrecedents:
    """Tests for PrecedentClient.search_precedents."""

    def test_search_returns_list(self, client: KoreanLawClient) -> None:
        """Parsing a two-item list returns two Precedent objects."""
        mock_resp = Mock()
        mock_resp.content = PREC_LIST_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_precedents(query="손해배상")

        assert len(results) == 2

    def test_search_fields_mapped_correctly(self, client: KoreanLawClient) -> None:
        """All list fields are mapped onto the Precedent model."""
        mock_resp = Mock()
        mock_resp.content = PREC_LIST_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_precedents()

        first = results[0]
        assert first.prec_id == "12345"
        assert first.case_name == "손해배상(기)"
        assert first.case_number == "2020다12345"
        assert first.decision_date == "20201201"
        assert first.court_name == "대법원"
        assert first.case_type == "민사"
        assert first.judgment_type == "판결"
        assert first.detail_link is not None and "12345" in first.detail_link

    def test_search_empty_result(self, client: KoreanLawClient) -> None:
        """Empty PrecSearch element returns an empty list."""
        mock_resp = Mock()
        mock_resp.content = PREC_LIST_EMPTY_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_precedents(query="없는판례")

        assert results == []

    def test_search_single_item_not_wrapped_in_list(self, client: KoreanLawClient) -> None:
        """xmltodict returns a dict (not list) for single items – still works."""
        mock_resp = Mock()
        mock_resp.content = PREC_SINGLE_LIST_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            results = client.search_precedents()

        assert len(results) == 1
        assert results[0].prec_id == "12345"

    def test_search_with_optional_params_sent(self, client: KoreanLawClient) -> None:
        """Optional filtering params are forwarded to the HTTP call."""
        mock_resp = Mock()
        mock_resp.content = PREC_LIST_EMPTY_XML
        mock_get = Mock(return_value=mock_resp)

        with patch.object(client._client, "get", mock_get):
            client.search_precedents(
                query="계약",
                court_type="400201",
                court_name="대법원",
                ref_statute="민법",
                case_gana="ga",
                sort="dasc",
                page=2,
                per_page=50,
            )

        call_kwargs = mock_get.call_args
        params = call_kwargs[1]["params"] if call_kwargs[1] else call_kwargs[0][1]
        assert params["query"] == "계약"
        assert params["org"] == "400201"
        assert params["curt"] == "대법원"
        assert params["JO"] == "민법"
        assert params["gana"] == "ga"
        assert params["sort"] == "dasc"
        assert params["page"] == 2
        assert params["display"] == 50
        assert params["target"] == "prec"

    def test_search_api_error(self, client: KoreanLawClient) -> None:
        """HTTP 500 is wrapped in APIError."""
        from httpx import HTTPStatusError

        mock_resp = Mock()
        mock_resp.status_code = 500
        err = HTTPStatusError("Server error", request=Mock(), response=mock_resp)

        with patch.object(client._client, "get", side_effect=err):
            with pytest.raises(APIError) as exc_info:
                client.search_precedents(query="민법")

        assert "HTTP error: 500" in str(exc_info.value)

    def test_search_invalid_xml_raises_parse_error(self, client: KoreanLawClient) -> None:
        """Malformed XML raises ParseError."""
        mock_resp = Mock()
        mock_resp.content = b"this is not xml at all <<<>>>"

        with patch.object(client._client, "get", return_value=mock_resp):
            with pytest.raises(ParseError):
                client.search_precedents()


# ---------------------------------------------------------------------------
# Test: get_precedent_detail
# ---------------------------------------------------------------------------


class TestGetPrecedentDetail:
    """Tests for PrecedentClient.get_precedent_detail."""

    def test_detail_fields_mapped_correctly(self, client: KoreanLawClient) -> None:
        """All detail fields are mapped onto PrecedentDetail."""
        mock_resp = Mock()
        mock_resp.content = PREC_DETAIL_XML

        with patch.object(client._client, "get", return_value=mock_resp):
            detail = client.get_precedent_detail("12345")

        assert detail.prec_id == "12345"
        assert detail.case_name == "손해배상(기)"
        assert detail.case_number == "2020다12345"
        assert detail.decision_date == "20201201"
        assert detail.court_name == "대법원"
        assert detail.case_type == "민사"
        assert detail.judgment_type == "판결"
        assert detail.decision_type == "선고"
        assert detail.ref_statutes == "민법 제750조"
        assert detail.ref_precedents is not None
        assert detail.ruling_summary == "불법행위로 인한 손해배상 책임의 성립 여부"
        assert detail.ruling_gist is not None and "손해를 배상" in detail.ruling_gist
        assert detail.full_text is not None and "상고를 기각" in detail.full_text

    def test_detail_id_param_sent(self, client: KoreanLawClient) -> None:
        """The ID parameter is forwarded correctly."""
        mock_resp = Mock()
        mock_resp.content = PREC_DETAIL_XML
        mock_get = Mock(return_value=mock_resp)

        with patch.object(client._client, "get", mock_get):
            client.get_precedent_detail("99999")

        call_kwargs = mock_get.call_args
        params = call_kwargs[1]["params"] if call_kwargs[1] else call_kwargs[0][1]
        assert params["ID"] == "99999"
        assert params["target"] == "prec"

    def test_detail_not_found(self, client: KoreanLawClient) -> None:
        """HTTP 404 raises NotFoundError."""
        from httpx import HTTPStatusError

        mock_resp = Mock()
        mock_resp.status_code = 404
        err = HTTPStatusError("Not found", request=Mock(), response=mock_resp)

        with patch.object(client._client, "get", side_effect=err):
            with pytest.raises(NotFoundError):
                client.get_precedent_detail("000000")

    def test_detail_api_error(self, client: KoreanLawClient) -> None:
        """HTTP 500 raises APIError."""
        from httpx import HTTPStatusError

        mock_resp = Mock()
        mock_resp.status_code = 500
        err = HTTPStatusError("Server error", request=Mock(), response=mock_resp)

        with patch.object(client._client, "get", side_effect=err):
            with pytest.raises(APIError):
                client.get_precedent_detail("12345")

    def test_detail_empty_root_raises_not_found(self, client: KoreanLawClient) -> None:
        """A response with an unrecognised root element raises NotFoundError."""
        mock_resp = Mock()
        mock_resp.content = b"""<?xml version="1.0"?><UnknownRoot/>"""

        with patch.object(client._client, "get", return_value=mock_resp):
            with pytest.raises(NotFoundError):
                client.get_precedent_detail("99999")

    def test_detail_invalid_xml_raises_parse_error(self, client: KoreanLawClient) -> None:
        """Malformed XML raises ParseError."""
        mock_resp = Mock()
        mock_resp.content = b"<broken xml <<<"

        with patch.object(client._client, "get", return_value=mock_resp):
            with pytest.raises(ParseError):
                client.get_precedent_detail("12345")
