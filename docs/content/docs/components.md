---
title: Components
description: Creating components with JinjaX
---
<Prose>

See the [JinjaX guide](https://jinjax.scaletti.dev/guide/components/#/) for an overview of JinjaX, 
particularly the [motivation](https://jinjax.scaletti.dev/guide/motivation/) for using components similar to other front end frameworks. 

The components in this project follow the patterns described in the JinjaX docs, with a few additional patterns. The following
overview describes the basic composition of a component.

## Example `Button` Component

### Button

The [Button](/components/button) component wraps options and behaviors for html buttons and provides variants for different styles, similar to the [shadcn/ui version](https://ui.shadcn.com/docs/components/button).

</Prose>
<IncludeComponents dir="button" :components="['Button.jinja']" />
<Prose>

You can see there are a lot of utility styles required to render a simple HTML button with styling.

## Components

Every component has similar qualities. They each: 

- Declare arguments in a block `{{ '{#def ... #}' }}` at the top of the file. 
- Use regular Jinja syntax for conditionals, variables or other logic.
- Can use the variables passed within the component template. 
- Have a special slot variable called `{{ '{{ content }}'}}` to render nested components or content.
- Can invoke extra arguments passed to the declaration via `{{ '{{ attrs.render() }}' }}`  
- Can have extra utility styles passed to it via the `className` argument.

Arguments:

- Arguments can have default values.
- Arguments are passed via HTML attributes when a component is declared.
- Arguments can pass objects via the `{{ ':attrValue={{ object }}' }}` notation, similar to vue (with a leading `:`). Otherwise arguments are evaluated as Strings.
See [expressions](https://jinjax.scaletti.dev/guide/components/#s-expressions) in the JinaX docs. 

## Using components

Within a template or another component, declare the `Button` with its html tags, passing attributes as needed. 
Content inside the tags will be rendered inside the `content` slot. 

The `Mail` component below renders an SVG icon from the [Lucide](https://lucide.dev/) icon set.

</Prose>

<TabPreview component="Components" template="examples/docs_button_component.html"/>

<Prose>

- The `Button` component is inserted directly into the template without macros or includes.
- Attribute like `id`, `className`, and `onclick` are set directly, and any additional attributes can be passed as needed.


### Adding htmx

Htmx attributes can be added to components when they are declared to add htmx behaviors.

<Button hx-get="/demo/button" hx-target="this" hx-swap="outerHTML" type="button" variant="outline">Click me</Button>

```html
<Button
  hx-get="/demo/button"
  hx-target="this"
  hx-swap="outerHTML"
  type="button"
  variant="outline"
>Click me</Button>
```

See the [using htmx](/docs/htmx) docs for further details. 

## shadcn/ui components 

The components in this project follow patterns from [shadcn/ui](https://ui.shadcn.com/) very closely, using identical names for each class (React) and template(JinjaX). 
In many cases, it's possible to copy/paste code using the react versions directly into templates. There are a few notable differences:

- JinjaX does not have the same semantics to refer to props from other components
- React code contaning `className` on regular html elements (like `div`) should be changed to `class`. Eg `<div className="mt-0">` should be changed to `<div class="mt-0">` so Tailwind will apply styles correctly. 
- Client side state needs to be implemented via Alpine.js
- Interactivity can be added via htmx


</Prose>