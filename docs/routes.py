from pathlib import Path
from fastapi import APIRouter, Request, HTTPException
from loguru import logger
from starlette.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from docs.config import BASE_DIR
from docs.markdown import parse_jinja_markdown
from docs.templates import templates, hotreload, template, catalog
from docs.site_config import site_config


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()

# web socket for hot reload
router.add_websocket_route("/hot-reload", endpoint=hotreload, name="hot-reload")


async def get_markdown_file(path, default="index"):
    # Ensure the Markdown file exists
    md_file_path = Path(f"{BASE_DIR}/docs/content/{path}")

    # if its a dir, look for the index.md
    if md_file_path.is_dir():
        md_file_path = Path(f"{BASE_DIR}/docs/content/{path}/{default}")

    md_file_path = md_file_path.with_suffix(".md")

    if not md_file_path.exists():
        raise HTTPException(
            status_code=404, detail=f"Markdown file {md_file_path} not found for {path}"
        )
    logger.info(f"Path '{path}' resolved to markdown file '{md_file_path}'")
    return md_file_path


async def render_content(path, md_file_path, request):
    metadata, toc, html_content = parse_jinja_markdown(md_file_path)
    # Prepare the context for the template
    context = {
        "metadata": metadata,
        "content": html_content,
        "config": site_config,
        "path": f"/{path}",
        "toc": toc,
    }
    # Render the template with the given context
    return templates.TemplateResponse(request, "content.html", context=context)


@router.get("/")
async def index(request: Request):
    context = {
        "config": site_config,
    }
    return templates.TemplateResponse(request, "index.html", context=context)


@router.get("/docs")
async def docs():
    return RedirectResponse(url="/docs/introduction")


@router.get("/examples")
async def examples(request: Request):
    context = {
        "config": site_config,
    }
    return templates.TemplateResponse(request, "examples.html", context=context)


@router.get("/icons/search")
async def icons_search(request: Request, query: str = ""):
    icons = site_config.icons
    results = [
        {
            "name": icon.name,
            "icon": catalog.render(f"{icon.name}Icon", className="w-8 h-8"),
        }
        for icon in icons
        if query.lower() in icon.name.lower()
    ]

    return template(request, "icons_search.html", context={"results": results})


@router.get("/{path:path}")
async def content(request: Request, path: str):
    md_path = await get_markdown_file(path)
    return await render_content(path, md_path, request)
