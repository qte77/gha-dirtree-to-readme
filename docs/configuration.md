# Configuration

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
