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
	@poetry run pylint -d C,R,fixme $(PACKAGE_NAME) tests
	@poetry run mypy --show-error-codes $(PACKAGE_NAME) tests

.PHONY: test
test:
	@poetry run pytest
	@poetry run coverage-badge -o coverage.svg

.PHONY: safety-check
safety-check:
	@poetry export --dev --format=requirements.txt --output=requirements.txt
	@poetry run safety check --file=requirements.txt
	@rm requirements.txt

.PHONY: pre-commit
pre-commit: format lint test safety-check