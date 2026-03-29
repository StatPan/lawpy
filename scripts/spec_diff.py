#!/usr/bin/env python3
"""
Diff two runs of scraped specs to detect API additions, removals, and changes.

Usage:
    python scripts/spec_diff.py --old specs/kr/ --new specs/kr/new/
    python scripts/spec_diff.py --old specs/kr/ --new specs/kr/  # rescrape inline

Exit code:
    0 = no changes
    1 = changes detected (params/response fields added or removed)
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SpecDiff:
    added_guides: list[str] = field(default_factory=list)
    removed_guides: list[str] = field(default_factory=list)
    changed_guides: list[dict] = field(default_factory=list)

    @property
    def has_changes(self) -> bool:
        return bool(self.added_guides or self.removed_guides or self.changed_guides)

    @property
    def has_breaking(self) -> bool:
        """Removed endpoints or removed fields."""
        if self.removed_guides:
            return True
        return any(
            g.get("removed_params") or g.get("removed_response")
            for g in self.changed_guides
        )


def _field_set(rows: list[dict], key: str) -> set[str]:
    """Extract unique field names from a list of row dicts."""
    result = set()
    for row in rows:
        val = row.get(key, "").strip()
        if val:
            result.add(val)
    return result


def diff_specs(old_dir: Path, new_dir: Path) -> SpecDiff:
    result = SpecDiff()

    old_index = {
        e["html_name"]: e
        for e in json.loads((old_dir / "_index.json").read_text())
    }
    new_index = {
        e["html_name"]: e
        for e in json.loads((new_dir / "_index.json").read_text())
    }

    result.added_guides = sorted(set(new_index) - set(old_index))
    result.removed_guides = sorted(set(old_index) - set(new_index))

    # Detail diff for shared guides
    for name in sorted(set(old_index) & set(new_index)):
        old_path = old_dir / f"{name}.json"
        new_path = new_dir / f"{name}.json"
        if not old_path.exists() or not new_path.exists():
            continue

        old_spec = json.loads(old_path.read_text())
        new_spec = json.loads(new_path.read_text())

        # Compare params
        old_params = _field_set(old_spec.get("params", []), "요청변수")
        new_params = _field_set(new_spec.get("params", []), "요청변수")

        # Try alternate header names
        if not old_params:
            old_params = _field_set(old_spec.get("params", []), "col0")
        if not new_params:
            new_params = _field_set(new_spec.get("params", []), "col0")

        # Compare response fields
        resp_key_candidates = ["출력변수", "출력결과", "col0"]
        old_resp: set[str] = set()
        new_resp: set[str] = set()
        for k in resp_key_candidates:
            old_resp = _field_set(old_spec.get("response", []), k)
            new_resp = _field_set(new_spec.get("response", []), k)
            if old_resp or new_resp:
                break

        added_params = sorted(new_params - old_params)
        removed_params = sorted(old_params - new_params)
        added_resp = sorted(new_resp - old_resp)
        removed_resp = sorted(old_resp - new_resp)

        if any([added_params, removed_params, added_resp, removed_resp]):
            result.changed_guides.append(
                {
                    "html_name": name,
                    "label": new_index[name].get("label", ""),
                    "added_params": added_params,
                    "removed_params": removed_params,
                    "added_response": added_resp,
                    "removed_response": removed_resp,
                }
            )

    return result


def print_report(diff: SpecDiff) -> None:
    if not diff.has_changes:
        print("✅ No spec changes detected.")
        return

    if diff.added_guides:
        print(f"\n🆕 New APIs ({len(diff.added_guides)}):")
        for g in diff.added_guides:
            print(f"   + {g}")

    if diff.removed_guides:
        print(f"\n🗑️  Removed APIs ({len(diff.removed_guides)}):")
        for g in diff.removed_guides:
            print(f"   - {g}")

    if diff.changed_guides:
        print(f"\n⚠️  Changed APIs ({len(diff.changed_guides)}):")
        for g in diff.changed_guides:
            print(f"   [{g['html_name']}] {g['label']}")
            for f in g.get("added_params", []):
                print(f"       + param: {f}")
            for f in g.get("removed_params", []):
                print(f"       - param: {f}  ⚠️ BREAKING")
            for f in g.get("added_response", []):
                print(f"       + response: {f}")
            for f in g.get("removed_response", []):
                print(f"       - response: {f}  ⚠️ BREAKING")


def main() -> None:
    parser = argparse.ArgumentParser(description="Diff two spec directories")
    parser.add_argument("--old", required=True, help="Old specs directory")
    parser.add_argument("--new", required=True, help="New specs directory")
    parser.add_argument("--output-json", help="Write diff result as JSON to this file")
    args = parser.parse_args()

    old_dir = Path(args.old)
    new_dir = Path(args.new)

    diff = diff_specs(old_dir, new_dir)
    print_report(diff)

    if args.output_json:
        out = {
            "has_changes": diff.has_changes,
            "has_breaking": diff.has_breaking,
            "added_guides": diff.added_guides,
            "removed_guides": diff.removed_guides,
            "changed_guides": diff.changed_guides,
        }
        Path(args.output_json).write_text(
            json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    sys.exit(1 if diff.has_changes else 0)


if __name__ == "__main__":
    main()
