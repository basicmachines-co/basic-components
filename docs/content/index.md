---
title: Basic Components
description: something 
---


<Prose>

## Build your component library.
Beautifully designed server side components that you can copy and paste into your apps. Accessible. Customizable. Open Source.
## Usage


{% include "examples/button.html" %}

## code fence 
```html
<button>this is html</button>
```
## Props

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component.                |
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |
| `size`      | String  | `"default"` | Size of the button: `sm`, `lg`, `icon`.                               |
| `disabled`  | Boolean | `False`     | Disables the button if `True`.                                        |


## Accordion


</Prose>

<TabPreview component="Accordion" template="examples/accordion.html"/>

