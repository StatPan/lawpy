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


def test_get_runner_falls_back_to_generic_api_key_env(monkeypatch):
    created = {}

    class FakeRunner:
        def __init__(self, api_key: str) -> None:
            created["api_key"] = api_key

    monkeypatch.delenv("LAWPY_KR_API_KEY", raising=False)
    monkeypatch.setenv("LAWPY_API_KEY", "generic-secret")
    monkeypatch.setattr(cli, "ProbeRunner", FakeRunner)

    runner = cli._get_runner(None)

    assert isinstance(runner, FakeRunner)
    assert created["api_key"] == "generic-secret"


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


def test_cmd_capture_json_stdout_is_valid_json(monkeypatch, capsys):
    class FakeCapture:
        saved_to = "/tmp/sample.json"

    class FakeRunner:
        def capture(self, name: str) -> FakeCapture:
            assert name == "sample"
            return FakeCapture()

        def close(self) -> None:
            pass

    monkeypatch.setattr(cli, "_get_runner", lambda api_key: FakeRunner())
    monkeypatch.setattr(cli, "CONFIGS_BY_NAME", {"sample": object()})

    exit_code = cli.cmd_capture(["sample"], api_key="secret", output_json=True)

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.startswith("[\n")
    assert "Capturing sample" not in captured.out
    assert "Capturing sample" in captured.err


def test_cmd_verify_json_stdout_is_valid_json(monkeypatch, capsys):
    from lawpy.probe.verify import VerifyResult

    result = VerifyResult(
        name="sample",
        model="SampleModel",
        snapshot_fields=["사건명"],
        model_aliases=["사건명"],
    )

    monkeypatch.setattr(cli, "SNAPSHOT_MODEL_MAP", {"sample": "SampleModel"})
    monkeypatch.setattr(cli, "verify_snapshots", lambda names: [result])

    exit_code = cli.cmd_verify(["sample"], output_json=True)

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.startswith("[\n")
    assert "snapshot fields covered" not in captured.out
    assert "snapshot fields covered" in captured.err


def test_main_accepts_verify_output_after_subcommand(monkeypatch, capsys):
    from lawpy.probe.verify import VerifyResult

    result = VerifyResult(name="sample", model="SampleModel")

    monkeypatch.setattr(cli, "SNAPSHOT_MODEL_MAP", {"sample": "SampleModel"})
    monkeypatch.setattr(cli, "verify_snapshots", lambda names: [result])

    try:
        cli.main(["verify", "--target", "sample", "--output", "json"])
    except SystemExit as exc:
        assert exc.code == 0

    captured = capsys.readouterr()
    assert captured.out.startswith("[\n")


def test_main_accepts_capture_api_key_after_subcommand(monkeypatch, capsys):
    captured_args = {}

    def fake_capture(names, api_key, output_json):
        captured_args["names"] = names
        captured_args["api_key"] = api_key
        captured_args["output_json"] = output_json
        return 0

    monkeypatch.setattr(cli, "cmd_capture", fake_capture)

    try:
        cli.main(["capture", "--target", "sample", "--api-key", "secret", "--output", "json"])
    except SystemExit as exc:
        assert exc.code == 0

    assert captured_args == {
        "names": ["sample"],
        "api_key": "secret",
        "output_json": True,
    }
    assert capsys.readouterr().out == ""
