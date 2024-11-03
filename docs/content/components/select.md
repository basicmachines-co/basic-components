---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
templates:
  - Select.jinja
  - SelectContent.jinja
  - SelectGroup.jinja
  - SelectItem.jinja
  - SelectLabel.jinja
  - SelectScrollDownButton.jinja
  - SelectScrollUpButton.jinja
  - SelectTrigger.jinja
  - SelectValue.jinja
---

<TabPreview component="Select" template="examples/select.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/select.html"/>

<Prose>

## Attributes

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
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Scrollable" template="examples/select_scrollable.html"/>
