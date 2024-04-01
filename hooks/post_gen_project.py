#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(relative_filepath):
    FILE_PATH = os.path.join(PROJECT_DIRECTORY, relative_filepath)
    if os.path.isfile(FILE_PATH):
        os.remove(FILE_PATH)


if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
