---
title: Utilities
description: Helper functions for setting up components and merging Tailwind classes
---

<Prose>

## Tailwind Class Merging

Basic Components provides a utility function `cn()` for merging Tailwind CSS classes while handling conflicts properly. 
This is available in all Jinja templates if it is added to the Jinja environment. 

```python
from starlette.templating import Jinja2Templates
from basic_components.utils.tailwind import tw

templates = Jinja2Templates(directory="templates")

# Add cn to globals
templates.env.globals["cn"] = tw

```

### Usage

The `cn()` function is then globally available in templates.

{{'
```jinja
{#def
    className: str = ""
#}
<div 
    class="{{ cn(
        'flex flex-col-reverse sm:flex-row sm:space-x-2',
        'sm:justify-end' if 'sm:justify-start' not in className else '',
        className
    ) }}"
>
    {{ content }}
</div>
```
'}}

### Features

- Handles class conflicts (last one wins)
- Supports responsive modifiers (sm:, md:, etc.)
- Supports state modifiers (hover:, focus:, etc.)
- Handles arbitrary values ([...])
- Preserves non-conflicting classes


## Setup JinjaX Catalog 

Basic Components includes a `setup_component_catalog()` helper function to include all components in subdirectories. 

Each component is assumed to be packaged in a subdirectory within the `components` root directory. Components are under the 
`components/ui` top level directory. Icon components are under `components/icons`.

```bash
project-root
├── components
    ├── custom
    │   ├── CustomComponent.jinja
    ├── icons
    │   ├── AArrowDown.jinja
    │   ├── ...
    └── ui
        ├── ...
        ├── button
        │   └── Button.jinja
        ├── card
        │   ├── Card.jinja
        │   ├── CardContent.jinja
        │   ├── CardDescription.jinja
        │   ├── CardFooter.jinja
        │   ├── CardHeader.jinja
        │   └── CardTitle.jinja
        ├── ...
```

You can place your own components within your own subdirectory also, for example `components/custom`. Note that components 
should be named uniquely, or JinjaX will load the first one it finds. 

```python
from basic_components.utils.jinjax import setup_component_catalog
from starlette.templating import Jinja2Templates
import jinjax

COMPONENT_DIR = "components"

templates = Jinja2Templates(directory="templates")
templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)

# include subdirectories in the JinjaX catalog. 
# optionally include icons 
catalog = setup_component_catalog(
    catalog, components_dir=COMPONENT_DIR, include_icons=True
)

# add any extra dirs to the catalog with custom components
catalog.add_folder("components/custom")
```


</Prose>