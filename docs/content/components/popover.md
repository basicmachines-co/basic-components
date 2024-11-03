---
title: Popover
description: Displays rich content in a portal, triggered by a button.
templates:
  - Popover.jinja
  - PopoverContent.jinja
  - PopoverTrigger.jinja
---

<TabPreview component="Popover" template="examples/popover.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/popover.html"/>

<Prose>

## Attributes

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |


## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Content" template="examples/popover_content.html"/>


