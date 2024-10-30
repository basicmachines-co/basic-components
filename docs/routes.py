from pathlib import Path
from fastapi import APIRouter, Request, HTTPException
from loguru import logger
from markdown_it import MarkdownIt
from markupsafe import Markup
from starlette.responses import HTMLResponse
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

from docs.config import BASE_DIR
from docs.templates import templates, hotreload
from docs.site import load_site_config
import frontmatter


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()

# web socket for hot reload
router.add_websocket_route("/hot-reload", endpoint=hotreload, name="hot-reload")


md = MarkdownIt().use(front_matter_plugin).use(footnote_plugin).enable("table")

site_config = load_site_config(f"{BASE_DIR}/docs/site_config.yml")
site_config_routes = site_config.routes()
logger.info(f"routes: {site_config_routes}")


def parse_markdown(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            # frontmatter
            post = frontmatter.loads(text)
            # content as html
            html_content = md.render(text)
            return post.metadata, Markup(html_content)
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Markdown not found for {file_path}"
        )


@router.get("/{path:path}")
async def catch_all(request: Request, path: str = None):
    path = path or "index"

    # Ensure the path exists in the routes
    if f"{path}.md" not in site_config_routes:
        raise HTTPException(status_code=404, detail=f"No route for found for {path}")

    # Ensure the Markdown file exists
    md_path = Path(f"{BASE_DIR}/docs/content/{path}.md")
    metadata, html_content = parse_markdown(md_path)

    # Prepare the context for the template
    context = {
        "metadata": metadata,
        "content": html_content,
        "config": site_config,
        "current_path": f"/{path}",
        "routes": site_config_routes,
    }

    # Render the template with the given context
    return templates.TemplateResponse(request, "content.html", context=context)
