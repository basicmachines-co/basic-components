---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
---


## Props

| Name      | Type    | Default     | Description                                            |
|-----------|---------|-------------|--------------------------------------------------------|
| className | String  |             | Additional tailwind classes to apply to the component. |

## Components



## Usage

```html
<Accordion>
    <AccordionItem value="item-1">
        <AccordionTrigger>Can I keep my options open?</AccordionTrigger>
        <AccordionContent>
            Yes, it's good to have options.
        </AccordionContent>
    </AccordionItem>
    <AccordionItem value="item-2">
        <AccordionTrigger>Do I have to choose just one?</AccordionTrigger>
        <AccordionContent>
            Yes, everyone must choose.
        </AccordionContent>
    </AccordionItem>
</Accordion>
```
