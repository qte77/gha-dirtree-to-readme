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
