"""
Django example application demonstrating:
- JinjaX component integration
- Static file serving for Tailwind CSS
- HTMX dynamic updates
- Component rendering
"""

from pathlib import Path
import django
from django.core.management import execute_from_command_line
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from basic_components.utils.tailwind import tw
from basic_components.utils.jinjax import setup_component_catalog


import jinja2
import jinjax

# Only configure settings if they haven't been configured yet
if not settings.configured:
    # Configure Django settings
    BASE_DIR = Path(__file__).resolve().parent

    settings.configure(
        DEBUG=True,
        SECRET_KEY="insecure-key-for-demo",
        ROOT_URLCONF=__name__,
        MIDDLEWARE=[
            "django.middleware.security.SecurityMiddleware",
            "django.middleware.common.CommonMiddleware",
        ],
        INSTALLED_APPS=[
            "django.contrib.staticfiles",
        ],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.jinja2.Jinja2",
                "DIRS": [BASE_DIR / "templates"],
                "APP_DIRS": True,
                "OPTIONS": {
                    "environment": f"{__name__}.environment",
                },
            }
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        },
        STATIC_URL="static/",
        STATICFILES_DIRS=[
            BASE_DIR / "static",
        ],
    )
    django.setup()


# Configure JinjaX environment
def environment(**options):
    env = jinja2.Environment(**options)
    env.add_extension(jinjax.JinjaX)

    # Add cn to globals
    env.globals["cn"] = tw

    # Setup JinjaX catalog
    catalog = jinjax.Catalog(jinja_env=env)
    setup_component_catalog(catalog)

    return env


def get_catalog():
    return django.template.engines["jinja2"].env.globals["catalog"]


# Define views
def index(request):
    return render(request, "index.html")


def button(request):
    """Example endpoint demonstrating direct component rendering.
    Used by htmx for dynamic button updates.
    """
    catalog = get_catalog()
    return HttpResponse(
        catalog.render("Button", variant="destructive", _content="HTMX IS ENABLED!")
    )


# URL patterns
urlpatterns = [
    path("", index),
    path("button/", button, name="button"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# WSGI application
application = get_wsgi_application()

# Command line interface
if __name__ == "__main__":
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:10000"])
