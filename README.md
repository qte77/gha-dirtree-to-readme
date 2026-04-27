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

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## Usage

```yaml
- uses: qte77/gha-dirtree-to-readme@v1
  with:
    OUT_FILE: README.md
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    CREATE_PR: 'true'
```text

Add marker comments in your target file where the tree should be inserted:

```markdown
<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->
```

## What it does

1. Sets environment variables and checks out the repository
2. Creates a new branch for the changes
3. Sets up Python and runs `src/app.py` to generate a directory tree
4. Inserts the tree output between the marker comments in the target file
5. Commits and pushes the changes if the file was modified
6. Optionally creates a pull request with the updated file
7. Cleans up the branch, PR, and tag on failure or cancellation

## Inputs

| Name | Required | Default | Description |
| --- | --- | --- | --- |
| `OUT_FILE` | Yes | `README.md` | The file to write the directory tree to |
| `GH_TOKEN` | Yes | `${{ github.token }}` | GitHub token for authentication |
| `REPOSITORY` | Yes | `${{ github.repository }}` | GitHub repository name |
| `COMMITTER_NAME` | Yes | `DirTreeToReadme-GHA` | Name of the committer for the commit |
| `COMMITTER_EMAIL` | Yes | `dirtree@gha` | Email of the committer for the commit |
| `CREATE_PR` | No | `false` | Whether to create a pull request with the changes |

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
├── LICENSE
├── mkdocs.yaml
├── pyproject.toml
├── README.md
└── uv.lock
```text
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->

## License

[Apache-2.0](LICENSE)
