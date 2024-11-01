---
title: Button
description: Displays a button.
component: button
examples:  
  - Destructive: examples/button_destructive.html 
  - Outline: examples/button_outline.html 
  - Secondary: examples/button_secondary.html 
  - Ghost: examples/button_ghost.html 
  - Link: examples/button_link.html 
---

## Usage

```html
--8<-- "docs/templates/examples/button.html"
```

## Props

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component.                |
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |
| `size`      | String  | `"default"` | Size of the button: `sm`, `lg`, `icon`.                               |
| `disabled`  | Boolean | `False`     | Disables the button if `True`.                                        |

## Code

/// tab | Button.jinja
```html
--8<-- "components/ui/Button.jinja"
```
///

