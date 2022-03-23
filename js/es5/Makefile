PACKAGE_NAME=src

.PHONY: format
format:
	@npm run format

.PHONY: format-check
format-check:
	@npm run format-check

.PHONY: lint
lint:
	@npm run lint

.PHONY: test
test:
	@npm run test

.PHONY: doc
doc:
	@npm run jsdoc

.PHONY: doc-view
doc-view: doc
	@google-chrome out/index.html

.PHONY: pre-commit
pre-commit: format lint test doc