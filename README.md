<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="roomGlow" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#241b35"/>
      <stop offset="60%" stop-color="#140f21"/>
      <stop offset="100%" stop-color="#0a0712"/>
    </radialGradient>

    <radialGradient id="cardBg" cx="30%" cy="30%" r="90%">
      <stop offset="0%" stop-color="#1e1438"/>
      <stop offset="50%" stop-color="#140d27"/>
      <stop offset="100%" stop-color="#0e081c"/>
    </radialGradient>

    <linearGradient id="neonBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="50%" stop-color="#e879f9"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>

    <!-- Neon Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&amp;family=Inter:wght@400;500;600;700&amp;family=Pacifico&amp;display=swap');

    .term-text { font-family: 'Fira Code', monospace; font-size: 11px; fill: #a78bfa; }
    .title-hi { font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 700; fill: #ffffff; }
    .name-title { font-family: 'Pacifico', cursive; font-size: 40px; fill: #f472b6; filter: drop-shadow(0px 0px 7px rgba(244,114,182,0.8)); }
    .sub-title { font-family: 'Inter', sans-serif; font-size: 13.5px; font-weight: 600; fill: #cbd5e1; letter-spacing: 0.5px; }
    .quote-text { font-family: 'Fira Code', monospace; font-size: 12px; fill: #f1f5f9; }
    .section-head { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; fill: #e2e8f0; }
    .pill-text { font-family: 'Inter', sans-serif; font-size: 10.5px; font-weight: 500; }
    .stat-label { font-family: 'Inter', sans-serif; font-size: 9.5px; fill: #94a3b8; }
    .stat-val { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; }
    .footer-text { font-family: 'Inter', sans-serif; font-size: 10.5px; fill: #94a3b8; }
    .code-editor { font-family: 'Fira Code', monospace; font-size: 10px; fill: #93c5fd; }
  </style>

  <!-- Ambient Room Background -->
  <rect width="1200" height="675" fill="url(#roomGlow)"/>

  <!-- Wall Frame / Poster (Left) -->
  <rect x="0" y="70" width="85" height="340" rx="4" fill="#1c162b" stroke="#372f47" stroke-width="6"/>
  <rect x="0" y="85" width="75" height="310" fill="#2d2244" opacity="0.6"/>

  <!-- Main Glow Card Outline -->
  <rect x="130" y="42" width="940" height="590" rx="30" fill="none" stroke="url(#neonBorder)" stroke-width="4" filter="url(#glow)" opacity="0.9"/>
  <!-- Card Background -->
  <rect x="130" y="42" width="940" height="590" rx="30" fill="url(#cardBg)"/>

  <!-- ================= LEFT COLUMN / CONTENT ================= -->

  <!-- Terminal prompt line -->
  <text x="165" y="115" class="term-text">krishna@frontend-developer:~$ <tspan fill="#e2e8f0">cat README.md</tspan></text>

  <!-- Greeting & Name -->
  <text x="165" y="156" class="title-hi">Hi, I'm 👋</text>
  <!-- Explicit capital 'A' in Ambadkar with cursive font -->
  <text x="165" y="215" class="name-title">Krishna Sunil Ambadkar</text>[span_0](start_span)[span_0](end_span)

  <!-- Subtitle -->
  <text x="165" y="250" class="sub-title">AI &amp; Data Science | GenAI / ML Engineering</text>[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span)

  <!-- Intelligence Quote Box -->
  <g transform="translate(165, 272)">
    <rect width="270" height="62" rx="12" fill="#1e153b" stroke="#3b2d5c" stroke-width="1.2"/>
    <text x="18" y="28" class="quote-text">I don't just build, I create</text>[span_3](start_span)[span_3](end_span)
    <text x="18" y="46" class="quote-text">intelligence. 💡✨</text>[span_4](start_span)[span_4](end_span)
  </g>

  <!-- Tech Stack Section -->
  <g transform="translate(165, 360)">
    <text x="0" y="0" class="section-head"><tspan fill="#4ade80">☘</tspan> Tech I Know</text>[span_5](start_span)[span_5](end_span)

    <!-- Row 1 -->
    <rect x="0" y="12" width="58" height="24" rx="12" fill="#3b1d28" stroke="#f43f5e" stroke-width="1"/>
    <text x="13" y="28" class="pill-text" fill="#fda4af">Python</text>[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)

    <rect x="65" y="12" width="68" height="24" rx="12" fill="#172e42" stroke="#38bdf8" stroke-width="1"/>
    <text x="78" y="28" class="pill-text" fill="#7dd3fc">FastAPI</text>[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span)

    <rect x="140" y="12" width="55" height="24" rx="12" fill="#143142" stroke="#0ea5e9" stroke-width="1"/>
    <text x="153" y="28" class="pill-text" fill="#7dd3fc">React</text>[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)

    <rect x="202" y="12" width="138" height="24" rx="12" fill="#2d1d42" stroke="#c084fc" stroke-width="1"/>
    <text x="214" y="28" class="pill-text" fill="#e9d5ff">OpenAI/Gemini API</text>[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span)

    <!-- Row 2 -->
    <rect x="0" y="43" width="94" height="24" rx="12" fill="#3b2b1d" stroke="#f59e0b" stroke-width="1"/>
    <text x="12" y="59" class="pill-text" fill="#fde68a">Scikit-learn</text>[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span)

    <rect x="101" y="43" width="48" height="24" rx="12" fill="#172b4d" stroke="#60a5fa" stroke-width="1"/>
    <text x="115" y="59" class="pill-text" fill="#bfdbfe">SQL</text>[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)

    <rect x="156" y="43" width="80" height="24" rx="12" fill="#42251d" stroke="#f97316" stroke-width="1"/>
    <text x="169" y="59" class="pill-text" fill="#fdba74">ChromaDB</text>[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)
  </g>

  <!-- About Me Section -->
  <g transform="translate(165, 452)">
    <text x="0" y="0" class="section-head"><tspan fill="#f472b6">♥</tspan> About Me</text>[span_20](start_span)[span_20](end_span)
    <text x="0" y="20" class="term-text" fill="#cbd5e1">>_ I build scalable AI, GenAI, and ML-backed full-stack systems.</text>
    <text x="0" y="38" class="term-text" fill="#cbd5e1">💡 Always learning, continuously exploring models.</text>
    <text x="0" y="56" class="term-text" fill="#cbd5e1">🚀 Turning real-world problems into production solutions.</text>
  </g>

  <!-- Stat Pills Box -->
  <g transform="translate(165, 532)">
    <rect width="380" height="46" rx="12" fill="#18112d" stroke="#312351" stroke-width="1.2"/>

    <!-- Stat 1 -->
    <circle cx="28" cy="23" r="4" fill="#fb923c"/>
    <text x="38" y="20" class="stat-label">Repos</text>[span_21](start_span)[span_21](end_span)
    <text x="38" y="35" class="stat-val" fill="#f8fafc">12+</text>[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span)

    <!-- Stat 2 -->
    <rect x="105" y="19" width="8" height="8" rx="2" fill="#38bdf8"/>
    <text x="119" y="20" class="stat-label">Deployed Apps</text>[span_24](start_span)[span_24](end_span)
    <text x="119" y="35" class="stat-val" fill="#f8fafc">6+</text>[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)

    <!-- Stat 3 -->
    <polygon points="215,16 217,21 222,21 218,24 219,29 215,26 211,29 212,24 208,21 213,21" fill="#facc15"/>
    <text x="228" y="20" class="stat-label">CGPA</text>[span_27](start_span)[span_27](end_span)
    <text x="228" y="35" class="stat-val" fill="#facc15">8.55+</text>[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span)

    <!-- Stat 4 -->
    <text x="300" y="24" font-family="'Fira Code', monospace" font-size="12" fill="#c084fc">#</text>
    <text x="312" y="20" class="stat-label">Hackathons</text>
    <text x="312" y="35" class="stat-val" fill="#f8fafc">1</text>[span_30](start_span)[span_30](end_span)
  </g>

  <!-- Footer Info Line -->
  <g transform="translate(165, 606)">
    <!-- GitHub -->
    <path d="M0 -3 C-4.4 -3 -8 0.6 -8 5 C-8 8.5 -5.7 11.5 -2.5 12.6 C-2.1 12.7 -1.9 12.4 -1.9 12.2 L-1.9 10.7 C-4.2 11.2 -4.6 9.7 -4.6 9.7 C-5 8.7 -5.6 8.4 -5.6 8.4 C-6.3 7.9 -5.5 7.9 -5.5 7.9 C-4.7 8 -4.3 8.8 -4.3 8.8 C-3.6 10 -2.4 9.6 -2 9.4 C-1.9 8.9 -1.7 8.5 -1.5 8.3 C-3.3 8.1 -5.2 7.4 -5.2 4.3 C-5.2 3.4 -4.9 2.7 -4.4 2.1 C-4.5 1.9 -4.8 0.9 -4.3 -0.5 C-4.3 -0.5 -3.6 -0.7 -2 0.4 C-1.3 0.2 -0.6 0.1 0.1 0.1 C0.8 0.1 1.5 0.2 2.2 0.4 C3.8 -0.7 4.5 -0.5 4.5 -0.5 C5 0.9 4.7 1.9 4.6 2.1 C5.1 2.7 5.4 3.4 5.4 4.3 C5.4 7.4 3.5 8.1 1.7 8.3 C2 8.5 2.2 9 2.2 9.7 L2.2 12.2 C2.2 12.4 2.4 12.7 2.8 12.6 C6 11.5 8.3 8.5 8.3 5 C8.3 0.6 4.6 -3 0 -3 Z" transform="translate(8, -4) scale(0.7)" fill="#94a3b8"/>
    <text x="22" y="0" class="footer-text">github.com/krishnaambadkar707-oss</text>[span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span)

    <circle cx="280" cy="-4" r="3" fill="#a855f7"/>
    <text x="290" y="0" class="footer-text">portfolio.com/krishna.ambadkar</text>[span_33](start_span)[span_33](end_span)

    <path d="M0,0 L12,0 L12,8 L0,8 Z M1,1 L6,5 L11,1" fill="none" stroke="#94a3b8" stroke-width="1.2" transform="translate(485, -9)"/>
    <text x="504" y="0" class="footer-text">krishnaambadkar707@gmail.com</text>[span_34](start_span)[span_34](end_span)[span_35](start_span)[span_35](end_span)

    <text x="710" y="0" class="footer-text" fill="#e2e8f0">AI is my medium, Data is my insight. <tspan fill="#f472b6">♥</tspan></text>[span_36](start_span)[span_36](end_span)
  </g>

  <!-- ================= TOP CODE WINDOW & BANNER ================= -->

  <!-- Floating Python Code Window -->
  <g transform="translate(470, 75)">
    <rect width="195" height="120" rx="10" fill="#140e24" stroke="#2d2247" stroke-width="1.2"/>
    <circle cx="14" cy="14" r="3.5" fill="#ef4444"/>
    <circle cx="26" cy="14" r="3.5" fill="#f59e0b"/>
    <circle cx="38" cy="14" r="3.5" fill="#10b981"/>
    <text x="90" y="16" font-family="'Fira Code', monospace" font-size="8.5" fill="#94a3b8">dreams.py</text>[span_37](start_span)[span_37](end_span)

    <text x="14" y="38" class="code-editor" fill="#c084fc">class <tspan fill="#67e8f9">BrainBuilder</tspan>:</text>[span_38](start_span)[span_38](end_span)
    <text x="24" y="54" class="code-editor" fill="#ec4899">def <tspan fill="#93c5fd">__init__</tspan>(self):</text>
    <text x="34" y="70" class="code-editor">self.model = create_model()</text>
    <text x="24" y="86" class="code-editor" fill="#ec4899">def <tspan fill="#93c5fd">predict</tspan>(self, x):</text>
    <text x="34" y="102" class="code-editor">return self.model(x)</text>
  </g>

  <!-- Keep Inventing Badge -->
  <g transform="translate(760, 80)">
    <rect width="155" height="75" rx="10" fill="#150f28" stroke="#6366f1" stroke-width="1.2" opacity="0.9"/>
    <text x="77" y="30" font-family="'Fira Code', monospace" font-size="14" font-weight="700" fill="#c084fc" text-anchor="middle">&lt;/&gt; ⚙</text>
    <text x="77" y="48" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#e2e8f0" text-anchor="middle" letter-spacing="1">KEEP INVENTING |</text>[span_39](start_span)[span_39](end_span)
    <text x="77" y="62" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#e2e8f0" text-anchor="middle" letter-spacing="1">KEEP SOLVING</text>[span_40](start_span)[span_40](end_span)
  </g>

  <!-- ================= RIGHT COLUMN / AVATAR & DESK ================= -->
  <!-- 
    The high-resolution developer avatar illustration with long brown hair,
    chair, laptop, table, coffee cup, and desk plants rendered via SVG image embedding.
  -->
  <g transform="translate(520, 160)">
    <!-- Wicker Chair & Table Stand Backdrops -->
    <ellipse cx="230" cy="390" rx="190" ry="25" fill="#080511" opacity="0.7"/>

    <!-- Desk Books Stack -->
    <g transform="translate(315, 270)">
      <rect x="0" y="30" width="70" height="15" rx="2" fill="#1e293b"/>
      <rect x="0" y="45" width="72" height="14" rx="2" fill="#0284c7"/>
      <rect x="0" y="59" width="70" height="16" rx="2" fill="#eab308"/>
      <rect x="0" y="75" width="75" height="16" rx="2" fill="#334155"/>
      <!-- Coffee Cup -->
      <path d="M-30,40 L-15,40 L-18,72 L-27,72 Z" fill="#f8fafc"/>
      <rect x="-32" y="36" width="19" height="5" rx="2" fill="#78350f"/>
    </g>

    <!-- Embedded High-Fidelity Girl Avatar with Long Hair and Laptop -->
    <image href="1790710038109.png" x="20" y="-120" width="530" height="530" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClip)"/>[span_41](start_span)[span_41](end_span)
  </g>

  <clipPath id="avatarClip">
    <rect x="600" y="160" width="450" height="430" rx="15"/>
  </clipPath>

  <!-- Corner Plants (Foliage on Right) -->
  <path d="M1100,260 Q1140,240 1200,250 Q1150,290 1100,260 Z" fill="#1e3a2b" opacity="0.6"/>
  <path d="M1080,310 Q1150,280 1200,320 Q1140,350 1080,310 Z" fill="#162e22" opacity="0.8"/>
  <path d="M1090,380 Q1170,360 1200,410 Q1130,430 1090,380 Z" fill="#0f231a"/>
</svg>

---

## 🌸 My AI Creations

<table width="100%">
<tr>
<td width="34%" align="center">

<img src="profile.jpeg" width="240" alt="Krishna profile artwork">

<br><br>

<b>KRISHNA AMBADKAR</b><br>
<sub>AI / ML / GENAI ENGINEER</sub>

<br><br>

`PYTHON` · `RAG` · `FASTAPI`

</td>

<td width="66%" valign="top">

### 🧠 Featured Projects

| ✦ Project | 🧪 Tech | 🚀 |
|---|---|---|
| 🔍 Enterprise RAG Knowledge Assistant | RAG · Embeddings · LLM | 🟣 |
| 🤟 HANA — AI Voice & ISL Learning Companion | MediaPipe · OpenCV | 🟣 |
| 💬 KUMARI — AI Virtual Companion | Gemini · OpenAI · Memory | 🟣 |
| 🚦 Nagpur Traffic AI | React · AI/ML | 🟢 |
| 🎧 AIVOA — AI Complaint Management | FastAPI · AI | 🟢 |
| 🏠 House Price Prediction API | FastAPI · Random Forest | 🔵 |
| 💰 Personal Finance Analyzer | NumPy · Pandas · Matplotlib | 🟢 |
| ❤️ ECG Analyzer | SciPy · Signal Processing | 🟢 |
| 📱 Social Media Behavior Analyzer | Pandas · Analytics | 🟢 |
| 🎵 Audio Signal Processor | NumPy · Wave | 🟢 |
| 🎬 Movie Recommendation Analytics | R · Statistics | 🔵 |
| 📁 Smart File Organizer + Search Engine | Python · OOP | 🔵 |

> 💜 **“Build it. Learn from it. Improve it.”**

</td>
</tr>
</table>

---

# 📊 GitHub Stats & Graphs

<div align="center">

<a href="https://github.com/krishnaambadkar707-oss">
<img src="https://github-readme-stats.vercel.app/api?username=krishnaambadkar707-oss&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&rank_icon=github&bg_color=0D0B1A&title_color=FF9EDB&text_color=E8E3F0&icon_color=9C7CFF" width="49%">
</a>

<a href="https://github.com/krishnaambadkar707-oss">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=krishnaambadkar707-oss&layout=compact&hide_border=true&langs_count=8&bg_color=0D0B1A&title_color=FF9EDB&text_color=E8E3F0" width="41%">
</a>

<br><br>

<img src="https://streak-stats.demolab.com?user=krishnaambadkar707-oss&theme=transparent&hide_border=true&ring=FF9EDB&fire=FF9EDB&currStreakLabel=FF9EDB&sideLabels=E8E3F0&dates=AAA4B5&currStreakNum=FFFFFF&sideNums=FFFFFF" width="70%">

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=krishnaambadkar707-oss&bg_color=0D0B1A&color=E8E3F0&line=FF9EDB&point=FFFFFF&area=true&hide_border=true" width="95%">

</div>

---

## 🏅 GitHub Journey

<table width="100%">
<tr>
<td align="center">

🌸<br>
<b>AI Builder</b><br>
<sub>AI / ML Projects</sub>

</td>
<td align="center">

⭐<br>
<b>Project Creator</b><br>
<sub>12 Projects</sub>

</td>
<td align="center">

💜<br>
<b>GenAI Explorer</b><br>
<sub>RAG + LLM Apps</sub>

</td>
<td align="center">

💻<br>
<b>Backend Builder</b><br>
<sub>FastAPI + REST</sub>

</td>
<td align="center">

📊<br>
<b>Data Explorer</b><br>
<sub>Analytics + ML</sub>

</td>
<td align="center">

🚀<br>
<b>Deployer</b><br>
<sub>6 Deployed Apps</sub>

</td>
</tr>
</table>

---

## 🏆 Hackathon

### 🚦 Manthan 4 Yuwa – Vikasit Nagpur · 2026

**Nagpur Traffic AI — Risk Heatmap & Police Deployment Decision Support**

**Role:** Full-Stack Developer

---

## 🧩 What I Work With

<div align="center">

`Python` `SQL` `C++` `R` `JavaScript` `HTML` `CSS`

`Scikit-learn` `RAG` `LLM APIs` `Embeddings`

`FastAPI` `REST APIs` `Pydantic` `SQLAlchemy`

`React` `Vite` `Three.js` `Web Speech API`

`NumPy` `Pandas` `Matplotlib` `MySQL` `Power BI`

`OpenCV` `MediaPipe Hands`

`Git` `GitHub` `VS Code`

</div>

---

# 📫 Let's Connect

<div align="center">

<a href="https://github.com/krishnaambadkar707-oss">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="https://www.linkedin.com/in/krishna-ambadkar-918955359">
<img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
</a>

<a href="mailto:krishnaambadkar707@gmail.com">
<img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white">
</a>

<a href="https://krishna-portfolio-1-neon.vercel.app/">
<img src="https://img.shields.io/badge/Portfolio-EA4335?style=for-the-badge&logo=portfolio&logoColor=white">
</a>

<br><br>

<sub>💜 Open to learning, building and collaborating on meaningful AI projects.</sub>

<br><br>

<img src="https://komarev.com/ghpvc/?username=krishnaambadkar707-oss&label=PROFILE%20VIEWS&color=ff9edb&style=for-the-badge" alt="profile views">

</div>

---

<div align="center">

### 🌸 “Turning ideas into intelligent applications.”

**AI • ML • GenAI • Data Science • Backend**

</div>
