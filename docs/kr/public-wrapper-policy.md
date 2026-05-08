# KR Generated Client to Public Wrapper Policy

This policy defines how KR generated clients graduate into the public wrapper
surface used by `KRClient` and downstream consumers such as `datapan-data`.

## Naming Conventions

- `KRClient` is the integrated public entry point for Korean APIs. New user
  workflows should target `KRClient` first.
- `KoreanLawClient` is a compatibility alias for existing callers. Do not use
  it as the name for new documentation, examples, or category policy.
- Category mixins are public wrapper classes named for the user-facing category:
  `LawClient`, `PrecedentClient`, `AdministrativeRuleClient`,
  `OrdinanceClient`, and future names such as `TreatyClient`.
- `KRClient` composes category mixins by inheritance. A category is part of the
  integrated public surface only after its mixin is included in `KRClient`.
- Generated clients live under `lawpy.kr.generated.<target>` and are named
  `Generated<Target>Client`, for example `GeneratedDeccClient` for `decc`.
  They preserve law.go.kr target and parameter names closely, including awkward
  generated method names such as `search_deccs` and `get_decc_detail`.

## When Generated Clients Are Acceptable

Direct generated client use is acceptable when:

- the target is low-level, narrow, or not yet common enough to justify a public
  category workflow;
- the generated method names and parameters are already clear to a caller who
  knows the law.go.kr API target;
- the target is mainly needed for coverage, parity checks, API drift detection,
  or exploratory data acquisition;
- downstream code is intentionally preserving raw law.go.kr semantics, including
  target names, aliases, and generated Pydantic models.

Generated-only targets must still have generated tests and coverage tracking.
They are not undocumented or private; they are simply not the ergonomic public
surface.

## When Public Wrappers Are Required

Add an ergonomic public wrapper when a category is expected to be used directly
by application code, notebooks, AI agents, or `datapan-data` ingestion flows.
This is required when any of the following are true:

- the target represents a recognizable legal research category rather than an
  implementation detail;
- callers need stable, readable method names instead of generated target names;
- the generated parameter names need user-facing names, defaults, or grouping;
- the category should appear on `KRClient`;
- `datapan-data` or another downstream package needs a durable public contract;
- examples, tutorials, or issue descriptions naturally describe the category in
  product terms rather than law.go.kr target terms.

Public wrappers may inherit from one or more generated clients. Keep wrapper
logic thin: translate ergonomic parameters, set sensible defaults, call the
generated method, and return the generated models unless a stronger public model
contract is explicitly needed.

## Wrapper Method Shape

Use three method shapes consistently:

- `search_<category_plural>(...)`: keyword search or filtered search over a
  category. Return a list.
- `get_<category>_list(...)`: list endpoints that are not primarily keyword
  search, such as current law lists or history lists. Return a list.
- `get_<category>_detail(...)`: detail or full-text endpoints. Return one
  detail model.

Prefer public category names over generated target names:

- Use `search_precedents`, not `search_precs`.
- Use `search_administrative_rules`, not `search_admruls`.
- Use `get_ordinance_detail`, not `get_ordin_detail`.

Keep generated identifiers only when they are unavoidable domain identifiers,
such as `law_id`, `prec_id`, `mst`, or documented law.go.kr codes.

## Return Model Guidance

Generated clients return generated Pydantic models from
`lawpy.kr.generated._models_generated`. Public wrappers should usually return
those generated models directly when they already represent the response well.

Use stable type annotations in wrappers:

- search/list methods return `list[<Target>List]`;
- detail methods return `<Target>Detail`;
- aliases and code values should remain visible when they are part of the API
  contract.

When serializing generated models for docs, snapshots, JSON output, or
downstream ingestion, use:

```python
model.model_dump(by_alias=True)
```

For lists:

```python
[item.model_dump(by_alias=True) for item in items]
```

`by_alias=True` preserves the generated law.go.kr field aliases. This matters
for `datapan-data`, where field lineage to source API names is useful for
datasets, audits, and schema comparisons.

## Tests And Docs For Future Category Issues

Every future issue that promotes a generated target to a public category should
include:

- generated coverage already present in `docs/kr/generated-coverage.md`;
- focused wrapper tests for parameter translation, defaults, return types, and
  `KRClient` composition;
- docs that show the public `KRClient` path and mention the generated fallback
  only when useful;
- examples using public wrapper names, not generated target method names;
- no README churn unless the issue explicitly owns that documentation surface.

For generated-only category issues, keep validation focused on generated tests,
coverage matrix accuracy, and importability. Do not add a public wrapper just to
avoid a "generated only" row in the coverage table.

## Relationship To datapan-data

`datapan-data` should depend on the public wrapper surface for stable ingestion
workflows whenever a wrapper exists. Generated clients remain useful there for
early exploration and source-parity checks, but they should not become long-term
dataset contracts for high-use categories.

When a `datapan-data` use case needs a generated-only target repeatedly, treat
that as evidence for a future wrapper issue. The wrapper should stabilize method
names, parameter names, defaults, and serialization guidance while keeping the
source aliases available through generated Pydantic models and
`model_dump(by_alias=True)`.
