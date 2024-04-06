# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
{% if cookiecutter.black_formatting == 'y' -%}
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
{% endif -%}
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Install

- TODO | How to install this project

## Usage

- TODO | How to use this project

{% if cookiecutter.is_cli_tool -%}
```shell
{{ cookiecutter.project_slug.lower().replace('_', '-') }} --help
```
{%- endif %}

## Development

To list available commands for your convenience:

```shell
make help
```

### Local environment setup

It is recommended to use [Pipenv](https://pipenv.pypa.io/en/latest/index.html),
to create a virtual environment with necessary dependencies run:

```shell
pipenv shell
pipenv sync --dev
```

Or create and manage your virtual environment more manually:

```shell
python3 -m venv ./venv
source ./venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Run tests

```shell
make pytest # Run pytest
make style # Run lint formatting and type check
make test-all # Run all tests with tox

make auto-fix # Auto-fix possible style issues
```

### Pre-commit hooks

To install optional [pre-commit](https://pre-commit.com/) hooks; after
environment set-up run:

```bash
pre-commit install
```

## Project maintenance

Intended for project maintainers

### Release

[Bump my version](https://callowayproject.github.io/bump-my-version/) is used
to bump the semantic version of the project.

For details see:

```shell
bump-my-version bump --help
```

Bump my version is configured to create a `new commit` and `tag` it with the
new version when a version is bumped.

To publish the new version to [PyPi](https://pypi.org/) run:

```shell
make publish-test # Publish pkg to PyPi test instance
make publish # Publish pkg to PyPi
```

This will build the project and publish to PyPi with help of
[Twine](https://twine.readthedocs.io/en/stable/). For authentication and
additional target repositories refer to your
[.pypirc](https://packaging.python.org/en/latest/specifications/pypirc/)
configuration file.

### Upgrade dependencies

To upgrade dependencies run:

```shell
make upgrade-deps
```

