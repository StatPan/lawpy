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

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PARAM_KEY = "요청변수"
RESP_KEY_CANDIDATES = ["출력변수", "출력결과", "필드", "col0"]
DESC_KEY = "설명"
VAL_KEY = "값"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_list_guide(html_name: str) -> bool:
    return html_name.endswith("ListGuide")


def is_info_guide(html_name: str) -> bool:
    return html_name.endswith("InfoGuide")


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
        result = f"field_{result}"
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
    params = extract_params(spec)
    endpoint_const = "SERVICE_URL" if extract_endpoint_type(spec) == "service" else "BASE_URL"

    param_sigs, param_docs, param_dict_lines = [], [], []
    for p in params:
        sig_type = "int | None" if p["pytype"].startswith("int") else "str | None"
        # Always default to None — some specs incorrectly mark params as required
        param_sigs.append(f"        {p['pyname']}: {sig_type} = None")
        param_docs.append(f"        {p['pyname']}: {p['description']}")
        param_dict_lines.append(
            f'        if {p["pyname"]} is not None:\n            params["{p["key"]}"] = {p["pyname"]}'
        )

    sigs = (",\n").join(param_sigs) or "        page: int | None = None,\n        display: int | None = None"
    docs = "\n".join(param_docs) or "        (no additional params)"
    pd = "\n".join(param_dict_lines)

    # Generate the actual parsing logic from root_key + item_key
    if root_key and item_key:
        parse_block = (
            f'        data = response.json()\n'
            f'        root = data.get("{root_key}", {{}})\n'
            f'        items = root.get("{item_key}", [])\n'
            f'        if isinstance(items, dict):\n'
            f'            items = [items]\n'
            f'        return items or []\n'
        )
        return_type = "list[dict]"
        note = f"Response path: {root_key}.{item_key}"
    elif root_key:
        parse_block = (
            f'        data = response.json()\n'
            f'        root = data.get("{root_key}", {{}})\n'
            f'        result = root if isinstance(root, list) else [root] if root else []\n'
            f'        return result\n'
        )
        return_type = "list[dict]"
        note = f"Response path: {root_key} (item key not discovered)"
    else:
        parse_block = (
            f'        data = response.json()\n'
            f'        if isinstance(data, list):\n'
            f'            return data\n'
            f'        for v in data.values():\n'
            f'            if isinstance(v, list):\n'
            f'                return v\n'
            f'            if isinstance(v, dict):\n'
            f'                return [v]\n'
            f'        return []\n'
        )
        return_type = "list[dict]"
        note = "Root key not discovered — using best-effort extraction"

    return f'''\
    def search_{target}s(
        self,
{sigs},
    ) -> {return_type}:
        """[GENERATED] {label}

        Args:
{docs}

        Returns:
            List of result dicts. Fields match the API response schema.
            {note}
        """
        params: dict = {{"target": "{target}", "type": "JSON"}}
{pd}
        response = self._make_request(self.{endpoint_const}, params=params)
{parse_block}
'''


def render_detail_method(spec: dict, target: str, root_key: str | None) -> str:
    label = spec["label"]
    params = extract_params(spec)
    endpoint_const = "SERVICE_URL" if extract_endpoint_type(spec) == "service" else "BASE_URL"

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
            f'        return data.get("{root_key}", data)\n'
        )
        note = f"Response path: {root_key}"
    else:
        parse_block = (
            f'        return response.json()\n'
        )
        note = "Root key not discovered — returning raw response"

    return f'''\
    def get_{target}_detail(
        self,
{sigs},
    ) -> dict:
        """[GENERATED] {label}

        Args:
{docs}

        Returns:
            Detail dict. Fields match the API response schema.
            {note}
        """
        params: dict = {{"target": "{target}", "type": "JSON"}}
{pd}
        response = self._make_request(self.{endpoint_const}, params=params)
{parse_block}
'''


def render_model(target: str, kind: str, label: str, fields: list[dict], html_name: str) -> str:
    class_name = f"{target.capitalize()}{kind}"
    field_lines = [
        f'    {f["pyname"]}: str | None = None  # {f["key"]}: {f["description"][:60]}'
        for f in fields
    ] or ["    pass  # no response fields in spec"]

    return f'''\
class {class_name}(BaseModel):
    """[GENERATED] Response model for {label}.

    Source: specs/kr/{html_name}.json
    Fields reflect API spec — actual data may differ.
    All fields are optional (str | None) as API may omit any field.
    """
{chr(10).join(field_lines)}

'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_specs(specs_dir: Path, out_dir: Path | None, dry_run: bool, target_filter: str | None) -> None:
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
        if target_filter and target != target_filter:
            continue
        kind = "list" if is_list_guide(html_name) else ("info" if is_info_guide(html_name) else None)
        if kind is None:
            continue
        by_target.setdefault(target, {})[kind] = spec

    print(f"Generating {len(by_target)} targets...")

    if out_dir and not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    model_lines = [
        '"""Auto-generated Pydantic models from specs/kr/*.json + _root_keys.json\n'
        "Run scripts/codegen.py to regenerate. Do not edit by hand.\n"
        '"""\n\n'
        "# ruff: noqa: E501\n\n"
        "from pydantic import BaseModel\n\n\n",
    ]

    for target in sorted(by_target):
        specs = by_target[target]
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

        if dry_run:
            print(method_code)
        elif out_dir:
            file_path = out_dir / f"{target}.py"
            header = (
                f'"""Auto-generated client for target={target}\n'
                f"Source: specs/kr/ + _root_keys.json\n"
                f"Run scripts/codegen.py to regenerate. Do not edit.\n"
                f'"""\n'
                f"# ruff: noqa: N802, E501\n"
                f"from __future__ import annotations\n\n"
                f"from lawpy.kr.base import KoreanBaseClient\n\n\n"
                f"class {target.capitalize()}Client(KoreanBaseClient):\n"
                f'    """Auto-generated client for target={target}.\n\n'
                f'    All methods return plain dicts matching the API response schema.\n'
                f'    See _models_generated.py for Pydantic models.\n'
                f'    """\n'
            )
            file_path.write_text(header + method_code, encoding="utf-8")
            print(f"  ✅ {target:<20} root={root_key_search or '?':<25} item={item_key or '?'}")

        # Models
        if out_dir or dry_run:
            for kind, spec in specs.items():
                label = spec["label"]
                html_name = spec["html_name"]
                fields = extract_response_fields(spec)
                kind_label = "List" if kind == "list" else "Detail"
                model_str = render_model(target, kind_label, label, fields, html_name)
                if dry_run:
                    print(model_str)
                else:
                    model_lines.append(model_str)

    if not dry_run and out_dir:
        models_path = out_dir / "_models_generated.py"
        models_path.write_text("".join(model_lines), encoding="utf-8")
        print(f"\n✅ {len(by_target)} targets → {out_dir}")
        print(f"✅ Models → {models_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate fully working client code from specs + root key mapping")
    parser.add_argument("--specs", default="specs/kr")
    parser.add_argument("--out", default="src/lawpy/kr/generated")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--target", default=None, help="Generate only this target")
    args = parser.parse_args()

    process_specs(
        Path(args.specs),
        None if args.dry_run else Path(args.out),
        args.dry_run,
        args.target,
    )


if __name__ == "__main__":
    main()
