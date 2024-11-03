---
title: Table
description: A responsive table component.
templates:
  - Table.jinja
  - TableBody.jinja
  - TableCaption.jinja
  - TableCell.jinja
  - TableFooter.jinja
  - TableHead.jinja
  - TableHeader.jinja
  - TableRow.jinja
---

<TabPreview component="Table" template="examples/table.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/table.html"/>

<Prose>

## Attributes

| Component    | Prop        | Type   | Default | Description                                                |
|--------------|-------------|--------|---------|------------------------------------------------------------|
| TableHead    | `sortable`  | bool   | `False` | Displays and indicator if table is sortable by this colum. |
| TableHead    | `ascending` | bool   | `True`  | True if the order is ascending.                            |

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

Server side sorting is enabled via htmx using `hx-get`
```html
<th hx-get="/table?order_by=invoice&ascending=False" 
    hx-swap="outerHTML" 
    hx-target="#sorted-table">
    ...
</th>
```

The server side endpoint returns the html content to swap. 

## Examples
</Prose>


[//]: # (<TabPreview component="Sorting" template="examples/table_sorting.html"/>)
