# E-Group Root Key Promotion

This note records the v1 root/item-key policy promoted by #48.

The source evidence is the prior live E-group probe review captured in issue
#48. The original scratch files (`scripts/probe_e_group.py`,
`temp_e_group_results.json`, `temp_integration_results.json`) were not kept in
main because they were dirty-session artifacts. The reproducible probe entry
point is now:

```bash
uv run python scripts/probe_e_group.py --api-key "$LAWPY_KR_API_KEY"
```

## Promoted Shapes

Special administrative decision targets use `Decc.decc`:

- `decc`
- `acrSpecialDecc`
- `adapSpecialDecc`
- `kmstSpecialDecc`
- `ttSpecialDecc`

Central ministry interpretation targets use `CgmExpc.cgmExpc`:

- `dapaCgmExpc`
- `kcgCgmExpc`
- `kcsCgmExpc`
- every other `*CgmExpc` target with root key `CgmExpc`

`baiPvcs` remains unchanged. The dirty-session result mixed 404, non-JSON, and
error payloads, so the manual generated-service fallback was not promoted.

`eflawjosub` remains unchanged as `법령.법령키`; its service response needs a
separate focused probe before changing generated root handling.

## Codegen Policy

Generated list parsers prefer the discovered item key when present. They also
accept the older root-list shape as a compatibility fallback, so setting
`item_key` in `_root_keys.json` does not make clients fail if the API returns
the root as a list for the same target.
