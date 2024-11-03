from pathlib import Path

import frontmatter
import markdown
from pymdownx import superfences

from docs.templates import templates


def create_markdown(examples=None):
    extensions = [
        "pymdownx.superfences",
        "pymdownx.blocks.tab",
        "pymdownx.snippets",
        "markdown.extensions.tables",
        "markdown.extensions.toc",
    ]
    extension_configs = {
        "pymdownx.superfences": {
            "custom_fences": [
                {
                    "name": "html",
                    "class": "language-html",
                    "format": superfences.fence_code_format,
                }
            ]
        },
    }
    return markdown.Markdown(extensions=extensions, extension_configs=extension_configs)


def parse_jinja_markdown(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        post = frontmatter.loads(text)

        metadata = post.metadata
        stripped_content = post.content
        examples = metadata.get("examples", [])

        md = create_markdown(examples=examples)
        html_content = md.convert(stripped_content)
        toc = md.toc

        # Render the template with context
        template = templates.env.from_string(html_content)
        rendered_template = template.render()
        return metadata, toc, rendered_template
