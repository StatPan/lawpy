#!/usr/bin/env python3
"""
Probe all targets from specs/kr/_index.json to discover:
  - root key in JSON response (e.g. "PrecSearch")
  - item key within root (e.g. "prec")

Then saves the mapping to specs/kr/_root_keys.json.
This is consumed by codegen.py to generate fully working parsers.

Usage:
    uv run python scripts/probe_root_keys.py
    uv run python scripts/probe_root_keys.py --delay 0.5
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import httpx

BASE_SEARCH = "https://www.law.go.kr/DRF/lawSearch.do"
BASE_SERVICE = "http://www.law.go.kr/DRF/lawService.do"

# Metadata keys present in all responses — not item keys
META_KEYS = {
    "resultMsg", "resultCode", "page", "totalCnt", "target",
    "키워드", "section", "numOfRows", "display", "query",
}

# Representative queries per target (to get non-empty results)
DEFAULT_QUERIES = {
    "law": {"query": "민법"},
    "eflaw": {"query": "민법"},
    "lsHistory": {"LID": "59602"},
    "prec": {"query": "손해배상"},
    "detc": {"query": "토지"},
    "decc": {"query": "민법"},
    "admrul": {"query": "민법"},
    "ordin": {"query": "조례"},
    "trty": {"query": "조약"},
    "elaw": {"query": "civil"},
    "lstrm": {"query": "민법"},
    "acr": {"query": "민법"},
}


def discover_root_key(client: httpx.Client, target: str, api_key: str, delay: float) -> dict:
    """Call the search endpoint for a target and discover its JSON structure."""
    extra = DEFAULT_QUERIES.get(target, {"query": "민법"})
    params = {
        "OC": api_key,
        "target": target,
        "type": "JSON",
        "display": "1",
        **extra,
    }
    try:
        r = client.get(BASE_SEARCH, params=params, timeout=10)
        r.raise_for_status()
        d = r.json()

        root_key = list(d.keys())[0]
        sub = d[root_key]

        # item key = first non-metadata key
        item_keys = [k for k in sub if k not in META_KEYS]
        item_key = item_keys[0] if item_keys else None

        # Is the item actually a list or dict?
        item_type = None
        if item_key and sub.get(item_key) is not None:
            item_type = type(sub[item_key]).__name__

        return {
            "target": target,
            "root_key": root_key,
            "item_key": item_key,
            "item_type": item_type,
            "status": "ok",
        }
    except Exception as e:
        return {"target": target, "status": "error", "error": str(e)}
    finally:
        time.sleep(delay)


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover JSON root keys for all KR targets")
    parser.add_argument("--specs", default="specs/kr", help="Specs directory")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--delay", type=float, default=0.3)
    args = parser.parse_args()

    import os
    api_key = args.api_key or os.environ.get("LAWPY_KR_API_KEY") or os.environ.get("LAWPY_API_KEY")
    if not api_key:
        raise SystemExit("Set LAWPY_KR_API_KEY or pass --api-key")

    specs_dir = Path(args.specs)
    index = json.loads((specs_dir / "_index.json").read_text())

    # Extract unique targets from all specs
    targets: set[str] = set()
    for entry in index:
        spec_path = specs_dir / f"{entry['html_name']}.json"
        if not spec_path.exists():
            continue
        spec = json.loads(spec_path.read_text())
        for row in spec.get("params", []):
            if row.get("요청변수", "").strip().lower() == "target":
                import re
                m = re.search(r":\s*([a-zA-Z][a-zA-Z0-9]*)", row.get("값", ""))
                if m:
                    targets.add(m.group(1))

    print(f"Discovered {len(targets)} unique targets. Probing...")

    results: dict[str, dict] = {}
    with httpx.Client() as client:
        for i, target in enumerate(sorted(targets), 1):
            print(f"  [{i:>3}/{len(targets)}] {target:<20} ", end="", flush=True)
            result = discover_root_key(client, target, api_key, args.delay)
            results[target] = result
            if result["status"] == "ok":
                print(f"✅ root={result['root_key']:<25} item={result['item_key']} ({result['item_type']})")
            else:
                print(f"❌ {result.get('error', '')}")

    out_path = specs_dir / "_root_keys.json"
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    ok = sum(1 for r in results.values() if r["status"] == "ok")
    print(f"\n✅ {ok}/{len(results)} root keys discovered → {out_path}")


if __name__ == "__main__":
    main()
