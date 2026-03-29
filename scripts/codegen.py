#!/usr/bin/env python3
"""
Generate Python client stub code from scraped API specs.

For each spec pair (e.g. precListGuide + precInfoGuide), generates:
  - A Python method stub in src/lawpy/kr/generated/{target}.py
  - A Pydantic model stub in src/lawpy/models_generated.py

Usage:
    python scripts/codegen.py --specs specs/kr/ --out src/lawpy/kr/generated/
    python scripts/codegen.py --specs specs/kr/ --dry-run   # print only
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

PARAM_KEY = "요청변수"
RESP_KEY_CANDIDATES = ["출력변수", "출력결과", "col0"]
DESC_KEY = "설명"
VAL_KEY = "값"

# HTML names that are list (search) endpoints vs detail (info) endpoints
LIST_SUFFIXES = ("ListGuide", "listGuide", "listguide")
INFO_SUFFIXES = ("InfoGuide", "infoGuide", "GuideInfo", "Guide")


def is_list(html_name: str) -> bool:
    return html_name.endswith(("ListGuide",))


def is_info(html_name: str) -> bool:
    return html_name.endswith(("InfoGuide",))


def extract_target(spec: dict) -> str:
    """Extract the API target value (e.g. 'prec') from spec params or request_url."""
    for row in spec.get("params", []):
        if row.get(PARAM_KEY, "").strip().lower() == "target":
            val = row.get(VAL_KEY, "")
            # e.g. "string : prec(필수)" → "prec"
            m = re.search(r":\s*([a-zA-Z][a-zA-Z0-9]*)", val)
            if m:
                return m.group(1)
    # Fallback: parse request_url
    url = spec.get("request_url", "")
    m = re.search(r"target=([a-zA-Z][a-zA-Z0-9]*)", url)
    return m.group(1) if m else "unknown"


def extract_endpoint_type(spec: dict) -> str:
    """Search or Service endpoint."""
    url = spec.get("request_url", "")
    if "lawService" in url or "lawService" in spec.get("raw_url", ""):
        return "service"
    return "search"


def snake_from_korean(s: str) -> str:
    """Very naive Korean → snake_case: just lowercase and strip non-alnum."""
    import unicodedata
    # Keep Korean, letters, numbers; replace others with _
    result = re.sub(r"[^\w가-힣]", "_", s.strip())
    result = re.sub(r"_+", "_", result).strip("_")
    return result.lower()


def is_required(val: str) -> bool:
    return "필수" in val


def val_to_pytype(val: str) -> str:
    v = val.lower()
    if "int" in v:
        return "int | None"
    return "str | None"


def extract_params(spec: dict) -> list[dict]:
    rows = spec.get("params", [])
    result = []
    for row in rows:
        key = row.get(PARAM_KEY, "").strip()
        if not key or key in ("OC", "target", "type"):
            continue
        val = row.get(VAL_KEY, "")
        desc = row.get(DESC_KEY, "")
        result.append(
            {
                "key": key,
                "pyname": snake_from_korean(key),
                "pytype": val_to_pytype(val),
                "required": is_required(val),
                "description": desc,
            }
        )
    return result


def extract_response_fields(spec: dict) -> list[dict]:
    rows = spec.get("response", [])
    result = []
    resp_key = "col0"
    for k in RESP_KEY_CANDIDATES:
        if rows and k in rows[0]:
            resp_key = k
            break
    for row in rows:
        field_name = row.get(resp_key, "").strip()
        if not field_name:
            continue
        desc = row.get(DESC_KEY, "")
        result.append(
            {
                "key": field_name,
                "pyname": snake_from_korean(field_name),
                "description": desc,
            }
        )
    return result


# ---------------------------------------------------------------------------
# Template rendering (pure string, no external deps)
# ---------------------------------------------------------------------------

def render_list_method(spec: dict, target: str) -> str:
    label = spec["label"]
    params = extract_params(spec)
    endpoint = extract_endpoint_type(spec)
    endpoint_const = "SERVICE_URL" if endpoint == "service" else "BASE_URL"

    param_sigs = []
    param_docs = []
    param_dict_lines = []

    for p in params:
        pytype = "int | None" if p["pytype"].startswith("int") else "str | None"
        if p["required"]:
            param_sigs.append(f"        {p['pyname']}: str")
            param_docs.append(f"        {p['pyname']}: {p['description']}")
        else:
            param_sigs.append(f"        {p['pyname']}: {pytype} = None")
            param_docs.append(f"        {p['pyname']}: {p['description']}")
        param_dict_lines.append(
            f'        if {p["pyname"]} is not None:\n'
            f'            params["{p["key"]}"] = {p["pyname"]}'
        )

    sigs = (",\n" + "").join(param_sigs) or "        page: int = 1,\n        display: int = 20"
    docs = "\n".join(param_docs) or "        (no additional params)"
    pd = "\n".join(param_dict_lines)

    method_name = f"search_{target}s"

    return f'''\
    def {method_name}(
        self,
{sigs},
    ) -> list[dict]:
        """[GENERATED] {label}

        Args:
{docs}

        Returns:
            List of result dicts.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/{spec["html_name"]}.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {{
            "target": "{target}",
            "type": "JSON",
        }}
{pd}
        response = self._make_request(self.{endpoint_const}, params=params)
        data = response.json()
        # TODO: navigate to the root list object and return items
        return []
