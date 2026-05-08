"""Regression tests for the API drift GitHub Actions workflow."""

from __future__ import annotations

from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "api-drift.yml"


def test_probe_diff_json_output_option_precedes_subcommand() -> None:
    workflow = WORKFLOW.read_text()

    assert "uv run lawpy-probe --output json diff --all > /tmp/probe_drift.json" in workflow
    assert "uv run lawpy-probe diff --all --output json > /tmp/probe_drift.json" not in workflow


def test_probe_verify_json_report_is_uploaded() -> None:
    workflow = WORKFLOW.read_text()

    assert "uv run lawpy-probe verify --all --output json > /tmp/probe_verify.json" in workflow
    assert "snapshot_verify_failed: ${{ steps.probe-verify.outputs.failed }}" in workflow
    assert 'echo "failed=true" >> $GITHUB_OUTPUT' in workflow
    assert "/tmp/probe_verify.json" in workflow


def test_notify_drift_tolerates_empty_probe_report() -> None:
    workflow = WORKFLOW.read_text()

    assert "const raw = fs.readFileSync('/tmp/probe_drift.json', 'utf8').trim();" in workflow
    assert "if (raw) parsed = JSON.parse(raw);" in workflow
    assert "JSON.parse(probe)" not in workflow


def test_probe_diff_only_marks_drift_for_breaking_changes() -> None:
    workflow = WORKFLOW.read_text()

    assert "const hasBreaking = rows.some((row) => row && row.has_breaking_changes === true);" in workflow
    assert "fs.appendFileSync(output, `drift=${hasBreaking}\\n`);" in workflow
    assert "uv run lawpy-probe --output json diff --all > /tmp/probe_drift.json" in workflow
    assert "|| echo \"drift=true\"" not in workflow


def test_probe_diff_reports_probe_failures_separately() -> None:
    workflow = WORKFLOW.read_text()

    assert "probe_failed: ${{ steps.probe-diff.outputs.probe_failed }}" in workflow
    assert "const hasProbeError = rows.some((row) => row && (row.status === 'error' || row.error));" in workflow
    assert "const probeFailed = parseFailed || hasProbeError || (probeExit !== 0 && !hasBreaking);" in workflow
    assert "fs.appendFileSync(output, `probe_failed=${probeFailed}\\n`);" in workflow


def test_detection_infrastructure_failures_use_separate_health_gate() -> None:
    workflow = WORKFLOW.read_text()

    assert "detection-health:" in workflow
    assert "needs: spec-check" in workflow
    assert "needs.spec-check.outputs.snapshot_verify_failed == 'true'" in workflow
    assert "needs.spec-check.outputs.probe_failed == 'true'" in workflow
    assert "name: Detection health gate" in workflow
    assert "Live API probe failed before a breaking drift decision" in workflow


def test_downstream_jobs_can_still_use_spec_check_outputs() -> None:
    workflow = WORKFLOW.read_text()

    assert "update-and-pr:" in workflow
    assert "if: needs.spec-check.outputs.spec_changed == 'true' || github.event.inputs.force_rescrape == 'true'" in workflow
    assert "notify-drift:" in workflow
    assert "if: needs.spec-check.outputs.drift_detected == 'true'" in workflow
    assert "name: Fail on detection infrastructure errors" not in workflow
    assert "if: always()" in workflow
