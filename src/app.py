"""
This module contains the main script for the dirtree-readme-action, which generates
and writes a directory tree to a specified file, typically README.md. It uses GitHub
API to push changes back to the repository if not running from a local action.

Key functionalities:
- Reads environment variables for configuration.
- Generates a formatted directory tree.
- Writes the tree to a file between specified markers.
- Optionally pushes changes to GitHub if not running locally.

Environment Variables:
- CMD_HIGHLIGHT: Syntax highlighting language for the tree output.
- EXCLUDE: Directories or files to exclude from the tree.
- INSERT_HERE_START_STRING: Start marker for tree insertion in the file.
- INSERT_HERE_END_STRING: End marker for tree insertion in the file.
- OUT_FILE: The file to write the directory tree to.
- TREE_THEME: Theme for the tree structure.
- USE_FROM_LOCAL_ACTION: Flag to determine if the action is running locally.
- GH_TOKEN: GitHub token for authentication.
- REPOSITORY: GitHub repository name.
- COMMITTER_NAME: Name of the committer for the commit.
- COMMITTER_EMAIL: Email of the committer for the commit.

Functions:
- push_file_to_github(files: str) -> None: Pushes the updated file to GitHub.

Main Execution:
- Checks for the existence of the output file and start path.
- Generates and writes the directory tree to the specified file.
- Pushes changes to GitHub if not running locally.
"""

from logging import (
    basicConfig,
    getLogger,
    INFO,
    error,
)
from os import getenv
from pathlib import Path
from utils import (
    get_formatted_tree_output,
    get_write_positions_in_file,
    write_to_file
)

basicConfig(level=INFO)
logger = getLogger(__name__)


def main() -> None:
    """Generate and write directory tree to the configured output file.

    Reads configuration from environment variables, generates a formatted
    directory tree, and writes it between marker comments in the output file.

    Raises:
        AssertionError: If the output file or start path does not exist.
    """
    cmd_highlight: str = str(getenv("CMD_HIGHLIGHT", 'sh'))
    exclude: str = str(getenv("EXCLUDE", '.git|.github|.gitignore|.gitmessage'))
    insert_start: str = str(getenv(
        "INSERT_HERE_START_STRING",
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->'
    ))
    insert_end: str = str(getenv(
        "INSERT_HERE_END_STRING",
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
    ))
    out_file: str = str(getenv("OUT_FILE", 'README.md'))
    tree_theme: str = str(getenv("TREE_THEME", 'sh'))

    excl_list: list[str] = exclude.split('|')
    fpath: Path = Path(out_file)
    spath: Path = Path('.')

    assert fpath.exists(), f"{fpath} not found. Aborting"
    assert spath.exists(), f"{spath} not found. Aborting"

    start_index, end_index = get_write_positions_in_file(
        fpath, insert_start, insert_end
    )
    if isinstance(start_index, int) \
       and isinstance(end_index, int) \
       and start_index >= 0 and end_index >= 1:
        dirtree = get_formatted_tree_output(
            spath, excl_list, cmd_highlight, tree_theme
        )
        write_to_file(fpath, dirtree, start_index, end_index)
    else:
        error(
            f"Could not write file. Index error: {start_index=}, {end_index=}"
        )


if __name__ == "__main__":
    main()
