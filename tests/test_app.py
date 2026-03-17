import pytest
from app import main


@pytest.fixture
def mock_env(monkeypatch, tmp_path):
    readme = tmp_path / 'README.md'
    readme.write_text(
        '# Title\n'
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->\n'
        'placeholder\n'
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->\n'
        'Footer\n'
    )
    (tmp_path / 'src').mkdir()
    (tmp_path / 'src' / 'app.py').touch()
    (tmp_path / 'src' / 'utils.py').touch()

    monkeypatch.setenv('CMD_HIGHLIGHT', 'sh')
    monkeypatch.setenv('EXCLUDE', '.git|__pycache__')
    monkeypatch.setenv(
        'INSERT_HERE_START_STRING',
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->'
    )
    monkeypatch.setenv(
        'INSERT_HERE_END_STRING',
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
    )
    monkeypatch.setenv('OUT_FILE', str(readme))
    monkeypatch.setenv('TREE_THEME', 'sh')
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_main_writes_tree(mock_env):
    main()
    content = (mock_env / 'README.md').read_text()
    assert '```sh' in content
    assert 'src' in content
    assert 'Footer' in content


def test_main_missing_file(mock_env, monkeypatch):
    monkeypatch.setenv('OUT_FILE', str(mock_env / 'nonexistent.md'))
    with pytest.raises(Exception):
        main()
