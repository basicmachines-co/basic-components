# app.py
from flask import Flask
import jinja2
import jinjax
from basic_components.utils.jinjax import setup_component_catalog
from basic_components.utils.tailwind import tw

# Initialize Flask
app = Flask(__name__)

# Configure Jinja environment with JinjaX
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"), extensions=[jinjax.JinjaX]
)
# Add cn to globals
env.globals["cn"] = tw

# Setup JinjaX catalog
catalog = jinjax.Catalog(jinja_env=env)
setup_component_catalog(catalog)


# Routes
@app.route("/")
def index():
    return env.get_template("index.html").render()


@app.route("/button")
def button():
    """Example endpoint for HTMX updates."""
    return catalog.render("Button", variant="destructive", _content="HTMX IS ENABLED!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
