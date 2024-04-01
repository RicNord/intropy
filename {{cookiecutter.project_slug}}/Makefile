
# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '##'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: test-all
test-all: ## Run all tests with tox
	@echo "+ $@"
	@tox

.PHONY: pytest
pytest: ## Run pytest
	@echo "+ $@"
	@pytest tests

.PHONY: style
style: lint format type ## Run lint formatting and type check
	@echo "+ $@"

.PHONY: lint
lint: ## Run lint
	@echo "+ $@"
	@ruff check

.PHONY: format
format: ## Run formatting
	@echo "+ $@"
	@ruff format

.PHONY: type
type: ## Run type checking
	@echo "+ $@"
	@mypy .

.PHONY: auto-fix
auto-fix: ## Auto-fix possible style issues
	@echo "+ $@"
	@ruff format
	@ruff check --fix --show-fixes

.PHONY: build
build: clean ## Build distribution
	@echo "+ $@"
	@python -m build
	@ls -l dist

.PHONY: clean-tox
clean-tox: # Remove tox testing artifacts
	@echo "+ $@"
	@rm -rf .tox/

.PHONY: clean-coverage
clean-coverage: # Remove coverage reports
	@echo "+ $@"
	@rm -rf htmlcov/
	@rm -rf .coverage
	@rm -rf coverage.xml

.PHONY: clean-pytest
clean-pytest: # Remove pytest cache
	@echo "+ $@"
	@rm -rf .pytest_cache/

.PHONY: clean-docs
clean-docs: # Remove local docs
	@echo "+ $@"
	@rm -rf docs/_build

.PHONY: clean-build
clean-build: # Remove build artifacts
	@echo "+ $@"
	@rm -rf build/
	@rm -rf dist/
	@find . -name '*.egg-info' -exec rm -rf {} +
	@find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: # Remove Python file artifacts
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -exec rm -f {} +
	@find . -type f -name '*.pyo' -exec rm -f {} +

.PHONY: clean
clean: clean-build clean-pyc clean-tox clean-coverage clean-pytest clean-docs ## Remove all file artifacts
	@echo "+ $@"

.PHONY: gen-req
gen-req: ## Generates new requirements{,-dev}.txt files from Pipfile.lock
	@echo "+ $@"
	@pipenv requirements --dev-only | sed '/^-i /d' > requirements-dev.txt
	@pipenv requirements | sed '/^-i /d' > requirements.txt

.PHONY: lock
lock: # Updates the Pipfile.lock
	@echo "+ $@"
	@pipenv lock --dev

.PHONY: upgrade-deps
upgrade-deps: lock gen-req ## Upgrades dependencies
	@echo "+ $@"

.PHONY: dev
dev: ## Set-up development environment
	@echo "+ $@"
	@pipenv sync --dev
