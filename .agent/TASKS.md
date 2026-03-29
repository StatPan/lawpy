# TASKS.md — Backlog and in-progress work

## In Progress
- [ ] Implement hand-written parsers for high-priority KR targets

## Backlog

### KR — High Priority (parser implementation)
- [ ] `detc` — Constitutional Court decisions: implement xmltodict parsing in `kr/constitutional_decision.py`
- [ ] `decc` — Administrative appeals: `kr/admin_review.py`
- [ ] `admrul` — Administrative rules: `kr/admin_rule.py`
- [ ] `ordin` — Local ordinances: `kr/ordinance.py`

### KR — Medium Priority
- [ ] `lstrm` — Legal terminology search + detail
- [ ] `trty` — Treaties
- [ ] `elaw` — English law text (useful for international users)
- [ ] `oldAndNew` — Old/new law comparison (신구법비교)

### KR — Probe & Observability
- [ ] Add probe configs for newly implemented targets
- [ ] Add runtime passive warning in `_make_request` (schema drift → `warnings.warn`)
- [ ] Unit tests for `lawpy.probe` (currently 0% coverage)

### Infrastructure
- [ ] Async support (`httpx.AsyncClient`) — `KoreanLawClient.asearch_laws()` etc.
- [ ] Rate limiting / retry with backoff
- [ ] Response caching (optional, opt-in)

### Multi-country Expansion
- [ ] JP — Research e-Gov API spec
- [ ] US — Research Congress.gov API spec

### Documentation & Release
- [ ] Update README with probe CLI usage
- [ ] Add `CONTRIBUTING.md` with codegen/scraping workflow docs
- [ ] Bump version to v0.2.0 after first new parser implementation

## Completed
- [x] `LawClient` base + exceptions + Pydantic models
- [x] KR `law.py` — search, detail, list, history
- [x] KR `precedent.py` — list + detail
- [x] `KoreanLawClient` unified client
- [x] `lawpy-probe` CLI (capture / diff / show / list)
- [x] 195 API specs scraped → `specs/kr/`
- [x] 87 auto-generated stubs → `src/lawpy/kr/generated/`
- [x] Bundled snapshots in pip wheel
- [x] GitHub Actions daily drift detection pipeline
- [x] Multi-country env var structure (`LAWPY_KR_API_KEY`)
- [x] PyPI v0.1.0 release
