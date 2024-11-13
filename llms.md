---
title: "Basic Components"
date: 2024-11-12
author: "Paul Hernandez"
description: "A collection of re-usable server-side components based on shadcn/ui, built with JinjaX, Alpine.js, and Tailwind CSS, with support for htmx. This project represents a fundamental shift in Python web development by bringing modern component patterns to server-side rendering while maintaining the simplicity and performance benefits of server-first architecture."
github: https://github.com/basicmachines-co/basic-components
license: MIT 
---

# Basic Components

## Project Philosophy

This project reimagines Python server-side web development for the modern age by:

1. **Server-First Architecture**
  - Fully rendered HTML pages from the server
  - Reduced time to first meaningful paint
  - Enhanced SEO and accessibility
  - Simplified state management

2. **Modern Development Pattern**
  - Component-based architecture without traditional package dependencies
  - Direct code ownership through copy/paste pattern
  - Full customization and extension capabilities
  - Integration with modern tooling

3. **Technology Integration**
  - JinjaX for server-side component composition
  - htmx for dynamic HTML updates without full page refreshes
  - Alpine.js for minimal client-side state management
  - Tailwind CSS for utility-first styling
  - FastAPI/Django/Flask backend support

## Core Benefits

### Server-Side Rendering (SSR) Advantages
- Improved initial page load performance
- Better SEO through static content
- Enhanced accessibility with JavaScript optional
- Reduced client-side complexity
- Simplified state management
- Easier traffic scaling through server resources

### Development Benefits
- Unified Python development stack
- No context switching between languages
- Reduced architecture complexity
- Modern component patterns
- Copy-paste customization
- Full code control


## Component Architecture

JinjaX components are the foundation of this project, providing a React-like component model for server-side rendering:

### Basic Component Structure
```jinja
{#def
    # Arguments are declared at the top with type hints
    className: str = "",    # Additional CSS classes
    variant: str = "default",   # Component variant
    size: str = "default",      # Component size
    disabled: bool = False      # Disabled state
#}

{# Variables and computed values use standard Jinja syntax #}
{% set baseclassName = "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-white transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 dark:ring-offset-zinc-950 dark:focus-visible:ring-zinc-300" %}

{# Components output HTML with dynamic values #}
<button
    class="{{ baseclassName }} {{ variantclassName }} {{ className }}"
    {% if disabled %}disabled{% endif %}
    {{ attrs.render() }}  {# Renders additional HTML attributes #}
>
  {{ content }}  {# Renders nested content #}
</button>
```

### Key Component Features
1. **Argument Declaration**
  - Uses `{#def ...#}` block at the top
  - Supports type hints and default values
  - Arguments passed via HTML attributes

2. **Template Logic**
  - Standard Jinja syntax for conditions and loops
  - Variable computation and class composition
  - Dynamic attribute handling

3. **Content Slots**
  - `{{ content }}` renders nested components/content
  - Supports component composition
  - Enables template reuse

4. **Additional Attributes**
  - `{{ attrs.render() }}` passes through HTML attributes
  - Supports htmx attributes
  - Handles Alpine.js directives

### Component Usage Examples

Basic Usage:
```html
<Button variant="primary" size="lg">
  Click Me
</Button>
```

With Nested Content:
```html
<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
  </CardHeader>
  <CardContent>
    Content goes here
  </CardContent>
</Card>
```

With Dynamic Behavior:
```html
<Button
  variant="outline"
  hx-get="/api/data"          {# htmx attribute #}
  x-on:click="open = true"    {# Alpine.js directive #}
  class="mt-4"                {# Additional classes #}
>
  Load More
</Button>
```

### Component Composition

Components can be nested and combined:

```html
<Card>
  <CardHeader>
    <CardTitle>User Profile</CardTitle>
    <CardDescription>Manage your account</CardDescription>
  </CardHeader>
  <CardContent>
    <form class="space-y-4">
      <Input 
        label="Username" 
        required
        x-model="username"
      />
      <Button type="submit">
        Save Changes
      </Button>
    </form>
  </CardContent>
</Card>
```

### Style Organization

Components use Tailwind CSS with a structured approach:

1. **Base Styles**
  - Core component styles
  - Layout and positioning
  - Basic typography

2. **Variant Styles**
  - Different visual variations
  - State-based styles
  - Theme-specific changes

3. **Size Variants**
  - Dimension modifications
  - Spacing adjustments
  - Responsive changes

4. **Custom Classes**
  - Additional styles via className prop
  - Extensible through Tailwind utilities
  - Dark mode support

### Integration Examples

