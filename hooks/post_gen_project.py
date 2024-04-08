#!/usr/bin/env python
import pathlib
import subprocess
from shutil import which
import sys

GIT_COMMIT_MESSAGE = """Adding generated project resources


This project was generated with the help of:
https://github.com/RicNord/intropy"""


def executable_exist(name: str) -> bool:
    return which(name) is not None


def git_init():
    if executable_exist("git"):
        try:
            subprocess.run(
                ["git", "init"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
            subprocess.run(
                ["git", "commit", "-m", "Intital commit", "--allow-empty"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )

            subprocess.run(
                ["git", "add", "."],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )

            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    GIT_COMMIT_MESSAGE,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
        except Exception as e:
            print(
                f"Could not initialize git repository. Continue project set-up anyway. Exception: {e}",
                file=sys.stderr,
            )


def main():
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        pathlib.Path("LICENSE").unlink()

    if not {{cookiecutter.is_cli_tool}}:
        pathlib.Path("{{ cookiecutter.project_slug }}", "cli.py").unlink()
        pathlib.Path("tests", "test_cli.py").unlink()

    if {{cookiecutter.git_init}}:
        git_init()


if __name__ == "__main__":
    main()
