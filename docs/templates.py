import os
import typing
from pathlib import Path

import arel

import jinjax
from icecream import ic
from jinja2 import pass_context
from jinja2.ext import DebugExtension
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from loguru import logger

import docs.config
from basic_components.utils.jinjax import setup_component_catalog
from basic_components.utils.tailwind import tw
from docs.config import BASE_DIR

COMPONENT_DIR = f"{BASE_DIR}/components"
TEMPLATE_DIR = f"{BASE_DIR}/docs/templates"
DOCS_COMPONENT_DIR = f"{TEMPLATE_DIR}/components"
DOCS_LAYOUT_DIR = f"{TEMPLATE_DIR}/layouts"

# hot reloading for local env
hotreload = arel.HotReload(
    paths=[
        arel.Path(f"{BASE_DIR}"),
    ],
)


@pass_context
def include_file(context, path):
    try:
        with open(Path(path), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"<!-- {path} not found -->"


def filename(value):
    # Return only the filename with the extension
    return os.path.basename(value)


# configure Jinja template location
templates = Jinja2Templates(directory=f"{TEMPLATE_DIR}")
templates.env.add_extension(DebugExtension)
templates.env.globals["hotreload"] = hotreload
templates.env.globals["DEBUG"] = docs.config.settings.ENVIRONMENT == "local"
templates.env.filters["include_file"] = include_file
templates.env.filters["filename"] = filename
templates.env.filters["include_file"] = include_file
templates.env.autoescape = False

# Add cn to globals
templates.env.globals["cn"] = tw

# configure JinjaX component catalog
templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)
catalog = setup_component_catalog(catalog, components_dir=COMPONENT_DIR)
catalog.add_folder(f"{TEMPLATE_DIR}")  # remove with IncludeTemplate
catalog.add_folder(f"{DOCS_COMPONENT_DIR}")
catalog.add_folder(f"{DOCS_LAYOUT_DIR}")


logger.info(f"template dir: {TEMPLATE_DIR}")
ic(f"catalog paths: {catalog.paths}")


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
