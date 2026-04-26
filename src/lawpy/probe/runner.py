"""ProbeRunner — orchestrates API calls, schema extraction, and snapshot management."""

from __future__ import annotations

import os
from dataclasses import dataclass

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

        # Navigate to the representative object
        target = navigate(data, config.schema_path)
        if target is None:
            # Fall back to full response schema
            target = data

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
