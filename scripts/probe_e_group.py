#!/usr/bin/env python3
"""Probe E-group KR API targets for live root/item keys.

The output is meant to be reviewed before copying stable results into
``specs/kr/_root_keys.json``. It does not write generated files.
"""

from __future__ import annotations

import argparse
import json
import os
from collections.abc import Mapping
from typing import Any

import httpx

BASE_SEARCH = "https://www.law.go.kr/DRF/lawSearch.do"

SPECIAL_DECC_TARGETS = [
    "decc",
    "acrSpecialDecc",
    "adapSpecialDecc",
    "kmstSpecialDecc",
    "ttSpecialDecc",
]

CGM_EXPC_TARGETS = [
    "dapaCgmExpc",
    "kcgCgmExpc",
    "kcsCgmExpc",
    "kdcaCgmExpc",
    "kfsCgmExpc",
    "khsCgmExpc",
    "kipoCgmExpc",
    "kmaCgmExpc",
    "kostatCgmExpc",
    "mafraCgmExpc",
    "mcstCgmExpc",
    "meCgmExpc",
    "mfdsCgmExpc",
    "mmaCgmExpc",
    "mndCgmExpc",
    "moeCgmExpc",
    "moefCgmExpc",
    "moelCgmExpc",
    "mofCgmExpc",
    "mofaCgmExpc",
    "mogefCgmExpc",
    "mohwCgmExpc",
    "moisCgmExpc",
    "mojCgmExpc",
    "molegCgmExpc",
    "molitCgmExpc",
    "motieCgmExpc",
    "mouCgmExpc",
    "mpmCgmExpc",
    "mpvaCgmExpc",
    "msitCgmExpc",
    "mssCgmExpc",
    "naaccCgmExpc",
    "nfaCgmExpc",
    "npaCgmExpc",
    "ntsCgmExpc",
    "okaCgmExpc",
    "ppsCgmExpc",
    "rdaCgmExpc",
]

TARGETS = SPECIAL_DECC_TARGETS + CGM_EXPC_TARGETS


def _params_for(target: str, api_key: str) -> dict[str, str]:
    query = "영업정지" if target in SPECIAL_DECC_TARGETS else "민원"
    return {
        "OC": api_key,
        "target": target,
        "type": "JSON",
        "query": query,
        "display": "1",
    }


def _root_item_shape(data: Any, target: str) -> dict[str, Any]:
    if not isinstance(data, Mapping) or not data:
        return {"target": target, "status": "error", "error": "response is not an object"}
    error_message = _find_error_message(data)
    if error_message is not None:
        return {"target": target, "status": "error", "error": error_message}

    root_key = next(iter(data))
    root = data[root_key]
    item_key = None
    item_type = None

    if isinstance(root, Mapping):
        payload_keys = [
            key
            for key in root
            if key not in {"resultCode", "resultMsg", "page", "totalCnt", "target", "키워드", "section"}
        ]
        for key in payload_keys:
            value = root[key]
            if isinstance(value, list | dict):
                item_key = key
                item_type = type(value).__name__
                break
    elif isinstance(root, list):
        item_type = "list"

    return {
        "target": target,
        "root_key": root_key,
        "item_key": item_key,
        "item_type": item_type,
        "status": "ok",
    }


def _find_error_message(data: Any) -> str | None:
    if not isinstance(data, Mapping):
        return None

    lower_keys = {str(key).lower(): key for key in data}
    code_key = lower_keys.get("resultcode")
    message_key = lower_keys.get("resultmsg")
    if code_key is not None and message_key is not None:
        code = data[code_key]
        if code not in (None, "", "00", "0", 0):
            return str(data[message_key])

    result_key = lower_keys.get("result")
    msg_key = lower_keys.get("msg")
    if result_key is not None and msg_key is not None:
        result = str(data[result_key]).strip().lower()
        if result not in {"", "0", "00", "ok", "success", "true"}:
            return str(data[msg_key])

    for value in data.values():
        nested = _find_error_message(value)
        if nested is not None:
            return nested
    return None


def probe_target(client: httpx.Client, target: str, api_key: str) -> dict[str, Any]:
    response = client.get(BASE_SEARCH, params=_params_for(target, api_key))
    response.raise_for_status()
    try:
        data = response.json()
    except ValueError as exc:
        return {"target": target, "status": "not_json", "error": str(exc)}
    return _root_item_shape(data, target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Probe E-group KR root/item keys")
    parser.add_argument("--api-key", default=os.environ.get("LAWPY_KR_API_KEY") or os.environ.get("LAWPY_API_KEY"))
    parser.add_argument("--target", action="append", choices=TARGETS)
    parser.add_argument("--indent", type=int, default=2)
    args = parser.parse_args()

    if not args.api_key:
        raise SystemExit("Provide --api-key or set LAWPY_KR_API_KEY")

    targets = args.target or TARGETS
    with httpx.Client(timeout=30) as client:
        results = {target: probe_target(client, target, args.api_key) for target in targets}
    print(json.dumps(results, ensure_ascii=False, indent=args.indent, sort_keys=True))


if __name__ == "__main__":
    main()
