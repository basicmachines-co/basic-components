---
title: Table
description: A responsive table component.
component: table
examples:  
  - Sorting: examples/table_sorting.html 
---

## Usage

```html
--8<-- "docs/templates/examples/table.html"
```

## Props

| Component    | Prop        | Type   | Default | Description                                                |
|--------------|-------------|--------|---------|------------------------------------------------------------|
| TableHead    | `sortable`  | bool   | `False` | Displays and indicator if table is sortable by this colum. |
| TableHead    | `ascending` | bool   | `True`  | True if the order is ascending.                            |

## Code

/// tab | Table.jinja
```html
--8<-- "components/ui/Table.jinja"
```
///

/// tab | TableBody.jinja
```html
--8<-- "components/ui/TableBody.jinja"
```
///

/// tab | TableCaption.jinja
```html
--8<-- "components/ui/TableCaption.jinja"
```
///

/// tab | TableCell.jinja
```html
--8<-- "components/ui/TableCell.jinja"
```
///

/// tab | TableFooter.jinja
```html
--8<-- "components/ui/TableFooter.jinja"
```
///

/// tab | TableHead.jinja
```html
--8<-- "components/ui/TableHead.jinja"
```
///

/// tab | TableHeader.jinja
```html
--8<-- "components/ui/TableHeader.jinja"
```
///

/// tab | TableRow.jinja
```html
--8<-- "components/ui/TableRow.jinja"
```
///


Server side sorting is enabled via htmx using `hx-get`
```html
<th hx-get="/table?order_by=invoice&ascending=False" 
    hx-swap="outerHTML" 
    hx-target="#sorted-table">
    ...
</th>
```

The server side endpoint returns the html content to swap. 
