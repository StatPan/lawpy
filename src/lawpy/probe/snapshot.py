"""Snapshot persistence for captured API schemas.

Snapshots are stored as JSON files under ``src/lawpy/snapshots/``.
They are **shipped with the pip package** and accessed via
``importlib.resources`` so they work after installation too.

File naming: ``{name}.json``  (e.g. ``kr.prec.search.json``)
"""

from __future__ import annotations

import importlib.resources
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import lawpy.snapshots as _snapshots_pkg
from lawpy.probe.schema import FieldSpec

# Directory where snapshots are written by `probe capture`
# (relative to the package source tree)
_SNAPSHOTS_PKG_PATH = Path(__file__).parent.parent / "snapshots"


@dataclass
class Snapshot:
    """A captured API response schema, persisted as JSON."""

    name: str
    """Unique probe name, e.g. 'kr.prec.search'."""

    endpoint: str
    """The URL that was called."""

    params: dict[str, Any]
    """The query parameters used (OC key is redacted)."""

    schema_path: str
    """Dot-path into the parsed response to the root object, e.g. 'PrecSearch.prec'."""

    schema: dict[str, FieldSpec]
    """Extracted field schema."""

    captured_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    lawpy_version: str = "unknown"

    # ------------------------------------------------------------------ #

    def to_dict(self) -> dict[str, Any]:
        safe_params = {k: v for k, v in self.params.items() if k.upper() != "OC"}
        return {
            "name": self.name,
            "lawpy_version": self.lawpy_version,
            "captured_at": self.captured_at,
            "endpoint": self.endpoint,
            "params": safe_params,
            "schema_path": self.schema_path,
            "schema": {k: v.to_dict() for k, v in self.schema.items()},
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Snapshot:
        return cls(
            name=d["name"],
            endpoint=d["endpoint"],
            params=d.get("params", {}),
            schema_path=d.get("schema_path", ""),
            schema={k: FieldSpec.from_dict(v) for k, v in d.get("schema", {}).items()},
            captured_at=d.get("captured_at", ""),
            lawpy_version=d.get("lawpy_version", "unknown"),
        )


class SnapshotStore:
    """Read/write snapshots from the bundled ``lawpy/snapshots/`` directory."""

    # ------------------------------------------------------------------
    # Write (capture)
    # ------------------------------------------------------------------

    @staticmethod
    def save(snapshot: Snapshot) -> Path:
        """Persist *snapshot* to the package source tree.

        This is only used by ``probe capture`` during development.
        The file is committed to git and shipped with the pip package.

        Returns:
            Path to the written file.
        """
        _SNAPSHOTS_PKG_PATH.mkdir(parents=True, exist_ok=True)
        path = _SNAPSHOTS_PKG_PATH / f"{snapshot.name}.json"
        path.write_text(
            json.dumps(snapshot.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return path

    # ------------------------------------------------------------------
    # Read (diff / runtime check)
    # ------------------------------------------------------------------

    @staticmethod
    def load(name: str) -> Snapshot | None:
        """Load a bundled snapshot by *name*.

        Works both from source tree and from an installed wheel
        (via ``importlib.resources``).

        Returns:
            :class:`Snapshot` or ``None`` if not found.
        """
        filename = f"{name}.json"

        # 1. Try importlib.resources (works after pip install)
        try:
            ref = importlib.resources.files(_snapshots_pkg).joinpath(filename)
            text = ref.read_text(encoding="utf-8")
            return Snapshot.from_dict(json.loads(text))
        except (FileNotFoundError, TypeError, AttributeError):
            pass

        # 2. Fallback: direct path (source tree)
        path = _SNAPSHOTS_PKG_PATH / filename
        if path.exists():
            return Snapshot.from_dict(json.loads(path.read_text(encoding="utf-8")))

        return None

    @staticmethod
    def exists(name: str) -> bool:
        """Return True if a snapshot for *name* exists."""
        return SnapshotStore.load(name) is not None

    @staticmethod
    def list_names() -> list[str]:
        """Return all snapshot names available in the bundle."""
        names: list[str] = []

        # importlib.resources
        try:
            pkg = importlib.resources.files(_snapshots_pkg)
            for item in pkg.iterdir():
                n = getattr(item, "name", "")
                if n.endswith(".json"):
                    names.append(n[: -len(".json")])
            if names:
                return sorted(names)
        except Exception:
            pass

        # Fallback: filesystem
        if _SNAPSHOTS_PKG_PATH.exists():
            names = [p.stem for p in _SNAPSHOTS_PKG_PATH.glob("*.json")]
        return sorted(names)
