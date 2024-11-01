---
title: Popover
description: Displays rich content in a portal, triggered by a button.
component: popover
examples:  
  - Content: examples/popover_content.html 
---

## Usage

```html
--8<-- "docs/templates/examples/popover.html"
```

## Props

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component.                |
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |


## Code

/// tab | Popover.jinja
```html
--8<-- "components/ui/Popover.jinja"
```
///

/// tab | PopoverContent.jinja
```html
--8<-- "components/ui/PopoverContent.jinja"
```
///

/// tab | PopoverTrigger.jinja
```html
--8<-- "components/ui/PopoverTrigger.jinja"
```
///



