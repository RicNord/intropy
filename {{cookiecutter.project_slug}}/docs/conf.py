#!/usr/bin/env python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

import {{ cookiecutter.project_slug }}

# Execute as file cwd
sys.path.insert(0, os.path.abspath(".."))

project = "{{ cookiecutter.project_slug }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"
release = {{ cookiecutter.project_slug }}.__version__
version = {{ cookiecutter.project_slug }}.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Pull in docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.coverage",
    "sphinx.ext.todo",
    "sphinx.ext.autosummary",
    "myst_parser",  # Import markdown to rst
]

# If true display todos in docs
todo_include_todos = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
