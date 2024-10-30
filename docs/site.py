import yaml
from pydantic import BaseModel, HttpUrl
from typing import List, Union, Any


class NavItem(BaseModel):
    type: str = "item"
    name: str
    path: str


class NavGroup(BaseModel):
    type: str = "group"
    name: str
    items: List[Union[NavItem, "NavGroup"]]


class SiteConfig(BaseModel):
    """The top-level configuration for the site."""

    site_name: str
    repo_url: HttpUrl
    nav: List[Union[NavItem, NavGroup]]

    class Config:
        arbitrary_types_allowed = True

    def routes(self) -> List[str]:
        """Extract all valid paths from the navigation structure."""
        paths = []
        for item in self.nav:
            paths.extend(self._extract_paths_from_item(item))
        return paths

    def _extract_paths_from_item(self, item) -> List[str]:
        """Recursively extract paths from NavItem or NavGroup."""
        if isinstance(item, NavItem):
            return [item.path]
        elif isinstance(item, NavGroup):
            paths = []
            for sub_item in item.items:
                paths.extend(self._extract_paths_from_item(sub_item))
            return paths
        return []


def parse_nav(nav: Any) -> List[Union[NavItem, NavGroup]]:
    parsed = []
    for item in nav:
        if isinstance(item, dict):
            name, value = next(iter(item.items()))
            if isinstance(value, str):
                parsed.append(NavItem(name=name, path=value))
            else:
                parsed.append(NavGroup(name=name, items=parse_nav(value)))
    return parsed


def load_site_config(config_path):
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)

    return SiteConfig(
        site_name=data["site_name"],
        repo_url=data["repo_url"],
        nav=parse_nav(data["nav"]),
    )
