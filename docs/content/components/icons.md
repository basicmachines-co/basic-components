---
title: Icons
description: Icons components from lucide.dev
---


<Prose>

Components are included for each of the icons in the <Link href="/https://lucide.dev/">Lucide</Link> icon library.

</Prose>


<TabPreview component="Icons" template="examples/icons.html"/>

<Prose>

**Note:**
Icon components are named `<IconName>Icon.jinja` to avoid naming conflicts with other components. Otherwise, for instance
the `Sheet` icon would have a naming conflict with the `Sheet` component. 

## Attributes

| Prop        | Type   | Default   | Description                                         |
|-------------|--------|-----------|-----------------------------------------------------|
| `className` | String | `h-4 w-4` | Additional CSS classes for customization like size. |

## Search

</Prose>


<Card className="p-4">

<Input
    id="search"
    type="search"
    name="query"
    className="w-full"
    placeholder="Search icons..."
    hx-get="/icons/search"
    hx-trigger="load, input changed delay:300ms, search"
    hx-target="#icons"
    hx-swap="outerHTML"
/>
  <!-- search results -->
  <div id="icons" class="w-full">
    <div class="flex justify-center py-8 {{ className }}">
        <LoaderCircleIcon className="text-zinc-300 dark:text-zinc-600 h-24 w-24 animate-spin"/>
    </div>
  </div>
</Card>
