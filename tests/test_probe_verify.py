"""Tests for snapshot-to-generated-model verification."""

from __future__ import annotations

from pydantic import BaseModel, Field

from lawpy.probe import verify
from lawpy.probe.schema import FieldSpec
from lawpy.probe.snapshot import Snapshot


class FakeModel(BaseModel):
    model_config = {"populate_by_name": True}

    사건명: str | None = Field(None, alias="사건명")
    사건번호: str | None = Field(None, alias="사건번호")
    extra: str | None = Field(None, alias="generated_only")


def _snapshot() -> Snapshot:
    return Snapshot(
        name="sample",
        endpoint="https://example.test",
        params={},
        schema_path="Sample.root",
        schema={
            "사건명": FieldSpec(type="str"),
            "사건번호": FieldSpec(type="str"),
            "중첩.하위필드": FieldSpec(type="str"),
        },
    )


def test_verify_snapshot_compares_snapshot_top_level_fields_to_model_aliases(monkeypatch):
    monkeypatch.setitem(verify.SNAPSHOT_MODEL_MAP, "sample", "FakeModel")
    monkeypatch.setattr(verify.SnapshotStore, "load", lambda name: _snapshot())
    monkeypatch.setattr(verify.generated_models, "FakeModel", FakeModel, raising=False)

    result = verify.verify_snapshot("sample")

    assert result.model == "FakeModel"
    assert result.snapshot_fields == ["사건명", "사건번호", "중첩"]
    assert result.missing_model_aliases == ["중첩"]
    assert result.extra_model_aliases == ["generated_only"]
    assert not result.is_clean


def test_verify_snapshot_reports_missing_mapping() -> None:
    result = verify.verify_snapshot("unknown")

    assert result.error == "no generated model mapping"
    assert not result.is_clean
