"""Tests for Korean law client."""

import os
from unittest.mock import Mock, patch

import pytest

from lawpy.exceptions import APIError, NotFoundError
from lawpy.kr import KoreanLawClient


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

    def test_init_from_env(self):
        """Test client initialization from environment variable."""
        with patch.dict(os.environ, {"LAWPY_API_KEY": "env_key"}):
            client = KoreanLawClient()
            assert client.api_key == "env_key"

    def test_init_env_override(self):
        """Test that explicit api_key overrides environment variable."""
        with patch.dict(os.environ, {"LAWPY_API_KEY": "env_key"}):
            client = KoreanLawClient(api_key="explicit_key")
            assert client.api_key == "explicit_key"

    def test_init_no_api_key(self):
        """Test error when no api_key is provided."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError) as exc_info:
                KoreanLawClient()

            assert "api_key must be provided or set LAWPY_API_KEY environment variable" in str(
                exc_info.value
            )

    def test_search_laws_success(self, client):
        """Test successful law search."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<LawSearch>
    <law id="1">
        <법령일련번호>188376</법령일련번호>
        <법령명한글><![CDATA[민법]]></법령명한글>
        <법령ID>001706</법령ID>
        <공포일자>20200101</공포일자>
        <공포번호>10000</공포번호>
        <시행일자>20200101</시행일자>
    </law>
</LawSearch>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.search_laws("민법")

            assert len(laws) == 1
            assert laws[0].law_id == "001706"
            assert laws[0].law_name == "민법"

    def test_search_laws_empty_result(self, client):
        """Test search with no results."""
        mock_response = Mock()
        mock_response.content = b"""<?xml version="1.0" encoding="UTF-8"?>
<LawSearch/>"""

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

    def test_get_law_detail_success(self, client):
        """Test successful law detail retrieval."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<법령>
    <기본정보>
        <법령ID>009682</법령ID>
        <법령명_한글>민법</법령명_한글>
        <법령명_한자>民法</법령명_한자>
        <공포일자>19600101</공포일자>
        <공포번호>4172</공포번호>
        <시행일자>19600101</시행일자>
        <법종구분 법종구분코드="A0002">법률</법종구분>
        <소관부처>법무부</소관부처>
    </기본정보>
    <조문>
        <조문단위>
            <조문번호>1</조문번호>
            <조문제목>(통칙)</조문제목>
            <조문내용>민사에 관하여 법률에 특별한 규정이 없으면 이 법에 의한다.</조문내용>
            <항>
                <항번호>1</항번호>
                <항내용>제1항의 내용</항내용>
                <호>
                    <호번호>1</호번호>
                    <호내용>호 내용</호내용>
                    <목>
                        <목번호>1</목번호>
                        <목내용>목 내용</목내용>
                    </목>
                </호>
            </항>
        </조문단위>
    </조문>
</법령>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            law_detail = client.get_law_detail(law_id="009682")

            assert law_detail.law_id == "009682"
            assert law_detail.law_name_korean == "민법"
            assert law_detail.law_name_chinese == "民法"
            assert law_detail.promulgation_date == "19600101"
            assert law_detail.promulgation_number == 4172
            assert law_detail.enforcement_date == "19600101"
            assert law_detail.law_type == "법률"
            assert law_detail.ministry == "법무부"
            assert len(law_detail.articles) == 1
            assert law_detail.articles[0].number == 1
            assert law_detail.articles[0].title == "(통칙)"
            assert (
                law_detail.articles[0].content
                == "민사에 관하여 법률에 특별한 규정이 없으면 이 법에 의한다."
            )

    def test_get_law_detail_by_mst(self, client):
        """Test law detail retrieval by MST."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<법령>
    <기본정보>
        <법령명_한글>민법</법령명_한글>
    </기본정보>
    <조문>
        <조문단위>
            <조문번호>1</조문번호>
            <조문제목>제1조</조문제목>
            <조문내용>내용</조문내용>
        </조문단위>
    </조문>
