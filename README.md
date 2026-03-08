<style>
:root {
  --md-sys-color-primary: #d0bcff;
  --md-sys-color-on-primary: #381e72;
  --md-sys-color-surface: #141218;
  --md-sys-color-surface-container: #211f26;
  --md-sys-color-surface-container-high: #2b2930;
  --md-sys-color-outline: #938f99;
  --md-sys-color-on-surface: #e6e0e9;
  --md-sys-color-on-surface-variant: #cac4d0;
}

.mdw {
  max-width: 1080px;
  margin: 0 auto;
  padding: 12px;
  color: var(--md-sys-color-on-surface);
  font-family: Roboto, "Segoe UI", sans-serif;
}

.mdw .hero,
.mdw .card,
.mdw .stats,
.mdw .chips {
  background: var(--md-sys-color-surface-container);
  border: 1px solid var(--md-sys-color-outline);
  border-radius: 28px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, .35);
}

.mdw .hero {
  text-align: center;
  padding: 24px 20px;
  margin: 12px 0 20px;
}

.mdw .title {
  margin: 8px 0 0;
  font-size: clamp(1.8rem, 3vw, 2.4rem);
}

.mdw .subtitle {
  color: var(--md-sys-color-on-surface-variant);
  margin-top: 8px;
}

.mdw .chips {
  margin-top: 16px;
  padding: 12px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
}

.mdw .section-title {
  margin: 24px 0 12px;
  color: var(--md-sys-color-primary);
}

.mdw .grid {
  display: grid;
  gap: 14px;
}

.mdw .journey { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.mdw .stack { grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); }

.mdw .card {
  padding: 16px;
}

.mdw .card h3 { margin: 0 0 8px; }
.mdw .muted { color: var(--md-sys-color-on-surface-variant); }

.mdw .icon {
  width: 36px;
  height: 36px;
  display: block;
  margin-bottom: 8px;
}

.mdw .stats {
  margin-top: 10px;
  padding: 16px;
}

.mdw .stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 12px;
}

.mdw img.responsive {
  width: 100%;
  height: auto;
  border-radius: 16px;
}

