---
title: Alert
description: Displays a callout for user attention.
templates:
  - Alert.jinja
  - AlertDescription.jinja
  - AlertDialogContent.jinja
---

<TabPreview component="Alert" template="examples/alert.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/alert.html"/>

<Prose>

## Attributes

| Component | Name      | Type   | Default   | Description                                                   |
|-----------|-----------|--------|-----------|---------------------------------------------------------------|
| Alert     | `variant` | String | `default` | Sets the component style. Available: `default`, `destructive` |


## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples 
</Prose>

<TabPreview component="Destructive" template="examples/alert_destructive.html"/>
