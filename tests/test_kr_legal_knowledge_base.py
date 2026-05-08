"""Tests for Korean legal knowledge-base client."""

from unittest.mock import Mock

from lawpy.kr import KoreanLawClient, KRClient, LegalKnowledgeBaseClient
from lawpy.kr.generated._models_generated import (
    AirltlsList,
    AisearchList,
    DlytrmList,
    DlytrmrltDetail,
    JorltlstrmDetail,
    LsrltList,
    LstrmaiList,
    LstrmrltDetail,
    LstrmrltjoDetail,
)


def _mock_response(payload: dict) -> Mock:
    response = Mock()
    response.json.return_value = payload
    return response


def test_legal_knowledge_base_client_is_on_kr_client() -> None:
    client = KRClient(api_key="test_key")

    assert isinstance(client, LegalKnowledgeBaseClient)
    assert isinstance(client, KoreanLawClient)


def test_search_legal_knowledge_terms_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"result": [{"target": "lstrmAI"}]}))

    result = client.search_legal_knowledge_terms("계약", homonym=True, page=2, per_page=5)

    assert isinstance(result[0], LstrmaiList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lstrmAI"
    assert params["query"] == "계약"
    assert params["homonymYn"] == "Y"
    assert params["page"] == 2
    assert params["display"] == 5


def test_search_daily_terms_maps_params() -> None:
    client = KRClient(api_key="test_key")
    client._make_request = Mock(return_value=_mock_response({"result": [{"target": "dlytrm"}]}))

    result = client.search_daily_terms("월세", page=3, per_page=7)

    assert isinstance(result[0], DlytrmList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "dlytrm"
    assert params["query"] == "월세"
    assert params["page"] == 3
    assert params["display"] == 7


def test_relation_methods_map_params() -> None:
    client = KRClient(api_key="test_key")

    client._make_request = Mock(return_value=_mock_response({"법령용어명": "계약"}))
    assert isinstance(
        client.get_legal_term_daily_term_relations("계약", term_id="10", relation_code=140305),
        LstrmrltDetail,
    )
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lstrmRlt"
    assert params["query"] == "계약"
    assert params["MST"] == "10"
    assert params["trmRltCd"] == 140305

    client._make_request = Mock(return_value=_mock_response({"일상용어명": "월세"}))
    assert isinstance(
        client.get_daily_term_legal_term_relations("월세", term_id="20", relation_code=140301),
        DlytrmrltDetail,
    )
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "dlytrmRlt"
    assert params["query"] == "월세"
    assert params["MST"] == "20"
    assert params["trmRltCd"] == 140301


def test_article_relation_methods_map_params() -> None:
    client = KRClient(api_key="test_key")

    client._make_request = Mock(return_value=_mock_response({"법령용어명": "계약"}))
    assert isinstance(client.get_legal_term_article_relations("계약"), LstrmrltjoDetail)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lstrmRltJo"
    assert params["query"] == "계약"

    client._make_request = Mock(return_value=_mock_response({"법령명": "민법"}))
    assert isinstance(
        client.get_article_legal_term_relations("민법", law_id=117202, article_number=563),
        JorltlstrmDetail,
    )
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "joRltLstrm"
    assert params["query"] == "민법"
    assert params["ID"] == 117202
    assert params["JO"] == 563


def test_law_search_methods_map_params() -> None:
    client = KRClient(api_key="test_key")

    client._make_request = Mock(return_value=_mock_response({"result": [{"target": "lsRlt"}]}))
    assert isinstance(client.search_related_laws("민법", law_id=117202, relation_code=1)[0], LsrltList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "lsRlt"
    assert params["query"] == "민법"
    assert params["ID"] == 117202
    assert params["rltClsCd"] == 1

    client._make_request = Mock(return_value=_mock_response({"result": [{"target": "aiSearch"}]}))
    assert isinstance(client.search_ai_laws("뺑소니", search_scope=0, page=2, per_page=6)[0], AisearchList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "aiSearch"
    assert params["search"] == 0
    assert params["query"] == "뺑소니"
    assert params["page"] == 2
    assert params["display"] == 6

    client._make_request = Mock(return_value=_mock_response({"result": [{"target": "aiRltLs"}]}))
    assert isinstance(client.search_ai_related_laws("뺑소니", search_scope=1)[0], AirltlsList)
    params = client._make_request.call_args.kwargs["params"]
    assert params["target"] == "aiRltLs"
    assert params["search"] == 1
    assert params["query"] == "뺑소니"
