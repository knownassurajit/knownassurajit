from __future__ import annotations

import html
import re
from pathlib import Path

ASSET_DIR = Path("assets")
BADGE_PATTERN = "badge-*.svg"

# Shared chip design tokens keep every generated badge visually consistent. The
# palette follows the existing dark Atlassian-inspired README theme while using
# the brighter foregrounds needed for readable Material-style chips.
CHIP_HEIGHT = 28
CHIP_RADIUS = CHIP_HEIGHT // 2
LEFT_PADDING = 12
ICON_SIZE = 16
ICON_LABEL_GAP = 8
RIGHT_PADDING = 12
FONT_SIZE = 12
FONT_FAMILY = 'system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif'
BACKGROUND = "#22272B"
FOREGROUND = "#F7F8F9"
ICON_COLOR = "#579DFF"

BADGES = {
    "bash": "Bash",
    "behance": "Behance",
    "company": "COMPANY: BOSCH INDIA",
    "compose": "Jetpack Compose",
    "cplusplus": "C++",
    "email": "Email",
    "figma": "Figma",
    "focus": "FOCUS: ETL & BI",
    "git": "Git",
    "github": "GitHub",
    "instagram": "Instagram",
    "jenkins": "Jenkins",
    "kotlin": "Kotlin",
    "linkedin": "LinkedIn",
    "linux": "Linux",
    "macos": "macOS",
    "mysql": "MySQL",
    "nextjs": "Next.js",
    "oracle": "Oracle",
    "pinterest": "Pinterest",
    "portfolio": "Portfolio",
    "postgresql": "PostgreSQL",
    "powerbi": "Power BI",
    "python": "Python",
    "react": "React",
    "role": "ROLE: ASSISTANT MANAGER",
    "sketch": "Sketch",
    "spotify": "Spotify",
    "tableau": "Tableau",
    "tailwind": "Tailwind CSS",
    "windows": "Windows",
    "x": "X",
}


def extract_existing_icon(svg: str) -> str | None:
    """Reuse the downloaded Simple Icons data URI so badge generation is offline.

    The previous Shields output already contains a normalized SVG icon for each
    branded badge. Keeping that data URI avoids adding a package dependency or a
    network step, and it means future regeneration is deterministic in CI.
    """
    match = re.search(r'<image[^>]+href="([^"]+)"', svg)
    return match.group(1) if match else None


def estimate_text_width(label: str) -> int:
    """Estimate chip width using a conservative average glyph width.

    GitHub renders README SVGs in browser fonts, so exact text metrics can vary
    across platforms. A slightly generous width prevents clipping while keeping
    rows compact enough to wrap cleanly on narrow profile layouts.
    """
    narrow_chars = sum(1 for char in label if char in " .:ilI|!")
    wide_chars = sum(1 for char in label if char in "MW@&")
    normal_chars = len(label) - narrow_chars - wide_chars
    return round((narrow_chars * 3.6) + (normal_chars * 6.6) + (wide_chars * 9.0))


def build_badge(name: str, label: str, icon_href: str | None) -> str:
    title = html.escape(label)
    text_width = estimate_text_width(label)
    content_width = LEFT_PADDING + text_width + RIGHT_PADDING
    if icon_href:
        content_width += ICON_SIZE + ICON_LABEL_GAP
    width = max(CHIP_HEIGHT, content_width)
    text_x = LEFT_PADDING + (ICON_SIZE + ICON_LABEL_GAP if icon_href else 0)
    icon_markup = ""
    if icon_href:
        # The icon is intentionally aligned to whole pixels to keep the 16px
        # artwork crisp after GitHub scales badges in dense README rows.
        icon_markup = (
            f'  <image x="{LEFT_PADDING}" y="6" width="{ICON_SIZE}" height="{ICON_SIZE}" '
            f'href="{icon_href}" />\n'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{CHIP_HEIGHT}" '
        f'viewBox="0 0 {width} {CHIP_HEIGHT}" role="img" aria-label="{title}">\n'
        f'  <title>{title}</title>\n'
        f'  <rect width="{width}" height="{CHIP_HEIGHT}" rx="{CHIP_RADIUS}" fill="{BACKGROUND}" />\n'
        f'{icon_markup}'
        f'  <text x="{text_x}" y="50%" dy="0.35em" fill="{FOREGROUND}" '
        f'font-family="{html.escape(FONT_FAMILY)}" font-size="{FONT_SIZE}" '
        f'font-weight="600">{title}</text>\n'
        f'</svg>\n'
    )


def main() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    existing_icons = {}
    for path in ASSET_DIR.glob(BADGE_PATTERN):
        existing_icons[path.stem.removeprefix("badge-")] = extract_existing_icon(path.read_text())

    for name, label in BADGES.items():
        path = ASSET_DIR / f"badge-{name}.svg"
        path.write_text(build_badge(name, label, existing_icons.get(name)), encoding="utf-8")
        print(f"Generated {path}")


if __name__ == "__main__":
    main()
