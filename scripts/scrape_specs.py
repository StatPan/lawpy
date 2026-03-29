#!/usr/bin/env python3
"""
Scrape ALL Korean law API guide specs from open.law.go.kr and save as JSON.

Usage:
    python scripts/scrape_specs.py
    python scripts/scrape_specs.py --output specs/kr/

Output: specs/kr/{guide_name}.json for each guide page
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

GUIDE_LIST_URL = "https://open.law.go.kr/LSO/openApi/guideList.do"
GUIDE_RESULT_URL = "https://open.law.go.kr/LSO/openApi/guideResult.do"


def get_all_guide_names() -> list[tuple[str, str]]:
    """Extract all (html_name, label) from the guide list page."""
    resp = httpx.get(GUIDE_LIST_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    entries: list[tuple[str, str]] = []
    for tag in soup.find_all("a", href=True):
        onclick = tag.get("onclick", "")
        m = re.search(r"openApiGuide\('([^']+)'\)", onclick)
        if m:
            html_name = m.group(1)
            label = tag.get_text(separator=" ", strip=True)
            entries.append((html_name, label))

    # Deduplicate preserving order
    seen: set[str] = set()
    result: list[tuple[str, str]] = []
    for name, label in entries:
        if name not in seen:
            seen.add(name)
            result.append((name, label))
    return result


def parse_table(table) -> list[dict[str, str]]:
    """Parse an HTML table into a list of row dicts keyed by header."""
    rows = []
    if table is None:
        return rows
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    for tr in table.find_all("tr"):
        cells = [td.get_text(separator=" ", strip=True) for td in tr.find_all("td")]
        if cells and len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
        elif cells:
            # Fallback: use positional keys
            rows.append({f"col{i}": v for i, v in enumerate(cells)})
    return rows


def scrape_guide(html_name: str, label: str, client: httpx.Client) -> dict:
    """Fetch one guide page and extract URL + param/response tables."""
    resp = client.post(
        GUIDE_RESULT_URL,
        data={"htmlName": html_name},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract request URL
    request_url = ""
    for tag in soup.find_all(["p", "div", "td", "li"]):
        txt = tag.get_text(strip=True)
        if "요청 URL" in txt or "Request URL" in txt:
            # Often the URL is in the same element or the next sibling
            url_match = re.search(r"(https?://[^\s<\"]+)", txt)
            if not url_match:
                url_match = re.search(r"(http[^\s<\"]+\.do[^\s<\"]*)", txt)
            if url_match:
                request_url = url_match.group(1)
            break

    # Extract all tables
    tables = soup.find_all("table")
    param_rows: list[dict] = []
    response_rows: list[dict] = []

    for table in tables:
        # Classify table by its preceding heading or caption
        prev = table.find_previous(["h2", "h3", "h4", "p", "strong", "caption"])
        heading = prev.get_text(strip=True) if prev else ""
        rows = parse_table(table)
        if not rows:
            continue

        is_request = any(k in heading for k in ["요청", "request", "Request", "파라미터", "parameter"])
        is_response = any(k in heading for k in ["출력", "response", "Response", "결과"])

        # Fallback: check header keys
        if not (is_request or is_response) and rows:
            keys = set(rows[0].keys())
            if "요청변수" in keys or "변수" in heading:
                is_request = True
            elif "출력결과" in keys or "출력변수" in keys:
                is_response = True

        if is_request and not param_rows:
            param_rows = rows
        elif is_response and not response_rows:
            response_rows = rows

    # If we still have two tables and didn't classify, use order
    if not param_rows and not response_rows and len(tables) >= 2:
        param_rows = parse_table(tables[0])
        response_rows = parse_table(tables[1])
    elif not response_rows and len(tables) >= 2:
        response_rows = parse_table(tables[-1])

    return {
        "html_name": html_name,
        "label": label,
        "request_url": request_url,
        "params": param_rows,
        "response": response_rows,
        "raw_url": str(resp.url),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape Korean law API guide specs")
    parser.add_argument("--output", default="specs/kr", help="Output directory")
    parser.add_argument("--delay", type=float, default=0.3, help="Delay between requests (s)")
    parser.add_argument("--limit", type=int, default=0, help="Max guides to scrape (0=all)")
    args = parser.parse_args()

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Fetching guide list...", flush=True)
    guides = get_all_guide_names()
    print(f"Found {len(guides)} guide pages")

    if args.limit:
        guides = guides[: args.limit]

    failed: list[str] = []

    with httpx.Client(timeout=30) as client:
        for i, (html_name, label) in enumerate(guides, 1):
            out_path = out_dir / f"{html_name}.json"
            print(f"  [{i:>3}/{len(guides)}] {html_name:<45} ", end="", flush=True)
            try:
                spec = scrape_guide(html_name, label, client)
                out_path.write_text(
                    json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                n_params = len(spec["params"])
                n_resp = len(spec["response"])
                print(f"✅  params={n_params}  response={n_resp}")
            except Exception as e:
                print(f"❌  {e}")
                failed.append(html_name)
            time.sleep(args.delay)

    # Summary index
    index: list[dict] = []
    for html_name, label in guides:
        path = out_dir / f"{html_name}.json"
        if path.exists():
            spec = json.loads(path.read_text())
            index.append(
                {
                    "html_name": html_name,
                    "label": label,
                    "request_url": spec.get("request_url", ""),
                    "n_params": len(spec.get("params", [])),
                    "n_response": len(spec.get("response", [])),
                }
            )

    index_path = out_dir / "_index.json"
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nDone. {len(guides) - len(failed)}/{len(guides)} specs saved to {out_dir}/")
    if failed:
        print(f"Failed: {failed}")
    print(f"Index: {index_path}")


if __name__ == "__main__":
    main()
