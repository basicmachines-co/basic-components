# JinjaX Component Library

This project provides a collection of UI components using [JinjaX](https://jinjax.scaletti.dev/), a component library for Jinja templates. 
It directly ports components from [shadcn/ui](https://ui.shadcn.com/) to JinjaX, maintaining compatibility in usage and style. 
Client side interactivity is implemented via [Alpine.js](https://alpinejs.dev/) and styling via [Tailwind.css](https://tailwindcss.com/). 

The goal is to equip developers using server-side rendering frameworks, such as FastAPI or Flask, with high-quality, 
responsive components that behave similarly to their React counterparts. Components can be further extended with [HTMX](https://htmx.org/) to create dynamic interfaces.

Features

- JinjaX: Components are implemented with JinjaX for use with server-rendered applications
- Tailwind CSS Styling: All components use Tailwind’s utility-based styling
- Alpine.js Interactivity: lightweight state management and dynamic client side behaviors 
- Direct shadcn/ui Ports: The structure and design of components closely match their React equivalents
- HTMX Support: Dynamic behavior such as content swaps and asynchronous updates is achieved with HTMX

## Example `Button` Component 

The `Button` component wraps options and behaviors for buttons and provides variants for different styles. 

```jinja
{# def
    id: str = "button",
    type: str = "",
    className: str = "",
    variant: str = "default",
    size: str = "default",
    disabled: bool = False
#}
{% set baseclassName = "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-white transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 dark:ring-offset-zinc-950 dark:focus-visible:ring-zinc-300" %}
{%
  set variantclassName = {
    'default': 'bg-zinc-900 text-zinc-50 hover:bg-zinc-900/90 dark:bg-zinc-50 dark:text-zinc-900 dark:hover:bg-zinc-50/90',
    'destructive': 'bg-red-500 text-zinc-50 hover:bg-red-500/90 dark:bg-red-900 dark:text-zinc-50 dark:hover:bg-red-900/90',
    'outline': 'border border-zinc-200 bg-white hover:bg-zinc-100 hover:text-zinc-900 dark:text-zinc-50 dark:border-zinc-700 dark:bg-zinc-950 dark:hover:bg-zinc-800 dark:hover:text-zinc-50',
    'secondary': 'bg-zinc-100 text-zinc-900 hover:bg-zinc-100/80 dark:bg-zinc-800 dark:text-zinc-50 dark:hover:bg-zinc-800/80',
    'ghost': 'hover:bg-zinc-100 hover:text-zinc-900 dark:hover:bg-zinc-800 dark:hover:text-zinc-50',
    'link': 'text-zinc-900 underline-offset-4 hover:underline dark:text-zinc-50'
  }[variant]
%}
{%
  set sizeclassName = {
    'default': 'h-10 px-4 py-2',
    'sm': 'h-9 rounded-md px-3',
    'lg': 'h-11 rounded-md px-8',
    'icon': 'h-10 w-10'
  }[size]
%}

<button
  {% if type %}type="{{ type }}"{% endif %}
  class="{{ baseclassName }} {{ variantclassName }} {{ sizeclassName }} {{ className }}"
  {% if disabled %}disabled{% endif %}
  {{ attrs.render() }}
>
  {{ content }}
</button>
```

## Using the `Button` Component

Within a template or another component, declare the component, passing attributes as needed, without needing to define tailwind css attributes repeatedly. 

```html
<Button variant="secondary">Secondary</Button>

<Button>
  <Mail className="mr-2 h-4 w-4" invert="True" />
  Login with Email
</Button>

<Button id="submitBtn" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="alert('Button Clicked!')">
    Click Me
</Button>
```

- The `Button` component is inserted directly into the template without macros or includes.
- Props like `id`, `className`, and `onclick` are set directly, and any additional attributes can be passed as needed.

- **Props**: Props are declared using `{# def ... #}` and define attributes such as `id`, `className`, and any booleans
  like `disabled`.
- **Dynamic Attributes**: The `{{ attrs.render() }}` in the component allows passing additional
  attributes dynamically when the component is used.

## Composing components

Components can be composed to create ui elements. 

```html
<Card className="sm:col-span-2">
  <CardHeader className="pb-3">
    <CardTitle>Your Orders</CardTitle>
    <CardDescription className="max-w-lg text-balance leading-relaxed">
      Introducing Our Dynamic Orders Dashboard for Seamless Management and
      Insightful Analysis.
    </CardDescription>
  </CardHeader>
  <CardFooter>
    <Button>Create New Order</Button>
  </CardFooter>
</Card>

```
See the related shadcn/ui [example](https://ui.shadcn.com/blocks).

## Adding htmx

Htmx attributes can be added to components when they are declared to add behavior.

```html
<Button
  hx-get="/some/url"
  hx-target="this"
  hx-swap="outerHTML"
  type="button"
  variant="outline"
>Click me
</Button>
```

## Vendoring Components

The components in this project can be copied (vendored) directly into your project and customized further. 
Using a tool like [Copier](https://copier.readthedocs.io/en/stable/), you can copy and then update them later if needed. 

To vendor these components into your project using copier:

1. Ensure you have Copier installed:
```
pip install copier
```

2. Run the following command from your project directory, specifying the destination:
```
copier copy https://github.com/basic-foundation/basic-components.git ./path/to/destination
```
Replace `./path/to/destination` with the directory where you want the components to be vendored.

3. To preview the operation without making any changes, use the `--pretend` flag:
```
copier copy --pretend https://github.com/basic-foundation/basic-components.git ./path/to/destination
```

### Versioning and Updates

When you vendor these components into your project, a `components/components-version.txt` file will be created. 
This file contains the version number of the basic-components library that you've vendored.

**Notes:**
- If updating, copier will preserve your existing files. It will show diffs for any conflicts and allow you to choose how to handle them.
- You can specify a specific branch, tag, or commit by appending it to the repository URL, e.g., `...basic-components.git@v1.0.0 ./path/to/destination`
- You can also fork this repo and use your own git url with copier or use a local copy of the repository.
- Using a local repository is particularly useful during development or when you've made custom modifications.

For more detailed information on Copier usage, refer to the [Copier documentation](https://copier.readthedocs.io/).

When reporting issues or seeking support related to these components, always mention the version number found in your `components/components-version.txt` file.
