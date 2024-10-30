from pathlib import Path
import frontmatter
from fastapi import APIRouter, Request, HTTPException
from loguru import logger
from markdown_it import MarkdownIt
from starlette.responses import HTMLResponse

from docs.config import BASE_DIR
from docs.templates import templates, hotreload
from docs.site import load_site_config


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()

router.add_websocket_route("/hot-reload", endpoint=hotreload, name="hot-reload")

md = MarkdownIt()
site_config = load_site_config(f"{BASE_DIR}/docs/site_config.yml")
routes = site_config.routes()
logger.info(f"routes: {routes}")


def parse_markdown_with_frontmatter(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)
            return post.metadata, post.content
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Page not found")


def convert_markdown_to_html(markdown_content: str) -> str:
    """Convert markdown content to HTML."""
    return md.render(markdown_content)


@router.get("/{path:path}")
async def catch_all(request: Request, path: str = None):
    path = path or "index"

    # Ensure the path exists in the routes
    if f"{path}.md" not in routes:
        raise HTTPException(status_code=404, detail=f"No route for found for {path}")

    # Ensure the Markdown file exists
    md_path = Path(f"{BASE_DIR}/docs/content/{path}.md")
    metadata, markdown_content = parse_markdown_with_frontmatter(md_path)

    # Convert markdown content to HTML
    html_content = convert_markdown_to_html(markdown_content)

    # Prepare the context for the template
    context = {
        "metadata": metadata,
        "content": html_content,
        "config": site_config,
        "current_path": f"/{path}",
        "routes": routes,
    }

    # Render the template with the given context
    return templates.TemplateResponse(request, "content.html", context=context)
