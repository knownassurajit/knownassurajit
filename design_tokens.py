"""Shared design tokens for profile README assets.

The profile is rendered by a mix of hand-authored SVG files, Shields.io badge
URLs, and GitHub stats image URLs. Keeping those values here gives every asset a
single source of truth instead of letting tiny color differences drift over time.
"""

DESIGN_TOKENS = {
    "surface": "#202124",
    "surface_variant": "#303134",
    "primary": "#1A73E8",
    "primary_container": "#0B57D0",
    "on_surface": "#E8EAED",
    "on_surface_variant": "#BDC1C6",
    "outline": "#5F6368",
}


def token(name: str) -> str:
    """Return a hex token with the leading # for SVG/CSS contexts."""
    return DESIGN_TOKENS[name]


def token_param(name: str) -> str:
    """Return a hex token without # for URL query parameters."""
    return token(name).lstrip("#")
