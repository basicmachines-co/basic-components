.PHONY: install docs-tailwind docs-tailwind-watch docs-dev docs-run

VENV := $(shell pwd)/.venv
PYTHON := $(VENV)/bin/python
UV := $(VENV)/bin/uv
MKDOCS := $(VENV)/bin/mkdocs

$(VENV)/bin/uv:
	python -m venv $(VENV)
	$(PYTHON) -m pip install uv

install: install-python install-node

install-python: $(VENV)/bin/uv
	$(UV) sync

install-node:
	cd docs && npm install

docs-tailwind:
	npx tailwindcss init && npm link tailwindcss && npm run build

docs-tailwind-watch:
	npx tailwindcss init && npm link tailwindcss && npm run watch

docs-dev:
	$(UV) run fastapi dev docs/app.py --reload --reload-include *.yml

docs-run:
	$(UV) run fastapi run docs/app.py --port 10000

create-icons:
	$(UV) run tools/create_svg_icons.py ../shadcn-ui/node_modules/lucide-static/icons components/ui/icons

build:
	$(UV) build .