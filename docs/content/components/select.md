---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
component: select
examples:  
  - Scrollable: examples/select_scrollable.html 
---


## Usage

```html
--8<-- "docs/templates/examples/select.html"
```


## Props
| Component     | Prop          | Type           | Default  | Description                               |
|---------------|---------------|----------------|----------|-------------------------------------------|
| Select        | `name`        | String         | `""`     | The name attribute for the input field.   |
| Select        | `className`   | String         | `""`     | Additional CSS classes for customization. |
| SelectItem    | `value`       | String         | `""`     | The form value for the item.              |
| SelectLabel   | `className`   | String         | `""`     | Additional CSS classes for customization. |
| SelectTrigger | `className`   | String         | `""`     | Additional CSS classes for customization. |
| SelectValue   | `placeholder` | String         | `""`     | The placeholder text.                     |

The value of the selected item is stored in a hidden input field.

## Code

/// tab | Select.jinja
```html
--8<-- "components/ui/Select.jinja"
```
///

/// tab | SelectContent.jinja
```html
--8<-- "components/ui/SelectContent.jinja"
```
///

/// tab | SelectGroup.jinja
```html
--8<-- "components/ui/SelectGroup.jinja"
```
///

/// tab | SelectItem.jinja
```html
--8<-- "components/ui/SelectItem.jinja"
```
///

/// tab | SelectLabel.jinja
```html
--8<-- "components/ui/SelectLabel.jinja"
```
///

/// tab | SelectScrollDownButton.jinja
```html
--8<-- "components/ui/SelectScrollDownButton.jinja"
```
///

/// tab | SelectScrollUpButton.jinja
```html
--8<-- "components/ui/SelectScrollUpButton.jinja"
```
///

/// tab | SelectTrigger.jinja
```html
--8<-- "components/ui/SelectTrigger.jinja"
```
///

/// tab | SelectValue.jinja
```html
--8<-- "components/ui/SelectValue.jinja"
```
///

