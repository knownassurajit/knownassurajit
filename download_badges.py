import urllib.request
import os

badges = {
    "python": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
    "cplusplus": "https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white",
    "bash": "https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white",
    "oracle": "https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white",
    "postgresql": "https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white",
    "mysql": "https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white",
    "git": "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
    "jenkins": "https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white",
    "powerbi": "https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black",
    "tableau": "https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white",
    "figma": "https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white",
    "linux": "https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black",
    "windows": "https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white",
    "macos": "https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white"
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
