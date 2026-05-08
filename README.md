# lawpy

Universal law information API client library.

## Features

- **Multi-country support**: Access law APIs from multiple countries (currently Korea)
- **Simple interface**: Intuitive API design for easy integration
- **Type-safe**: Full type hints for better IDE support
- **KRClient first**: One ergonomic entry point for implemented Korean APIs
- **Generated KR coverage**: 98 Korean law.go.kr target clients are generated from specs; 8 are generated-only until public wrappers are added

## Installation

```bash
pip install lawpy
```

## Quick Start

### Installed help

If you installed `lawpy` without cloning the repository, start here:

```python
import lawpy

print(lawpy.help())
print(lawpy.help("kr"))
print(lawpy.help("generated"))
```

The same guide is available from the shell:

```bash
python -m lawpy.help kr
```

### Korean Law API

Set your API key (email ID) as an environment variable:

```bash
export LAWPY_API_KEY="your-email-id"
```

Or pass it directly:

```python
from lawpy import KRClient

# Using environment variable
client = KRClient()

# Or pass api_key directly
client = KRClient(api_key="your-api-key")
```

`KRClient` is the main ergonomic object for Korean law.go.kr data. It combines
the current public wrappers for laws, precedents, administrative rules, notices,
annexes, forms, local ordinances, local notices, legal terminology, legal interpretations,
constitutional decisions, administrative review decisions, committee decisions,
ministry interpretations, and treaties.
`KoreanLawClient` remains available as a compatibility alias.

#### Collector method metadata

Automation code can ask the installed client which methods need seeds,
catalogs, enum values, or alternative parameter sets:

```python
specs = client.get_method_specs()
detail_spec = client.describe_method("get_law_detail")

assert detail_spec["alternatives"] == [["law_id"], ["mst"]]
```

Use this metadata to generate collection targets safely:

- call search methods directly when `required` is empty
- expand catalog/enum methods when `allowed_values` or `catalog` is present
- seed detail methods from `seed_source`
- skip methods with missing seeds and record the reason

#### Search for laws

```python
laws = client.search_laws("민법", per_page=5)
for law in laws:
    print(f"{law.law_name} (ID: {law.law_id})")
```

#### Get detailed law information

```python
law_detail = client.get_law_detail(law_id="001706")
print(f"Law: {law_detail.law_name_korean}")
print(f"Ministry: {law_detail.ministry}")
print(f"Promulgation Date: {law_detail.promulgation_date}")
print(f"Enforcement Date: {law_detail.enforcement_date}")

# Access articles
for article in law_detail.articles[:3]:
    print(f"Article {article.number}: {article.title}")
    for paragraph in article.paragraphs:
        print(f"  {paragraph.content}")
```

#### Get specific article

```python
law_detail = client.get_law_detail(law_id="001706", article_number=1)
```

#### Get law by MST (master number)

```python
law_detail = client.get_law_detail(mst=123456)
```

#### Get original text

```python
law_detail = client.get_law_detail(law_id="001706", language="ORI")
```

#### Get current law list

```python
laws = client.get_law_list(per_page=10)
for law in laws:
    print(f"{law.law_name} (Effective: {law.enforcement_date})")
```

#### Get law amendment history

```python
history = client.get_law_history(query="민법", per_page=10)
for h in history:
    print(f"{h.law_name} ({h.promulgation_date})")
```

#### Get detailed law history

```python
history_detail = client.get_law_history_detail(mst=9094)
print(history_detail)  # Returns HTML text
```

#### Get old/new law comparison metadata

```python
old_new = client.search_law_old_and_new(query="민법", per_page=10)
print(old_new[0])
```

#### Get old/new law comparison detail

```python
old_new_detail = client.get_law_old_and_new_detail(law_id="009682")
print(old_new_detail)
```

#### Get law abbreviations

```python
abbrs = client.search_law_abbreviations(start_date=20240101, end_date=20240131)
print(abbrs)
```

#### Get law/article change history

```python
changes = client.search_law_change_history(registered_date=20240101)
article_changes = client.search_law_article_change_history(law_id="009682", article_number=2)
```

### Generated-only KR targets

