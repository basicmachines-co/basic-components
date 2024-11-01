from pathlib import Path
from fastapi import APIRouter, Request, HTTPException
from icecream import ic
from loguru import logger
from starlette.responses import HTMLResponse

from docs.config import BASE_DIR
from docs.markdown import parse_markdown
from docs.templates import templates, hotreload
from docs.site import load_site_config


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()

# web socket for hot reload
router.add_websocket_route("/hot-reload", endpoint=hotreload, name="hot-reload")


site_config = load_site_config(f"{BASE_DIR}/docs/site_config.yml")
site_config_routes = site_config.routes()
logger.info(f"routes: {site_config_routes}")


@router.get("/{path:path}")
async def catch_all(request: Request, path: str = None):
    path = path or "index"

    current_path = f"/{path}"

    # Ensure the path exists in the routes
    if current_path not in site_config_routes:
        raise HTTPException(status_code=404, detail=f"No route for found for {path}")

    # Ensure the Markdown file exists
    md_path = Path(f"{BASE_DIR}/docs/content/{path}.md")

    metadata, toc, html_content = parse_markdown(md_path)

    # Prepare the context for the template
    context = {
        "metadata": metadata,
        "content": html_content,
        "config": site_config,
        "current_path": current_path,
        "toc": toc,
    }
    ic(context)

    # Render the template with the given context
    return templates.TemplateResponse(request, "component.html", context=context)
