"""Verify bundled snapshots against generated Pydantic model aliases."""

from __future__ import annotations

from dataclasses import dataclass, field

from pydantic import BaseModel

from lawpy.kr.generated import _models_generated as generated_models
from lawpy.probe.snapshot import Snapshot, SnapshotStore

SNAPSHOT_MODEL_MAP: dict[str, str] = {
    "kr.law.search": "LawList",
    "kr.law.eflaw.search": "LawList",
    "kr.law.detail": "LawDetail",
    "kr.prec.search": "PrecList",
    "kr.prec.detail": "PrecDetail",
}


@dataclass
class VerifyResult:
    """Result of comparing one snapshot schema to one generated model."""

    name: str
    model: str | None
    snapshot_fields: list[str] = field(default_factory=list)
    model_aliases: list[str] = field(default_factory=list)
    missing_model_aliases: list[str] = field(default_factory=list)
    extra_model_aliases: list[str] = field(default_factory=list)
    error: str | None = None

    @property
    def is_clean(self) -> bool:
        """True when the generated model covers every snapshot field."""
        return not self.error and not self.missing_model_aliases

    def summary(self) -> str:
        """Return a human-readable one-line summary."""
        if self.error:
            return f"❌ {self.name}  {self.error}"
        if self.is_clean:
            return f"✅ {self.name}  snapshot fields covered by {self.model}"
        return (
            f"🚨 {self.name}  missing_model_aliases={self.missing_model_aliases} "
            f"extra_model_aliases={self.extra_model_aliases}"
        )

    def to_dict(self) -> dict[str, object]:
        """Return a stable JSON-serialisable representation."""
        return {
            "name": self.name,
            "model": self.model,
            "snapshot_fields": self.snapshot_fields,
            "model_aliases": self.model_aliases,
            "missing_model_aliases": self.missing_model_aliases,
            "extra_model_aliases": self.extra_model_aliases,
            "is_clean": self.is_clean,
            "error": self.error,
        }


def _snapshot_top_level_fields(snapshot: Snapshot) -> list[str]:
    fields = {path.split(".", 1)[0] for path in snapshot.schema}
    return sorted(fields)


def _model_aliases(model: type[BaseModel]) -> list[str]:
    aliases = {
        field.alias or name
        for name, field in model.model_fields.items()
    }
    return sorted(aliases)


def verify_snapshot(name: str) -> VerifyResult:
    """Verify one bundled snapshot against its configured generated model."""
    model_name = SNAPSHOT_MODEL_MAP.get(name)
    if model_name is None:
        return VerifyResult(name=name, model=None, error="no generated model mapping")

    snapshot = SnapshotStore.load(name)
    if snapshot is None:
        return VerifyResult(name=name, model=model_name, error="snapshot not found")

    model = getattr(generated_models, model_name, None)
    if model is None or not issubclass(model, BaseModel):
        return VerifyResult(name=name, model=model_name, error="generated model not found")

    snapshot_fields = _snapshot_top_level_fields(snapshot)
    aliases = _model_aliases(model)
    snapshot_set = set(snapshot_fields)
    alias_set = set(aliases)

    return VerifyResult(
        name=name,
        model=model_name,
        snapshot_fields=snapshot_fields,
        model_aliases=aliases,
        missing_model_aliases=sorted(snapshot_set - alias_set),
        extra_model_aliases=sorted(alias_set - snapshot_set),
    )


def verify_snapshots(names: list[str] | None = None) -> list[VerifyResult]:
    """Verify multiple bundled snapshots.

    When *names* is omitted, verify every known mapped snapshot in stable order.
    """
    targets = names or sorted(SNAPSHOT_MODEL_MAP)
    return [verify_snapshot(name) for name in targets]
