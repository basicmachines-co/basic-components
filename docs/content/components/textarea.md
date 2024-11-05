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

<Prose>

### Disabled

</Prose>
<TabPreview component="Disabled" template="examples/textarea_disabled.html"/>

<Prose>

### With Label

</Prose>
<TabPreview component="With Label" template="examples/textarea_label.html"/>

<Prose>

### With Text

</Prose>
<TabPreview component="With Text" template="examples/textarea_text.html"/>

<Prose>

### With Button

</Prose>
<TabPreview component="With Button" template="examples/textarea_button.html"/>

<Prose>

### With Form

</Prose>
<TabPreview component="With Form" template="examples/textarea_form.html"/>

