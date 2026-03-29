# MEMORY.md — lawpy project context

## Project Overview
- **Package:** `lawpy` (pip-installable, globally targeted)
- **Purpose:** Multi-country law/legislation API client library
- **Tech stack:** Python 3.13+, Pydantic v2, httpx, xmltodict
- **PyPI status:** Published at v0.1.0
- **GitHub:** https://github.com/StatPan/lawpy

## Architecture

```
src/lawpy/
├── client.py              # Base LawClient (httpx wrapper)
├── exceptions.py          # APIError, NotFoundError, ParseError
├── models.py              # Shared Pydantic models
├── kr/                    # South Korea — National Law Information Center
│   ├── base.py            # KoreanBaseClient (env: LAWPY_KR_API_KEY)
│   ├── law.py             # ✅ Implemented: law/eflaw/lsHistory endpoints
│   ├── precedent.py       # ✅ Implemented: prec list + detail
│   ├── client.py          # KoreanLawClient (unified, multiple inheritance)
│   └── generated/         # 🤖 Auto-generated stubs (87 targets, codegen.py)
├── probe/                 # API response schema capture + drift detection
│   ├── schema.py          # Extract field schema from parsed responses
│   ├── snapshot.py        # Save/load bundled snapshots (importlib.resources)
│   ├── differ.py          # SchemaDiffer → DiffResult
│   ├── runner.py          # ProbeRunner (capture / diff)
│   ├── cli.py             # lawpy-probe CLI
│   └── configs/kr.py      # Korean API probe configs (5 registered)
└── snapshots/             # Bundled JSON snapshots (shipped in pip wheel)
    ├── kr.law.search.json
    ├── kr.law.eflaw.search.json
    ├── kr.law.detail.json
    ├── kr.prec.search.json
    └── kr.prec.detail.json

specs/kr/                  # 195 scraped API spec JSONs (source of truth)
scripts/
├── scrape_specs.py        # Scrape open.law.go.kr guide pages → specs/kr/
├── spec_diff.py           # Diff two spec runs (detect added/removed APIs)
└── codegen.py             # Generate client stubs from spec JSONs
```

## Environment Variables

| Variable              | Country | Description |
|-----------------------|---------|-------------|
| `LAWPY_KR_API_KEY`    | KR      | Email username (before @) registered at open.law.go.kr |
| `LAWPY_JP_API_KEY`    | JP      | (planned) |
| `LAWPY_US_API_KEY`    | US      | (planned) |

> **KR note:** The API key is the email **username only** — e.g. for `user@example.com`, set `LAWPY_KR_API_KEY=user`.  
> `LAWPY_API_KEY` still works as a backwards-compat fallback.

## Key Endpoints (KR)

| Target | Endpoint | Description |
|--------|----------|-------------|
| `law` / `eflaw` | `lawSearch.do` | Law list search |
| `lsHistory` | `lawSearch.do` | Amendment history list |
| `law` | `lawService.do` | Law full text |
| `prec` | `lawSearch.do` | Precedent list search |
| `prec` | `lawService.do` | Precedent full text |

## Automated Pipeline (GitHub Actions)

`.github/workflows/api-drift.yml` runs **daily at 09:00 KST**:
1. **Spec drift**: Re-scrape `open.law.go.kr` → diff vs `specs/kr/` → if changed, create PR with regenerated stubs
2. **Response drift**: `lawpy-probe diff --all` → compare live API responses vs `snapshots/` → if breaking changes, open GitHub Issue

Secret required: `LAWPY_KR_API_KEY` (set in repo Actions secrets)
