.PHONY: test lint format
test:
	python -m pytest -q
lint:
	ruff check .
format:
	ruff format .
