from pathlib import Path
from fastapi import HTTPException
import frontmatter
import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from pymdownx import superfences
import re


class HeadingExtractor(Treeprocessor):
    def __init__(self, md):
        super().__init__(md)
        self.headings = []

    def run(self, root):
        for element in root.iter():
            if element.tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                heading_id = re.sub(r"\s+", "-", element.text.lower())
                element.set("id", heading_id)
                self.headings.append(
                    {
                        "level": int(element.tag[1]),
                        "content": element.text,
                        "id": heading_id,
                    }
                )
        return root


class HeadingExtractorExtension(Extension):
    def extendMarkdown(self, md):
        heading_extractor = HeadingExtractor(md)
        md.treeprocessors.register(heading_extractor, "heading_extractor", 15)
        md.heading_extractor = heading_extractor


def create_markdown():
    extensions = [
        "pymdownx.superfences",
        "pymdownx.blocks.tab",
        "pymdownx.snippets",
        HeadingExtractorExtension(),
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


def extract_headings(markdown_text):
    md = create_markdown()
    md.convert(markdown_text)
    return md.heading_extractor.headings


def parse_markdown(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            post = frontmatter.loads(text)

            metadata = post.metadata
            stripped_content = post.content

            headings = extract_headings(stripped_content)

            md = create_markdown()
            html_content = md.convert(stripped_content)

            return metadata, headings, html_content
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Markdown not found for {file_path}"
        )
