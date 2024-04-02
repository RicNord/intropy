import datetime

import pytest

# NOTE
# cookies is a fixure provided by the pytest-cookies plugin

_PROJECT_FILE = "pyproject.toml"


def test_bake_with_defaults(cookies):
    result = cookies.bake()
    assert result.project_path.is_dir()
    assert result.exit_code == 0
    assert result.exception is None

    toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert _PROJECT_FILE in toplevel_files
    assert ".editorconfig" in toplevel_files
    assert ".gitignore" in toplevel_files
    assert "Makefile" in toplevel_files
    assert "README.md" in toplevel_files
    assert "tests" in toplevel_files
    assert "tox.ini" in toplevel_files


@pytest.mark.parametrize(
    "project_name,expected",
    [
        ("snake_case", "snake_case"),
        ("camelCase", "camelcase"),
        ("kebab-case", "kebab_case"),
        ("ODD-WIth space", "odd_with_space"),
    ],
)
def test_bake_project_with_custom_names(cookies, project_name, expected):
    result = cookies.bake(extra_context={"project_name": project_name})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == expected
    assert result.project_path.is_dir()


@pytest.mark.parametrize(
    "license,expected",
    [
        ("MIT", "MIT "),
    ],
)
def test_bake_selecting_license(cookies, license, expected):
    result = cookies.bake(extra_context={"open_source_license": license})
    assert expected in result.project_path.joinpath("LICENSE").read_text()
    assert "LICENSE" in result.project_path.joinpath(_PROJECT_FILE).read_text()


def test_bake_not_open_source(cookies):
    result = cookies.bake(extra_context={"open_source_license": "Not open source"})
    toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert _PROJECT_FILE in toplevel_files
    assert "LICENSE" not in toplevel_files
    assert "license" not in result.project_path.joinpath(_PROJECT_FILE).read_text()


def test_year_in_license_file(cookies):
    result = cookies.bake()
    license_file_path = result.project_path.joinpath("LICENSE")
    now = datetime.datetime.now()
    assert str(now.year) in license_file_path.read_text()
