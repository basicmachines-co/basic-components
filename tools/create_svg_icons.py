import os
import re
from os import mkdir

import typer
import json

app = typer.Typer()

# Template for the JinjaX component
component_template = """{{#def
    className: str = "h-4 w-4",
#}}
<!-- {component_name} -->
<svg
  class="{{{{ className }}}}"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  aria-hidden="true"
  {{{{ attrs.render() }}}}
>
{svg_content}
</svg>
"""


def extract_svg_content(svg_text: str) -> str:
    """
    Extracts the content inside the SVG tags.
    """
    # Match the opening <svg> tag and its attributes
    svg_open_tag_pattern = re.compile(r"<svg[^>]*>", re.IGNORECASE)
    # Find and remove the opening <svg> tag
    svg_text = svg_open_tag_pattern.sub("", svg_text)
    # Remove the closing </svg> tag
    svg_text = svg_text.replace("</svg>", "").strip()
    return svg_text


@app.command()
def create_icons(svg_dir: str, output_dir: str, json_output: str = "icons.json"):
    """
    Converts SVG files into JinjaX components and generates a JSON file with icon metadata.
    """
    icon_metadata = []
    mkdir(output_dir)

    # Iterate over each SVG file in the directory
    for filename in os.listdir(svg_dir):
        if filename.endswith(".svg"):
            # Read the SVG content
            with open(os.path.join(svg_dir, filename), "r") as file:
                svg_content = file.read()

            # Extract the name of the component by converting the filename (e.g., 'a-arrow-down.svg' -> 'AArrowDown')
            name_parts = filename.replace(".svg", "").split("-")
            component_name = "".join(part.capitalize() for part in name_parts)

            # Extract the inner SVG content (e.g., paths, groups, etc.)
            svg_inner_content = extract_svg_content(svg_content)

            # Replace placeholder in the template with the actual SVG content
            component_content = component_template.format(
                component_name=component_name, svg_content=svg_inner_content
            )

            file_name = f"{component_name}Icon.jinja"
            # Define the output file path for the component
            output_path = os.path.join(output_dir, file_name)

            # Write the component content to the output file
            with open(output_path, "w") as output_file:
                output_file.write(component_content)

            # Add metadata to the JSON
            icon_metadata.append({"name": component_name, "file": file_name})

            print(f"Component {file_name} created.")

    output_path = os.path.join(output_dir, json_output)

    # Write metadata to a JSON file
    with open(output_path, "w") as json_file:
        json.dump(icon_metadata, json_file, indent=2)
        print(f"Icon metadata JSON file created at {output_path}.")


if __name__ == "__main__":
    app()
