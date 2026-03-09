<style>
:root {
  /* Material Design 3 (Material You) Colors */
  --md-sys-color-primary: #d0bcff;
  --md-sys-color-on-primary: #381e72;
  --md-sys-color-primary-container: #4f378b;
  --md-sys-color-on-primary-container: #eaddff;
  --md-sys-color-secondary: #ccc2dc;
  --md-sys-color-on-secondary: #332d41;
  --md-sys-color-secondary-container: #4a4458;
  --md-sys-color-on-secondary-container: #e8def8;
  --md-sys-color-surface: #141218;
  --md-sys-color-surface-container: #211f26;
  --md-sys-color-surface-container-high: #2b2930;
  --md-sys-color-outline: #938f99;
  --md-sys-color-outline-variant: #49454f;
  --md-sys-color-on-surface: #e6e0e9;
  --md-sys-color-on-surface-variant: #cac4d0;

  --border-radius-xl: 28px;
  --border-radius-l: 16px;
  --border-radius-m: 12px;

  --spacing-s: 8px;
  --spacing-m: 16px;
  --spacing-l: 24px;
  --spacing-xl: 32px;
}

body {
    background-color: var(--md-sys-color-surface);
}

.mdw {
  max-width: 1000px;
  margin: 0 auto;
  padding: var(--spacing-l);
  color: var(--md-sys-color-on-surface);
  font-family: 'Roboto', -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
}

/* Base Card Style */
.mdw .card {
  background: var(--md-sys-color-surface-container);
  border: 1px solid var(--md-sys-color-outline-variant);
  border-radius: var(--border-radius-l);
  padding: var(--spacing-l);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

.mdw .card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  background: var(--md-sys-color-surface-container-high);
}

/* Hero Section */
.mdw .hero {
  text-align: center;
  padding: var(--spacing-xl) var(--spacing-l);
  margin-bottom: var(--spacing-xl);
  background: linear-gradient(135deg, var(--md-sys-color-surface-container-high), var(--md-sys-color-surface-container));
  border-radius: var(--border-radius-xl);
  border: 1px solid var(--md-sys-color-outline-variant);
  position: relative;
  overflow: hidden;
}

.mdw .hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(208, 188, 255, 0.05) 0%, transparent 50%);
    pointer-events: none;
}

.mdw .title {
  margin: 0 0 var(--spacing-s);
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 700;
  letter-spacing: -0.5px;
  color: var(--md-sys-color-primary);
}

.mdw .subtitle {
  color: var(--md-sys-color-on-surface-variant);
  font-size: 1.1rem;
  margin-bottom: var(--spacing-m);
}

.mdw .contact-info {
    display: flex;
    justify-content: center;
    gap: var(--spacing-m);
    flex-wrap: wrap;
    margin-top: var(--spacing-m);
}

.mdw .contact-chip {
    display: inline-flex;
    align-items: center;
    padding: 6px 16px;
    background: var(--md-sys-color-secondary-container);
    color: var(--md-sys-color-on-secondary-container);
    border-radius: 20px;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: background 0.2s ease;
}

.mdw .contact-chip:hover {
    background: var(--md-sys-color-primary-container);
    color: var(--md-sys-color-on-primary-container);
}

/* Sections */
.mdw .section-title {
  margin: var(--spacing-xl) 0 var(--spacing-l);
  font-size: 1.8rem;
  font-weight: 600;
  color: var(--md-sys-color-primary);
  display: flex;
  align-items: center;
  gap: var(--spacing-s);
}

/* Typography Helpers */
.mdw h3 {
    margin: 0 0 var(--spacing-s);
    font-size: 1.3rem;
    color: var(--md-sys-color-on-surface);
}

.mdw p {
    margin: 0 0 var(--spacing-s);
}

.mdw .muted {
    color: var(--md-sys-color-on-surface-variant);
    font-size: 0.9rem;
}

.mdw .accent {
    color: var(--md-sys-color-primary);
    font-weight: 500;
}

.mdw ul {
    margin: 0;
    padding-left: 20px;
}

.mdw li {
    margin-bottom: 4px;
}

/* Grids */
.mdw .grid {
  display: grid;
  gap: var(--spacing-m);
}

