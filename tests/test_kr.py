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

            assert "LAWPY_KR_API_KEY" in str(exc_info.value)

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

            assert "Resource not found" in str(exc_info.value)

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

    def test_get_law_history_success(self, client):
        """Test successful law history retrieval."""
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
            laws = client.get_law_history(per_page=5)

            assert len(laws) == 1
            assert laws[0].law_id == "001706"
            assert laws[0].law_name == "민법"

    def test_get_law_history_with_query(self, client):
        """Test law history retrieval with query."""
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
            laws = client.get_law_history(query="민법", per_page=5)

            assert len(laws) == 1
            assert laws[0].law_name == "민법"

    def test_get_law_history_with_law_id(self, client):
        """Test law history retrieval with law ID."""
        mock_response = Mock()
        mock_response.content = """<?xml version="1.0" encoding="UTF-8"?>
<LawSearch>
    <law id="1">
        <법령명한글><![CDATA[민법]]></법령명한글>
        <법령ID>009682</법령ID>
        <공포일자>19600101</공포일자>
        <시행일자>19600101</시행일자>
    </law>
</LawSearch>""".encode()

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.get_law_history(law_id="009682", per_page=5)

            assert len(laws) == 1
            assert laws[0].law_id == "009682"

    def test_get_law_history_empty(self, client):
        """Test law history with no results."""
        mock_response = Mock()
        mock_response.content = b"""<?xml version="1.0" encoding="UTF-8"?>
<LawSearch/>"""

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.get_law_history(per_page=5)

            assert len(laws) == 0

    def test_get_law_history_with_sort(self, client):
        """Test law history retrieval with sort."""
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
            laws = client.get_law_history(sort="lasc", per_page=5)

            assert len(laws) == 1
            assert laws[0].enforcement_date == "20200101"

    def test_get_law_history_api_error(self, client):
        """Test law history API error handling."""
        from httpx import HTTPStatusError

        mock_response = Mock()
        mock_response.status_code = 500
        error = HTTPStatusError("Server error", request=Mock(), response=mock_response)

        with patch.object(client._client, "get", side_effect=error):
            with pytest.raises(APIError) as exc_info:
                client.get_law_history()

            assert "HTTP error: 500" in str(exc_info.value)

    def test_get_law_history_detail_by_mst(self, client):
        """Test successful law history detail retrieval by MST."""
        mock_response = Mock()
        mock_response.text = """
<html>
<head><title>법령 연혁</title></head>
<body>
<div class="history">
    <h1>민법 개정 연혁</h1>
</div>
</body>
</html>
        """.strip()

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_history_detail(mst=9094)

            assert "<html>" in result
            assert "민법 개정 연혁" in result

    def test_get_law_history_detail_by_law_id(self, client):
        """Test successful law history detail retrieval by law ID."""
        mock_response = Mock()
        mock_response.text = """
<html>
<head><title>법령 연혁</title></head>
<body>
<div class="history">
    <h1>법률 연혁</h1>
</div>
</body>
</html>
        """.strip()

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_history_detail(law_id="009682")

            assert "<html>" in result
            assert "법률 연혁" in result

    def test_get_law_history_detail_with_params(self, client):
        """Test law history detail with additional parameters."""
        mock_response = Mock()
        mock_response.text = """
<html>
<body>
<div class="history">
    <h1>특정 공포일자 연혁</h1>
</div>
</body>
</html>
        """.strip()

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_history_detail(
                mst=166500,
                promulgation_date="20240101",
                promulgation_number=12345,
            )

            assert "<html>" in result
            assert "특정 공포일자 연혁" in result

    def test_get_law_history_detail_no_id_or_mst(self, client):
        """Test error when neither law_id nor mst is provided."""
        with pytest.raises(ValueError) as exc_info:
            client.get_law_history_detail()

        assert "Either law_id or mst must be provided" in str(exc_info.value)

    def test_get_law_history_detail_api_error(self, client):
        """Test law history detail API error handling."""
        from httpx import HTTPStatusError

        mock_response = Mock()
        mock_response.status_code = 404
        error = HTTPStatusError("Not found", request=Mock(), response=mock_response)

        with patch.object(client._client, "get", side_effect=error):
            with pytest.raises(APIError) as exc_info:
                client.get_law_history_detail(mst=999999)

            assert "HTTP error: 404" in str(exc_info.value)

    def test_get_law_old_new_success(self, client):
        """Test old/new comparison list retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "OldAndNewLawSearch": {
                "oldAndNew": [{"법령ID": "009682", "법령명한글": "민법"}],
            }
        }

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_old_new(query="민법", per_page=5)

            assert len(result) == 1
            assert result[0]["법령ID"] == "009682"

    def test_get_law_old_new_detail_success(self, client):
        """Test old/new comparison detail retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "OldAndNewLawSearch": {"법령ID": "009682", "신구법비교": "..."}
        }

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_old_new_detail(law_id="009682")

            assert result["법령ID"] == "009682"

    def test_get_law_old_new_detail_requires_id_or_mst(self, client):
        """Test error when neither law_id nor mst is provided for old/new detail."""
        with pytest.raises(ValueError) as exc_info:
            client.get_law_old_new_detail()

        assert "Either law_id or mst must be provided" in str(exc_info.value)

    def test_get_law_abbreviations_success(self, client):
        """Test law abbreviation retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": {"law": [{"법령명한글": "근로기준법", "약칭명": "근기법"}]}
        }

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_abbreviations(start_date=20240101, end_date=20240131)

            assert len(result) == 1
            assert result[0]["약칭명"] == "근기법"

    def test_get_law_change_history_success(self, client):
        """Test law change history retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": {"법령ID": "009682", "법령명한글": "민법"}
        }

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_change_history(registered_date=20240101)

            assert len(result) == 1
            assert result[0]["법령ID"] == "009682"

    def test_get_law_article_change_history_success(self, client):
        """Test article-level change history retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": {"법령ID": "009682", "조문번호": "000200"}
        }

        with patch.object(client._client, "get", return_value=mock_response):
            result = client.get_law_article_change_history(law_id="009682", article_code=200)

            assert len(result) == 1
            assert result[0]["법령ID"] == "009682"

    def test_search_english_laws_success(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": {
                "law": [
                    {
                        "법령ID": "009682",
                        "법령명영문": "Civil Act",
                        "공포번호": "4172",
                        "공포일자": "19600101",
                        "시행일자": "19600101",
                    }
                ]
            }
        }

        with patch.object(client._client, "get", return_value=mock_response):
            laws = client.search_english_laws("civil")

            assert len(laws) == 1
            assert laws[0].law_id == "009682"
            assert laws[0].law_name == "Civil Act"

    def test_get_english_law_detail_success(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": {
                "법령ID": "009682",
                "법령명영문": "Civil Act",
                "공포번호": "4172",
                "공포일자": "19600101",
                "시행일자": "19600101",
            }
        }

        with patch.object(client._client, "get", return_value=mock_response):
            detail = client.get_english_law_detail(law_id="009682")

            assert detail.law_id == "009682"
            assert detail.language == "EN"

    def test_search_law_old_and_new_success(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "OldAndNewLawSearch": {
                "oldAndNew": [{"법령ID": "009682", "법령명한글": "민법", "공포번호": "4172"}]
            }
        }

        with patch.object(client._client, "get", return_value=mock_response):
            rows = client.search_law_old_and_new(query="민법")

            assert len(rows) == 1
            assert rows[0].law_id == "009682"

    def test_get_law_old_and_new_detail_success(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "OldAndNewLawSearch": {"법령ID": "009682", "신구법비교": "변경내용"}
        }

        with patch.object(client._client, "get", return_value=mock_response):
            row = client.get_law_old_and_new_detail(law_id="009682")

            assert row.law_id == "009682"
            assert row.comparison_text == "변경내용"

    def test_search_law_abbreviations_success(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": {"law": [{"법령ID": "007777", "법령명한글": "근로기준법", "약칭명": "근기법"}]}
        }

        with patch.object(client._client, "get", return_value=mock_response):
            rows = client.search_law_abbreviations()

            assert len(rows) == 1
            assert rows[0].abbreviation == "근기법"

    def test_search_law_change_history_success(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": [{"법령ID": "009682", "법령명한글": "민법", "변경일자": "20240101"}]
        }

        with patch.object(client._client, "get", return_value=mock_response):
            rows = client.search_law_change_history(registered_date=20240101)

            assert len(rows) == 1
            assert rows[0].law_id == "009682"

    def test_search_law_article_change_history_jo_mapping(self, client):
        mock_response = Mock()
        mock_response.json.return_value = {
            "LawSearch": [{"법령ID": "009682", "조문번호": "001000"}]
        }

        with patch.object(client._client, "get", return_value=mock_response) as mock_get:
            rows = client.search_law_article_change_history(law_id="009682", article_number=10)

            assert len(rows) == 1
            assert rows[0].article_code == "001000"
            assert mock_get.call_args.kwargs["params"]["JO"] == 1000

    def test_search_law_article_change_history_requires_law_id(self, client):
        with pytest.raises(ValueError):
            client.search_law_article_change_history(law_id="", article_number=10)
