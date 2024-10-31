---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
components:  
  - components/ui/Accordion.jinja
  - components/ui/AccordionContent.jinja 
  - components/ui/AccordionItem.jinja 
  - components/ui/AccordionTrigger.jinja 
---


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

## Code


/// tab | Tab A title
```html
{#def
    className: str = ""
#}
<div
    x-data="{
      activeItem: undefined,
      toggleItem(value) {
        this.activeItem = this.activeItem === value ? undefined : value;
      }
    }"
    x-init="console.log('initial state:', activeItem);"
    class="{{ className }} w-full"
    {{ attrs.render() }}
>
  {{ content }}
</div>
```
///

/// tab | Tab B title
Tab B content
///

/// tab | Tab C Title
new: true

Will be part of a separate, new tab group.
///

