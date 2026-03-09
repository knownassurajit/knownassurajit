import urllib.request
import os

# Use monochrome (0d1117) and green (2ea043) theme with flat-square style
theme = "0d1117"
logo_color = "2ea043"
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
    "macos": f"https://img.shields.io/badge/macOS-{theme}?style={style}&logo=apple&logoColor={logo_color}"
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
