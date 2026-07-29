"""Shared design tokens for profile README assets.

The profile is rendered by a mix of hand-authored SVG files, generated pill
badges, and API-driven stat cards. Keeping values here gives every asset a
single source of truth instead of letting tiny color differences drift over time.
"""

DESIGN_TOKENS = {
    "surface": "#22272B",
    "surface_variant": "#2C333A",
    "primary": "#579DFF",
    "primary_container": "#0C66E4",
    "on_surface": "#C7D1DB",
    "on_surface_variant": "#8C9BAB",
    "on_surface_bright": "#F7F8F9",
    "outline": "#2C333A",
}

LAYOUT = {
    "card_width": 720,
    "card_height": 180,
    "card_radius": 14,
    "accent_rail_width": 4,
    "content_inset": 32,
    "pill_height": 28,
    "chip_height": 24,
    "pill_radius": 14,
}


def token(name: str) -> str:
    """Return a hex token with the leading # for SVG/CSS contexts."""
    return DESIGN_TOKENS[name]


def token_param(name: str) -> str:
    """Return a hex token without # for URL query parameters."""
    return token(name).lstrip("#")


def layout(name: str):
    """Return a shared layout constant."""
    return LAYOUT[name]
