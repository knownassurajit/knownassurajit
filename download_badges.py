"""Generate compact pill badges for social links and tech stack chips.

Downloads Shields.io SVGs to extract embedded logos, then wraps them in a
shared pill template driven by design_tokens.py.
"""

import os
import re
import ssl
import urllib.parse
import urllib.request

from design_tokens import layout, token, token_param

ssl._create_default_https_context = ssl._create_unverified_context

SURFACE = token("surface")
LOGO_COLOR = token("primary")
TEXT_COLOR = token("on_surface_bright")
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"

SOCIAL_BADGES = {
    "portfolio": ("Portfolio", "vercel"),
    "email": ("Email", "gmail"),
    "linkedin": ("LinkedIn", "linkedin"),
    "github": ("GitHub", "github"),
    "x": ("X", "x"),
    "instagram": ("Instagram", "instagram"),
    "behance": ("Behance", "behance"),
    "pinterest": ("Pinterest", "pinterest"),
    "spotify": ("Spotify", "spotify"),
}

TECH_BADGES = {
    "python": ("Python", "python"),
    "sql": ("SQL", None),
    "oracle": ("Oracle", "oracle"),
    "postgresql": ("PostgreSQL", "postgresql"),
    "mysql": ("MySQL", "mysql"),
    "powerbi": ("Power BI", "powerbi"),
    "tableau": ("Tableau", "tableau"),
    "kotlin": ("Kotlin", "kotlin"),
    "react": ("React", "react"),
    "nextjs": ("Next.js", "nextdotjs"),
    "git": ("Git", "git"),
    "jenkins": ("Jenkins", "jenkins"),
    "linux": ("Linux", "linux"),
}


def _shields_url(label: str, logo: str | None) -> str:
    theme = token_param("surface")
    logo_color = token_param("primary")
    encoded = urllib.parse.quote(label)
    base = f"https://img.shields.io/badge/{encoded}-{theme}?style=flat-square"
    if logo:
        return f"{base}&logo={logo}&logoColor={logo_color}"
    return base


def _fetch_logo_href(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        svg = response.read().decode()
    match = re.search(r'href="(data:image/svg\+xml;base64,[^"]+)"', svg)
    return match.group(1) if match else None


def _text_width(label: str, font_size: int) -> int:
    """Approximate label width for pill sizing."""
    return int(len(label) * font_size * 0.58) + 8


def pill_badge(name: str, label: str, logo_href: str | None, *, chip: bool = False) -> str:
    height = layout("chip_height") if chip else layout("pill_height")
    radius = height // 2
    font_size = 11 if chip else 12
    icon_size = 14 if chip else 16
    icon_x = 10 if chip else 12
    text_x = icon_x + icon_size + 6
    text_width = _text_width(label, font_size)
    width = text_x + text_width + 12

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{label}">',
        f"<title>{label}</title>",
        f'<rect width="{width}" height="{height}" rx="{radius}" fill="{SURFACE}" />',
    ]
    if logo_href:
        icon_y = (height - icon_size) / 2
        parts.append(
            f'<image x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" '
            f'href="{logo_href}" />'
        )
    parts.append(
        f'<text x="{text_x}" y="50%" dy="0.35em" fill="{TEXT_COLOR}" '
        f'font-family="{FONT}" font-size="{font_size}" font-weight="600">{label}</text>'
    )
    parts.append("</svg>")
    return "".join(parts)


def generate_badges(badge_map: dict, *, chip: bool = False) -> None:
    os.makedirs("assets", exist_ok=True)
    for name, (label, logo) in badge_map.items():
        print(f"Generating {'chip' if chip else 'pill'} {name}...")
        logo_href = _fetch_logo_href(_shields_url(label, logo)) if logo else None
        svg = pill_badge(name, label, logo_href, chip=chip)
        with open(f"assets/badge-{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg)


if __name__ == "__main__":
    generate_badges(SOCIAL_BADGES, chip=False)
    generate_badges(TECH_BADGES, chip=True)
