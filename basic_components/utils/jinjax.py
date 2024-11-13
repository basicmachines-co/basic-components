from pathlib import Path

import jinjax


def setup_component_catalog(
    catalog: jinjax.Catalog,
    components_dir: str = "components",
    include_icons: bool = False,
):
    """
    :param catalog: An instance of jinjax.Catalog used to register component directories.
    :param components_dir: The base directory where component subdirectories are located. Default is "components".
    :param include_icons: A boolean indicating whether to include the icons directory. Default is False.
    :return: The updated catalog after adding the specified component directories.
    """

    # basic components ui directory
    components_ui_dir = Path(f"{components_dir}/ui")

    # Register each component subdirectory
    for dir in components_ui_dir.iterdir():
        if dir.is_dir():
            catalog.add_folder(dir)

    if include_icons:
        catalog.add_folder(f"{components_dir}/icons")
    return catalog
