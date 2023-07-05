"""Recognizers for different naming conventions."""

import re


def is_snake(input: str) -> bool:
    """Check if input is snake case."""
    return bool(re.match(r"^[a-z]+(_[a-z]+)*$", input))


def is_camel(input: str) -> bool:
    """Check if input is camel case."""
    return bool(re.match(r"^[a-z]+([A-Z][a-z]+)*$", input))


def is_pascal(input: str) -> bool:
    """Check if input is pascal case."""
    return bool(re.match(r"^[A-Z][a-z]*([A-Z][a-z]*)*$", input))


def is_kebab(input: str) -> bool:
    """Check if input is kebab case."""
    return bool(re.match(r"^[a-z]+(-[a-z]+)*$", input))
