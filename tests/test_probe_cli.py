"""Tests for the lawpy-probe CLI."""

from __future__ import annotations

from lawpy.probe import cli


def test_get_runner_accepts_kr_api_key_env(monkeypatch):
    created = {}

    class FakeRunner:
        def __init__(self, api_key: str) -> None:
            created["api_key"] = api_key

    monkeypatch.delenv("LAWPY_API_KEY", raising=False)
    monkeypatch.setenv("LAWPY_KR_API_KEY", "kr-secret")
    monkeypatch.setattr(cli, "ProbeRunner", FakeRunner)

    runner = cli._get_runner(None)

    assert isinstance(runner, FakeRunner)
    assert created["api_key"] == "kr-secret"


def test_get_runner_prefers_explicit_api_key(monkeypatch):
    created = {}

    class FakeRunner:
        def __init__(self, api_key: str) -> None:
            created["api_key"] = api_key

    monkeypatch.setenv("LAWPY_KR_API_KEY", "kr-secret")
    monkeypatch.setenv("LAWPY_API_KEY", "generic-secret")
    monkeypatch.setattr(cli, "ProbeRunner", FakeRunner)

    runner = cli._get_runner("explicit-secret")

    assert isinstance(runner, FakeRunner)
    assert created["api_key"] == "explicit-secret"


def test_cmd_diff_json_stdout_is_valid_json(monkeypatch, capsys):
    from lawpy.probe.differ import DiffResult

    class FakeRun:
        diff = DiffResult(name="sample")

    class FakeRunner:
        def diff(self, name: str) -> FakeRun:
            assert name == "sample"
            return FakeRun()

        def close(self) -> None:
            pass

    monkeypatch.setattr(cli, "_get_runner", lambda api_key: FakeRunner())
    monkeypatch.setattr(cli, "CONFIGS_BY_NAME", {"sample": object()})

    exit_code = cli.cmd_diff(["sample"], api_key="secret", output_json=True)

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.startswith("[\n")
    assert "Checking sample" not in captured.out
