# gha-dirtree-to-readme

Copy directory tree into file, e.g. README.md, instead of manual effort.

![Version](https://img.shields.io/badge/version-1.1.0-8A2BE2)
[![pytest](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/pytest.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/pytest.yaml)
[![test-action](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/test-dirtree-readme-action.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/test-dirtree-readme-action.yaml)
[![CodeQL](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/codeql.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/codeql.yaml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/gha-dirtree-to-readme/badge)](https://www.codefactor.io/repository/github/qte77/gha-dirtree-to-readme)
[![ruff](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/ruff.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/ruff.yaml)
[![Link Checker](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/links-fail-fast.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/links-fail-fast.yaml)
[![Deploy Docs](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/generate-deploy-mkdocs-ghpages.yaml/badge.svg)](https://github.com/qte77/gha-dirtree-to-readme/actions/workflows/generate-deploy-mkdocs-ghpages.yaml)
[![vscode.dev](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=vscode.dev&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://vscode.dev/github/qte77/gha-dirtree-to-readme)

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## Usage

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

## Inputs

| Name | Description | Default | Required |
| --- | --- | --- | --- |
| `OUT_FILE` | The file to write the directory tree to | `README.md` | Yes |
| `GH_TOKEN` | GitHub token for authentication | `${{ github.token }}` | Yes |
| `REPOSITORY` | GitHub repository name | `${{ github.repository }}` | Yes |
| `COMMITTER_NAME` | Name of the committer for the commit | `DirTreeToReadme-GHA` | Yes |
| `COMMITTER_EMAIL` | Email of the committer for the commit | `dirtree@gha` | Yes |
| `CREATE_PR` | Whether to create a pull request with the changes | `false` | No |

## Environment variables

These are read by `src/app.py` and can be overridden via `$GITHUB_ENV`.

| Name | Default |
| --- | --- |
| `CMD_HIGHLIGHT` | `sh` |
| `EXCLUDE` | `.git\|.github\|.gitignore\|.gitmessage` (separated by `\|`) |
| `INSERT_HERE_START_STRING` | `<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->` |
| `INSERT_HERE_END_STRING` | `<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->` |
| `OUT_FILE` | `README.md` |
| `TREE_THEME` | `sh` |

## Sample output

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
```sh
2025-01-01 23:27:29.737265+00:00
├── src
│ ├── app.py
│ └── utils.py
├── action.yaml
├── CHANGELOG.md
├── LICENSE.md
├── mkdocs.yaml
├── pyproject.toml
├── README.md
└── uv.lock
```
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->