'''


def render_detail_method(spec: dict, target: str) -> str:
    label = spec["label"]
    params = extract_params(spec)
    endpoint = extract_endpoint_type(spec)
    endpoint_const = "SERVICE_URL" if endpoint == "service" else "BASE_URL"

    param_sigs = []
    param_docs = []
    param_dict_lines = []

    for p in params:
        pytype = "int | None" if p["pytype"].startswith("int") else "str | None"
        param_sigs.append(f"        {p['pyname']}: {pytype} = None")
        param_docs.append(f"        {p['pyname']}: {p['description']}")
        param_dict_lines.append(
            f'        if {p["pyname"]} is not None:\n'
            f'            params["{p["key"]}"] = {p["pyname"]}'
        )

    sigs = (",\n" + "").join(param_sigs) or "        record_id: str | None = None"
    docs = "\n".join(param_docs) or "        (no additional params)"
    pd = "\n".join(param_dict_lines)

    method_name = f"get_{target}_detail"

    return f'''\
    def {method_name}(
        self,
{sigs},
    ) -> dict:
        """[GENERATED] {label}

        Args:
{docs}

        Returns:
            Detail dict.  Parse/validate with a Pydantic model.

        Note:
            This is an auto-generated stub from specs/kr/{spec["html_name"]}.json.
            Implement the actual xmltodict parsing logic before use.
        """
        params: dict = {{
            "target": "{target}",
            "type": "JSON",
        }}
{pd}
        response = self._make_request(self.{endpoint_const}, params=params)
        return response.json()
'''


def render_model(spec: dict, target: str, kind: str) -> str:
    label = spec["label"]
    fields = extract_response_fields(spec)
    class_name = f"{target.capitalize()}{kind}"

    field_lines = []
    for f in fields:
        desc = f["description"].replace('"', "'")
        field_lines.append(
            f'    {f["pyname"]}: str | None = None  # {f["key"]}: {desc[:60]}'
        )

    body = "\n".join(field_lines) or "    pass  # no response fields parsed"

    return f'''\
class {class_name}(BaseModel):
    """[GENERATED] Response model for {label}.

    Source: specs/kr/{spec["html_name"]}.json
    """
{body}

'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_specs(specs_dir: Path, out_dir: Path | None, dry_run: bool) -> None:
    index = json.loads((specs_dir / "_index.json").read_text())

    # Group by target
    by_target: dict[str, dict[str, dict]] = {}  # target → {list: spec, info: spec}
    for entry in index:
        html_name = entry["html_name"]
        path = specs_dir / f"{html_name}.json"
        if not path.exists():
            continue
        spec = json.loads(path.read_text())
        target = extract_target(spec)
        if target == "unknown":
            continue
        kind = "list" if is_list(html_name) else ("info" if is_info(html_name) else None)
        if kind is None:
            continue
        by_target.setdefault(target, {})[kind] = spec

    print(f"Found {len(by_target)} unique targets: {sorted(by_target)[:20]}...")

    if out_dir and not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)
        model_lines = [
            '"""Auto-generated Pydantic models from specs/kr/*.json\n'
            "Do not edit by hand — regenerate with scripts/codegen.py\n"
            '"""\n',
            "from pydantic import BaseModel\n\n",
        ]

    generated_count = 0
    for target in sorted(by_target):
        specs = by_target[target]

        method_code = f"\n# ── {target} ──────────────────────────────────────\n"

        if "list" in specs:
            method_code += render_list_method(specs["list"], target)
        if "info" in specs:
            method_code += render_detail_method(specs["info"], target)

        if dry_run:
            print(method_code)
        else:
            # Write per-target file
            file_path = out_dir / f"{target}.py"
            header = (
                f'"""Auto-generated client stubs for target={target}\n'
                f"Source: specs/kr/\n"
                f'Do not edit by hand — regenerate with scripts/codegen.py\n"""\n'
                f"from __future__ import annotations\n\n"
                f"from lawpy.kr.base import KoreanBaseClient\n\n\n"
                f"class {target.capitalize()}Client(KoreanBaseClient):\n"
                f'    """Auto-generated client for target={target}."""\n'
            )
            file_path.write_text(header + method_code, encoding="utf-8")
            print(f"  ✅ Generated {file_path}")

        # Model
        for kind, spec in specs.items():
            model_class_name = f"{target.capitalize()}{'List' if kind == 'list' else 'Detail'}"
            if dry_run:
                print(render_model(spec, target, "List" if kind == "list" else "Detail"))
            elif out_dir:
                model_lines.append(render_model(spec, target, "List" if kind == "list" else "Detail"))

        generated_count += 1

    if not dry_run and out_dir:
        models_path = out_dir / "_models_generated.py"
        models_path.write_text("\n".join(model_lines), encoding="utf-8")
        print(f"\n✅ Generated {generated_count} target stubs → {out_dir}")
        print(f"✅ Models → {models_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate client stubs from scraped specs")
    parser.add_argument("--specs", default="specs/kr", help="Specs directory")
    parser.add_argument("--out", default="src/lawpy/kr/generated", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout, do not write files")
    args = parser.parse_args()

    process_specs(Path(args.specs), None if args.dry_run else Path(args.out), args.dry_run)


if __name__ == "__main__":
    main()
