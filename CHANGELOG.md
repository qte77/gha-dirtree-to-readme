# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html), i.e. MAJOR.MINOR.PATCH (Breaking.Feature.Patch).

Types of changes:

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## [Unreleased]

### Fixed

- "Deploy Docs" runs on the push to `main` instead of on closed pull requests. The `github-pages` environment only allows `main` and `dev-gh-pages` to deploy, so every `pull_request` run (ref `refs/pull/<N>/merge`) was rejected before any step started. The workflow also copies the extension-less `LICENSE` to `docs/LICENSE.md`, the name the mkdocs nav expects
- `uv.lock` synced to the 1.1.2 project version, so `uv run --locked` (used by the docs build) no longer fails

### Security

- Pinned every remaining `uses:` ref in `.github/workflows/*` and `action.yaml` to its commit SHA (`actions/checkout@v7`, `callowayproject/bump-my-version@1.4.1`, `github/codeql-action/{init,autobuild,analyze}@v4`, `actions/configure-pages@v6`, `astral-sh/setup-uv@v7`, `actions/upload-pages-artifact@v5`, `actions/deploy-pages@v5`, `astral-sh/ruff-action@v3`, `actions/setup-python@v6`), required by the org's new SHA-pinning Actions policy. No version changes.

---

## [1.1.2] - 2026-11-09

### Security

- Dependency security update in `uv.lock`: certifi 2026.10.23, urllib3 2.8.0, mkdocs-material 9.8.0, pymdown-extensions 11.0.2 (kept below 12, which breaks the mkdocstrings build). The uv `exclude-newer` cutoff moves from 2026-05-13 to 2026-11-02, since the fixed releases are newer than the old cutoff

### Changed

- Dependabot uses its `uv` ecosystem instead of `pip` for this uv-managed project; `.gitignore` lists `.claude/settings.local.json`
- Ruff lint enables the `S` (flake8-bandit) rule set; `tests/*` ignore `S101`
- `main()` raises `FileNotFoundError`, `_is_path_in_exclude` raises `TypeError`, and `write_to_file` raises `ValueError` instead of using `assert` (which `python -O` strips)
- README follows the qte77 doc-structure canon (What → How → Why → Refs → License); inputs and environment-variable tables moved to `docs/configuration.md`

---

## [1.1.1] - 2026-03-23

---

## [1.1.0] - 2026-03-23

### Changed

- `callowayproject/bump-my-version` `@0.29.0` → `@1.2.7`
- `actions/checkout` `@v4` → `@v6`
- `github/codeql-action` `@v3` → `@v4`
- Bump workflow creates GitHub Release and updates floating major tag
- Cleanup script includes release deletion

### Added

- `github-actions` ecosystem to dependabot

### Removed

- Orphaned `summarize-jobs-reusable.yaml`

---

## [1.0.0] - 2026-03-17

### Added

- `main()` function in `src/app.py` for testability
- Tests for `main()` in `tests/test_app.py`
- Usage section, inputs table, and environment variables table in README
- Input descriptions in `action.yaml` for marketplace validation

### Changed

- Renamed action to "GHA Dirtree to Readme"
- Pytest CI workflow now uses `uv` instead of pip
- Moved pytest `pythonpath` config into `pyproject.toml`

### Removed

- Stale `Dockerfile` (action is composite, not Docker)
- Unused `pydantic` dev dependency
- Non-standard fields from `action.yaml` (`repo`, `keywords`, `permissions`, `type`)

### Fixed

- `write_to_file` silently skipping insertion when markers are consecutive (no content between)
- Test assertions in `test_utils.py`: trailing space in `_get_tree_theme('sh')`, `deque` return type, dead `write_to_file` assertions
- Badge URLs in README: `dirtree-readme-action` → `gha-dirtree-to-readme`
- `test_get_write_positions_in_file` indentation causing marker mismatch
- CI pytest workflow now caches uv dependencies

---

## [0.2.2] - 2025-01-02

### Added

- Basic tests for all functions

---

## [0.2.1] - 2025-01-01

---

## [0.2.0] - 2025-01-01

### Added

- Push and PR

### Changed

- From `pip` to `uv` for test and docs
- Action from `Dockerfile` to `composite`
