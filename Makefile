.PHONY: install docs-tailwind docs-tailwind-watch docs-dev docs-run

VENV := $(shell pwd)/.venv
PYTHON := $(VENV)/bin/python
UV := $(VENV)/bin/uv
MKDOCS := $(VENV)/bin/mkdocs

$(VENV)/bin/uv:
	python -m venv $(VENV)
	$(PYTHON) -m pip install uv

install: $(VENV)/bin/uv
	$(UV) sync

docs-tailwind:
	cd documentation && npm install && npx tailwindcss init && npm link tailwindcss && npm run build

docs-tailwind-watch:
	cd documentation && npm install && npx tailwindcss init && npm link tailwindcss && npm run watch

docs-dev:
	$(UV) run fastapi dev docs/app.py --reload --reload-include *.yml

docs-run:
	$(UV) run fastapi run docs/app.py --port 10000
