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
                heading_id = re.sub(
                    r"\s+", "-", element.text.lower()
                )  # Generate ID from heading text
                element.set("id", heading_id)  # Add ID attribute to the heading
                self.headings.append(
                    {
                        "level": int(element.tag[1]),
                        "content": element.text,
                        "id": heading_id,  # Store the generated ID for reference
                    }
                )
        return root


class HeadingExtractorExtension(Extension):
    def extendMarkdown(self, md):
        heading_extractor = HeadingExtractor(md)
        md.treeprocessors.register(heading_extractor, "heading_extractor", 15)
        md.heading_extractor = heading_extractor


extensions = [
    "pymdownx.superfences",
    "pymdownx.blocks.tab",
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

md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)


def extract_headings(markdown_text):
    md.convert(markdown_text)
    return md.heading_extractor.headings


def parse_markdown(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            post = frontmatter.loads(text)  # Load frontmatter

            # Get metadata and stripped Markdown content
            metadata = post.metadata
            stripped_content = post.content

            # Extract headings
            headings = extract_headings(stripped_content)

            # Convert content to HTML
            html_content = md.convert(stripped_content)

            return metadata, headings, html_content
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Markdown not found for {file_path}"
        )
