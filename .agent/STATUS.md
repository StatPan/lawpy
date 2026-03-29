# STATUS.md — Current development status

## Last Updated
2026-03-29

## Overall Progress

### ✅ Done

**Infrastructure**
- `LawClient` base class (httpx, timeout, error handling)
- Pydantic v2 models (`Law`, `LawDetail`, `LawHistory`, `Precedent`, `PrecedentDetail`)
- Exception hierarchy (`APIError`, `NotFoundError`, `ParseError`)
- PyPI published at v0.1.0

**KR — South Korea (법제처)**
- `law.py` — search, detail (full text + articles), list, amendment history
- `precedent.py` — list search + full text detail
- `KoreanLawClient` — unified client via multiple inheritance
- 195 API specs scraped from `open.law.go.kr` → `specs/kr/*.json`
- 87 auto-generated stubs → `src/lawpy/kr/generated/*.py`

**Automation / Observability**
- `lawpy-probe` CLI — capture / diff / show / list
- 5 probe configs registered (law search, law detail, eflaw, prec search, prec detail)
- Bundled snapshots (pip-shipped): `src/lawpy/snapshots/*.json`
- GitHub Actions daily pipeline:
  - Spec drift: re-scrape → diff → auto-PR with regenerated stubs
  - Response drift: probe diff → GitHub Issue
- `LAWPY_KR_API_KEY` secret registered in GitHub Actions

### ⏳ Backlog (KR)

**High priority** — hand-written parsers needed (generated stubs are placeholders):
- `detc` — Constitutional Court decisions (헌재결정례)
- `decc` — Administrative appeals (행정심판례)
- `admrul` — Administrative rules (행정규칙)
- `ordin` — Local ordinances (자치법규)

**Medium priority**
- `lstrm` — Legal terminology (법령용어)
- `trty` — Treaties (조약)
- `elaw` — English law text (영문법령)

**Low priority / large surface**
- 12 committee decision APIs (`ppc`, `ftc`, `kcc`, etc.)
- 26 ministry interpretation APIs (`cgmExpc*`)
- Mobile API variants (`mob*`)

### 🌍 Other Countries (planned)
- JP — e-Gov API
- US — Congress.gov API
- EU — EUR-Lex API

## Active Blockers
None. Probe pipeline operational. Generated stubs ready for parser implementation.