.mdw .grid-2 {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.mdw .grid-3 {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* Chips/Badges */
.mdw .chip-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: var(--spacing-s);
}

.mdw .chip {
    padding: 4px 12px;
    border-radius: 16px;
    background: var(--md-sys-color-surface-container-high);
    border: 1px solid var(--md-sys-color-outline-variant);
    font-size: 0.85rem;
    color: var(--md-sys-color-on-surface-variant);
}

/* Tech Stack Specific */
.mdw .tech-stack img {
    height: 28px;
    margin: 4px;
    border-radius: 4px;
}

/* Github Stats */
.mdw .stats-container {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-m);
    align-items: center;
}

.mdw .stats-row {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-m);
    justify-content: center;
    width: 100%;
}

.mdw .stats-img {
    max-width: 100%;
    height: auto;
    border-radius: var(--border-radius-m);
}

/* Interactive Elements */
#greeting-container {
    margin-top: var(--spacing-m);
    padding: var(--spacing-s) var(--spacing-m);
    background: rgba(208, 188, 255, 0.1);
    border-radius: var(--border-radius-m);
    display: inline-block;
    font-weight: 500;
    color: var(--md-sys-color-primary);
}

/* Responsive */
@media (max-width: 768px) {
  .mdw { padding: var(--spacing-m); }
  .mdw .hero { padding: var(--spacing-l) var(--spacing-m); }
  .mdw .section-title { font-size: 1.5rem; }
}
</style>