KR v1 includes generated clients for 98 public law.go.kr targets. `KRClient`
wraps 90 of them today: `law`, `elaw`, `oldAndNew`, `lsAbrv`, `lsHstInf`,
`lsJoHstInf`, `prec`, `admrul`, `licbyl`, `admbyl`, `ordinbyl`, `ordin`,
`lstrm`, `lstrmAI`, `dlytrm`, `lstrmRlt`, `dlytrmRlt`, `lstrmRltJo`,
`joRltLstrm`, `lsRlt`, `aiSearch`, `aiRltLs`, `expc`, `detc`, `decc`,
`acr`, `baiPvcs`, `ecc`, `eiac`, `fsc`, `ftc`, `iaciac`, `kcc`, `nhrck`,
`nlrc`, `oclt`, `ppc`, `sfc`, the `*CgmExpc` ministry interpretation targets,
`school`, `trty`, `couseAdmrul`, `couseLs`, `couseOrdin`, `lawjosub`,
`eflawjosub`, `lnkLs`, `lnkOrd`, `drlaw`, `lsDelegated`, `oneview`, and
`thdCmp`. The remaining 8 targets are generated-only; import those clients directly from
`lawpy.kr.generated`.

```python
from lawpy.kr.generated.acrSpecialDecc import GeneratedAcrspecialdeccClient

client = GeneratedAcrspecialdeccClient(api_key="your-api-key")
decisions = client.search_acrSpecialDeccs(query="영업정지", display=10, page=1)
row = decisions[0].model_dump(by_alias=True)
```

Run `import lawpy; print(lawpy.help("generated"))` or see
[docs/kr/generated-coverage.md](docs/kr/generated-coverage.md) for the generated
target matrix.

## Specs and codegen policy

The Korean specs, code generator, generated clients, generated models, and
generated tests are public. The project treats reproducible generation, coverage
documentation, and CI as the maintenance contract rather than hiding source
specs.

## API Key

To use the Korean Law API, you need an API key:

1. Visit [Korean Law Open API](https://open.law.go.kr/)
2. Sign up and get your email ID as API key
3. Set it as environment variable: `LAWPY_API_KEY`

## Development

```bash
# Clone repository
git clone https://github.com/statpan/lawpy.git
cd lawpy

# Install development dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Run linting
uv run ruff check src/lawpy tests
uv run ruff format src/lawpy tests

# Type checking
uv run mypy src/lawpy

# Build package
uv build
```

## Project Structure

```
lawpy/
├── src/lawpy/
│   ├── __init__.py
│   ├── client.py          # Base client class
│   ├── exceptions.py      # Exception definitions
│   ├── models.py         # Data models
│   └── kr/             # Korean API modules
│       ├── __init__.py
│       ├── base.py       # Base class for Korean clients
│       ├── client.py     # KRClient integrated Korean client
│       ├── law.py       # Law (법령) APIs
│       ├── administrative_rule.py # Administrative rule (행정규칙) wrapper
│       ├── annex_form.py # Annex/form (별표·서식) wrapper
│       ├── ordinance.py # Local ordinance (자치법규) wrapper
│       ├── legal_terminology.py # Legal terminology (법령용어) wrapper
│       ├── legal_knowledge_base.py # Legal knowledge-base (법령정보지식베이스) wrapper
│       ├── legal_interpretation.py # Legal interpretation (법령해석례) wrapper
│       ├── constitutional_decision.py # Constitutional decision (헌재결정례) wrapper
│       ├── administrative_review_decision.py # Administrative review decision (행정심판례) wrapper
│       ├── precedent.py # Precedent (판례) wrapper
│       ├── treaty.py # Treaty (조약) wrapper
│       ├── generated/   # 98 spec-generated Korean API clients
│       └── README.md     # Korean API documentation
└── tests/
    ├── test_kr.py       # Korean API tests
    └── test_generated/  # Generated client tests
```

## Roadmap

- [ ] Add more countries (Japan, China, etc.)
- [ ] Add public wrappers for generated-only Korean targets
- [ ] Add async support
- [ ] Add caching layer

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- [GitHub Repository](https://github.com/statpan/lawpy)
- [PyPI Package](https://pypi.org/project/lawpy/)
- [Korean Law Open API Guide](https://open.law.go.kr/LSO/openApi/guideList.do)
