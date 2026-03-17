"""
This module contains utility functions for the GitHub dirtree-readme-action, which generates
and writes a directory tree to a specified file, typically README.md. It provides functionalities
for:

- Generating a formatted directory tree
- Excluding paths: Methods to exclude certain paths from the tree generation.
- File operations: Functions to read, write, and manipulate file contents.

**Key Functions:**

- `_get_tree_theme`: Returns tree indicator themes for different visual styles.
- `_is_path_in_exclude`: Checks if a given path should be excluded from the tree.
- `_generate_tree`: Recursively generates a visual tree structure of directories and files.
- `get_formatted_tree_output`: Generates a formatted directory tree output with syntax highlighting.
- `get_write_positions_in_file`: Finds the positions in a file where the tree should be inserted.
- `write_to_file`: Writes the generated directory tree to a file between specified markers.

**Usage:**

This module is designed to be used within the context of a GitHub Action to automate the process
of updating README files with directory structures. It reads environment variables for configuration
and can optionally push changes back to the repository if not running from a local action.

**Environment Variables:**

- `CMD_HIGHLIGHT`: Syntax highlighting language for the tree output.
- `EXCLUDE`: Directories or files to exclude from the tree.
- `INSERT_HERE_START_STRING`: Start marker for tree insertion in the file.
- `INSERT_HERE_END_STRING`: End marker for tree insertion in the file.
- `OUT_FILE`: The file to write the directory tree to.
- `TREE_THEME`: Theme for the tree structure.

**Possible Improvements:**

- Caching `.gitignore` content to improve performance for large directory structures.
- More robust error handling for file operations.
"""

from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, List, Tuple

def _get_tree_theme(theme: str = 'sh') -> Tuple[str, str, str, str]:
    """Returns tree indicator themes: space, branch, tee, last."""
    if theme == 'cmd':
        return ' ', '│ ', '├──', '└──'
    elif theme == 'slash':
        return ' ', '│ ', '│── ', '\── '
    elif theme == 'elli':
        return ' ', '︙ ', '︙··· ', ' ···· '
    elif theme == 'null':
        return ' ', ' ', ' ', ' '
    elif theme == 'sh':
        return ' ', '│ ', '├── ', '└── '
    else:
        raise NotImplementedError

def _is_path_in_exclude(path: Path, exclude_list: list) -> bool:
    """Check if path contains any excluded items."""
    assert isinstance(path, Path)
    assert isinstance(exclude_list, list)
    for pt in path.parts:
        if pt in exclude_list:
            return True
    return False

# list-directory-tree-structure-in-python:
# https://stackoverflow.com/a/59109706
def _generate_tree(
    path: Path, exclude_list: List[str],
    space: str, branch: str, tee: str, last: str,
    prefix: str = '', suffix: str = ''
) -> Iterator[str]:
    """ 
    A recursive generator, given a directory Path object 
    will yield a visual tree structure line by line 
    with each line prefixed by the same characters. 
    Returns a string of the current folder or file 
    and hierarchical indicators. 
    """
    # add items in .gitignore to exclude_list
    gitignore_path = path / '.gitignore'
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as gitignore_file:
            exclude_list.extend(
                line.strip() for line in gitignore_file
                if line.strip() and not line.startswith('#')
            )
    # sort content of path
    contents = sorted(
        path.iterdir(),
        key=lambda p: (not p.is_dir(), p.name.lower())
    )
    # contents each get pointers that are 'tee' with a final 'last'
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        if not _is_path_in_exclude(path, exclude_list):
            yield prefix + pointer + path.name + suffix
        if path.is_dir():
            extension = branch if pointer == tee else space
            yield from _generate_tree(
                path, exclude_list,
                space, branch, tee, last,
                prefix + extension, suffix
            )

def get_formatted_tree_output(
    startpath: Path, exclude_list: list,
    cmd_highlight: str, tree_theme: str
) -> deque[str]:
    """
    Returns a list of startpath and its children. cmd_highlight has 
    to be one of Github's native syntax highlighting languages. 
    https://github.com/github-linguist/linguist/blob/master/lib/linguist/languages.yml 
    """
    suffix = '\n'
    space, branch, tee, last = _get_tree_theme(tree_theme)
    dirtree = _generate_tree(
        startpath, exclude_list,
        space, branch, tee, last,
        suffix = suffix
    )
    out = deque(dirtree)
    out.appendleft(f"{datetime.now(timezone.utc)}{suffix}")
    out.appendleft(f"```{cmd_highlight}{suffix}")
    out.append(f"```{suffix}")
    return out

def get_write_positions_in_file(
    outfpath: Path, start_string: str, end_string: str
) -> Tuple[int, int]:
    """Returns position of first consecutive start_string and end_string."""
    sdx, edx = None, None
    f_in = (line for line in open(outfpath, 'r'))
    for index, line in enumerate(f_in):
        if line.startswith(start_string):
            sdx = index
        elif line.startswith(end_string) and sdx:
            edx = index
            break
    return sdx, edx

def write_to_file(
    outfpath: Path, dirtree: deque,
    start_index: int, end_index: int
) -> None:
    """
    Replaces content between indices start_index and end_index. 
    At least one line between start_index and end end_index needed. 
    """
    outfpath_temp = outfpath.with_suffix(".temp_outfile_ghact")
    assert start_index >= 0 and end_index >= 1, \
        f"Can not insert: {start_index=}, {end_index=}"
    f_in = (line for line in open(outfpath, 'r'))
    tree_written = False
    with open(outfpath_temp, 'w') as f_out:
        for index, line in enumerate(f_in):
            if index <= start_index:
                f_out.write(line)
            elif not tree_written:
                f_out.writelines(dirtree)
                tree_written = True
                if index >= end_index:
                    f_out.write(line)
            elif index >= end_index:
                f_out.write(line)
    outfpath.unlink() # missing_ok=True
    outfpath_temp.rename(outfpath)
