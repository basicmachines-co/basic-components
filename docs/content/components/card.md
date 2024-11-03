---
title: Card
description: Displays a callout for user attention.
component: card
templates:
  - Card.jinja
  - CardContent.jinja
  - CardDescription.jinja
  - CardFooter.jinja
  - CardHeader.jinja
  - CardTitle.jinja
---

<TabPreview component="Card" template="examples/card.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/card.html"/>

<Prose>

## Attributes


| Name        | Type    | Default     | Description                                            |
|-------------|---------|-------------|--------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component. |

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Example" template="examples/card_example.html"/>
