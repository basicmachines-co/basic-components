---
title: Toast
description: A succinct message that is displayed temporarily.
component: toast
examples:  
  - Success: examples/toast_success.html 
  - Warning: examples/toast_warning.html 
  - Error: examples/toast_error.html 
  - Destructive: examples/toast_destructive.html 
---

## Usage

```html
--8<-- "docs/templates/examples/toast.html"
```

## Props

| Component    | Prop           | Type   | Default     | Description                                                                                             |
|--------------|----------------|--------|-------------|---------------------------------------------------------------------------------------------------------|
| Toast        | `id`           | String |             | The css id for the Toast.                                                                               |
| Toast        | `duration`     | Number | `30000`     | Duration in milliseconds before toast auto-dismisses.                                                   |
| ToastContent | `type`         | String | `"default"` | Style variant of the toast. Options: `"default"`, `"success"`, `"error"`, `"warning"`, `"destructive"`. |
| ToastContent | `title`        | String | `""`        | The title text displayed in the toast.                                                                  |
| ToastContent | `description`  | String | `""`        | The description text displayed below the title.                                                         |
| ToastTrigger | `variant`      | String | `"default"` | The Button component variant to use.                                                                    |
| ToastTrigger | `toast_target` | String |             | The target toast identifier to trigger.                                                                 |

Toast components require an `id` so that the dispatch event can call the component to display it. 

## Code

/// tab | Toast.jinja
```html
--8<-- "components/ui/Toast.jinja"
```
///

/// tab | ToastContent.jinja
```html
--8<-- "components/ui/ToastContent.jinja"
```
///

/// tab | ToastTrigger.jinja
```html
--8<-- "components/ui/ToastTrigger.jinja"
```
///

