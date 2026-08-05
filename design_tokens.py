"""Shared design tokens for the SQL-terminal profile aesthetic."""

DESIGN_TOKENS = {
    "surface": "#0E1420",
    "surface_raised": "#161D2B",
    "surface_inset": "#1D2536",
    "primary": "#E0A458",
    "primary_soft": "#C98A4B",
    "accent": "#579DFF",
    "on_surface": "#E7EBF5",
    "on_surface_variant": "#7C89A6",
    "on_surface_faint": "#3F4A63",
    "on_surface_bright": "#F7F8F9",
    "outline": "#2A3348",
    "heatmap_0": "#1D2536",
    "heatmap_1": "#3F4A63",
    "heatmap_2": "#5C6883",
    "heatmap_3": "#C98A4B",
    "heatmap_4": "#E0A458",
    "pill_surface": "#22272B",
}

LAYOUT = {
    "card_width": 900,
    "card_radius": 12,
    "content_inset": 28,
    "pill_height": 28,
    "chip_height": 24,
}


def token(name: str) -> str:
    return DESIGN_TOKENS[name]


def token_param(name: str) -> str:
    return token(name).lstrip("#")


def layout(name: str):
    return LAYOUT[name]
