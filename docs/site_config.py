import json

from pydantic import BaseModel, HttpUrl
from typing import List, Union

from docs.config import settings, BASE_DIR


class SVGIcon(BaseModel):
    name: str
    file: str


class NavItem(BaseModel):
    type: str = "item"
    group: str = None
    title: str
    href: str


class NavGroup(BaseModel):
    type: str = "group"
    title: str
    items: List[Union[NavItem, "NavGroup"]]


class SiteConfig(BaseModel):
    """The top-level configuration for the site."""

    site_name: str
    repo_url: HttpUrl
    mainNav: List[NavItem]
    sidebarNav: List[Union[NavItem, NavGroup]]
    icons: List[SVGIcon]


def load_icons(json_path: str) -> List[SVGIcon]:
    with open(json_path, "r") as file:
        icons_data = json.load(file)
    return [SVGIcon.model_validate(icon) for icon in icons_data]


config = {
    "site_name": settings.APP_NAME,
    "repo_url": "https://github.com/basicmachines-co/basic-components",
    "mainNav": [
        {"title": "Docs", "group": "/docs", "href": "/docs/introduction"},
        {
            "title": "Components",
            "group": "/components",
            "href": "/components/accordion",
        },
        {"title": "Examples", "group": "/examples", "href": "/examples"},
    ],
    "sidebarNav": [
        {
            "title": "Getting Started",
            "items": [
                {"title": "Introduction", "href": "/docs/introduction"},
                {"title": "Modern Tools", "href": "/docs/modern_tools"},
                {"title": "Components", "href": "/docs/components"},
                {"title": "Installation", "href": "/docs/installation"},
                {"title": "CLI", "href": "/docs/cli"},
                {"title": "AI", "href": "/docs/ai"},
                {"title": "Dark Mode", "href": "/docs/dark_mode"},
                {"title": "Typography", "href": "/docs/typography"},
                {"title": "htmx", "href": "/docs/htmx"},
                {"title": "About", "href": "/docs/about"},
                {"title": "Contribution", "href": "/docs/contribution"},
                {"title": "Changelog", "href": "/docs/changelog"},
            ],
        },
        {
            "title": "Installation",
            "items": [
                {"title": "Fastapi", "href": "/docs/fastapi"},
                {"title": "Flask", "href": "/docs/flask"},
                {"title": "Django", "href": "/docs/django"},
                {"title": "Utilities", "href": "/docs/utilities"},
            ],
        },
        {
            "title": "Components",
            "items": [
                {"title": "Accordion", "href": "/components/accordion"},
                {"title": "Alert", "href": "/components/alert"},
                {"title": "Alert Dialog", "href": "/components/alert_dialog"},
                {"title": "Badge", "href": "/components/Badge"},
                {"title": "Button", "href": "/components/button"},
                {"title": "Card", "href": "/components/card"},
                {"title": "Checkbox", "href": "/components/checkbox"},
                {"title": "Dialog", "href": "/components/dialog"},
                {"title": "Dropdown Menu", "href": "/components/dropdown_menu"},
                {"title": "Form", "href": "/components/form"},
                {"title": "Icons", "href": "/components/icons"},
                {"title": "Input", "href": "/components/input"},
                {"title": "Label", "href": "/components/label"},
                {"title": "Link", "href": "/components/link"},
                {"title": "Popover", "href": "/components/popover"},
                {"title": "Radio Group", "href": "/components/radio_group"},
                {"title": "Select", "href": "/components/select"},
                {"title": "Sheet", "href": "/components/sheet"},
                {"title": "Table", "href": "/components/table"},
                {"title": "Textarea", "href": "/components/textarea"},
                {"title": "Toast", "href": "/components/toast"},
            ],
        },
        {
            "title": "Extended",
            "items": [
                {"title": "Mode Toggle", "href": "/components/mode_toggle"},
                {"title": "WTForm", "href": "/components/wtform"},
            ],
        },
    ],
}

site_config = SiteConfig.model_validate(
    config | {"icons": load_icons(f"{BASE_DIR}/components/ui/icons/icons.json")}
)
