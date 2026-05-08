#!/usr/bin/env python3
"""
Generate fully working Python client code from scraped API specs + discovered root keys.

Sources:
  - specs/kr/*.json      : parameter + response field specs (scraped from docs)
  - specs/kr/_root_keys.json : actual JSON root/item keys (discovered by probe_root_keys.py)

Output:
  - src/lawpy/kr/generated/{target}.py : working client class per target
  - src/lawpy/kr/generated/_models_generated.py : Pydantic models

Usage:
    uv run python scripts/codegen.py
    uv run python scripts/codegen.py --specs specs/kr/ --out src/lawpy/kr/generated/
    uv run python scripts/codegen.py --dry-run --target prec
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from textwrap import dedent

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PARAM_KEY = "요청변수"
RESP_KEY_CANDIDATES = ["출력변수", "출력결과", "필드", "요청변수", "col0"]
DESC_KEY = "설명"
VAL_KEY = "값"
DETAIL_COMPAT_FIELDS: dict[str, list[tuple[str, str]]] = {
    "decc": [
        ("행정심판례일련번호", "행정심판례일련번호"),
        ("사건명", "사건명"),
        ("사건번호", "사건번호"),
        ("주문", "주문"),
    ],
    "detc": [("id", "ID"), ("lm", "LM")],
    "expc": [("id", "ID"), ("lm", "LM")],
    "prec": [
        ("판례정보일련번호", "판례정보일련번호"),
        ("사건명", "사건명"),
        ("사건번호", "사건번호"),
        ("선고일자", "선고일자"),
        ("선고", "선고"),
        ("법원명", "법원명"),
        ("법원종류코드", "법원종류코드"),
        ("사건종류명", "사건종류명"),
        ("사건종류코드", "사건종류코드"),
        ("판결유형", "판결유형"),
        ("판시사항", "판시사항"),
        ("판결요지", "판결요지"),
        ("참조조문", "참조조문"),
        ("참조판례", "참조판례"),
        ("판례내용", "판례내용"),
    ],
    "trty": [("id", "ID")],
}
MODEL_COMPAT_FIELDS: dict[tuple[str, str], list[tuple[str, str]]] = {
    ("decc", "List"): [
        ("행정심판재결례일련번호", "행정심판재결례일련번호"),
        ("사건명", "사건명"),
        ("사건번호", "사건번호"),
        ("의결일자", "의결일자"),
    ],
    ("ordin", "List"): [
        ("자치법규명", "자치법규명"),
        ("자치법규일련번호", "자치법규일련번호"),
        ("자치법규종류", "자치법규종류"),
    ],
}
MOBILE_COMPAT_PARAMS: dict[str, list[dict[str, object]]] = {
    target: [
        {
            "key": "mobileYn",
            "pyname": "mobileyn",
            "pytype": "str | None",
            "required": False,
            "description": "모바일여부",
        }
    ]
    for target in (
        "admbyl",
        "admrul",
        "detc",
        "expc",
        "law",
        "licbyl",
        "lstrm",
        "ordin",
        "ordinbyl",
        "prec",
        "trty",
    )
}

SPECIAL_MODELS = dedent('''


def _normalize_to_list(v: Any) -> list[Any]:
    if v is None:
        return []
    if isinstance(v, dict):
        return [v]
    return v


class LsdelegatedDepartmentInfo(BaseModel):
    content: str | None = None
    소관부처코드: str | None = None


class LsdelegatedLawInfo(BaseModel):
    법령ID: str | None = None
    법령일련번호: str | None = None
    소관부처: LsdelegatedDepartmentInfo | None = None
    법령명: str | None = None
    시행일자: str | None = None
    공포번호: str | None = None
    전화번호: str | None = None
    공포일자: str | None = None


class LsdelegatedArticleInfo(BaseModel):
    조문번호: str | None = None
    조문제목: str | None = None
    조문가지번호: str | None = None


class LsdelegatedAdminRuleArticle(BaseModel):
    위임행정규칙제목: str | None = None
    라인텍스트: str | None = None
    위임행정규칙일련번호: str | None = None
    조항호목: str | None = None
    링크텍스트: str | None = None


class LsdelegatedLawRuleArticle(BaseModel):
    라인텍스트: str | None = None
    위임법령조문번호: str | None = None
    조항호목: str | None = None
    링크텍스트: str | None = None
    위임법령조문제목: str | None = None


class LsdelegatedDelegateInfo(BaseModel):
    위임구분: str | None = None
    위임법령제목: str | None = None
    위임법령일련번호: str | None = None
    위임행정규칙조문정보: list[LsdelegatedAdminRuleArticle] = []
    위임법령조문정보: list[LsdelegatedLawRuleArticle] = []

    _normalize_admin = field_validator("위임행정규칙조문정보", mode="before")(_normalize_to_list)
    _normalize_law = field_validator("위임법령조문정보", mode="before")(_normalize_to_list)


class LsdelegatedDelegateArticle(BaseModel):
    위임정보: list[LsdelegatedDelegateInfo] = []
    조정보: LsdelegatedArticleInfo | None = None

    _normalize_delegate = field_validator("위임정보", mode="before")(_normalize_to_list)


class LsdelegatedDetail(BaseModel):
    법령정보: LsdelegatedLawInfo | None = None
    위임조문정보: list[LsdelegatedDelegateArticle] = []


class DrlawList(BaseModel):
    """Response model for 법령-자치법규 연계현황 조회 (drlaw, XML-only).

    Source: specs/kr/lsOrdinConGuide.json + live API response analysis
    """
    model_config = {"populate_by_name": True}

    법령일련번호: str | None = None
    법령ID: str | None = None
    법령공포일자: str | None = None
    법령공포번호: str | None = None
    법령명한글: str | None = None
    조문일련번호: str | None = None
    조문번호: str | None = None
    조문가지번호: str | None = None
    조문제목: str | None = None
    조문개정표시포함여부: str | None = None
    조문공포일자: str | None = None
    조문시행일자: str | None = None
    조문변경여부: str | None = None
    전체건수: str | None = None
    서울특별시: str | None = None
    부산광역시: str | None = None
    대구광역시: str | None = None
    인천광역시: str | None = None
    광주광역시: str | None = None
    대전광역시: str | None = None
    세종특별자치시: str | None = None
    울산광역시: str | None = None
    경기도: str | None = None
    강원도: str | None = None
    충청북도: str | None = None
    충청남도: str | None = None
    전라북도: str | None = None
    전라남도: str | None = None
    경상북도: str | None = None
    경상남도: str | None = None
    제주특별자치도: str | None = None
    교육청: str | None = None
    위임규제여부: str | None = None
    소관부처명: str | None = None
    소관부처코드: str | None = None
    법령시행일자: str | None = None
''')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_list_guide(html_name: str) -> bool:
    return html_name.endswith("ListGuide")


def is_info_guide(html_name: str) -> bool:
    return html_name.endswith("InfoGuide")


def is_knowledge_base_guide(spec: dict) -> bool:
    return "법령정보지식베이스" in spec.get("request_url", "")


def is_mobile_guide(spec: dict) -> bool:
    html_name = spec.get("html_name", "")
    request_url = spec.get("request_url", "") + spec.get("raw_url", "")
    return html_name.startswith("mob") or "mobileYn=Y" in request_url


def guide_family(html_name: str) -> str:
    if not html_name.startswith("mob") or len(html_name) <= 3:
        return html_name
    return html_name[3].lower() + html_name[4:]


def is_same_mobile_family(current: dict, candidate: dict) -> bool:
    return guide_family(current.get("html_name", "")) == guide_family(candidate.get("html_name", ""))


def should_replace_spec(target: str, current: dict | None, candidate: dict) -> bool:
    if current is None:
        return True
    same_mobile_family = is_same_mobile_family(current, candidate)
    if same_mobile_family and is_mobile_guide(current) and not is_mobile_guide(candidate):
        return True
    if same_mobile_family and not is_mobile_guide(current) and is_mobile_guide(candidate):
        return False
    if target != "decc":
        return True
    return len(extract_response_fields(candidate)) > len(extract_response_fields(current))


def classify_spec_kind(html_name: str, spec: dict) -> str | None:
    if is_list_guide(html_name):
        return "list"
    if is_info_guide(html_name):
        return "info"
    if is_knowledge_base_guide(spec):
        return "info" if extract_endpoint_type(spec) == "service" else "list"
    return None


def extract_target(spec: dict) -> str:
    for row in spec.get("params", []):
        if row.get(PARAM_KEY, "").strip().lower() == "target":
            val = row.get(VAL_KEY, "")
            m = re.search(r":\s*([a-zA-Z][a-zA-Z0-9]*)", val)
            if m:
                return m.group(1)
    url = spec.get("request_url", "")
    m = re.search(r"target=([a-zA-Z][a-zA-Z0-9]*)", url)
    return m.group(1) if m else "unknown"


def extract_endpoint_type(spec: dict) -> str:
    url = spec.get("request_url", "") + spec.get("raw_url", "")
    return "service" if "lawService" in url else "search"


_URL_RE = re.compile(r"https?://\S+")


def _is_valid_field_name(name: str) -> bool:
    if not name:
        return False
    if _URL_RE.match(name):
        return False
    if re.match(r"^\d+\.", name):
        return False
    if name in ("샘플 URL", "샘플 URL:"):
        return False
    return True


def snake_from_str(s: str) -> str:
    """Convert any string (incl. Korean) to a valid snake_case Python identifier."""
    result = re.sub(r"[^\w가-힣]", "_", s.strip())
    result = re.sub(r"_+", "_", result).strip("_")
    if not result:
        return "field_unknown"
    result = result.lower()
    if result[0].isdigit():
        result = f"f_{result}"
    return result


def is_required(val: str) -> bool:
    return "필수" in val


def val_to_pytype(val: str) -> str:
    return "int | None" if "int" in val.lower() else "str | None"


def extract_params(spec: dict) -> list[dict]:
    rows = spec.get("params", [])
    result = []
    for row in rows:
        key = row.get(PARAM_KEY, "").strip()
        if not key or key in ("OC", "target", "type"):
            continue
        val = row.get(VAL_KEY, "")
        result.append({
            "key": key,
            "pyname": snake_from_str(key),
            "pytype": val_to_pytype(val),
            "required": is_required(val),
            "description": row.get(DESC_KEY, "").replace('"', "'"),
        })
    return result


def append_compat_params(params: list[dict], target: str) -> list[dict]:
    existing = {param["pyname"] for param in params}
    return params + [
        param for param in MOBILE_COMPAT_PARAMS.get(target, [])
        if param["pyname"] not in existing
    ]


def extract_response_fields(spec: dict) -> list[dict]:
    rows = spec.get("response", [])
    if not rows:
        return []
    resp_key = "col0"
    for k in RESP_KEY_CANDIDATES:
        if k in rows[0]:
            resp_key = k
            break
    seen: set[str] = set()
    result = []
    for row in rows:
        field_name = row.get(resp_key, "").strip()
        if not field_name or not _is_valid_field_name(field_name):
            continue
        pyname = snake_from_str(field_name)
        if pyname in seen:
            continue
        seen.add(pyname)
        result.append({
            "key": field_name,
            "pyname": pyname,
            "description": row.get(DESC_KEY, "").replace('"', "'")[:80],
        })
    return result


# ---------------------------------------------------------------------------
# Code rendering — fully working parsers
# ---------------------------------------------------------------------------

def render_list_method(spec: dict, target: str, root_key: str | None, item_key: str | None) -> str:
    label = spec["label"]
    params = append_compat_params(extract_params(spec), target)
    endpoint_const = "SERVICE_URL" if extract_endpoint_type(spec) == "service" else "BASE_URL"
    model_cls = f"{target.capitalize()}List"

    param_sigs, param_docs, param_dict_lines = [], [], []
    for p in params:
        sig_type = "int | None" if p["pytype"].startswith("int") else "str | None"
        param_sigs.append(f"        {p['pyname']}: {sig_type} = None")
        param_docs.append(f"        {p['pyname']}: {p['description']}")
        param_dict_lines.append(
            f'        if {p["pyname"]} is not None:\n            params["{p["key"]}"] = {p["pyname"]}'
        )

    sigs = (",\n").join(param_sigs) or "        page: int | None = None,\n        display: int | None = None"
    docs = "\n".join(param_docs) or "        (no additional params)"
    pd = "\n".join(param_dict_lines)

    if root_key and item_key:
        parse_block = (
            f'        data = response.json()\n'
            f'        root = data.get("{root_key}", {{}})\n'
            f'        if isinstance(root, dict):\n'
            f'            items = root.get("{item_key}", [])\n'
            f'        else:\n'
            f'            items = root if isinstance(root, list) else []\n'
            f'        if isinstance(items, dict):\n'
            f'            items = [items]\n'
            f'        return [{model_cls}.model_validate(item) for item in items]\n'
        )
        note = f"Response path: {root_key}.{item_key}"
    elif root_key:
        parse_block = (
            f'        data = response.json()\n'
            f'        root = data.get("{root_key}", {{}})\n'
            f'        if isinstance(root, list):\n'
            f'            items = root\n'
            f'        elif isinstance(root, dict):\n'
            f'            items = []\n'
            f'            found_items = False\n'
            f'            for value in root.values():\n'
            f'                if isinstance(value, list):\n'
            f'                    items = value\n'
            f'                    found_items = True\n'
            f'                    break\n'
            f'            if not found_items and root:\n'
            f'                items = [root]\n'
            f'        else:\n'
            f'            items = []\n'
            f'        if isinstance(items, dict):\n'
            f'            items = [items]\n'
            f'        return [{model_cls}.model_validate(item) for item in items]\n'
        )
        note = f"Response path: {root_key} (item key not discovered)"
    else:
        parse_block = (
            f'        data = response.json()\n'
            f'        if isinstance(data, list):\n'
            f'            raw = data\n'
            f'        else:\n'
            f'            raw = []\n'
            f'            for v in data.values():\n'
            f'                if isinstance(v, list):\n'
            f'                    raw = v\n'
            f'                    break\n'
            f'                if isinstance(v, dict):\n'
            f'                    for _ik, _iv in v.items():\n'
            f'                        if _ik in ("resultMsg", "resultCode", "page", "totalCnt", "target", "키워드", "section", "numOfRows", "display", "query"):\n'
            f'                            continue\n'
            f'                        if isinstance(_iv, list) and _iv:\n'
            f'                            raw = _iv\n'
            f'                            break\n'
            f'                    if not raw:\n'
            f'                        raw = [v]\n'
            f'                    break\n'
            f'        return [{model_cls}.model_validate(item) for item in raw]\n'
        )
        note = "Root key not discovered — using best-effort extraction"

    return f'''\
    def search_{target}s(
        self,
{sigs},
    ) -> list[{model_cls}]:
        """[GENERATED] {label}

        Args:
{docs}

        Returns:
            List of {model_cls} instances.
            {note}
        """
        params: dict = {{"target": "{target}", "type": "JSON"}}
{pd}
        response = self._make_request(self.{endpoint_const}, params=params)
{parse_block}
'''


def render_detail_method(spec: dict, target: str, root_key: str | None) -> str:
    label = spec["label"]
    params = append_compat_params(extract_params(spec), target)
    endpoint_const = "SERVICE_URL" if extract_endpoint_type(spec) == "service" else "BASE_URL"
    model_cls = f"{target.capitalize()}Detail"

    param_sigs, param_docs, param_dict_lines = [], [], []
    for p in params:
        sig_type = "int | None" if p["pytype"].startswith("int") else "str | None"
        param_sigs.append(f"        {p['pyname']}: {sig_type} = None")
        param_docs.append(f"        {p['pyname']}: {p['description']}")
        param_dict_lines.append(
            f'        if {p["pyname"]} is not None:\n            params["{p["key"]}"] = {p["pyname"]}'
        )

    sigs = (",\n").join(param_sigs) or "        record_id: str | None = None"
    docs = "\n".join(param_docs) or "        (no additional params)"
    pd = "\n".join(param_dict_lines)

    if root_key:
        parse_block = (
            f'        data = response.json()\n'
            f'        raw = data.get("{root_key}", data)\n'
            f'        return {model_cls}.model_validate(raw)\n'
        )
        note = f"Response path: {root_key}"
    else:
        parse_block = (
            f'        return {model_cls}.model_validate(response.json())\n'
        )
        note = "Root key not discovered — returning raw response"

    return f'''\
    def get_{target}_detail(
        self,
{sigs},
    ) -> {model_cls}:
        """[GENERATED] {label}

        Args:
{docs}

        Returns:
            {model_cls} instance.
            {note}
        """
        params: dict = {{"target": "{target}", "type": "JSON"}}
{pd}
        response = self._make_request(self.{endpoint_const}, params=params)
{parse_block}
'''


def render_test_file(
    target: str,
    specs: dict[str, dict],
    root_key_search: str | None,
    item_key: str | None,
    root_key_detail: str | None,
) -> str:
    cap = target.capitalize()
    has_list = "list" in specs
    has_detail = "info" in specs

    list_fields = extract_response_fields(specs["list"]) if has_list else []
    detail_fields = extract_response_fields(specs["info"]) if has_detail else []

    list_model = f"{cap}List"
    detail_model = f"{cap}Detail"

    client_import = f"from lawpy.kr.generated.{target} import Generated{cap}Client"
    model_names = sorted(
        [list_model] * has_list + [detail_model] * has_detail
    )
    model_import = (
        f"from lawpy.kr.generated._models_generated import {', '.join(model_names)}"
        if model_names else ""
    )

    def sample_data(fields: list[dict]) -> str:
        if not fields:
            return "{}"
        body = ", ".join(f'"{field["key"]}": "val"' for field in fields[:3])
        return f"{{{body}}}"

    sample_list_data = sample_data(list_fields)
    sample_detail_data = sample_data(detail_fields)
    if target == "decc":
        sample_list_data = '{"target": "val", "키워드": "val", "section": "val", "의결일자": "20240131"}'
        sample_detail_data = '{"행정심판례일련번호": "val", "사건명": "val", "사건번호": "val", "주문": "val"}'
    elif target == "prec":
        sample_detail_data = '{"판례정보일련번호": "val", "사건명": "val", "사건번호": "val", "판례내용": "val"}'

    if root_key_search and item_key:
        list_mock_json = f'{{"{root_key_search}": {{"{item_key}": [{sample_list_data}]}}}}'
    elif root_key_search:
        list_mock_json = f'{{"{root_key_search}": [{sample_list_data}]}}'
    else:
        list_mock_json = f'{{"result": [{sample_list_data}]}}'

    if root_key_detail:
        detail_mock_json = f'{{"{root_key_detail}": {sample_detail_data}}}'
    else:
        detail_mock_json = sample_detail_data

    list_params = extract_params(specs["list"]) if has_list else []
    first_list_param = list_params[0] if list_params else None

    test_methods = []

    if has_list:
        extra_list_asserts = ""
        if target == "decc":
            extra_list_asserts = "\n        assert result[0].의결일자 == \"20240131\""
        test_methods.append(f'''\
    def test_search_returns_list_of_models(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({list_mock_json}))
        result = client.search_{target}s()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], {list_model}){extra_list_asserts}''')

        test_methods.append(f'''\
    def test_search_empty_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({{}}))
        result = client.search_{target}s()
        assert isinstance(result, list)
        assert len(result) == 0''')

        if first_list_param:
            pkey = first_list_param["key"]
            pname = first_list_param["pyname"]
            pval = "1" if first_list_param["pytype"].startswith("int") else '"test"'
            test_methods.append(f'''\
    def test_search_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({list_mock_json}))
        client.search_{target}s({pname}={pval})
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {{}}))
        assert "{pkey}" in call_params''')

        if target == "decc":
            test_methods.append(f'''\
    def test_search_passes_popyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({list_mock_json}))
        client.search_{target}s(popyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {{}}))
        assert call_params["popYn"] == "Y"
        assert "mobileYn" not in call_params''')

        if target in MOBILE_COMPAT_PARAMS:
            test_methods.append(f'''\
    def test_search_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({list_mock_json}))
        client.search_{target}s(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {{}}))
        assert call_params["mobileYn"] == "Y"''')

    if has_list and root_key_search and item_key:
        test_methods.append(f'''\
    def test_search_accepts_root_list_fallback(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({{"{root_key_search}": [{sample_list_data}]}}))
        result = client.search_{target}s()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], {list_model})''')

    if has_list and root_key_search and not item_key:
        test_methods.append(f'''\
    def test_search_nested_empty_list_response(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({{"{root_key_search}": {{"items": []}}}}))
        result = client.search_{target}s()
        assert isinstance(result, list)
        assert len(result) == 0''')

    if has_detail:
        detail_params = extract_params(specs["info"])
        first_detail_param = detail_params[0] if detail_params else None
        extra_detail_asserts = ""
        if target == "decc":
            extra_detail_asserts = "\n        assert result.사건명 == \"val\"\n        assert result.주문 == \"val\""
        elif target == "prec":
            extra_detail_asserts = "\n        assert result.사건명 == \"val\"\n        assert result.판례내용 == \"val\""

        test_methods.append(f'''\
    def test_detail_returns_model(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({detail_mock_json}))
        result = client.get_{target}_detail()
        assert isinstance(result, {detail_model}){extra_detail_asserts}''')

        if first_detail_param:
            pkey = first_detail_param["key"]
            pname = first_detail_param["pyname"]
            pval = '"1"' if first_detail_param["pytype"].startswith("str") else "1"
            test_methods.append(f'''\
    def test_detail_passes_params(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({detail_mock_json}))
        client.get_{target}_detail({pname}={pval})
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {{}}))
        assert "{pkey}" in call_params''')

        if target in MOBILE_COMPAT_PARAMS:
            test_methods.append(f'''\
    def test_detail_passes_mobileyn_param(self):
        client = _make_client()
        client._make_request = Mock(return_value=_mock_response({detail_mock_json}))
        client.get_{target}_detail(mobileyn="Y")
        call_params = client._make_request.call_args.kwargs.get("params", client._make_request.call_args[1].get("params", {{}}))
        assert call_params["mobileYn"] == "Y"''')

    methods_block = "\n\n".join(test_methods)

    import_block = f"from unittest.mock import Mock\n\n{model_import}\n{client_import}" if model_import else f"from unittest.mock import Mock\n\n{client_import}"

    return f'''\
"""Auto-generated tests for target={target}."""

{import_block}


def _make_client() -> Generated{cap}Client:
    return Generated{cap}Client(api_key="test_key")


def _mock_response(json_data):
    mock = Mock()
    mock.json.return_value = json_data
    return mock


class TestGenerated{cap}Client:
{methods_block}
'''


def render_model(target: str, kind: str, label: str, fields: list[dict], html_name: str) -> str:
    class_name = f"{target.capitalize()}{kind}"
    field_lines: list[str]
    if fields:
        field_lines = [
            f'    {f["pyname"]}: str | None = Field(None, alias="{f["key"]}")'
            for f in fields
        ]
    else:
        field_lines = ["    pass  # no response fields in spec"]

    if kind == "Detail" and target in DETAIL_COMPAT_FIELDS:
        existing_pynames = {f["pyname"] for f in fields}
        if field_lines == ["    pass  # no response fields in spec"]:
            field_lines = []
        for pyname, alias in DETAIL_COMPAT_FIELDS[target]:
            if pyname not in existing_pynames:
                field_lines.append(f'    {pyname}: str | None = Field(None, alias="{alias}")')

    compat_fields = MODEL_COMPAT_FIELDS.get((target, kind), [])
    if compat_fields:
        existing_pynames = {
            f["pyname"] for f in fields
        } | {
            line.split(":", 1)[0].strip()
            for line in field_lines
            if ":" in line
        }
        if field_lines == ["    pass  # no response fields in spec"]:
            field_lines = []
        for pyname, alias in compat_fields:
            if pyname not in existing_pynames:
                field_lines.append(f'    {pyname}: str | None = Field(None, alias="{alias}")')

    return f'''\
class {class_name}(BaseModel):
    """[GENERATED] Response model for {label}.

    Source: specs/kr/{html_name}.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
    model_config = {{"populate_by_name": True}}