.mdw .social {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

@media (max-width: 640px) {
  .mdw { padding: 8px; }
  .mdw .hero { padding: 20px 12px; border-radius: 20px; }
  .mdw .card { border-radius: 20px; }
}
</style>

<div class="mdw">
  <div class="hero">
    <h1 class="title">👋 Hi, I'm Surajit Das</h1>
    <p class="subtitle">Assistant Manager @ Bosch India • Data Engineering • Backend Systems</p>
    <img src="./assets/typing-intro.svg" alt="Animated introduction" class="responsive" />
    <div class="chips">
      <img src="./assets/badge-role.svg" alt="Role badge" />
      <img src="./assets/badge-company.svg" alt="Company badge" />
      <img src="./assets/badge-focus.svg" alt="Focus badge" />
    </div>
  </div>

  <h2 class="section-title">🎯 About Me</h2>
  <div class="card">
    I’m an <strong>Assistant Manager at Bosch India</strong> with 3+ years of experience in <strong>database engineering, ETL pipelines, and backend systems</strong>.
    I focus on delivering reliable data platforms with clean, user-friendly design principles inspired by <strong>Material Design for the web</strong>.
  </div>

  <h2 class="section-title">💼 Professional Journey</h2>
  <div class="grid journey">
    <div class="card"><h3>🚀 Bosch India</h3><p><strong>Assistant Manager</strong> <span class="muted">• Feb 2025 – Present</span></p><ul><li>Leading ETL development and Oracle SQL optimization.</li><li>Automated BI reporting pipelines and KPI standardization.</li></ul></div>
    <div class="card"><h3>🔍 Adapt Ready</h3><p><strong>Database Engineer</strong> <span class="muted">• Nov 2024 – Jan 2025</span></p><ul><li>Built robust data pipelines and automated backups.</li><li>Reduced manual database maintenance by 80%.</li></ul></div>
    <div class="card"><h3>🛍️ Walmart Global Tech India</h3><p><strong>Backend Engineer</strong></p><ul><li>Built PL/SQL modules with CI/CD for real-time apps.</li><li>Improved performance with test-first DB workflows.</li></ul></div>
    <div class="card"><h3>⚡ GE Renewables</h3><p><strong>Database Developer</strong></p><ul><li>Delivered PostgreSQL analytics solutions.</li><li>Supported process optimization with SQL insights.</li></ul></div>
    <div class="card"><h3>🏛️ Tata Consultancy Services</h3><p><strong>PL/SQL Developer – TCS BaNCS</strong> <span class="muted">• Oct 2021 – Nov 2024</span></p><ul><li>Built financial systems for BFSI clients.</li><li>Migrated PostgreSQL to Oracle with faster retrieval.</li></ul></div>
    <div class="card"><h3>💻 Wipro Limited</h3><p><strong>Backend Engineer – Alight Solutions</strong> <span class="muted">• May 2021 – Oct 2021</span></p><ul><li>Managed core DB operations and tuning.</li><li>Strengthened compliant infrastructure delivery.</li></ul></div>
  </div>

  <h2 class="section-title">🧰 Tech Stack</h2>
  <div class="grid stack">
    <div class="card"><img src="./assets/icon-database.svg" alt="Database icon" class="icon" /><strong>Databases</strong><br/><span class="muted">Oracle • PostgreSQL • MySQL</span></div>
    <div class="card"><img src="./assets/icon-backend.svg" alt="Backend icon" class="icon" /><strong>Backend</strong><br/><span class="muted">PL/SQL • SQL • Python • Bash</span></div>
    <div class="card"><img src="./assets/icon-dataops.svg" alt="Data operations icon" class="icon" /><strong>Data Ops</strong><br/><span class="muted">ETL • Migration • Tuning • Automation</span></div>
    <div class="card"><img src="./assets/icon-uiux.svg" alt="UI/UX icon" class="icon" /><strong>UI/UX</strong><br/><span class="muted">Material UI • Figma • UX Systems</span></div>
  </div>

  <h2 class="section-title">🏆 Certifications</h2>
  <div class="card">
    <ul>
      <li><strong>Google IT Support Professional Certificate</strong></li>
      <li><strong>Google UX Design Professional Certificate</strong></li>
      <li><strong>Machine Learning</strong> (Stanford University)</li>
      <li><strong>Python Programming</strong> (University of Michigan)</li>
      <li><strong>Cybersecurity Tools & Cyber Attacks</strong> (IBM)</li>
    </ul>
  </div>

  <h2 class="section-title">📈 GitHub Live Dashboard</h2>
  <div class="stats">
    <div class="stats-grid">
      <img class="responsive" src="https://github-readme-stats.vercel.app/api?username=knownassurajit&show_icons=true&title_color=D0BCFF&icon_color=D0BCFF&text_color=E6E0E9&bg_color=211f26&hide_border=true&rank_icon=github" alt="GitHub stats" />
      <img class="responsive" src="https://github-readme-streak-stats.herokuapp.com?user=knownassurajit&background=211f26&ring=D0BCFF&fire=D0BCFF&currStreakLabel=E6E0E9&sideLabels=E6E0E9&currStreakNum=E6E0E9&sideNums=E6E0E9&dates=CAC4D0&hide_border=true" alt="GitHub streak" />
    </div>
    <br/>
    <img class="responsive" src="https://ghchart.rshah.org/d0bcff/knownassurajit" alt="Real-time GitHub contribution board" />
    <br/><br/>
    <img class="responsive" src="https://github-readme-activity-graph.vercel.app/graph?username=knownassurajit&bg_color=211f26&color=E6E0E9&line=D0BCFF&point=CAC4D0&area=true&hide_border=true" alt="GitHub activity graph" />
  </div>

  <h2 class="section-title">🤝 Connect with Me</h2>
  <div class="social">
    <a href="mailto:isurajit123@gmail.com"><img src="./assets/badge-email.svg" alt="Email" /></a>
    <a href="https://www.linkedin.com/in/surajit-das-661186203/"><img src="./assets/badge-linkedin.svg" alt="LinkedIn" /></a>
  </div>

  <p class="muted" style="text-align:center; margin-top: 24px;"><sub>💡 Open to collaboration, data engineering opportunities, and meaningful conversations.</sub></p>
</div>
