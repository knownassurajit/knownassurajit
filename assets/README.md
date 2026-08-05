# 🎨 GitHub Profile Assets (`knownassurajit/assets`)

A curated collection of vector badges, interactive SVG banners, database-themed statistic cards, and UI icons powering the GitHub profile README for [**Surajit Das**](https://github.com/knownassurajit).

---

## 📐 Asset Architecture & Manifest

### 1. 🖥️ Banners & Header Illustrations
| Asset | Dimensions | Description | Preview Path |
| :--- | :---: | :--- | :--- |
| [`header.svg`](file:///Users/knownassurajit/Documents/Codes/GitHub/knownassurajit/assets/header.svg) | `900 × 260` | psql interactive terminal header showcasing name, role, and organization. | `assets/header.svg` |
| [`typing-intro.svg`](file:///Users/knownassurajit/Documents/Codes/GitHub/knownassurajit/assets/typing-intro.svg) | `600 × 50` | Animated CSS typing SVG banner displaying key professional titles. | `assets/typing-intro.svg` |

---

### 2. 📊 Database-Themed Statistic Cards
| Asset | Dimensions | Description | Preview Path |
| :--- | :---: | :--- | :--- |
| [`stat-overview.svg`](file:///Users/knownassurajit/Documents/Codes/GitHub/knownassurajit/assets/stat-overview.svg) | `900 × 220` | PostgreSQL `EXPLAIN ANALYZE` query plan card for public repositories, commits, streaks, and PRs. | `assets/stat-overview.svg` |
| [`stat-languages.svg`](file:///Users/knownassurajit/Documents/Codes/GitHub/knownassurajit/assets/stat-languages.svg) | `900 × 230` | PostgreSQL `GROUP BY` query result chart displaying top language breakdown with custom progress indicators. | `assets/stat-languages.svg` |

---

### 3. 🧩 Domain & Section Icons (`assets/icon-*.svg`)
Custom 24×24 vector icons matching the dark database aesthetic:

| Category | Icon Assets | Description |
| :--- | :--- | :--- |
| **Profile & Core** | `icon-profile.svg`, `icon-stack.svg`, `icon-works.svg`, `icon-journey.svg` | Main section header markers for README navigation |
| **Engineering Domains** | `icon-database.svg`, `icon-backend.svg`, `icon-frontend.svg`, `icon-dataops.svg`, `icon-uiux.svg` | Domain expertise & architectural discipline badges |
| **Meta & Credentials** | `icon-certs.svg`, `icon-education.svg`, `icon-activity.svg` | Certification, education, and automated GitHub activity feed headers |

---

### 4. 🏷️ Technology & Platform Badges (`assets/badges/`)
All technology and social platform badges reside inside the [`assets/badges/`](file:///Users/knownassurajit/Documents/Codes/GitHub/knownassurajit/assets/badges) subfolder:

#### 🔹 Data & Enterprise Engineering
`badge-sql.svg` · `badge-oracle.svg` · `badge-postgresql.svg` · `badge-mysql.svg` · `badge-python.svg` · `badge-powerbi.svg` · `badge-tableau.svg`

#### 🔹 Software Engineering & DevOps
`badge-kotlin.svg` · `badge-compose.svg` · `badge-cplusplus.svg` · `badge-react.svg` · `badge-nextjs.svg` · `badge-tailwind.svg` · `badge-git.svg` · `badge-jenkins.svg` · `badge-linux.svg` · `badge-macos.svg` · `badge-windows.svg` · `badge-bash.svg`

#### 🔹 Design & UI/UX
`badge-figma.svg` · `badge-sketch.svg`

#### 🔹 Social & Professional Profiles
`badge-portfolio.svg` · `badge-email.svg` · `badge-linkedin.svg` · `badge-github.svg` · `badge-x.svg` · `badge-instagram.svg` · `badge-behance.svg` · `badge-pinterest.svg` · `badge-spotify.svg`

#### 🔹 Meta Chips
`badge-company.svg` · `badge-role.svg` · `badge-focus.svg`

---

## 🎨 Design System Specifications

All SVGs follow a cohesive psql terminal theme engineered for maximum visual impact across GitHub Light and Dark modes:

```ini
[Theme Tokens]
Background   = #0E1420 (Dark Terminal Slate)
Title Bar    = #161D2B (Elevated Console Header)
SQL Prompt   = #E0A458 (Amber / Gold `surajit=#`)
Primary Text = #E7EBF5 (High-contrast Off-White)
Muted Text   = #7C89A6 (Steel Gray)
Subtle Text  = #3F4A63 (Dark Slate Accent)
Border       = #2A3348 (Subtle Divider Line)
Corner Radius= rx="10" / rx="14"
Typography   = 'JetBrains Mono', 'Berkeley Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
```

---

## 🚀 Usage in Profile README

To render badges or cards in the profile README, use standard HTML image tags pointing to the correct relative asset paths:

```html
<!-- Badges -->
<a href="https://linkedin.com/in/knownassurajit/">
  <img src="./assets/badges/badge-linkedin.svg" height="30" alt="LinkedIn" />
</a>
<img src="./assets/badges/badge-postgresql.svg" height="26" alt="PostgreSQL" />

<!-- Dynamic Cards -->
<img src="./assets/header.svg" width="720" height="auto" alt="Surajit Das — Terminal Header" />
<img src="./assets/stat-overview.svg" width="720" height="auto" alt="Profile Query Plan Overview" />
```
