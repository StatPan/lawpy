"""Schema diff between two captured snapshots."""

from __future__ import annotations

from dataclasses import dataclass, field

from lawpy.probe.schema import FieldSpec


@dataclass
class DiffResult:
    """Result of comparing a baseline snapshot schema against a current schema."""

    name: str

    added_fields: list[str] = field(default_factory=list)
    """Fields present in current response but absent from snapshot.
    Safe (new API capability) but worth noting for parser extension."""

    removed_fields: list[str] = field(default_factory=list)
    """Fields absent from current response but expected by snapshot.
    ⚠️ HIGH RISK — existing parser code may break."""

    type_changed: dict[str, tuple[str, str]] = field(default_factory=dict)
    """Fields whose type changed: {path: (old_type, new_type)}.
    ⚠️ May silently corrupt parsed models."""

    @property
    def has_breaking_changes(self) -> bool:
        """True if any removed or type-changed fields were detected."""
        return bool(self.removed_fields or self.type_changed)

    @property
    def is_clean(self) -> bool:
        """True when no differences at all."""
        return not (self.added_fields or self.removed_fields or self.type_changed)

    def summary(self) -> str:
        """Return a human-readable one-line summary."""
        if self.is_clean:
            return f"✅ {self.name}  No changes"
        parts = []
        if self.removed_fields:
            parts.append(f"removed={self.removed_fields}")
        if self.added_fields:
            parts.append(f"added={self.added_fields}")
        if self.type_changed:
            parts.append(f"type_changed={list(self.type_changed.keys())}")
        icon = "🚨" if self.has_breaking_changes else "⚠️ "
        return f"{icon} {self.name}  {', '.join(parts)}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "added_fields": self.added_fields,
            "removed_fields": self.removed_fields,
            "type_changed": {k: list(v) for k, v in self.type_changed.items()},
            "has_breaking_changes": self.has_breaking_changes,
        }


class SchemaDiffer:
    """Compare two field-schema dicts and produce a :class:`DiffResult`."""

    @staticmethod
    def diff(
        name: str,
        baseline: dict[str, FieldSpec],
        current: dict[str, FieldSpec],
    ) -> DiffResult:
        """Compare *baseline* (stored snapshot) against *current* (live response).

        Args:
            name: Probe name for identification.
            baseline: Schema dict from the stored snapshot.
            current: Schema dict extracted from the latest API response.

        Returns:
            :class:`DiffResult` with categorised differences.
        """
        result = DiffResult(name=name)

        baseline_keys = set(baseline.keys())
        current_keys = set(current.keys())

        result.added_fields = sorted(current_keys - baseline_keys)
        result.removed_fields = sorted(baseline_keys - current_keys)

        for key in baseline_keys & current_keys:
            old_type = baseline[key].type
            new_type = current[key].type
            # Ignore NoneType transitions (nullable drift is expected)
            if old_type != new_type and "NoneType" not in (old_type, new_type):
                result.type_changed[key] = (old_type, new_type)

        return result
