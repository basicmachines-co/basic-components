import typing
from pathlib import Path

import arel

import jinjax
from jinja2.ext import DebugExtension
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from loguru import logger

import docs.config
from docs.config import BASE_DIR

COMPONENT_DIR = f"{BASE_DIR}/components"
TEMPLATE_DIR = f"{BASE_DIR}/docs/templates"
DOCS_COMPONENT_DIR = f"{TEMPLATE_DIR}/components"
DOCS_LAYOUT_DIR = f"{TEMPLATE_DIR}/layouts"

# hot reloading for local env
hotreload = arel.HotReload(
    paths=[
        arel.Path(TEMPLATE_DIR),
        arel.Path(DOCS_LAYOUT_DIR),
        arel.Path(COMPONENT_DIR),
    ],
)

# configure Jinja template location
templates = Jinja2Templates(directory=f"{TEMPLATE_DIR}")
templates.env.add_extension(DebugExtension)
templates.env.globals["hotreload"] = hotreload
templates.env.globals["DEBUG"] = docs.config.settings.ENVIRONMENT == "local"
templates.env.autoescape = False


# configure JinjaX component catalog
templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)
catalog.add_folder(f"{COMPONENT_DIR}/ui")
catalog.add_folder(f"{COMPONENT_DIR}/icons")
catalog.add_folder(f"{DOCS_COMPONENT_DIR}")
catalog.add_folder(f"{DOCS_LAYOUT_DIR}")

logger.info(f"template dir: {TEMPLATE_DIR}")
logger.info(f"layout dir: {DOCS_LAYOUT_DIR}")
logger.info(f"component dir: {COMPONENT_DIR}")
logger.info(f"docs component dir: {DOCS_COMPONENT_DIR}")


def setup_filters():
    def include_file(path: str) -> str:
        file_path = Path(path)
        if not file_path.exists():
            return f"<!-- {path} not found -->"
        return file_path.read_text()

    templates.env.filters["include_file"] = include_file


def template(
    request: Request,
    name: str,
    context: dict,
    status_code: int = 200,
    headers: typing.Optional[typing.Mapping[str, str]] = None,
    **kwargs,
) -> templates.TemplateResponse:  # pyright: ignore [reportInvalidTypeForm]
    return templates.TemplateResponse(
        request, name, context, status_code, headers, **kwargs
    )


def render(
    name: str,
    **kwargs,
) -> str:
    return catalog.render(name, **kwargs)
