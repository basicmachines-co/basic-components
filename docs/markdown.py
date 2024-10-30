from pathlib import Path
from fastapi import HTTPException
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

import frontmatter

md = MarkdownIt().use(front_matter_plugin).use(footnote_plugin).enable("table")


def parse_markdown(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            # frontmatter
            post = frontmatter.loads(text)

            # headings from markdown
            headings = extract_headings(text)

            # content as html
            html_content = md.render(text)

            return post.metadata, headings, html_content
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Markdown not found for {file_path}"
        )


def extract_headings(markdown_content):
    tokens = md.parse(markdown_content)
    headings = []

    for token in tokens:
        if token.type == "heading_open":
            heading_level = int(token.tag[1])  # Extract heading level (e.g., h2 -> 2)
            heading_content = extract_heading_content(tokens, token)
            if heading_content:
                headings.append({"level": heading_level, "content": heading_content})

    return headings


def extract_heading_content(tokens, heading_token):
    content_token = tokens[
        tokens.index(heading_token) + 1
    ]  # The next token is the text content
    if content_token.type == "inline":
        return content_token.content
    return None
