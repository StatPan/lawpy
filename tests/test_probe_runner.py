"""Tests for probe runner snapshot safety."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock

import pytest

from lawpy.probe.configs.kr import ProbeConfig
from lawpy.probe.runner import ProbeResponseError, ProbeRunner
from lawpy.probe.snapshot import SnapshotStore


def _runner_with_payload(payload: dict) -> ProbeRunner:
    response = Mock()
    response.json.return_value = payload
    response.raise_for_status.return_value = None

    runner = ProbeRunner(api_key="test_key")
    runner._http = Mock()
    runner._http.get.return_value = response
    return runner


def _config() -> ProbeConfig:
    return ProbeConfig(
        name="sample",
        url="https://example.test",
        fixed_params={"target": "law", "type": "JSON"},
        schema_path="LawSearch.law",
    )


def test_fetch_schema_rejects_missing_schema_path() -> None:
    runner = _runner_with_payload({"unexpected": {"law": {"사건명": "x"}}})

    with pytest.raises(ProbeResponseError, match="schema_path 'LawSearch.law' not found"):
        runner._fetch_schema(_config())


def test_fetch_schema_rejects_api_error_payload() -> None:
    runner = _runner_with_payload({"result": "fail", "msg": "사용자 검증 실패"})

    with pytest.raises(ProbeResponseError, match="사용자 검증 실패"):
        runner._fetch_schema(_config())


def test_fetch_schema_allows_success_result_metadata() -> None:
    runner = _runner_with_payload(
        {
            "LawSearch": {"law": {"사건명": "x"}},
            "result": "success",
            "msg": "정상",
        }
    )

    schema, _snapshot = runner._fetch_schema(_config())

    assert schema["사건명"].sample == "x"


def test_capture_does_not_save_snapshot_when_payload_is_invalid(monkeypatch) -> None:
    runner = _runner_with_payload({"result": "fail", "msg": "사용자 검증 실패"})
    save = Mock(return_value=Path("/tmp/sample.json"))

    monkeypatch.setattr("lawpy.probe.runner.CONFIGS_BY_NAME", {"sample": _config()})
    monkeypatch.setattr(SnapshotStore, "save", save)

    with pytest.raises(ProbeResponseError):
        runner.capture("sample")

    save.assert_not_called()
