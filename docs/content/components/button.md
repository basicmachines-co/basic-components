---
title: Button
description: Displays a button.
component: button
templates:  
  - Button.jinja 
---

<TabPreview component="Button" template="examples/button.html"/>

<Prose>

## Usage
</Prose>

<IncludeTemplate template="examples/button.html"/>

<Prose>

## Attributes

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component.                |
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |
| `size`      | String  | `"default"` | Size of the button: `sm`, `lg`, `icon`.                               |
| `disabled`  | Boolean | `False`     | Disables the button if `True`.                                        |

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Destructive" template="examples/button_destructive.html"/>
<TabPreview component="Outline" template="examples/button_outline.html"/>
<TabPreview component="Secondary" template="examples/button_secondary.html"/>
<TabPreview component="Ghost" template="examples/button_ghost.html"/>
<TabPreview component="Link" template="examples/button_link.html"/>

