---
title: Input
description: Displays a form input field.
component: input
examples:  
  - Error: examples/input_error.html 
  - Disabled: examples/input_disabled.html 
  - Label: examples/input_label.html 
  - File: examples/input_file.html 
  - Button: examples/input_button.html 
  - Disabled: examples/input_disabled.html 
---

## Usage

```html
--8<-- "docs/templates/examples/input.html"
```


## Props

| Prop           | Type           | Default  | Description                                                    |
|----------------|----------------|----------|----------------------------------------------------------------|
| `name`         | String         | `""`     | The name attribute for the input field.                        |
| `type`         | String         | `"text"` | Specifies the type of input (e.g., `text`, `password`).        |
| `value`        | String         | `""`     | The initial value of the input.                                |
| `placeholder`  | String         | `""`     | Placeholder text shown inside the input.                       |
| `autocomplete` | Optional[String] | `""` | Determines if autocomplete is enabled for the input.           |
| `required`     | Boolean        | `False`  | Marks the input as required.                                   |
| `className`    | String         | `""`     | Additional CSS classes for customization.                      |
| `disabled`     | Boolean        | `False`  | Disables the input if `True`.                                  |
| `error`        | Boolean        | `False`  | Applies error styling if `True`.                               |

## Code

/// tab | Input.jinja
```html
--8<-- "components/ui/Input.jinja"
```
///


