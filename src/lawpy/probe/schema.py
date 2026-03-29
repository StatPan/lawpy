"""Schema extraction from API responses.

Converts a parsed XML/JSON dict (from xmltodict or json.loads) into a flat
*schema* mapping of ``field_path -> FieldSpec``.  This schema is what we
store in snapshots and diff against future responses.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class FieldSpec:
    """Metadata for a single field observed in an API response."""

    type: str
    """Python type name: 'str', 'int', 'float', 'bool', 'dict', 'list', 'NoneType'."""

    sample: str | None = None
    """A short sample value (truncated to 120 chars) for human reference."""

    nullable: bool = False
    """True if we have ever seen this field be None/null."""

    def to_dict(self) -> dict[str, Any]:
        return {"type": self.type, "sample": self.sample, "nullable": self.nullable}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "FieldSpec":
        return cls(type=d["type"], sample=d.get("sample"), nullable=d.get("nullable", False))


def _type_name(value: Any) -> str:
    if value is None:
        return "NoneType"
    return type(value).__name__


def _sample(value: Any, max_len: int = 120) -> str | None:
    if value is None:
        return None
    s = str(value)
    return s[:max_len] + "…" if len(s) > max_len else s


def extract_schema(
    data: Any,
    *,
    prefix: str = "",
    max_depth: int = 6,
    _depth: int = 0,
) -> dict[str, FieldSpec]:
    """Recursively extract a flat field schema from a parsed response dict.

    Args:
        data: Parsed response value (dict, list, scalar, or None).
        prefix: Dot-separated key prefix for nested fields.
        max_depth: Maximum recursion depth (prevents runaway on deeply nested XML).
        _depth: Internal recursion counter.

    Returns:
        Dict mapping dotted field paths to :class:`FieldSpec`.

    Example::

        >>> extract_schema({"PrecSearch": {"prec": {"사건명": "손해배상"}}})
        {"PrecSearch.prec.사건명": FieldSpec(type="str", sample="손해배상")}
    """
    schema: dict[str, FieldSpec] = {}

    if _depth >= max_depth:
        return schema

    if isinstance(data, dict):
        for key, value in data.items():
            child_prefix = f"{prefix}.{key}" if prefix else key

            if isinstance(value, dict):
                # Recurse into nested dict
                schema[child_prefix] = FieldSpec(type="dict", sample=None)
                schema.update(
                    extract_schema(value, prefix=child_prefix, max_depth=max_depth, _depth=_depth + 1)
                )
            elif isinstance(value, list):
                schema[child_prefix] = FieldSpec(type="list", sample=f"[{len(value)} items]")
                # Use the first element as the representative schema
                if value:
                    schema.update(
                        extract_schema(
                            value[0],
                            prefix=child_prefix + "[]",
                            max_depth=max_depth,
                            _depth=_depth + 1,
                        )
                    )
            elif value is None:
                schema[child_prefix] = FieldSpec(type="NoneType", sample=None, nullable=True)
            else:
                schema[child_prefix] = FieldSpec(
                    type=_type_name(value),
                    sample=_sample(value),
                    nullable=False,
                )

    elif isinstance(data, list):
        # Top-level list — use first element
        if data:
            schema.update(
                extract_schema(data[0], prefix=prefix, max_depth=max_depth, _depth=_depth + 1)
            )

    elif data is not None:
        schema[prefix] = FieldSpec(type=_type_name(data), sample=_sample(data))

    return schema


def navigate(data: Any, path: str) -> Any:
    """Retrieve a nested value from *data* using a dot-separated *path*.

    Returns ``None`` if any intermediate key is missing.

    Example::

        >>> navigate({"PrecSearch": {"prec": {"사건명": "X"}}}, "PrecSearch.prec")
        {"사건명": "X"}
    """
    parts = path.split(".")
    current = data
    for part in parts:
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current