Basic Component Usage:
```html
<!-- Static button -->
<Button variant="default">Click me</Button>

<!-- Dynamic updates with htmx -->
<Button
  hx-get="/api/data"
  hx-target="#result"
  hx-swap="innerHTML"
>
  Load Data
</Button>

<!-- Client state with Alpine.js -->
<div x-data="{ count: 0 }">
  <Button x-on:click="count++">
    Clicked: <span x-text="count">0</span>
  </Button>
</div>
```

## Modern Tooling Details

The project combines specific modern tools that together enable a powerful server-side component architecture:

### JinjaX
[JinjaX](https://jinjax.scaletti.dev/) solves the component composition problem for server-side templates:
- Extends Jinja2 with a component-based architecture
- Enables React-like component patterns on the server
- Provides clear separation of component logic and presentation
- Supports typed arguments and default values
- Allows composition through nested components

Example component:
```jinja
{#def
    label: str = "",
    required: bool = False
#}
<div class="space-y-2">
  <label>{{ label }}</label>
  <input {{ attrs.render() }} />
</div>
```

### htmx
[htmx](https://htmx.org/) enables dynamic server updates without complex JavaScript:
- Extends HTML with AJAX, WebSockets, and Server-Sent Events
- Returns HTML directly from server endpoints
- Updates DOM fragments without full page reloads
- Provides hypermedia-driven patterns for interactivity

Key capabilities:
- `hx-get/post/put/delete` for AJAX requests
- `hx-trigger` for custom events
- `hx-target` for DOM updates
- `hx-swap` for content replacement strategies

Example:
```html
<button 
  hx-post="/submit" 
  hx-target="#result"
  hx-swap="outerHTML"
>
  Submit
</button>
```

### Alpine.js
[Alpine.js](https://alpinejs.dev/) provides lightweight client-side reactivity:
- Minimal JavaScript framework for basic interactivity
- Declarative syntax directly in HTML
- Simple state management without complex setup
- Progressive enhancement approach

Core directives:
- `x-data` for component state
- `x-model` for two-way binding
- `x-on` for event handling
- `x-show/x-if` for conditional rendering

Example:
```html
<div x-data="{ open: false }">
  <button x-on:click="open = !open">Toggle</button>
  <div x-show="open">Content</div>
</div>
```

### Tailwind CSS
[Tailwind CSS](https://tailwindcss.com/) enables rapid UI development through utility classes:
- Utility-first CSS framework
- Component-friendly class organization
- Built-in dark mode support
- Consistent design system

Key features:
- Utility classes for all CSS properties
- Component variants through class composition
- Responsive design utilities
- Dark mode via `dark:` prefix

Example:
```html
<div class="p-4 bg-white dark:bg-zinc-800 rounded-lg shadow-md hover:shadow-lg transition-shadow">
  <h2 class="text-lg font-semibold text-zinc-900 dark:text-zinc-100">
    Title
  </h2>
</div>
```

### Tool Integration
These tools work together to create a cohesive development experience:
1. JinjaX provides the component architecture
2. Tailwind CSS handles styling
3. htmx manages server communication
4. Alpine.js handles client-state

Example of tools working together:
```html
<div x-data="{ loading: false }" class="p-4">
  <Button
    variant="primary"
    hx-get="/api/data"
    hx-target="#result"
    x-on:htmx:before-request="loading = true"
    x-on:htmx:after-request="loading = false"
    :disabled="loading"
  >
    <span x-show="!loading">Load Data</span>
    <span x-show="loading">Loading...</span>
  </Button>
  <div id="result" class="mt-4"></div>
</div>
```

## Porting shadcn/ui Components

This project ports React components from shadcn/ui to our server-side stack. Here's how to approach the conversion process:

### Core Conversion Rules

1. **Props and Arguments**
```jinja
{# React #}
interface ButtonProps {
  variant?: "default" | "destructive"
  size?: "default" | "sm" | "lg"
  className?: string
  disabled?: boolean
}

{# JinjaX #}
{#def
    variant: str = "default",
    size: str = "default",
    className: str = "",
    disabled: bool = False
#}
```

2. **Component Structure**
```jinja
{# Each component is self-contained #}
{#def
    className: str = "",
    error: str = ""
#}
<div class="space-y-2">
  {# Use class instead of className for HTML elements #}
  <input 
    class="w-full rounded-md border {{ className }}"
    {{ attrs.render() }}  {# Always include for extra attributes #}
  />
  {% if error %}
    <p class="text-sm text-red-500">{{ error }}</p>
  {% endif %}
</div>
```

3. **State Management Conversion**
```jsx
// React state
const [open, setOpen] = React.useState(false)

// Becomes Alpine.js state
<div x-data="{ open: false }">
  <button x-on:click="open = !open">Toggle</button>
  <div x-show="open">Content</div>
</div>
```

### Conversion Guidelines

1. **Component Definition**
  - Replace React props interface with JinjaX def block
  - Convert TypeScript types to Python types
  - Move default values to def declarations

2. **HTML Structure**
  - Keep the same basic HTML structure
  - Replace React fragments with regular HTML
  - Convert className to class on HTML elements
  - Keep className as prop name in component definition

3. **Interactivity**
  - Replace React state hooks with Alpine.js x-data
  - Convert React event handlers to Alpine.js directives
  - Use htmx for server interactions
  - Keep component behavior localized

4. **Styling**
  - Maintain Tailwind utility classes
  - Keep variant and size class mappings
  - Preserve dark mode classes
  - Support custom className extensions

### Example Conversion

React Button:
```jsx
export interface ButtonProps {
  variant?: "default" | "destructive"
  size?: "default" | "sm"
  className?: string
  disabled?: boolean
  children: React.ReactNode
}

export function Button({
  variant = "default",
  size = "default",
  className,
  disabled,
  children
}: ButtonProps) {
  return (
    <button
      className={cn(
        "rounded-md font-medium transition-colors",
        variantStyles[variant],
        sizeStyles[size],
        className
      )}
      disabled={disabled}
    >
      {children}
    </button>
  )
}
```

JinjaX Conversion:
```jinja
{#def
    variant: str = "default",
    size: str = "default",
    className: str = "",
    disabled: bool = False
#}
{% set variantStyles = {
    'default': 'bg-zinc-900 text-zinc-50 hover:bg-zinc-900/90',
    'destructive': 'bg-red-500 text-zinc-50 hover:bg-red-500/90'
} %}
{% set sizeStyles = {
    'default': 'h-10 px-4 py-2',
    'sm': 'h-9 px-3'
} %}
<button
    class="rounded-md font-medium transition-colors {{ variantStyles[variant] }} {{ sizeStyles[size] }} {{ className }}"
    {% if disabled %}disabled{% endif %}
    {{ attrs.render() }}
>
    {{ content }}
</button>
```

### Complex Component Example

React Dialog:
```jsx
function Dialog({ open, onOpenChange, children }) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay />
        <DialogPrimitive.Content>
          {children}
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  )
}
```

JinjaX/Alpine Conversion:
```jinja
{#def
    className: str = ""
#}
<div
    x-data="{ open: false }"
    x-on:keydown.escape.window="open = false"
    class="{{ className }}"
>
    {{ content }}
    <div
        x-show="open"
        x-transition
        class="fixed inset-0 bg-black/50"
        x-on:click="open = false"
    >
        <div
            class="fixed inset-x-4 top-8 mx-auto max-w-lg rounded-lg bg-white p-4"
            x-on:click.stop
        >
            <div class="content">
                {{ content }}
            </div>
        </div>
    </div>
</div>
```


### ID and Attribute Handling

1. **Using attrs.render()**
```jinja
{#def
    label: str = "",
    className: str = ""
#}
{# Good - allows id and other attributes to be passed through #}
<div class="form-group {{ className }}" {{ attrs.render() }}>
    <label>{{ label }}</label>
</div>

{# Bad - no way to add id or other HTML attributes #}
<div class="form-group {{ className }}">
    <label>{{ label }}</label>
</div>
```

2. **ID Management**
```jinja
{#def
    label: str = "",
    error: str = ""
#}
<div class="space-y-2">
  {# Input will use any id passed via attrs.render() #}
  <input 
    type="text"
    {% if error %}
      aria-describedby="{{ attrs.get('id', '') }}-error"
    {% endif %}
    {{ attrs.render() }}
  />
  {% if error %}
    {# Safely reference id even if not provided #}
    <p id="{{ attrs.get('id', '') }}-error" class="text-sm text-red-500">
      {{ error }}
    </p>
  {% endif %}
</div>
```

3. **Linked Components**
```jinja
{#def
    label: str = "",
    className: str = ""
#}
<div class="{{ className }}">
  {# Label's for attribute will match input's id if provided #}
  <label 
    {% if attrs.get('id') %}
      for="{{ attrs.get('id') }}"
    {% endif %}
    class="text-sm font-medium"
  >
    {{ label }}
  </label>
  <input 
    type="text"
    class="mt-1 block w-full"
    {{ attrs.render() }}
  />
</div>
```

4. **Dynamic References**
```jinja
{#def
    triggerId: str = None
#}
<div 
  x-show="open"
  role="dialog"
  {% if triggerId %}
    aria-labelledby="{{ triggerId }}"
  {% endif %}
  {{ attrs.render() }}
>
  {{ content }}
</div>
```

### Advanced Component Patterns

#### Global State and Document Effects
When porting components that affect the document body (like modals/dialogs):
```jinja
{#def
    className: str = ""
#}
<div
    x-data="{ 
        open: false,
        init() {
            this.$watch('open', value => {
                if (value) {
                    document.body.classList.add('overflow-hidden');
                } else {
                    document.body.classList.remove('overflow-hidden');
                }
            });
        }
    }"
>
    {{ content }}
</div>
```
- Use Alpine.js `init()` and `$watch` for managing body classes
- Handle scroll locking appropriately
- Clean up effects when component is closed
- Consider z-index management for stacked modals

#### Event Propagation and Overlays
Different components require different overlay behaviors:
```jinja
{# Dialog - Closes on overlay click #}
<div 
    class="fixed inset-0"
    x-show="open"
    x-on:click="close"
>
    <div x-on:click.stop>
        {{ content }}
    </div>
</div>

{# AlertDialog - No close on overlay #}
<div 
    class="fixed inset-0"
    x-show="open"
>
    {{ content }}
</div>
```

#### Icon Integration
When using Lucide icons:
```jinja
<button class="absolute right-4 top-4">
    <X class="h-4 w-4"/>
    <span class="sr-only">Close</span>
</button>
```
- Import icons using the Lucide React syntax
- Maintain consistent sizing and positioning
- Add screen reader text for accessibility

#### Class Management with cn()
Use the utility for consistent class merging:
```jinja
{#def
    variant: str = "default",
    className: str = ""
#}
<div class="{{ cn(
    'base-classes',
    variant == 'primary' and 'primary-classes',
    'sm:responsive-classes',
    className
) }}">
    {{ content }}
</div>
```
- Handles class conflicts
- Supports conditional classes
- Maintains responsive and state modifiers
- Preserves arbitrary values

#### Component Composition
Complex components often require specific composition:
```jinja
<Dialog>
    <DialogTrigger>
        <Button>Open</Button>
    </DialogTrigger>
    <DialogContent>
        <DialogHeader>
            <DialogTitle>Title</DialogTitle>
            <DialogDescription>Description</DialogDescription>
        </DialogHeader>
    </DialogContent>
</Dialog>
```
- Maintain consistent component hierarchy
- Preserve ARIA relationships
- Share state between related components
- Handle nested interactions correctly


### Best Practices for Attribute Handling

1. **Always Include attrs.render()**
  - Add to the main/root element of component
  - Enables passing of standard HTML attributes
  - Allows for dynamic attribute addition
  - Preserves accessibility attributes

2. **Safe ID References**
  - Use attrs.get('id', '') for optional IDs
  - Generate related IDs using base ID
  - Handle cases where ID is not provided
  - Maintain ARIA relationships

3. **Accessibility Connections**
  - Link labels to inputs
  - Connect error messages
  - Maintain ARIA attributes
  - Support screen readers
  - Support keyboard navigation

4. **State Management**
    - Use Alpine.js for component-level state
    - Manage document effects carefully
    - Clean up side effects appropriately

5. **Event Handling**
    - Consider click propagation
    - Handle keyboard interactions
    - Maintain accessibility features

6. **Styling**
    - Use cn() for class management
    - Preserve responsive classes
    - Maintain dark mode support

### Testing Converted Components

1. **Functionality Testing**
  - Verify all props work correctly
  - Test interactive behaviors
  - Check accessibility features
  - Validate dark mode support

2. **Integration Testing**
  - Test htmx interactions
  - Verify Alpine.js state management
  - Check component composition
  - Validate prop passing


## Reference Documentation

- [Modern Tools Guide](docs/content/docs/modern_tools.md): Detailed exploration of the tech stack
- [Component Creation](docs/content/docs/components.md): Building and extending components
- [Setup Guide](docs/content/docs/installation.md): Environment configuration
- [Framework Integration](docs/content/docs/fastapi.md): FastAPI setup
- [CLI Usage](docs/content/docs/cli.md): Component CLI tool
- [AI Guide](docs/content/docs/ai.md): Using AI for component development

## External Resources

- JinjaX [Documentation](https://jinjax.scaletti.dev/) and [Examples](https://jinjax.scaletti.dev/docs/introduction#example)
- htmx [Guide](https://htmx.org/docs/) and [Examples](https://htmx.org/examples/)
- Alpine.js [Documentation](https://alpinejs.dev/start-here) and [Directives](https://alpinejs.dev/directives/overview)
- Tailwind CSS [Documentation](https://tailwindcss.com/docs) and [Component Examples](https://tailwindui.com/)
- [shadcn/ui Components](https://ui.shadcn.com/)




