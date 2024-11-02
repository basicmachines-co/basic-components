from pathlib import Path
import frontmatter
import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from pymdownx import superfences
import re

from docs.templates import templates


class HeadingExtractor(Treeprocessor):
    def __init__(self, md, examples=None):
        super().__init__(md)
        self.headings = []
        self.examples = examples or []

    def run(self, root):
        # Extract regular headings
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

        # Add "Examples" top-level heading if examples exist
        if self.examples:
            self.headings.append(
                {
                    "level": 2,  # Set the level to 1 for the top-level "Examples" heading
                    "content": "Examples",
                    "id": "examples",
                }
            )
            # Add each example as a subheading under "Examples"
            for example in self.examples:
                for name, path in example.items():
                    example_id = re.sub(r"\s+", "-", name.lower())
                    self.headings.append(
                        {
                            "level": 3,  # Set the level as appropriate for TOC depth under "Examples"
                            "content": name,
                            "id": example_id,
                        }
                    )

        return root


class HeadingExtractorExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {"examples": [[], "List of examples from metadata"]}
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        examples = self.getConfig("examples")
        heading_extractor = HeadingExtractor(md, examples)
        md.treeprocessors.register(heading_extractor, "heading_extractor", 15)
        md.heading_extractor = heading_extractor


def create_markdown(examples=None):
    extensions = [
        "pymdownx.superfences",
        "pymdownx.blocks.tab",
        "pymdownx.snippets",
        "markdown.extensions.tables",
        HeadingExtractorExtension(examples=examples),
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


def extract_headings(markdown_text, examples=None):
    md = create_markdown(examples=examples)
    md.convert(markdown_text)
    return md.heading_extractor.headings


def parse_jinja_markdown(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        post = frontmatter.loads(text)

        metadata = post.metadata
        stripped_content = post.content
        examples = metadata.get("examples", [])
        headings = extract_headings(stripped_content, examples=examples)

        template = templates.env.from_string(stripped_content)
        # Render the template with context
        template_processed_markdown = template.render()

        md = create_markdown(examples=examples)
        html_content = md.convert(template_processed_markdown)

        return metadata, headings, html_content


def doc_markdown(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        post = frontmatter.loads(text)

        metadata = post.metadata
        stripped_content = post.content
        headings = extract_headings(stripped_content)

        md = create_markdown()
        html_content = md.convert(stripped_content)

        return metadata, headings, html_content
