---
title: Installation
description: How to install dependencies.
---

<Prose>


## JinjaX

Install the required JinjaX library into your project using your package manager.

```bash
pip install jinjax  
```

Configure your Jinja environment to load the components according to the [JinjaX docs](https://jinjax.scaletti.dev/guide/).   

## Tailwind CSS

Components are styled using Tailwind CSS. You need to install Tailwind CSS in your project.

Follow the Tailwind CSS [installation instructions](https://tailwindcss.com/docs/installation) to get started.

### Config

You will need to set the paths to your templates and components in the `tailwind.config.js` file.

```javascript
const { fontFamily } = require("tailwindcss/defaultTheme")

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
      "templates/**/*.{html}",  /* any Jinja templates that use tailwind styles */
      "components/**/*.{jinja}" /* any JinjaX components that use tailwind styles */
  ],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: `var(--radius)`,
        md: `calc(var(--radius) - 2px)`,
        sm: "calc(var(--radius) - 4px)",
      },
      fontFamily: {
        sans: ["var(--font-sans)", ...fontFamily.sans],
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
```

### CSS styles 

Add the following to your tailwind `input.css` file. You can learn more about using CSS variables for theming in the [tailwind theming docs](https://ui.shadcn.com/docs/theming).

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 47.4% 11.2%;

    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;

    --popover: 0 0% 100%;
    --popover-foreground: 222.2 47.4% 11.2%;

    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;

    --card: 0 0% 100%;
    --card-foreground: 222.2 47.4% 11.2%;

    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;

    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;

    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;

    --destructive: 0 100% 50%;
    --destructive-foreground: 210 40% 98%;

    --ring: 215 20.2% 65.1%;

    --radius: 0.5rem;
  }

  .dark {
    --background: 224 71% 4%;
    --foreground: 213 31% 91%;

    --muted: 223 47% 11%;
    --muted-foreground: 215.4 16.3% 56.9%;

    --accent: 216 34% 17%;
    --accent-foreground: 210 40% 98%;

    --popover: 224 71% 4%;
    --popover-foreground: 215 20.2% 65.1%;

    --border: 216 34% 17%;
    --input: 216 34% 17%;

    --card: 224 71% 4%;
    --card-foreground: 213 31% 91%;

    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 1.2%;

    --secondary: 222.2 47.4% 11.2%;
    --secondary-foreground: 210 40% 98%;

    --destructive: 0 63% 31%;
    --destructive-foreground: 210 40% 98%;

    --ring: 216 34% 17%;

    --radius: 0.5rem;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
}

```

### Build Tailwind CSS


You will probably want to add some commands to build tailwind styles and have it watch for changes.
Assuming your main css file is `src/input.css`, You could use this `package.json`.

```json
{
  "name": "basic-components",
  "version": "1.0.0",
  "main": "tailwind.config.js",
  "directories": {
    "doc": "docs"
  },
  "scripts": {
    "build": "npx tailwindcss -i docs/static/src/input.css -o docs/static/dist/output.css",
    "build-prod": "npx tailwindcss -i docs/static/src/input.css -o docs/static/dist/output.css --minify",
    "watch": "npx tailwindcss -i docs/static/src/input.css -o docs/static/dist/output.css --watch"
  },
  "devDependencies": {
    "@tailwindcss/forms": "^0.5.7",
    "tailwind-merge": "^2.5.3",
    "tailwindcss": "3.4.10",
    "tailwindcss-animate": "^1.0.7"
  },
  "dependencies": {
    "@tailwindcss/typography": "^0.5.15"
  }
}
```

## Frameworks

See the docs for setting your project with [FastAPI](/docs/fastapi), [Django](/docs/django), or [Flask](/docs/flask).

</Prose>