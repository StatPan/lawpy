"""Tests for Korean law client."""

import pytest
from lawpy.kr import KoreanLawClient
from lawpy.exceptions import APIError, NotFoundError, ParseError
from lawpy.models import Law

from unittest.mock import Mock, patch


@pytest.fixture
def client():
    """Create a test client."""
    return KoreanLawClient(api_key="test_key")


class TestKoreanLawClient:
    """Tests for KoreanLawClient."""

    def test_init(self, client):
        """Test client initialization."""
        assert client.api_key == "test_key"
        assert client.base_url == KoreanLawClient.BASE_URL
        assert client.timeout == 30

    def test_search_laws_success(self, client):
        """Test successful law search."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<law>
    <list>
        <법령ID>000001</법령ID>
        <법령명한글>민법</법령명한글>
        <법령일련번호>000001</법령일련번호>
        <공포일자>20200101</공포일자>
        <시행일자>20200101</시행일자>
    </list>
</law>""".encode("utf-8")

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.search_laws("민법")

            assert len(laws) == 1
            assert laws[0].law_id == "000001"
            assert laws[0].law_name == "민법"

    def test_search_laws_empty_result(self, client):
        """Test search with no results."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<law/>""".encode("utf-8")

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.search_laws("없는법")

            assert len(laws) == 0

    def test_search_laws_api_error(self, client):
        """Test API error handling."""
        from httpx import HTTPStatusError

        mock_response = Mock()
        mock_response.status_code = 500
        error = HTTPStatusError("Server error", request=Mock(), response=mock_response)

        with patch.object(client._client, "get", side_effect=error):
            with pytest.raises(APIError) as exc_info:
                client.search_laws("민법")

            assert "HTTP error: 500" in str(exc_info.value)

    def test_get_law_text_success(self, client):
        """Test successful law text retrieval."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<law>
    <법령명한글>민법</법령명한글>
</law>""".encode("utf-8")

        with patch.object(client._client, "get", return_value=mock_response):
            law_text = client.get_law_text("000001")

            assert law_text.law_id == "000001"
            assert law_text.law_name == "민법"

    def test_get_law_text_not_found(self, client):
        """Test law not found error."""
        from httpx import HTTPStatusError

        mock_response = Mock()
        mock_response.status_code = 404
        error = HTTPStatusError("Not found", request=Mock(), response=mock_response)

        with patch.object(client._client, "get", side_effect=error):
            with pytest.raises(NotFoundError) as exc_info:
                client.get_law_text("999999")

            assert "Law not found: 999999" in str(exc_info.value)
