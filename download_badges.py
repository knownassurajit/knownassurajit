import urllib.request
import os
import ssl

from design_tokens import token_param

# Bypass SSL certificate verification issues on macOS python
ssl._create_default_https_context = ssl._create_unverified_context

# Profile design tokens (Material dark surface + Google Blue primary).
# Shields.io expects URL color parameters without a leading #, so token_param()
# keeps the generated badge SVGs aligned with the rest of the profile assets.
theme = token_param("surface")
label_color = token_param("surface_variant")
logo_color = token_param("primary")
style = "flat-square"
badges = {
    "python": f"https://img.shields.io/badge/Python-{theme}?style={style}&labelColor={label_color}&logo=python&logoColor={logo_color}",
    "cplusplus": f"https://img.shields.io/badge/C%2B%2B-{theme}?style={style}&labelColor={label_color}&logo=c%2B%2B&logoColor={logo_color}",
    "bash": f"https://img.shields.io/badge/Bash-{theme}?style={style}&labelColor={label_color}&logo=gnu-bash&logoColor={logo_color}",
    "oracle": f"https://img.shields.io/badge/Oracle-{theme}?style={style}&labelColor={label_color}&logo=oracle&logoColor={logo_color}",
    "postgresql": f"https://img.shields.io/badge/PostgreSQL-{theme}?style={style}&labelColor={label_color}&logo=postgresql&logoColor={logo_color}",
    "mysql": f"https://img.shields.io/badge/MySQL-{theme}?style={style}&labelColor={label_color}&logo=mysql&logoColor={logo_color}",
    "git": f"https://img.shields.io/badge/Git-{theme}?style={style}&labelColor={label_color}&logo=git&logoColor={logo_color}",
    "jenkins": f"https://img.shields.io/badge/Jenkins-{theme}?style={style}&labelColor={label_color}&logo=jenkins&logoColor={logo_color}",
    "powerbi": f"https://img.shields.io/badge/Power_BI-{theme}?style={style}&labelColor={label_color}&logo=powerbi&logoColor={logo_color}",
    "tableau": f"https://img.shields.io/badge/Tableau-{theme}?style={style}&labelColor={label_color}&logo=tableau&logoColor={logo_color}",
    "figma": f"https://img.shields.io/badge/Figma-{theme}?style={style}&labelColor={label_color}&logo=figma&logoColor={logo_color}",
    "linux": f"https://img.shields.io/badge/Linux-{theme}?style={style}&labelColor={label_color}&logo=linux&logoColor={logo_color}",
    "windows": f"https://img.shields.io/badge/Windows-{theme}?style={style}&labelColor={label_color}&logo=windows&logoColor={logo_color}",
    "macos": f"https://img.shields.io/badge/macOS-{theme}?style={style}&labelColor={label_color}&logo=apple&logoColor={logo_color}",
    "kotlin": f"https://img.shields.io/badge/Kotlin-{theme}?style={style}&labelColor={label_color}&logo=kotlin&logoColor={logo_color}",
    "react": f"https://img.shields.io/badge/React-{theme}?style={style}&labelColor={label_color}&logo=react&logoColor={logo_color}",
    "nextjs": f"https://img.shields.io/badge/Next.js-{theme}?style={style}&labelColor={label_color}&logo=nextdotjs&logoColor={logo_color}",
    "tailwind": f"https://img.shields.io/badge/Tailwind_CSS-{theme}?style={style}&labelColor={label_color}&logo=tailwindcss&logoColor={logo_color}",
    "compose": f"https://img.shields.io/badge/Jetpack_Compose-{theme}?style={style}&labelColor={label_color}&logo=jetpackcompose&logoColor={logo_color}",
    "sketch": f"https://img.shields.io/badge/Sketch-{theme}?style={style}&labelColor={label_color}&logo=sketch&logoColor={logo_color}",
    "portfolio": f"https://img.shields.io/badge/Portfolio-{theme}?style={style}&labelColor={label_color}&logo=vercel&logoColor={logo_color}",
    "email": f"https://img.shields.io/badge/Email-{theme}?style={style}&labelColor={label_color}&logo=gmail&logoColor={logo_color}",
    "linkedin": f"https://img.shields.io/badge/LinkedIn-{theme}?style={style}&labelColor={label_color}&logo=linkedin&logoColor={logo_color}",
    "github": f"https://img.shields.io/badge/GitHub-{theme}?style={style}&labelColor={label_color}&logo=github&logoColor={logo_color}",
    "x": f"https://img.shields.io/badge/X-{theme}?style={style}&labelColor={label_color}&logo=x&logoColor={logo_color}",
    "instagram": f"https://img.shields.io/badge/Instagram-{theme}?style={style}&labelColor={label_color}&logo=instagram&logoColor={logo_color}",
    "behance": f"https://img.shields.io/badge/Behance-{theme}?style={style}&labelColor={label_color}&logo=behance&logoColor={logo_color}",
    "pinterest": f"https://img.shields.io/badge/Pinterest-{theme}?style={style}&labelColor={label_color}&logo=pinterest&logoColor={logo_color}",
    "spotify": f"https://img.shields.io/badge/Spotify-{theme}?style={style}&labelColor={label_color}&logo=spotify&logoColor={logo_color}"
}

os.makedirs("assets", exist_ok=True)
for name, url in badges.items():
    print(f"Downloading {name}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            with open(f"assets/badge-{name}.svg", 'wb') as f:
                f.write(response.read())
    except Exception as e:
        print(f"Failed to download {name}: {e}")
