"""ProbeRunner — orchestrates API calls, schema extraction, and snapshot management."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import httpx

from lawpy.probe.configs.kr import ALL_CONFIGS, CONFIGS_BY_NAME, ProbeConfig
from lawpy.probe.differ import DiffResult, SchemaDiffer
from lawpy.probe.schema import FieldSpec, extract_schema, navigate
from lawpy.probe.snapshot import Snapshot, SnapshotStore

try:
    from lawpy import __version__ as _lawpy_version
except Exception:
    _lawpy_version = "unknown"


@dataclass
class CaptureResult:
    """Result of a single probe capture run."""

    config: ProbeConfig
    snapshot: Snapshot
    saved_to: str


@dataclass
class ProbeRunResult:
    """Result of a single probe diff run."""

    config: ProbeConfig
    snapshot: Snapshot | None  # baseline (bundled)
    current_schema: dict[str, FieldSpec]
    diff: DiffResult


class ProbeResponseError(RuntimeError):
    """Raised when a probe response is not a valid schema capture payload."""


class ProbeRunner:
    """Orchestrates probe captures and diffs for all registered configs.

    Args:
        api_key: OC parameter for the law API.  Reads ``LAWPY_API_KEY``
            env var if not supplied.
        timeout: HTTP request timeout in seconds.
    """

    def __init__(self, api_key: str | None = None, timeout: int = 30) -> None:
        self.api_key = (
            api_key
            or os.environ.get("LAWPY_KR_API_KEY")
            or os.environ.get("LAWPY_API_KEY")  # backwards compat
        )
        if not self.api_key:
            raise ValueError(
                "api_key must be provided or set LAWPY_KR_API_KEY environment variable"
            )
        self._http = httpx.Client(timeout=timeout)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> ProbeRunner:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    # ------------------------------------------------------------------ #
    # Capture                                                              #
    # ------------------------------------------------------------------ #

    def capture(self, name: str) -> CaptureResult:
        """Call the API for *name* and save the schema snapshot.

        Args:
            name: Probe name registered in ``CONFIGS_BY_NAME``.

        Returns:
            :class:`CaptureResult`.

        Raises:
            KeyError: If *name* is not registered.
            httpx.HTTPError: If the request fails.
        """
        config = CONFIGS_BY_NAME[name]
        schema, snapshot = self._fetch_schema(config)
        path = SnapshotStore.save(snapshot)
        return CaptureResult(config=config, snapshot=snapshot, saved_to=str(path))

    def capture_all(self) -> list[CaptureResult]:
        """Capture snapshots for every registered probe config."""
        return [self.capture(c.name) for c in ALL_CONFIGS]

    # ------------------------------------------------------------------ #
    # Diff                                                                 #
    # ------------------------------------------------------------------ #

    def diff(self, name: str) -> ProbeRunResult:
        """Compare current API response schema against the bundled snapshot.

        Args:
            name: Probe name.

        Returns:
            :class:`ProbeRunResult` with diff details.
        """
        config = CONFIGS_BY_NAME[name]
        current_schema, snapshot_live = self._fetch_schema(config)

        baseline = SnapshotStore.load(name)
        baseline_schema = baseline.schema if baseline else {}

        diff_result = SchemaDiffer.diff(name, baseline_schema, current_schema)

        return ProbeRunResult(
            config=config,
            snapshot=baseline,
            current_schema=current_schema,
            diff=diff_result,
        )

    def diff_all(self) -> list[ProbeRunResult]:
        """Diff every registered probe config."""
        return [self.diff(c.name) for c in ALL_CONFIGS]

    # ------------------------------------------------------------------ #
    # Internal                                                             #
    # ------------------------------------------------------------------ #

    def _fetch_schema(self, config: ProbeConfig) -> tuple[dict[str, FieldSpec], Snapshot]:
        """Fetch the API and return (extracted schema, Snapshot(not yet saved))."""
        params: dict[str, str | int] = dict(config.fixed_params)
        params["OC"] = self.api_key  # type: ignore[assignment]

        response = self._http.get(config.url, params=params)
        response.raise_for_status()

        data = response.json()
        self._raise_if_api_error(data, config)

        # Navigate to the representative object
        target = navigate(data, config.schema_path)
        if target is None:
            msg = (
                f"schema_path {config.schema_path!r} not found in response for "
                f"{config.name}; refusing to save snapshot"
            )
            raise ProbeResponseError(msg)

        schema = extract_schema(target)

        snapshot = Snapshot(
            name=config.name,
            endpoint=config.url,
            params=params,
            schema_path=config.schema_path,
            schema=schema,
            lawpy_version=_lawpy_version,
        )
        return schema, snapshot

    @staticmethod
    def _raise_if_api_error(data: Any, config: ProbeConfig) -> None:
        """Reject known law.go.kr error payload shapes before snapshot extraction."""
        if not isinstance(data, dict):
            return

        error_msg = _find_error_message(data)
        if error_msg is None:
            return

        msg = f"API error response for {config.name}: {error_msg}"
        raise ProbeResponseError(msg)


def _find_error_message(data: Any) -> str | None:
    if not isinstance(data, dict):
        return None

    lower_keys = {str(key).lower(): key for key in data}
    result_key = lower_keys.get("result")
    msg_key = lower_keys.get("msg")
    if result_key is not None and msg_key is not None:
        result = data[result_key]
        if _is_error_result(result):
            return str(data[msg_key])

    code_key = lower_keys.get("resultcode")
    message_key = lower_keys.get("resultmsg")
    if code_key is not None and message_key is not None:
        code = data[code_key]
        if code not in (None, "", "00", "0", 0):
            return str(data[message_key])

    for value in data.values():
        nested = _find_error_message(value)
        if nested is not None:
            return nested
    return None


def _is_error_result(value: Any) -> bool:
    if value is None:
        return False
    normalized = str(value).strip().lower()
    if normalized in {"", "0", "00", "ok", "success", "true"}:
        return False
    return normalized in {"fail", "failed", "failure", "error", "false", "n", "no"} or not normalized.isdigit()
