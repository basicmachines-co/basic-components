---
title: Mode Toggle
description: A dropdown menu with options to switch between light and dark modes.
component: mode_toggle
templates:
  - ModeToggle.jinja

---

<TabPreview component="ModeToggle" template="examples/mode_toggle.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/mode_toggle.html"/>

<Prose>

The mode is toggled by setting a 'mode' value in localStorage and setting the `dark` utility style on the `body` tag. 
Add the following logic to the `html` element on the page to perform toggling logic. 
Any component can call the `toggleMode` function to switch the mode. 

```html
<html
    class="h-full"
    lang="en"
    x-data="{
        mode: localStorage.getItem('mode') || 'system',
        init() {
            this.applyMode();
        },
        applyMode() {
            if (this.mode === 'dark') {
                document.documentElement.classList.add('dark');
            } else if (this.mode === 'light') {
                document.documentElement.classList.remove('dark');
            } else {
                // System preference
                const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                if (prefersDark) {
                    document.documentElement.classList.add('dark');
                } else {
                    document.documentElement.classList.remove('dark');
                }
            }
        },
        toggleMode(mode) {
            this.mode = mode;
            localStorage.setItem('mode', mode);
            this.applyMode();
        }
    }"
    x-init="init()"
>
```

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Button" template="examples/mode_toggle_button.html"/>
