# Porting Components with AI

The components in this repo have been ported primarily using AI from React to JinjaX implementations.

The following guide outlines the process for porting React components from **shadcn/ui** to **JinjaX** templates using
an LLM.

## Porting Process

1. **Select** a component from shadcn/ui to port.
2. **Gather** information about the component (name, description, React code, usage examples).
3. **Use AI** to assist with the initial port (see Part 2 for AI prompting guidelines).
4. **Implement** the AI-provided JinjaX version in your project.
5. **Test and iterate** on the implementation.
6. **Refine** the component based on testing results.
7. **Document** the component's usage and any differences from the React version.
8. **Review** to ensure adherence to project guidelines and consistency with other components.

## AI Assistance Guidelines

The following section is a reference for prompting AI models when porting components. It includes rules,
guidelines, and example prompts to ensure consistent and effective component creation.

## Rules for Creating Components

1. **Props Definition**:
    - Use `{#def ... #}` to declare props.
    - Include `id`, `className`, and other relevant attributes.

2. **Dynamic Attributes**:
    - Always include `{{ attrs.render() }}` for additional attributes.

3. **Content Slots**:
    - Use `{{ content }}` as the default slot for main content.
    - Create separate components for additional slots instead of using multiple slots in a single component.

4. **Class Handling**:
    - Use `className` for component props.
    - Convert `className` to `class` for native HTML elements in the output.

5. **Event Handlers and Interactivity**:
    - Use Alpine.js for dynamic behaviors (e.g., `@click`, `x-show`).
    - Set attributes like `onclick` directly as props.

6. **ID Handling**:
    - Generally, an id may be passed as an extra arg when the component is declared.
    - The component should behave correctly if `id` is not provided, preventing any invalid HTML output.
    - Always include `{{ attrs.render() }}` for attributes that might be passed dynamically when the component is
      declared (including `id`).

7. **Conditional Classes and States**:
    - Use Alpine.js for managing conditional classes and states.
    - Limit the scope of Alpine `x-data` to the component.

8. **Component Structure**:
    - Components should be standalone units without relying on includes or macros.

9. **Logic**
    - Components can use Jinja logic, conditionals and macros internally when needed.
    - Components should not have any external jinja template dependencies (extends, includes).


## Effective AI Prompting

When providing a new component for porting, copy/paste this README into a chat to give context. Then, use the following
template to port a component:

```
I'm porting the [Component Name] from shadcn/ui to JinjaX. Here's the relevant information:

1. Component Name: [Name]
   Documentation: [Link to shadcn/ui docs]

2. Description:
   [Brief description of component functionality]

3. React Source Code:
   
   [Paste React component code here]
   
4. Example Usage:
   
   [Copy/paste shadnc component usage example]
   
Please create a JinjaX version of this component that:

1. Uses Tailwind CSS for styling
2. Implements interactivity using Alpine.js
3. Follows the project guidelines for component creation (as detailed in the Rules section)
4. Maintains the same functionality and accessibility features as the original

Explain any complex logic or Alpine.js implementations in your response.

```
