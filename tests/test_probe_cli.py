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
