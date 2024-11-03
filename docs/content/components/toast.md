---
title: Toast
description: A succinct message that is displayed temporarily.
templates:
  - Toast.jinja
  - ToastContent.jinja
  - ToastTrigger.jinja
---

<TabPreview component="Toast" template="examples/toast.html"/>

<Prose>

## Usage

</Prose>

<IncludeTemplate template="examples/toast.html"/>

<Prose>

## Attributes

| Component    | Prop           | Type   | Default     | Description                                                                                             |
|--------------|----------------|--------|-------------|---------------------------------------------------------------------------------------------------------|
| Toast        | `id`           | String |             | The css id for the Toast.                                                                               |
| Toast        | `duration`     | Number | `30000`     | Duration in milliseconds before toast auto-dismisses.                                                   |
| ToastContent | `type`         | String | `"default"` | Style variant of the toast. Options: `"default"`, `"success"`, `"error"`, `"warning"`, `"destructive"`. |
| ToastContent | `title`        | String | `""`        | The title text displayed in the toast.                                                                  |
| ToastContent | `description`  | String | `""`        | The description text displayed below the title.                                                         |
| ToastTrigger | `variant`      | String | `"default"` | The Button component variant to use.                                                                    |
| ToastTrigger | `toast_target` | String |             | The target toast identifier to trigger.                                                                 |

Toast components require an `id` so that the dispatch event can call the component to display it. 

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Success" template="examples/toast_success.html"/>
<TabPreview component="Warning" template="examples/toast_warning.html"/>
<TabPreview component="Error" template="examples/toast_error.html"/>
<TabPreview component="Destructive" template="examples/toast_destructive.html"/>
