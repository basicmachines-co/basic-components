---
title: Label
description: Displays a label for a form field.
templates:
  - Label.jinja
---

<TabPreview component="Label" template="examples/label.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/label.html"/>

<Prose>

## Attributes

| Prop        | Type    | Default | Description                               |
|-------------|---------|---------|-------------------------------------------|
| `htmlFor`   | String  | `False` | The id of the field the label refers to.  |
| `className` | String  | `""`    | Additional CSS classes for customization. |


## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

