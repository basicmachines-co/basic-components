---
title: Alert
description: Displays a callout for user attention.
component: alert
examples:  
  - Destructive: examples/alert_destructive.html 
---


## Usage

```html
--8<-- "docs/templates/examples/alert.html"
```

## Props

| Name        | Type    | Default   | Description                                                   |
|-------------|---------|-----------|---------------------------------------------------------------|
| `className` | String  |           | Additional tailwind classes to apply to the component.        |
| `variant`   | String  | `default` | Specify variant style, valid values: `default`, `destructive` |

## Code

/// tab | Alert.jinja
```html
--8<-- "components/ui/Alert.jinja"
```
///

/// tab | AlertDescription.jinja
```html
--8<-- "components/ui/AlertDescription.jinja"
```
///

/// tab | AlertDialogContent.jinja
```html
--8<-- "components/ui/AlertDialogContent.jinja"
```
///

