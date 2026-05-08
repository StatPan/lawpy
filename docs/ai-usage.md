# lawpy AI Usage Guide

This guide is written for AI agents and automation code that need to use
`lawpy` after installing it with `uv add lawpy` or `pip install lawpy`.

## Installed Help

The package includes an installed help surface:

```python
import lawpy

print(lawpy.help())
print(lawpy.help("kr"))
print(lawpy.help("generated"))
print(lawpy.help("codegen"))
```

It is also available as:

```bash
python -m lawpy.help
python -m lawpy.help kr
python -m lawpy.help generated
python -m lawpy.help codegen
```

## Main Object

Use `KRClient` first.

```python
from lawpy import KRClient

client = KRClient(api_key="your-open-law-email-id")
```

`KRClient` is the ergonomic public surface for Korean law.go.kr data. It
combines the implemented public wrappers for:

- laws
- precedents
- administrative rules and notices
- local ordinances and local notices

`KoreanLawClient` remains available as a compatibility alias for existing code.

## One Pattern

Search returns a list. Detail methods fetch one full record.

```python
laws = client.search_laws("민법", per_page=5)
detail = client.get_law_detail(law_id=laws[0].law_id)
```

The same pattern applies to other public wrappers:

```python
precedents = client.search_precedents("손해배상", per_page=5)
precedent = client.get_precedent_detail(case_id=precedents[0].case_id)

rules = client.search_administrative_rules("개인정보", per_page=5)
rule = client.get_administrative_rule_detail(rule_id=rules[0].행정규칙ID)

ordinances = client.search_ordinances("서울", per_page=5)
ordinance = client.get_ordinance_detail(ordinance_id=ordinances[0].자치법규ID)
```

## Generated-Only Targets

If `KRClient` does not expose a public wrapper for the target, import the
generated client directly:

```python
from lawpy.kr.generated.trty import GeneratedTrtyClient

client = GeneratedTrtyClient(api_key="your-open-law-email-id")
treaties = client.search_trtys(query="FTA", display=10, page=1)
row = treaties[0].model_dump(by_alias=True)
```

Naming pattern:

- target file: `lawpy.kr.generated.{target}`
- client class: `Generated{Target.capitalize()}Client`
- search method: `search_{target}s(...)`
- detail method: `get_{target}_detail(...)`

For the complete generated target matrix, see
[`docs/kr/generated-coverage.md`](kr/generated-coverage.md).

## Codegen And Specs

The Korean specs, code generator, generated clients, generated models, and
generated tests are public.

Support contract:

- Prefer `KRClient` for stable public workflows.
- Use generated clients for covered targets without a wrapper.
- Generated output is reviewed through deterministic diffs, coverage docs, and CI.
- Raw scraped specs may reflect upstream documentation quirks.
