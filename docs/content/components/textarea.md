---
title: Textarea
description: Displays a resizable form textarea.
component: textarea
examples:
  - Disabled: examples/textarea_disabled.html 
  - With Label: examples/textarea_label.html 
  - With Text: examples/textarea_text.html 
  - With Button: examples/textarea_button.html 
  - With Form: examples/textarea_form.html 
---

## Usage

```html
--8<-- "docs/templates/examples/textarea.html"
```

## Props

| Prop          | Type   | Default | Description                                 |
|---------------|--------|---------|---------------------------------------------|
| `className`   | String | `""`    | Additional CSS classes for customization.   |
| `value`       | String | `""`    | The value of the textarea                   |
| `placeholder` | String | `""`    | Placeholder text displayed in the textarea. |
| `disabled`    | bool   | `""`    | Disables the textarea                       |

## Code

/// tab | TextArea.jinja
```html
--8<-- "components/ui/TextArea.jinja"
```
///


