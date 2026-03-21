# Project Conventions

This document defines the core engineering standards and architectural rules for `lawpy`. These conventions must be strictly followed by all developers and AI agents to ensure code quality and system integrity.

## 1. Engineering Standards
- **Data Modeling**: All data structures for public APIs must use **Pydantic (v2+)** models. Plain classes or dictionaries are prohibited for data interfaces.
- **Type Safety**: Full Python type hints are mandatory for all function signatures and public APIs.
- **Inheritance**: All country-specific law clients must inherit from `lawpy.client.LawClient` to maintain a unified HTTP client lifecycle.
- **Code Style**: We strictly adhere to `ruff` and `mypy` configurations as defined in `pyproject.toml`.

## 2. File & Development Management
- **Test Organization**: Formal tests reside in `tests/` as `test_*.py`.
- **Scratchpads**: Use the `temp_*.py` prefix for local debugging or experiments. These are git-ignored and must never be committed.
- **Documentation**: All public methods must include Google-style docstrings.

## 3. Governance & CI/CD
- **Branch Protection**: No direct pushes to `main` or `develop`. All changes require a Pull Request.
- **CI Enforcement**: Passing all CI checks (Tests, Lint, Type-check) is a non-negotiable prerequisite for merging.
- **Automated Releases**: Deployment to PyPI is strictly automated via GitHub Actions (OIDC) triggered by `v*.*.*` tags. Manual uploads are prohibited.
