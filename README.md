# Intropy

[![Version](https://img.shields.io/pypi/v/intropy?color=blue)](https://pypi.org/project/intropy/)
[![Build Status](https://github.com/RicNord/intropy/actions/workflows/ci.yaml/badge.svg)](https://github.com/RicNord/intropy/actions)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter),
intropy is a framework for jump-starting production-grade python projects. The
python project will be generated and configured automatically with:

- Build system
- Test and code quality tooling
- Documentation
- Automation pipelines
- etc...

## Features

- [Ruff](https://docs.astral.sh/ruff/) | Linter and formatter (Optionally
  strict [Black](https://black.readthedocs.io/en/stable/) as code formatter)
- [Pytest](https://docs.pytest.org/en/latest/) | Test framework
- [Tox](https://tox.wiki/en/latest/) | Standardized testing and automation
- [Coverage](https://coverage.readthedocs.io/en/latest/) | Code coverage
- [Mypy](https://www.mypy-lang.org/) | Static type checker
- Package and environment management
  - Deployable applications: [Pipenv](https://pipenv.pypa.io/en/latest/) |
    Version pinning and virtual environment setup
  - Libraries: Pyproject explicit defined dependencies
- [Pre-commit](https://pre-commit.com/) | pre-commit hooks
- [Bump my version](https://callowayproject.github.io/bump-my-version/) | Bump
  semantic version
- [Sphinx](https://www.sphinx-doc.org/) | Documentation tool
- [Logging](https://docs.python.org/3/library/logging.html) boilerplate
- DevOps platform options
  - Github
    - Github workflows | CI and publishing to PyPi
    - Github templates | Pull Requests and Issues
  - Azure Devops
    - Azure pipelines | CI
- Makefile for convenience

## Usage

Install cookiecutter:

```shell
pip install cookiecutter
```

Create project:

```shell
cookiecutter https://github.com/RicNord/intropy
```

You will be prompted for some values. After that the project will be generated!

### (Optional) Standalone CLI

A wrapper around the `cookiecutter` CLI is also provided and can be installed
with:

```shell
pip install intropy
```

For API reference see:

```shell
intropy --help
```
