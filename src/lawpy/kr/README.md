# Korean Law API Modules

This package implements Korean National Law Information Center Open API clients.
Use `KRClient` first for normal work; use `lawpy.kr.generated` when a law.go.kr
target does not have an ergonomic wrapper yet.

## Current Structure

```
lawpy/kr/
├── __init__.py
├── base.py                    # Shared Korean HTTP client behavior
├── client.py                  # KRClient, the primary integrated client
├── law.py                     # Public law (법령) wrapper
├── administrative_rule.py     # Public administrative rule (행정규칙) wrapper
├── ordinance.py               # Public local ordinance (자치법규) wrapper
├── legal_terminology.py       # Public legal terminology (법령용어) wrapper
├── legal_interpretation.py    # Public legal interpretation (법령해석례) wrapper
├── constitutional_decision.py # Public constitutional decision (헌재결정례) wrapper
├── precedent.py               # Public precedent (판례) wrapper
├── treaty.py                  # Public treaty (조약) wrapper
├── generated/                 # 89 spec-generated law.go.kr target clients
└── README.md
```

Targets such as `committee/` or `ministry_interpretation/` are not public
wrapper modules today. Their targets are available only through generated
clients until wrappers are added.

## Primary Usage

```python
from lawpy.kr import KRClient

client = KRClient(api_key="your_email_id")

laws = client.search_laws("민법")
law_detail = client.get_law_detail(law_id="009682")
law_history = client.get_law_history(query="민법")

precedents = client.search_precedents("민법")
precedent_detail = client.get_precedent_detail(precedents[0].prec_id)

rules = client.search_administrative_rules("개인정보", rule_type="3")
notices = client.search_notices("고시")

ordinances = client.search_ordinances("서울특별시", ordinance_type="30001")
local_notices = client.search_local_notices("고시")

terms = client.search_legal_terms("과태료", law_kind_code=10101)
term_detail = client.get_legal_term_detail("과태료")

interpretations = client.search_legal_interpretations("건축")
interpretation_detail = client.get_legal_interpretation_detail(
    interpretation_id=int(interpretations[0].법령해석례일련번호)
)

constitutional_decisions = client.search_constitutional_decisions("기본권")
constitutional_decision_detail = client.get_constitutional_decision_detail(
    decision_id=constitutional_decisions[0].헌재결정례일련번호
)

treaties = client.search_treaties("FTA", treaty_class=1)
treaty_detail = client.get_treaty_detail(treaties[0].조약일련번호)
```

`KoreanLawClient` is a compatibility alias for `KRClient`. New code should
prefer `KRClient`.

## Public Wrapper Status

| Public surface | Backing target | Status |
|----------------|----------------|--------|
| `KRClient`, `law.py` | `law` | Partial public wrapper: search, detail, current list, history list, history detail |
| `KRClient`, `administrative_rule.py` | `admrul` | Partial public wrapper over generated `admrul`: administrative rule search, notice search (`knd=3`), detail |
| `KRClient`, `ordinance.py` | `ordin` | Partial public wrapper over generated `ordin`: local ordinance search, local notice search (`knd=30010`), detail |
| `KRClient`, `legal_terminology.py` | `lstrm` | Public wrapper over generated `lstrm`: legal term search and detail |
| `KRClient`, `legal_interpretation.py` | `expc` | Thin public wrapper over generated `expc`: legal interpretation search and detail |
| `KRClient`, `constitutional_decision.py` | `detc` | Thin public wrapper over generated `detc`: constitutional decision search and detail |
| `KRClient`, `precedent.py` | `prec` | Partial public wrapper: precedent search and detail using handwritten XML parsing; generated `prec` also exists |
| `KRClient`, `treaty.py` | `trty` | Public wrapper over generated `trty`: treaty search and detail |

## Generated-Only Targets

The generated package contains 89 law.go.kr target clients. Eight targets are
wrapped by `KRClient` today (`law`, `prec`, `admrul`, `ordin`, `lstrm`, `expc`, `detc`, `trty`), leaving 81
generated-only target modules.

Use generated-only clients directly:

```python
from lawpy.kr.generated.decc import GeneratedDeccClient

client = GeneratedDeccClient(api_key="your_email_id")
decisions = client.search_deccs(query="영업정지", display=10, page=1)
```

Generated clients return Pydantic models from
`lawpy.kr.generated._models_generated`. Use `model_dump(by_alias=True)` when you
need the original Korean field names.

For the target matrix, run:

```python
import lawpy

print(lawpy.help("generated"))
```

or read `docs/kr/generated-coverage.md` in the repository.

## API Key

The API key is the email ID registered with the Korean National Law Information
Center.

```bash
export LAWPY_API_KEY=your_email_id
```

or pass it directly:

```python
from lawpy.kr import KRClient

client = KRClient(api_key="your_email_id")
```

## References

- [Korean Law Open API Guide](https://open.law.go.kr/LSO/openApi/guideList.do)
- [API Application](https://open.law.go.kr/LSO/openApi/cuAskList.do)