</법령>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            law_detail = client.get_law_detail(mst=123456)

            assert law_detail.law_id == "123456"
            assert law_detail.law_name_korean == "민법"

    def test_get_law_detail_with_article_number(self, client):
        """Test law detail retrieval with specific article number."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<법령>
    <기본정보>
        <법령명_한글>민법</법령명_한글>
    </기본정보>
    <조문>
        <조문단위>
            <조문번호>10</조문번호>
            <조문제목>제10조</조문제목>
            <조문내용>내용</조문내용>
        </조문단위>
    </조문>
</법령>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            law_detail = client.get_law_detail(law_id="009682", article_number=10)

            assert len(law_detail.articles) == 1
            assert law_detail.articles[0].number == 10

    def test_get_law_detail_no_id_or_mst(self, client):
        """Test error when neither law_id nor mst is provided."""
        with pytest.raises(ValueError) as exc_info:
            client.get_law_detail()

        assert "Either law_id or mst must be provided" in str(exc_info.value)

    def test_get_law_detail_not_found(self, client):
        """Test law detail not found error."""
        from httpx import HTTPStatusError

        mock_response = Mock()
        mock_response.status_code = 404
        error = HTTPStatusError("Not found", request=Mock(), response=mock_response)

        with patch.object(client._client, "get", side_effect=error):
            with pytest.raises(NotFoundError) as exc_info:
                client.get_law_detail(law_id="999999")

            assert "Law not found" in str(exc_info.value)

    def test_get_law_list_success(self, client):
        """Test successful law list retrieval."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<LawSearch>
    <law id="1">
        <법령일련번호>188376</법령일련번호>
        <법령명한글><![CDATA[민법]]></법령명한글>
        <법령ID>001706</법령ID>
        <공포일자>20200101</공포일자>
        <공포번호>10000</공포번호>
        <시행일자>20200101</시행일자>
    </law>
</LawSearch>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.get_law_list(per_page=5)

            assert len(laws) == 1
            assert laws[0].law_id == "001706"
            assert laws[0].law_name == "민법"
            assert laws[0].promulgation_date == "20200101"
            assert laws[0].enforcement_date == "20200101"

    def test_get_law_list_with_query(self, client):
        """Test law list retrieval with query."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<LawSearch>
    <law id="1">
        <법령명한글><![CDATA[민법]]></법령명한글>
        <법령ID>001706</법령ID>
        <공포일자>20200101</공포일자>
        <시행일자>20200101</시행일자>
    </law>
</LawSearch>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.get_law_list(query="민법", per_page=5)

            assert len(laws) == 1
            assert laws[0].law_name == "민법"

    def test_get_law_list_empty(self, client):
        """Test law list with no results."""
        mock_response = Mock()
        mock_response.content = b"""<?xml version="1.0" encoding="UTF-8"?>
<LawSearch/>"""

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.get_law_list(per_page=5)

            assert len(laws) == 0

    def test_get_law_list_with_sort(self, client):
        """Test law list retrieval with sort."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<LawSearch>
    <law id="1">
        <법령명한글><![CDATA[민법]]></법령명한글>
        <법령ID>001706</법령ID>
        <시행일자>20200101</시행일자>
    </law>
</LawSearch>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.get_law_list(sort="ldes", per_page=5)

            assert len(laws) == 1
            assert laws[0].enforcement_date == "20200101"

    def test_get_law_list_api_error(self, client):
        """Test law list API error handling."""
        from httpx import HTTPStatusError

        mock_response = Mock()
        mock_response.status_code = 500
        error = HTTPStatusError("Server error", request=Mock(), response=mock_response)

        with patch.object(client._client, "get", side_effect=error):
            with pytest.raises(APIError) as exc_info:
                client.get_law_list()

            assert "HTTP error: 500" in str(exc_info.value)
