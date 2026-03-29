# NOTES.md — Developer notes and gotchas

## KR API — law.go.kr

### Authentication
- `OC` parameter = email **username** (before `@`) of the account registered at open.law.go.kr
- Full email does NOT work. `user@example.com` → set `OC=user`
- Env var: `LAWPY_KR_API_KEY`

### Endpoints
| URL | Usage |
|-----|-------|
| `https://www.law.go.kr/DRF/lawSearch.do` | List / search (`BASE_URL`) |
| `http://www.law.go.kr/DRF/lawService.do` | Full text detail (`SERVICE_URL`) |

### Response format
- Default: XML. We request `type=JSON` for JSON.
- xmltodict is used for XML parsing (in older methods).
- JSON is preferred for new implementations.

### Known quirks
- `display` max = 100 per page
- Single-item responses are returned as a dict, not a list — always wrap with `ensure_list()` helper
- Some endpoints return Korean field names as XML tags (e.g. `<판례일련번호>`)
- `lawService.do` uses HTTP (not HTTPS) — intentional, upstream issue

### Spec scraping
- Guide list URL: `https://open.law.go.kr/LSO/openApi/guideList.do`
- Guide detail URL: POST to `https://open.law.go.kr/LSO/openApi/guideResult.do` with `htmlName=<guide_name>`
- All 195 guide names extracted via `onclick="openApiGuide('<name>')"` in the HTML
- Scraped specs stored in `specs/kr/*.json`
- Re-run: `uv run python scripts/scrape_specs.py --output specs/kr/`

### Probe system
- Capture: `LAWPY_KR_API_KEY=xxx lawpy-probe capture --all`
- Diff:    `LAWPY_KR_API_KEY=xxx lawpy-probe diff --all`
- Bundled snapshots live in `src/lawpy/snapshots/` and are shipped in the pip wheel

## Codegen
- Source: `specs/kr/*.json` (scraped)
- Output: `src/lawpy/kr/generated/*.py` (stubs — `# TODO` parse logic needed)
- Re-run: `uv run python scripts/codegen.py --specs specs/kr/ --out src/lawpy/kr/generated/`
- Generated files are intentionally checked in so users of the pip package see the stubs

## Global Package Guidelines
- All code, comments, docstrings, and agent files must be in **English**
- Korean appears only in: response field names (from API), test fixtures, spec JSON values
- Error messages must be English
- Env vars use country prefix: `LAWPY_{COUNTRY}_API_KEY`
