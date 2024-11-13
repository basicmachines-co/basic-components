import re
from typing import Dict, List, Optional, Tuple

# Core Tailwind modifiers and prefixes
MODIFIERS = {
    "sm:",
    "md:",
    "lg:",
    "xl:",
    "2xl:",
    "hover:",
    "focus:",
    "active:",
    "disabled:",
    "dark:",
}

# Define order of properties for consistent output
PROPERTY_ORDER = [
    "display",
    "position",
    "background",
    "width",
    "height",
    "padding",
    "margin",
    "text",
    "border",
    "rounded",
    "flex",
    "grid",
    "order",
    "justify",
    "align",
    "space",
]

# Core Tailwind property conflicts
PROPERTY_CONFLICTS = {
    "width": {"w-"},
    "height": {"h-"},
    "padding": {"p-", "px-", "py-", "pt-", "pr-", "pb-", "pl-"},
    "margin": {"m-", "m-", "mx-", "my-", "mt-", "mr-", "mb-", "ml-"},
    "background": {"bg-"},
    "text": {"text-"},
    "border": {"border-"},
    "rounded": {"rounded-"},
    "flex": {"flex-"},
    "grid": {"grid-"},
    "order": {"order-"},
    "justify": {"justify-"},
    "align": {"items-", "content-"},
    "space": {"space-x-", "space-y-"},
    "display": {"block", "inline", "flex", "grid", "hidden"},
    "position": {"static", "fixed", "absolute", "relative", "sticky"},
}


class TailwindMerge:
    def __init__(self):
        self.arbitrary_pattern = re.compile(r"^\[.*\]$")

    def _split_classes(self, class_string: str) -> List[str]:
        """Split a class string into individual classes."""
        return [c.strip() for c in class_string.split() if c.strip()]

    def _parse_class(self, class_name: str) -> Tuple[str, Optional[str], str]:
        """Parse a class into (modifier, property, value)."""
        # Handle modifiers (sm:, hover:, etc.)
        modifier = None
        remaining = class_name

        for mod in MODIFIERS:
            if class_name.startswith(mod):
                modifier = mod
                remaining = class_name[len(mod) :]
                break

        # Find matching property
        property_name = None
        for prop, prefixes in PROPERTY_CONFLICTS.items():
            for prefix in prefixes:
                if remaining.startswith(prefix) or remaining in prefixes:
                    property_name = prop
                    value = remaining
                    break
            if property_name:
                break

        if not property_name:
            property_name = "other"
            value = remaining

        return (modifier or "", property_name, value)

    def _has_arbitrary_value(self, class_name: str) -> bool:
        """Check if class has arbitrary value [...]."""
        return bool(self.arbitrary_pattern.search(class_name))

    def _sort_classes(self, classes: List[str]) -> List[str]:
        """Sort classes according to property order with base classes first."""

        def get_sort_key(class_name: str) -> tuple:
            modifier, prop, _ = self._parse_class(class_name)
            try:
                prop_order = PROPERTY_ORDER.index(prop)
            except ValueError:
                prop_order = len(PROPERTY_ORDER)

            # Base classes (no modifier) should come before modified classes
            modifier_order = 1 if modifier else 0

            return (modifier_order, prop_order, class_name)

        return sorted(classes, key=get_sort_key)

    def merge(self, *class_lists: str) -> str:
        """Merge multiple class lists, resolving conflicts."""
        winners: Dict[Tuple[str, str], str] = {}

        for class_list in class_lists:
            if not class_list:
                continue

            classes = self._split_classes(class_list)

            for class_name in classes:
                if not class_name:
                    continue

                modifier, property_name, value = self._parse_class(class_name)

                if self._has_arbitrary_value(value):
                    winners[(modifier, class_name)] = class_name
                    continue

                key = (modifier, property_name)
                winners[key] = class_name

        # Collect all classes
        result = []
        for key, class_name in winners.items():
            result.append(class_name)

        # Sort according to property order
        return " ".join(self._sort_classes(result))


def tw(*classes: str) -> str:
    """Merge Tailwind CSS classes while handling conflicts and maintaining consistent ordering.

    The function resolves conflicts between Tailwind classes by:
    - Taking the last instance of conflicting classes
    - Maintaining a consistent ordering of properties
    - Preserving modifiers (responsive, state, etc.)
    - Handling arbitrary values correctly

    Args:
        *classes: Variable number of strings containing space-separated Tailwind classes.
                 Falsy values (None, False, empty strings) are ignored.

    Returns:
        str: Merged class string with conflicts resolved and consistent ordering

    Examples:
        Basic class merging:
        >>> tw("p-4 bg-red-500", "p-8")
        'bg-red-500 p-8'

        With responsive modifiers:
        >>> tw("sm:p-4 bg-red-500", "sm:p-8")
        'bg-red-500 sm:p-8'

        Using conditionals with 'and':
        >>> is_active = True
        >>> tw(
        ...     "base-class",
        ...     is_active and "active-class",  # Will include 'active-class' if is_active is True
        ...     False and "never-shown"        # Will be ignored (evaluates to False)
        ... )
        'base-class active-class'

        Multiple conditionals:
        >>> is_active = True
        >>> is_disabled = False
        >>> tw(
        ...     "btn",
        ...     is_active and "bg-blue-500",   # Included
        ...     is_disabled and "opacity-50"    # Ignored (False and "opacity-50" evaluates to False)
        ... )
        'btn bg-blue-500'

        With arbitrary values:
        >>> tw("grid grid-cols-[1fr,auto] p-4", "p-8")
        'grid p-8 grid-cols-[1fr,auto]'

    Notes:
        The 'and' operator in Python returns its second operand if the first is True,
        otherwise it returns the first operand. This allows for conditional classes:

        True and "my-class"  -> "my-class"
        False and "my-class" -> False

        Since the function ignores falsy values, False and None are filtered out.
    """
    merger = TailwindMerge()
    return merger.merge(*classes)
