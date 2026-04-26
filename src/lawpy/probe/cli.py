"""lawpy-probe CLI — capture and diff API response schemas."""

from __future__ import annotations

import json
import os
import sys

from lawpy.probe.configs.kr import ALL_CONFIGS, CONFIGS_BY_NAME
from lawpy.probe.runner import ProbeRunner
from lawpy.probe.snapshot import SnapshotStore


def _get_runner(api_key: str | None) -> ProbeRunner:
    key = api_key or os.environ.get("LAWPY_KR_API_KEY") or os.environ.get("LAWPY_API_KEY")
    if not key:
        print(
            "Error: API key required. Set LAWPY_KR_API_KEY or LAWPY_API_KEY env var, or use --api-key.",
            file=sys.stderr,
        )
        sys.exit(1)
    return ProbeRunner(api_key=key)


def cmd_list() -> None:
    """lawpy-probe list — show all registered probes."""
    print(f"{'NAME':<30} {'DESCRIPTION'}")
    print("-" * 70)
    for c in ALL_CONFIGS:
        has_snap = "✅" if SnapshotStore.exists(c.name) else "  "
        print(f"{has_snap} {c.name:<28} {c.description}")


def cmd_show(name: str | None) -> None:
    """lawpy-probe show [--target NAME] — print bundled snapshot."""
    names = [name] if name else SnapshotStore.list_names()
    for n in names:
        snap = SnapshotStore.load(n)
        if snap is None:
            print(f"No snapshot found for '{n}'", file=sys.stderr)
            continue
        print(f"\n=== {snap.name}  (captured {snap.captured_at}) ===")
        for path, spec in snap.schema.items():
            nullable = " [nullable]" if spec.nullable else ""
            sample = f"  e.g. {spec.sample!r}" if spec.sample else ""
            print(f"  {path:<50} {spec.type}{nullable}{sample}")


def cmd_capture(names: list[str] | None, api_key: str | None, output_json: bool) -> int:
    """lawpy-probe capture — fetch live API and save snapshots."""
    runner = _get_runner(api_key)
    targets = names or [c.name for c in ALL_CONFIGS]
    results = []
    exit_code = 0

    try:
        for n in targets:
            if n not in CONFIGS_BY_NAME:
                print(f"  ❌ Unknown probe: {n}", file=sys.stderr)
                exit_code = 1
                continue
            print(f"  Capturing {n}...", end=" ", flush=True)
            try:
                result = runner.capture(n)
                results.append({"name": n, "saved_to": result.saved_to, "status": "ok"})
                print(f"✅  saved → {result.saved_to}")
            except Exception as e:
                results.append({"name": n, "error": str(e), "status": "error"})
                print(f"❌  {e}")
                exit_code = 1
    finally:
        runner.close()

    if output_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))

    return exit_code


def cmd_diff(names: list[str] | None, api_key: str | None, output_json: bool) -> int:
    """lawpy-probe diff — compare live API against bundled snapshots."""
    runner = _get_runner(api_key)
    targets = names or [c.name for c in ALL_CONFIGS]
    results = []
    exit_code = 0

    try:
        for n in targets:
            if n not in CONFIGS_BY_NAME:
                print(f"  ❌ Unknown probe: {n}", file=sys.stderr)
                exit_code = 1
                continue
            progress_stream = sys.stderr if output_json else sys.stdout
            print(f"  Checking {n}...", end=" ", flush=True, file=progress_stream)
            try:
                run = runner.diff(n)
                summary = run.diff.summary()
                print(summary, file=progress_stream)
                results.append(run.diff.to_dict())
                if run.diff.has_breaking_changes:
                    exit_code = 1
            except Exception as e:
                print(f"❌  {e}", file=progress_stream)
                results.append({"name": n, "error": str(e), "status": "error"})
                exit_code = 1
    finally:
        runner.close()

    if output_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))

    return exit_code


def main(argv: list[str] | None = None) -> None:
    """Entry point for the ``lawpy-probe`` CLI."""
    import argparse

    parser = argparse.ArgumentParser(
        prog="lawpy-probe",
        description="lawpy API schema capture and drift detection",
    )
    parser.add_argument(
        "--api-key",
        metavar="KEY",
        default=None,
        help="OC API key (default: LAWPY_API_KEY env var)",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # list
    sub.add_parser("list", help="Show all registered probes")

    # show
    p_show = sub.add_parser("show", help="Print bundled snapshot fields")
    p_show.add_argument("--target", metavar="NAME", help="Probe name (default: all)")

    # capture
    p_cap = sub.add_parser("capture", help="Fetch live API and save snapshots")
    p_cap.add_argument(
        "--target", metavar="NAME", action="append", help="Probe name (repeatable; default: all)"
    )
    p_cap.add_argument("--all", action="store_true", help="Capture all probes (default when no --target)")

    # diff
    p_diff = sub.add_parser("diff", help="Compare live API against bundled snapshots")
    p_diff.add_argument(
        "--target", metavar="NAME", action="append", help="Probe name (repeatable; default: all)"
    )
    p_diff.add_argument("--all", action="store_true", help="Diff all probes (default when no --target)")

    args = parser.parse_args(argv)
    output_json = args.output == "json"

    if args.command == "list":
        cmd_list()
        sys.exit(0)

    elif args.command == "show":
        cmd_show(getattr(args, "target", None))
        sys.exit(0)

    elif args.command == "capture":
        sys.exit(cmd_capture(args.target, args.api_key, output_json))

    elif args.command == "diff":
        sys.exit(cmd_diff(args.target, args.api_key, output_json))


if __name__ == "__main__":
    main()
