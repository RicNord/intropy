import pathlib

from intropy import cli

_PROJECT_FILE = "pyproject.toml"

TEMPLATE_LOCATION = pathlib.Path(__file__).parent.parent.resolve()


def test_cli_runner(tmpdir):
    exit_code = cli.main(
        [str(TEMPLATE_LOCATION), "--output-dir", str(tmpdir), "--no-input"]
    )
    project_path = tmpdir.join("python_project")
    assert exit_code == 0
    assert project_path.check(dir=1)

    toplevel_files = [f.basename for f in project_path.listdir()]
    assert _PROJECT_FILE in toplevel_files
    assert ".editorconfig" in toplevel_files
    assert ".gitignore" in toplevel_files
    assert "Makefile" in toplevel_files
    assert "README.md" in toplevel_files
    assert "tests" in toplevel_files
    assert "tox.ini" in toplevel_files