<div class="mdw">
  <!-- Hero Section -->
  <div class="hero">
    <h1 class="title">Surajit Das</h1>
    <p class="subtitle">Accomplished Database Engineer & Backend Developer</p>

    <div class="contact-info">
        <a href="mailto:isurajit123@gmail.com" class="contact-chip">✉️ isurajit123@gmail.com</a>
        <span class="contact-chip">📞 +91 8670043341</span>
        <a href="https://www.linkedin.com/in/surajit-das-661186203/" class="contact-chip">🔗 LinkedIn</a>
        <a href="#" class="contact-chip">🌐 Portfolio</a>
    </div>

    <div id="greeting-container">Loading greeting...</div>
  </div>

  <!-- Professional Summary -->
  <h2 class="section-title">🎯 Professional Summary</h2>
  <div class="card">
    <p>Accomplished Database Engineer with over 3 years of experience in designing, optimizing, and managing enterprise-grade databases. Demonstrated expertise in <strong>PL/SQL, PostgreSQL, and MySQL</strong> with a strong command of data migration, cloud deployment, and performance tuning.</p>
    <p>Adept in Agile methodologies, DevOps principles, and cross-functional collaboration. Committed to developing scalable and secure systems, driven by a passion for emerging technologies, HCI, and sustainable software practices.</p>
  </div>

  <!-- Technical Skills -->
  <h2 class="section-title">🧰 Technical Skills</h2>
  <div class="grid grid-2 tech-stack">
    <div class="card">
        <h3>💻 Programming & DB</h3>
        <p class="muted">Python, C/C++, Bash, SQL, PL/SQL</p>
        <p class="muted">Oracle, PostgreSQL, MySQL</p>
        <div class="chip-container">
            <img src="./assets/badge-python.svg" alt="Python" />
            <img src="./assets/badge-cplusplus.svg" alt="C++" />
            <img src="./assets/badge-bash.svg" alt="Bash" />
            <img src="./assets/badge-oracle.svg" alt="Oracle" />
            <img src="./assets/badge-postgresql.svg" alt="PostgreSQL" />
            <img src="./assets/badge-mysql.svg" alt="MySQL" />
        </div>
    </div>
    <div class="card">
        <h3>⚙️ DevOps & Tools</h3>
        <p class="muted">Git, Jenkins, Bash Scripting, Linux, macOS, Windows</p>
        <div class="chip-container">
            <img src="./assets/badge-git.svg" alt="Git" />
            <img src="./assets/badge-jenkins.svg" alt="Jenkins" />
            <img src="./assets/badge-linux.svg" alt="Linux" />
            <img src="./assets/badge-windows.svg" alt="Windows" />
            <img src="./assets/badge-macos.svg" alt="macOS" />
        </div>
    </div>
    <div class="card">
        <h3>📊 Data Operations</h3>
        <p class="muted">Data Modeling, ETL, Data Cleaning, Migration, Power BI, Tableau</p>
        <div class="chip-container">
            <img src="./assets/badge-powerbi.svg" alt="Power BI" />
            <img src="./assets/badge-tableau.svg" alt="Tableau" />
        </div>
    </div>
    <div class="card">
        <h3>🎨 UI/UX & Design</h3>
        <p class="muted">Figma, Adobe XD, Sketch</p>
        <div class="chip-container">
            <img src="./assets/badge-figma.svg" alt="Figma" />
        </div>
    </div>
  </div>

  <!-- Professional Experience -->
  <h2 class="section-title">💼 Professional Experience</h2>
  <div class="grid grid-2">
    <div class="card">
      <h3>🚀 Bosch India</h3>
      <p><span class="accent">Assistant Manager</span> <span class="muted">• Feb 2025 – Present</span></p>
      <ul>
        <li>Led ETL development and Oracle SQL optimization for scalable BI systems.</li>
        <li>Automated reporting pipelines and migrated BI dashboards, enhancing performance by 30%.</li>
        <li>Directed KPI standardization across projects, ensuring data accuracy and compliance.</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔍 Adapt Ready</h3>
      <p><span class="accent">Database Engineer</span> <span class="muted">• Nov 2024 – Jan 2025</span></p>
      <ul>
        <li>Developed robust data pipelines and automated backup systems using shell scripts.</li>
        <li>Achieved 80% reduction in manual database maintenance.</li>
        <li>Reinforced data security by integrating encrypted cloud storage for backups.</li>
      </ul>
    </div>

    <div class="card">
      <h3>🛍️ Walmart Global Tech India</h3>
      <p><span class="accent">Backend Engineer</span></p>
      <ul>
        <li>Designed high-performance PL/SQL modules with CI/CD pipelines for real-time applications.</li>
        <li>Implemented unit tests, version control workflows, and optimized query execution.</li>
      </ul>
    </div>

    <div class="card">
      <h3>⚡ GE Renewables</h3>
      <p><span class="accent">Database Developer</span></p>
      <ul>
        <li>Delivered PostgreSQL-driven analytics solutions for operational efficiency.</li>
        <li>Conducted business process optimization with SQL insights for better decision support.</li>
      </ul>
    </div>

    <div class="card">
      <h3>🏛️ Tata Consultancy Services (TCS)</h3>
      <p><span class="accent">PL/SQL Developer – TCS BaNCS</span> <span class="muted">• Oct 2021 – Nov 2024</span></p>
      <ul>
        <li>Engineered scalable financial systems for BFSI clients under strict regulatory compliance.</li>
        <li>Spearheaded a database migration from PostgreSQL to Oracle, enhancing retrieval speeds by 25% and cutting storage costs by 20%.</li>
      </ul>
    </div>

    <div class="card">
      <h3>💻 Wipro Limited</h3>
      <p><span class="accent">Backend Engineer – Alight Solutions</span> <span class="muted">• May 2021 – Oct 2021</span></p>
      <ul>
        <li>Managed core database operations, performance tuning, and data integrity assurance.</li>
        <li>Contributed to secure, compliant infrastructure aligned with evolving tech standards.</li>
      </ul>
    </div>
  </div>

  <!-- Key Projects -->
  <h2 class="section-title">🛠️ Key Projects</h2>
  <div class="grid grid-3">
    <div class="card">
      <h3>Cloud Database Migration</h3>
      <p class="muted">Transitioned PostgreSQL data to Oracle; improved access speeds and optimized storage.</p>
    </div>
    <div class="card">
      <h3>Automated Backup Solution</h3>
      <p class="muted">Bash-scripted system for daily incremental/full backups, integrated with cloud security.</p>
    </div>
    <div class="card">
      <h3>Limit Order Book Engine</h3>
      <p class="muted">Implemented a data structure-based trading engine with order matching and execution logic.</p>
    </div>
    <div class="card">
      <h3>Facial Expression Recognition</h3>
      <p class="muted">Built using Python ML libraries; included training, evaluation, and deployment.</p>
    </div>
    <div class="card">
      <h3>Calculator Application</h3>
      <p class="muted">Developed robust logic for I/O, error handling, and mathematical computations.</p>
    </div>
    <div class="card">
      <h3>Personal Portfolio Website</h3>
      <p class="muted">Designed and hosted using GitHub Pages with CMS integration and responsive design.</p>
    </div>
  </div>

  <!-- Certifications -->
  <h2 class="section-title">🏆 Certifications</h2>
  <div class="card">
    <ul>
      <li><strong>Google IT Support Professional Certificate</strong> <br><span class="muted">OS administration, automation, security, troubleshooting (Linux, MacOS, Windows)</span></li>
      <li><strong>Google UX Design Professional Certificate</strong> <br><span class="muted">UX research, wireframing, responsive design (Figma, Adobe XD, Sketch)</span></li>
      <li><strong>Machine Learning – Stanford University</strong> <br><span class="muted">Data preparation, model building, evaluation (TensorFlow, NumPy, Scikit-learn)</span></li>
      <li><strong>Python Programming – University of Michigan</strong> <br><span class="muted">Control structures, data types, functions, data structures</span></li>
      <li><strong>Introduction to Cybersecurity Tools & Cyber Attacks – IBM</strong> <br><span class="muted">CIA Triad, cryptography, incident response</span></li>
    </ul>
  </div>

  <!-- Education -->
  <h2 class="section-title">🎓 Education</h2>
  <div class="grid grid-2">
    <div class="card">
      <h3>University of Engineering & Management – Jaipur</h3>
      <p><strong>Bachelor of Technology in Computer Science Engineering</strong></p>
      <p class="muted">Jul 2017 – Jun 2021 | Grade: A+</p>
      <div class="chip-container">
          <span class="chip">Hackathon Team</span>
          <span class="chip">Festival Organizer</span>
          <span class="chip">Guitarist</span>
      </div>
    </div>
    <div class="card">
      <h3>Umesh Chandra Basuhara Vidyalaya – Malda</h3>
      <p><strong>Higher Secondary – Computer Science</strong></p>
      <p class="muted">Jan 2011 – Jun 2017 | Grade: A</p>
      <div class="chip-container">
          <span class="chip">Cricket</span>
          <span class="chip">Football</span>
          <span class="chip">Guitarist</span>
      </div>
    </div>
    <div class="card">
      <h3>Harishchandrapur High School – Malda</h3>
      <p><strong>Secondary – Science</strong></p>
      <p class="muted">Jan 2009 – Dec 2010 | Grade: A+</p>
      <div class="chip-container">
          <span class="chip">Running Club</span>
          <span class="chip">Drummer</span>
      </div>
    </div>
  </div>

  <!-- GitHub Live Dashboard -->
  <h2 class="section-title">📈 GitHub Contributions</h2>
  <div class="card stats-container">
    <div class="stats-row">
      <img class="stats-img" src="https://github-readme-stats-fast.vercel.app/api?username=knownassurajit&show_icons=true&theme=tokyonight&title_color=D0BCFF&icon_color=D0BCFF&text_color=E6E0E9&bg_color=211f26&hide_border=true&rank_icon=github" alt="GitHub Stats" />
      <img class="stats-img" src="https://github-readme-streak-stats.herokuapp.com?user=knownassurajit&theme=tokyonight&background=211f26&ring=D0BCFF&fire=D0BCFF&currStreakLabel=E6E0E9&sideLabels=E6E0E9&currStreakNum=E6E0E9&sideNums=E6E0E9&dates=CAC4D0&hide_border=true" alt="GitHub Streak" />
    </div>
    <img class="stats-img" src="https://ghchart.rshah.org/d0bcff/knownassurajit" alt="Real-time GitHub Contribution Board" style="width: 100%; max-width: 800px; margin-top: 16px;" />
    <img class="stats-img" src="https://github-readme-activity-graph.vercel.app/graph?username=knownassurajit&bg_color=211f26&color=E6E0E9&line=D0BCFF&point=CAC4D0&area=true&hide_border=true" alt="GitHub Activity Graph" style="width: 100%; max-width: 800px; margin-top: 16px;" />
  </div>

</div>

<script>
  // Simple JS to add dynamic greeting based on time of day
  document.addEventListener('DOMContentLoaded', (event) => {
    const hour = new Date().getHours();
    let greeting = '';

    if (hour < 12) {
      greeting = 'Good morning! ☀️';
    } else if (hour < 18) {
      greeting = 'Good afternoon! ☕';
    } else {
      greeting = 'Good evening! 🌙';
    }

    document.getElementById('greeting-container').innerHTML = `${greeting} Welcome to my profile.`;
  });
</script>
