from pathlib import Path
from fastapi import APIRouter, Request, HTTPException
from jinja2 import Template
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

router.add_websocket_route("/hot-reload", endpoint=hotreload, name="hot-reload")


from markdown_it.renderer import RendererHTML
import re


class CustomHTMLRenderer(RendererHTML):
    def render_html_block(self, tokens, idx, options, env):
        token = tokens[idx]
        return self._preserve_case(token.content)

    def render_html_inline(self, tokens, idx, options, env):
        token = tokens[idx]
        return self._preserve_case(token.content)

    def _preserve_case(self, content: str) -> str:
        """Ensure that HTML tags remain case-sensitive."""
        # Regex to find component-like tags with optional attributes
        tag_pattern = r"(<\/?\w+\b(?:\s*[^>]*?)?>)"
        matches = re.finditer(tag_pattern, content)
        result = ""
        last_index = 0

        # Rebuild the string by keeping the original case of the tags
        for match in matches:
            start, end = match.span()
            result += content[last_index:start] + match.group(1)
            last_index = end

        result += content[last_index:]
        return result


md = (
    MarkdownIt(renderer_cls=CustomHTMLRenderer)
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .enable("table")
)

site_config = load_site_config(f"{BASE_DIR}/docs/site_config.yml")
routes = site_config.routes()
logger.info(f"routes: {routes}")


def parse_markdown(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

            post = frontmatter.loads(text)
            html_text = md.render(text)
            return post.metadata, Markup(html_text)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Page not found")


@router.get("/{path:path}")
async def catch_all(request: Request, path: str = None):
    path = path or "index"

    # Ensure the path exists in the routes
    if f"{path}.md" not in routes:
        raise HTTPException(status_code=404, detail=f"No route for found for {path}")

    # Ensure the Markdown file exists
    md_path = Path(f"{BASE_DIR}/docs/content/{path}.md")
    metadata, html_content = parse_markdown(md_path)

    # Process the HTML through Jinja
    template = Template(html_content)
    rendered_content = template.render()

    # Prepare the context for the template
    context = {
        "metadata": metadata,
        "content": rendered_content,
        "config": site_config,
        "current_path": f"/{path}",
        "routes": routes,
    }

    # Render the template with the given context
    return templates.TemplateResponse(request, "content.html", context=context)
