PACKAGE_NAME=src

.PHONY: format
format:
	@poetry run isort .
	@poetry run black .

.PHONY: format-check
format-check:
	@poetry run isort --check .
	@poetry run black --check .

.PHONY: lint
lint:
	@poetry run pylint -d C,R,fixme $(PACKAGE_NAME)
	@poetry run mypy -p $(PACKAGE_NAME)

.PHONY: test
test:
	@poetry run pytest

.PHONY: pre-commit
pre-commit: format lint test
	