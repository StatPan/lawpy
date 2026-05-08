"""Tests for malformed KR API response diagnostics."""

from unittest.mock import Mock

import pytest

from lawpy.exceptions import ApiResponseTypeError, ParseError
from lawpy.kr import KRClient


def _bad_json_response(body: str, content_type: str = "text/html") -> Mock:
    response = Mock()
    response.json.side_effect = ValueError("Expecting value: line 1 column 1 (char 0)")
    response.text = body
    response.content = body.encode()
    response.headers = {"content-type": content_type}
    response.request = Mock(url="https://www.law.go.kr/DRF/lawService.do?target=test")
    return response


def _xml_response(body: str) -> Mock:
    response = Mock()
    response.content = body.encode()
    response.text = body
    response.headers = {"content-type": "application/xml"}
    response.status_code = 200
    response.request = Mock(url="https://www.law.go.kr/DRF/lawSearch.do?target=lsHistory")
    return response


def test_generated_detail_wraps_malformed_json_with_context() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(
        return_value=_bad_json_response("<html>server error for OC=secret-user&target=lsDelegated</html>")
    )

    with pytest.raises(ParseError) as exc_info:
        client.get_delegated_law_detail(law_id="009682")

    message = str(exc_info.value)
    assert "target 'lsDelegated'" in message
    assert "content-type: text/html" in message
    assert "secret-user" not in message
    assert "response preview: <html>server error for OC=***&target=lsDelegated</html>" in message


def test_generated_search_wraps_malformed_json_with_context() -> None:
    client = KRClient(api_key="test_key")
    response = _bad_json_response("")
    response.request = Mock(
        url="https://www.law.go.kr/DRF/lawSearch.do?OC=secret-user&target=couseLs&type=JSON"
    )
    client._make_request = Mock(return_value=response)

    with pytest.raises(ParseError) as exc_info:
        client.search_couseLss(vcode="L0000000000001", lj_jo="Y")

    message = str(exc_info.value)
    assert "target 'couseLs'" in message
    assert "OC=%2A%2A%2A" in message
    assert "secret-user" not in message
    assert "response preview: <empty>" in message


def test_law_history_wraps_malformed_xml_with_preview() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_xml_response("<LawSearch><law></LawSearch>"))

    with pytest.raises(ParseError) as exc_info:
        client.get_law_history(query="임대사업자")

    message = str(exc_info.value)
    assert "Failed to parse XML law list response" in message
    assert "mismatched tag" in message
    assert "response preview: <LawSearch><law></LawSearch>" in message


def test_law_history_rejects_html_response_before_xml_parse() -> None:
    client = KRClient(api_key="test_key")
    html = '<?xml version="1.0"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"><html></html>'
    client._make_request = Mock(return_value=_xml_response(html))

    with pytest.raises(ApiResponseTypeError) as exc_info:
        client.get_law_history(query="임대사업자")

    message = str(exc_info.value)
    assert "Expected XML law list response but received HTML" in message
    assert "response preview: <?xml version=\"1.0\"?><!DOCTYPE html PUBLIC" in message


def test_xml_request_rejects_html_response_from_url_type_before_parse() -> None:
    client = KRClient(api_key="test_key")
    html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"><html></html>'
    response = _xml_response(html)
    response.headers = {"content-type": "text/html;charset=UTF-8"}
    response.request = Mock(
        url="https://www.law.go.kr/DRF/lawSearch.do?OC=secret-user&target=lsHistory&type=XML"
    )

    with pytest.raises(ApiResponseTypeError) as exc_info:
        client._check_response(response, "lsHistory")

    message = str(exc_info.value)
    assert "Target 'lsHistory' returned HTML instead of XML" in message
    assert "content-type: text/html;charset=UTF-8" in message
    assert "OC=%2A%2A%2A" in message
    assert "secret-user" not in message
    assert "response preview: <!DOCTYPE html PUBLIC" in message
