---
title: Sheet
description: Displays content on one side of the screen in a modal dialog.
templates:
  - Sheet.jinja
  - SheetClose.jinja
  - SheetContent.jinja
  - SheetDescription.jinja
  - SheetFooter.jinja
  - SheetHeader.jinja
  - SheetOverlay.jinja
  - SheetTitle.jinja
  - SheetTrigger.jinja
---

<TabPreview component="Alert" template="examples/alert.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/alert.html"/>

<Prose>

## Attributes

| Component        | Prop        | Type   | Default           | Description                                    |
|------------------|-------------|--------|-------------------|------------------------------------------------|
| SheetContent     | `side`      | String | `"right"`         | Position of the sheet (top/bottom/left/right). |


## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Sides" template="examples/sheet_side.html"/>
