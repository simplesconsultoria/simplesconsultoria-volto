SHELL := /bin/bash
NOW:=$(shell date -u +"%Y%m%d%H%M%S")
PACKAGE_NAME = simplesconsultoria.volto
PACKAGE_PATH = src/simplesconsultoria/volto
IMAGE_NAME = simplesconsultoria/simplesconsultoria.volto
CHECK_PATH   = setup.py scripts/ $(PACKAGE_PATH)


# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/


.PHONY: black
black: ## Format codebase
	./bin/black $(CHECK_PATH)


.PHONY: isort
isort: ## Format imports in the codebase
	./bin/isort $(CHECK_PATH)


.PHONY: format
format: black isort ## Format the codebase according to our standards


.PHONY: lint
lint: lint-isort lint-black lint-code ## check style with flake8


.PHONY: lint-black
lint-black: ## validate black formating
	./bin/black --check --diff $(CHECK_PATH)


.PHONY: lint-code
lint-code: ## validate using code-analysis
	./bin/code-analysis


.PHONY: lint-isort
lint-isort: ## validate using isort
	./bin/isort --check-only $(CHECK_PATH)


.PHONY: test_all
test_all: lint ## run linters and tests
	./bin/test

.PHONY: test
test: ## run tests
	./bin/test

.PHONY: test_quiet
test_quiet: ## run tests removing deprecation warnings
	PYTHONWARNINGS=ignore ./bin/test

.PHONY: install
install: clean ## Installs this package and runs buildout
	pip install -r requirements.txt
	buildout -c buildout.cfg

.PHONY: update
update: ## Update this installation
	git pull
	buildout -Nc buildout.cfg

.PHONY: create_site
create_site: ## Create a new site from scratch
	PYTHONWARNINGS=ignore ./bin/instance run ./scripts/create_site.py

.PHONY: start
start: ## Start a Plone instance on localhost:8080
	PYTHONWARNINGS=ignore ./bin/instance fg
