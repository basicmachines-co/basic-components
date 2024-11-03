---
title: Textarea
description: Displays a resizable form textarea.
templates:
  - Textarea.jinja

examples:
  - Disabled: examples/textarea_disabled.html 
  - With Label: examples/textarea_label.html 
  - With Text: examples/textarea_text.html 
  - With Button: examples/textarea_button.html 
  - With Form: examples/textarea_form.html 
---

<TabPreview component="TextArea" template="examples/textarea.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/textarea.html"/>

<Prose>

## Attributes

| Prop          | Type   | Default | Description                                 |
|---------------|--------|---------|---------------------------------------------|
| `className`   | String | `""`    | Additional CSS classes for customization.   |
| `value`       | String | `""`    | The value of the textarea                   |
| `placeholder` | String | `""`    | Placeholder text displayed in the textarea. |
| `disabled`    | bool   | `""`    | Disables the textarea                       |

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Disabled" template="examples/textarea_disabled.html"/>
<TabPreview component="With Label" template="examples/textarea_label.html"/>
<TabPreview component="With Text" template="examples/textarea_text.html"/>
<TabPreview component="With Button" template="examples/textarea_button.html"/>
<TabPreview component="With Form" template="examples/textarea_form.html"/>