{chr(10).join(field_lines)}

'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_specs(specs_dir: Path, out_dir: Path | None, dry_run: bool, target_filter: str | None, test_dir: Path | None = None) -> None:
    index = json.loads((specs_dir / "_index.json").read_text())

    # Load root key mapping
    root_keys_path = specs_dir / "_root_keys.json"
    root_keys: dict[str, dict] = {}
    if root_keys_path.exists():
        root_keys = json.loads(root_keys_path.read_text())
    else:
        print("⚠️  _root_keys.json not found — run scripts/probe_root_keys.py first for full parsers")

    # Group specs by target → {list: spec, info: spec}
    by_target: dict[str, dict[str, dict]] = {}
    for entry in index:
        html_name = entry["html_name"]
        path = specs_dir / f"{html_name}.json"
        if not path.exists():
            continue
        spec = json.loads(path.read_text())
        target = extract_target(spec)
        if target == "unknown":
            continue
        kind = classify_spec_kind(html_name, spec)
        if kind is None:
            continue
        target_specs = by_target.setdefault(target, {})
        if should_replace_spec(target, target_specs.get(kind), spec):
            target_specs[kind] = spec

    selected_targets = [
        target for target in sorted(by_target)
        if target_filter is None or target == target_filter
    ]
    print(f"Generating {len(selected_targets)} targets...")

    if out_dir and not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    if test_dir and not dry_run:
        test_dir.mkdir(parents=True, exist_ok=True)

    model_lines = [
        '"""Auto-generated Pydantic models from specs/kr/*.json + _root_keys.json\n'
        "Run scripts/codegen.py to regenerate. Do not edit by hand.\n"
        '"""\n\n'
        "# ruff: noqa: E501\n\n"
        "from __future__ import annotations\n\n"
        "from typing import Any\n\n"
        "from pydantic import BaseModel, Field, field_validator\n\n\n",
    ]

    for target in sorted(by_target):
        specs = by_target[target]
        selected = target_filter is None or target == target_filter
        rk = root_keys.get(target, {})
        root_key_search = rk.get("root_key") if rk.get("status") == "ok" else None
        item_key = rk.get("item_key") if rk.get("status") == "ok" else None

        # Detail endpoint root key (typically same as search but without item key)
        # Try to find it — for now use same root_key
        root_key_detail = root_key_search  # heuristic, good enough for most

        method_code = f"\n# ── {target} ──────────────────────────────────────\n"

        if "list" in specs:
            method_code += render_list_method(specs["list"], target, root_key_search, item_key)
        if "info" in specs:
            method_code += render_detail_method(specs["info"], target, root_key_detail)

        list_model = f"{target.capitalize()}List"
        detail_model = f"{target.capitalize()}Detail"
        model_imports = []
        if "list" in specs:
            model_imports.append(list_model)
        if "info" in specs:
            model_imports.append(detail_model)
        import_line = ", ".join(sorted(model_imports))

        if dry_run and selected:
            print(method_code)
        elif out_dir and selected:
            file_path = out_dir / f"{target}.py"
            header = (
                f'"""Auto-generated client for target={target}\n'
                f"Source: specs/kr/ + _root_keys.json\n"
                f"Run scripts/codegen.py to regenerate. Do not edit.\n"
                f'"""\n'
                f"# ruff: noqa: N802, E501\n"
                f"from __future__ import annotations\n\n"
                f"from lawpy.kr.base import KoreanBaseClient\n"
                f"from lawpy.kr.generated._models_generated import {import_line}\n\n\n"
                f"class Generated{target.capitalize()}Client(KoreanBaseClient):\n"
                f'    """Auto-generated client for target={target}.\n\n'
                f"    All methods return Pydantic models parsed from the API response.\n"
                f'    """\n'
            )
            file_path.write_text(header + method_code, encoding="utf-8")
            print(f"  ✅ {target:<20} root={root_key_search or '?':<25} item={item_key or '?'}")

        if test_dir and not dry_run and selected:
            test_code = render_test_file(
                target, specs, root_key_search, item_key, root_key_detail,
            )
            (test_dir / f"test_{target}.py").write_text(test_code, encoding="utf-8")

        # Models
        if out_dir or dry_run:
            for kind, spec in specs.items():
                label = spec["label"]
                html_name = spec["html_name"]
                fields = extract_response_fields(spec)
                kind_label = "List" if kind == "list" else "Detail"
                model_str = render_model(target, kind_label, label, fields, html_name)
                if dry_run and selected:
                    print(model_str)
                elif not dry_run:
                    model_lines.append(model_str)

    if not dry_run and out_dir:
        model_lines.append(SPECIAL_MODELS)
        models_path = out_dir / "_models_generated.py"
        models_path.write_text("".join(model_lines), encoding="utf-8")
        print(f"\n✅ {len(selected_targets)} client targets → {out_dir}")
        print("✅ Special targets → drlaw, lsDelegated")
        print(f"✅ Models for {len(by_target)} targets → {models_path}")
    if test_dir and not dry_run:
        print(f"✅ Tests → {test_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate fully working client code from specs + root key mapping")
    parser.add_argument("--specs", default="specs/kr")
    parser.add_argument("--out", default="src/lawpy/kr/generated")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--target", default=None, help="Generate only this target")
    parser.add_argument("--test-dir", default=None, help="Output dir for auto-generated tests (e.g. tests/test_generated)")
    args = parser.parse_args()

    process_specs(
        Path(args.specs),
        None if args.dry_run else Path(args.out),
        args.dry_run,
        args.target,
        Path(args.test_dir) if args.test_dir else None,
    )


if __name__ == "__main__":
    main()
