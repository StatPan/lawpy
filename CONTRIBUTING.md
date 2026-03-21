# Contributing to lawpy

Thank you for your interest in contributing! This guide outlines the process for submitting contributions to this project.

## How to Contribute
1. **Report Bugs**: Open an issue describing the bug and providing a reproduction script if possible.
2. **Suggest Features**: Open an issue to discuss new features or improvements.
3. **Submit Code**:
   - Fork the repository and create a feature branch (`feat/your-feature`).
   - Follow the technical standards defined in **[CONVENTIONS.md](./CONVENTIONS.md)**.
   - Ensure all tests pass locally using `uv run pytest`.
   - Submit a Pull Request (PR) to the `develop` branch.

## Development Setup
We use `uv` for dependency management:
```bash
uv sync --extra dev
uv run ruff check --fix
uv run mypy src/lawpy
```

## Pull Request Guidelines
- Keep PRs focused on a single change.
- Update documentation in `README.md` if your change affects public APIs.
- A maintainer will review your PR and provide feedback.
