---
title: Badge
description: Displays a badge or a component that looks like a badge.
component: badge
examples:  
  - Destructive: examples/badge_destructive.html 
  - Outline: examples/badge_outline.html 
  - Secondary: examples/badge_secondary.html 
---


## Usage

```html
--8<--  "docs/templates/examples/badge.html"
```

## Props

| Name        | Type   | Default     | Description                                                       |
|-------------|--------|-------------|-------------------------------------------------------------------|
| `className` | String |             | Additional tailwind classes to apply to the component.            |
| `variant`   | String | `"default"` | Sets the component style. Available: `default`, `secondary`, etc. |

## Code

/// tab | Badge.jinja
```html
--8<-- "components/ui/Badge.jinja"
```
///

