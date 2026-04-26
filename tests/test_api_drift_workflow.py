"""Regression tests for the API drift GitHub Actions workflow."""

from __future__ import annotations

from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "api-drift.yml"


def test_probe_diff_json_output_option_precedes_subcommand() -> None:
    workflow = WORKFLOW.read_text()

    assert "uv run lawpy-probe --output json diff --all > /tmp/probe_drift.json" in workflow
    assert "uv run lawpy-probe diff --all --output json > /tmp/probe_drift.json" not in workflow


def test_notify_drift_tolerates_empty_probe_report() -> None:
    workflow = WORKFLOW.read_text()

    assert "const raw = fs.readFileSync('/tmp/probe_drift.json', 'utf8').trim();" in workflow
    assert "if (raw) parsed = JSON.parse(raw);" in workflow
    assert "JSON.parse(probe)" not in workflow
