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

# Bypass SSL certificate verification issues on macOS python
ssl._create_default_https_context = ssl._create_unverified_context

# Atlassian Design System (dark theme): raised surface (#22272B) background with
# brand-blue (#579DFF) logos. Flat-square keeps the ADS flat aesthetic.
theme = "22272B"
logo_color = "579DFF"
style = "flat-square"

badges = {
    "python": f"https://img.shields.io/badge/Python-{theme}?style={style}&logo=python&logoColor={logo_color}",
    "cplusplus": f"https://img.shields.io/badge/C%2B%2B-{theme}?style={style}&logo=c%2B%2B&logoColor={logo_color}",
    "bash": f"https://img.shields.io/badge/Bash-{theme}?style={style}&logo=gnu-bash&logoColor={logo_color}",
    "oracle": f"https://img.shields.io/badge/Oracle-{theme}?style={style}&logo=oracle&logoColor={logo_color}",
    "postgresql": f"https://img.shields.io/badge/PostgreSQL-{theme}?style={style}&logo=postgresql&logoColor={logo_color}",
    "mysql": f"https://img.shields.io/badge/MySQL-{theme}?style={style}&logo=mysql&logoColor={logo_color}",
    "git": f"https://img.shields.io/badge/Git-{theme}?style={style}&logo=git&logoColor={logo_color}",
    "jenkins": f"https://img.shields.io/badge/Jenkins-{theme}?style={style}&logo=jenkins&logoColor={logo_color}",
    "powerbi": f"https://img.shields.io/badge/Power_BI-{theme}?style={style}&logo=powerbi&logoColor={logo_color}",
    "tableau": f"https://img.shields.io/badge/Tableau-{theme}?style={style}&logo=tableau&logoColor={logo_color}",
    "figma": f"https://img.shields.io/badge/Figma-{theme}?style={style}&logo=figma&logoColor={logo_color}",
    "linux": f"https://img.shields.io/badge/Linux-{theme}?style={style}&logo=linux&logoColor={logo_color}",
    "windows": f"https://img.shields.io/badge/Windows-{theme}?style={style}&logo=windows&logoColor={logo_color}",
    "macos": f"https://img.shields.io/badge/macOS-{theme}?style={style}&logo=apple&logoColor={logo_color}",
    "kotlin": f"https://img.shields.io/badge/Kotlin-{theme}?style={style}&logo=kotlin&logoColor={logo_color}",
    "react": f"https://img.shields.io/badge/React-{theme}?style={style}&logo=react&logoColor={logo_color}",
    "nextjs": f"https://img.shields.io/badge/Next.js-{theme}?style={style}&logo=nextdotjs&logoColor={logo_color}",
    "tailwind": f"https://img.shields.io/badge/Tailwind_CSS-{theme}?style={style}&logo=tailwindcss&logoColor={logo_color}",
    "compose": f"https://img.shields.io/badge/Jetpack_Compose-{theme}?style={style}&logo=jetpackcompose&logoColor={logo_color}",
    "sketch": f"https://img.shields.io/badge/Sketch-{theme}?style={style}&logo=sketch&logoColor={logo_color}",
    "portfolio": f"https://img.shields.io/badge/Portfolio-{theme}?style={style}&logo=vercel&logoColor={logo_color}",
    "email": f"https://img.shields.io/badge/Email-{theme}?style={style}&logo=gmail&logoColor={logo_color}",
    "linkedin": f"https://img.shields.io/badge/LinkedIn-{theme}?style={style}&logo=linkedin&logoColor={logo_color}",
    "github": f"https://img.shields.io/badge/GitHub-{theme}?style={style}&logo=github&logoColor={logo_color}",
    "x": f"https://img.shields.io/badge/X-{theme}?style={style}&logo=x&logoColor={logo_color}",
    "instagram": f"https://img.shields.io/badge/Instagram-{theme}?style={style}&logo=instagram&logoColor={logo_color}",
    "behance": f"https://img.shields.io/badge/Behance-{theme}?style={style}&logo=behance&logoColor={logo_color}",
    "pinterest": f"https://img.shields.io/badge/Pinterest-{theme}?style={style}&logo=pinterest&logoColor={logo_color}",
    "spotify": f"https://img.shields.io/badge/Spotify-{theme}?style={style}&logo=spotify&logoColor={logo_color}"
}

TECH_BADGES = {
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
