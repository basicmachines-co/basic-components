# Project: Basic Components 

## Goals Summary

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

## Porting ShadCN Components to JinjaX:

- Component Development:
  - Break down ShadCN components into reusable JinjaX components.
  - Follow existing patterns from react version. Use the same class names and tailwind styles.
  - Include {{ attrs.render() }} in the component to pass along any additional attributes (for compatibility with things like Alpine.js and htmx)

## Components

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


## Example `Button` Component

### Button

The `Button` component wraps options and behaviors for buttons and provides variants for different styles, similar to the [shadcn/ui version](https://ui.shadcn.com/docs/components/button).

```jinja
{#def
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

### Using the `Button` Component

Within a template or another component, declare the `Button`, passing attributes as needed, without needing to define tailwind css attributes repeatedly.

```html
<Button variant="secondary">Secondary</Button>

<Button>
  <!-- include and svg icon -->
  <Mail className="mr-2 h-4 w-4" invert="True" /> 
  Login with Email
</Button>

<Button id="submitBtn"  onclick="alert('Button Clicked!')">
    Click Me
</Button>
```

- The `Button` component is inserted directly into the template without macros or includes.
- Props like `id`, `className`, and `onclick` are set directly, and any additional attributes can be passed as needed.

- **Props**: Props are declared using `{#def ... #}` and define attributes such as `id`, `className`, and any booleans
  like `disabled`.
- **Dynamic Attributes**: The `{{ attrs.render() }}` in the component allows passing additional
  attributes dynamically when the component is used.

### Adding htmx

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

The components in this project can be copied (vendored) directly into your project and customized further using [Copier](https://copier.readthedocs.io/en/stable/).
You can then customize them as needed.

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





# Testing Strategy for JinjaX Component Library

## Overview

Our testing strategy focuses on ensuring the reliability, functionality, and consistency of our JinjaX components. We use Playwright for end-to-end testing, leveraging server-side endpoints to test components in a real-world-like environment.

## Key Aspects of Our Testing Approach

1. **Server-side Endpoints for Components:**
    - Create endpoints that serve individual components with various props and states.
    - This allows testing components in their intended server-side rendered context.

2. **Real-world Examples:**
    - Use practical, real-world scenarios in tests to uncover potential issues.

3. **Playwright for E2E Testing:**
    - Utilize Playwright's cross-browser support and powerful API for comprehensive testing.
    - Simulate user interactions to test component behavior thoroughly.

## Testing Enhancements

1. **Component Isolation Tests:**
    - Implement isolated tests for quick identification of component-specific issues.

2. **Visual Regression Testing:**
    - Use Playwright's visual comparison features to ensure UI consistency across changes.

3. **Accessibility Testing:**
    - Incorporate WCAG compliance checks into component tests.

4. **Performance Metrics:**
    - Gather and analyze performance metrics for components using Playwright.

5. **Interactivity Coverage:**
    - Ensure thorough testing of all interactive aspects, especially Alpine.js functionality.

6. **Parameterized Tests:**
    - Create tests with various prop combinations to cover different component states.

7. **Error State Testing:**
    - Include tests for error states and edge cases in components.

8. **Documentation Generation:**
    - Use test cases to automatically generate or update component documentation.

9. **CI/CD Integration:**
    - Integrate tests into the CI/CD pipeline for automated testing on each commit or PR.

10. **Test Helpers:**
    - Develop utilities specific to component testing to streamline test writing and maintenance.

## Implementation Approach

1. Create a dedicated `tests` directory for component tests.
2. Set up a simple server (e.g., using FastAPI) to serve individual components.
3. Write Playwright tests that interact with these component endpoints.
4. Include both "happy path" and edge case scenarios in tests.
5. Utilize Playwright's assertions and add custom assertions as needed.

## Example Test Structure

```python
from playwright.sync_api import Page, expect

def test_button_component(page: Page):
    # Navigate to the button component test page
    page.goto("/test/components/button")

    # Test default state
    button = page.locator("button")
    expect(button).to_be_visible()
    expect(button).to_have_text("Click me")

    # Test click behavior
    button.click()
    expect(page.locator(".clicked-state")).to_be_visible()

    # Test disabled state
    page.goto("/test/components/button?state=disabled")
    expect(button).to_be_disabled()

# Additional tests for other components and their variations
```

## Next Steps

1. Set up the testing environment with Playwright and necessary dependencies.
2. Create initial test endpoints for core components.
3. Develop a set of base tests that can be applied to most components.
4. Gradually expand test coverage to include all components and their variations.
5. Integrate testing into the development workflow and CI/CD pipeline.

By following this testing strategy, we aim to ensure the reliability and quality of our JinjaX component library, facilitating its integration into the basic-foundation project and its adoption by other developers.
