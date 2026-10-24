# gha-dirtree-to-readme

Copy directory tree into file, e.g. README.md, instead of manual effort.

![Version](https://img.shields.io/badge/version-1.1.1-8A2BE2)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)
[![test-action](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/test-dirtree-readme-action.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/test-dirtree-readme-action.yaml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/gha-dirtree-to-readme/badge)](https://www.codefactor.io/repository/github/qte77/gha-dirtree-to-readme)
[![CodeQL](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/codeql.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/codeql.yaml)
[![Dependabot](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/dependabot/dependabot-updates)
[![Ruff](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/ruff.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/ruff.yaml)
[![pytest](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/pytest.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/pytest.yaml)

## What

- Keeps a directory tree in your README (or any file) up to date, with no manual editing
- Inserts the tree between two marker comments and leaves the rest of the file untouched
- Commits the change to a new branch and pushes it, and opens a pull request when `CREATE_PR` is set
- Respects `.gitignore` and a configurable exclude list
- Offers several tree themes and any GitHub syntax-highlighting language for the code block
- Cleans up its branch and PR if a run fails or is cancelled

<details>
<summary>Sample output</summary>

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
```sh
2025-01-01 23:27:29.737265+00:00
├── src
│ ├── app.py
│ └── utils.py
├── action.yaml
├── CHANGELOG.md
├── LICENSE
├── mkdocs.yaml
├── pyproject.toml
├── README.md
└── uv.lock
```
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->

</details>

## How

```yaml
- uses: qte77/gha-dirtree-to-readme@v1
  with:
    OUT_FILE: README.md
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    CREATE_PR: 'true'
```

Add marker comments in your target file where the tree should be inserted:

```markdown
<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->
```

All inputs and environment variables: [docs/configuration.md](docs/configuration.md).

## Why

Hand-maintained directory trees in READMEs go stale as soon as files move, and fixing them by hand
is tedious and error-prone. This action regenerates the tree from the repository itself and delivers
it as a commit or a reviewable PR.

## Refs

- [CHANGELOG](CHANGELOG.md)
- [Configuration](docs/configuration.md)
- [action.yaml](action.yaml)

## License

[Apache-2.0](LICENSE)
