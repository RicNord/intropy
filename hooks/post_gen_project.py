#!/usr/bin/env python
import pathlib


def main():
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        pathlib.Path("LICENSE").unlink()

    if not {{cookiecutter.is_cli_tool}}:
        pathlib.Path("{{ cookiecutter.project_slug }}", "cli.py").unlink()
        pathlib.Path("tests", "test_cli.py").unlink()


if __name__ == "__main__":
    main()
