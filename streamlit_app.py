"""
HR Centralized System — Darma Henwa Brand
v3: Professional redesign with DH brand, real images from GitHub, 
    embedded AppScript, failed = X mark, no team notes
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="PTDH Recruitment Portal",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GITHUB_RAW = "https://raw.githubusercontent.com/naviantar-ptdh/202605-centralized/main"
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwmPcoTPCljSWj22rOclkduNJQMvxbPAOs9czLjrMD8yF4TjbXKh2lTp9uLXVYTZUaK/exec"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --dh-orange:       #FF5000;
  --dh-orange-light: #FF7501;
  --dh-black:        #1A1614;
  --dh-dark:         #211C1C;

  --bg:              #F5F4F2;
  --surface:         #FFFFFF;
  --surface-2:       #F0EDEA;
  --surface-3:       #E5E0DB;
  --border:          rgba(33,28,28,0.09);
  --border-mid:      rgba(33,28,28,0.16);
  --text:            #1A1614;
  --text-secondary:  #54504C;
  --text-muted:      #8A847E;

  --accent:          #FF5000;
  --accent-hover:    #E04500;
  --accent-soft:     rgba(255,80,0,0.07);
  --accent-border:   rgba(255,80,0,0.22);

  --green:           #166534;
  --green-bg:        rgba(22,101,52,0.07);
  --amber:           #92400E;
  --amber-bg:        rgba(146,64,14,0.08);
  --red:             #991B1B;
  --red-bg:          rgba(153,27,27,0.07);

  --radius:          10px;
  --radius-sm:       7px;
  --radius-lg:       14px;
  --shadow-sm:       0 1px 3px rgba(26,22,20,0.07);
  --shadow:          0 3px 12px rgba(26,22,20,0.09);
  --shadow-lg:       0 8px 28px rgba(26,22,20,0.12);
}}

html, body, .stApp {{
  background: var(--bg) !important;
  font-family: 'Sora', sans-serif !important;
  color: var(--text) !important;
}}

#MainMenu, footer, header, .stDeployButton {{ display: none !important; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
[data-testid="stAppViewBlockContainer"] {{ padding: 0 !important; }}
.element-container {{ margin: 0 !important; }}

::-webkit-scrollbar {{ width: 5px; height: 5px; }}
::-webkit-scrollbar-track {{ background: var(--surface-2); }}
::-webkit-scrollbar-thumb {{ background: var(--surface-3); border-radius: 3px; }}

/* ── TOPBAR ── */
.topbar {{
  position: sticky; top: 0; z-index: 999;
  background: var(--dh-black);
  height: 58px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 40px;
  border-bottom: 2.5px solid var(--dh-orange);
  box-shadow: 0 2px 12px rgba(0,0,0,0.25);
}}
.topbar-left {{ display: flex; align-items: center; gap: 16px; }}
.topbar-logo {{ height: 30px; width: auto; }}
.topbar-sep {{ width: 1px; height: 22px; background: rgba(255,255,255,0.12); }}
.topbar-text {{ font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.80); letter-spacing: 0.005em; }}
.topbar-right {{ display: flex; align-items: center; gap: 14px; }}
.topbar-date {{ font-size: 11px; color: rgba(255,255,255,0.38); font-family: 'IBM Plex Mono', monospace; }}
.topbar-badge {{
  font-size: 10px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
  background: var(--dh-orange); color: #fff;
  padding: 3px 10px; border-radius: 20px;
}}

/* ── HOME ── */
.home-wrap {{ padding: 32px 40px 60px; }}

/* Section label */
.sec-label {{
  display: flex; align-items: center; gap: 12px; margin-bottom: 16px;
}}
.sec-label-line {{ flex: 1; height: 1px; background: var(--border-mid); }}
.sec-label-text {{
  font-size: 10px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--text-muted); white-space: nowrap;
  display: flex; align-items: center; gap: 7px;
}}
.sec-label-dot {{
  width: 5px; height: 5px; border-radius: 50%;
  background: var(--dh-orange);
}}

/* Dashboard embed */
.dash-frame {{
  background: var(--dh-black);
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 28px;
  box-shadow: var(--shadow-lg);
  border: 1px solid rgba(255,255,255,0.04);
}}
.dash-frame-header {{
  padding: 13px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
  display: flex; align-items: center; justify-content: space-between;
}}
.dash-frame-title {{
  font-size: 12px; font-weight: 600; color: rgba(255,255,255,0.70);
  display: flex; align-items: center; gap: 8px;
}}
.dash-frame-live {{
  width: 7px; height: 7px; border-radius: 50%;
  background: #22C55E;
  box-shadow: 0 0 5px #22C55E;
  animation: pulse 2s infinite;
}}
@keyframes pulse {{
  0%, 100% {{ opacity: 1; }}
  50% {{ opacity: 0.4; }}
}}
.dash-chrome {{ display: flex; gap: 6px; }}
.dash-chrome span {{
  width: 10px; height: 10px; border-radius: 50%; display: block;
}}

/* Nav cards */
.nav-grid {{
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px;
  margin-top: 4px;
}}
.nav-card {{
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius-lg); padding: 24px 26px 20px;
  position: relative; overflow: hidden;
  transition: all 0.22s ease;
}}
.nav-card:hover {{
  border-color: var(--accent-border);
  box-shadow: var(--shadow);
  transform: translateY(-2px);
}}
.nav-card-stripe {{
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light));
  opacity: 0; transition: opacity 0.22s;
}}
.nav-card:hover .nav-card-stripe {{ opacity: 1; }}
.nav-card-icon {{
  width: 42px; height: 42px; border-radius: var(--radius-sm);
  margin-bottom: 14px;
  overflow: hidden; display: flex; align-items: center; justify-content: center;
}}
.nav-card-icon img {{ width: 100%; height: 100%; object-fit: contain; }}
.nav-card-title {{ font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 5px; }}
.nav-card-desc {{ font-size: 12px; color: var(--text-muted); line-height: 1.6; }}
.nav-card-cta {{
  margin-top: 16px; display: flex; align-items: center; gap: 5px;
  font-size: 11px; font-weight: 700; color: var(--accent);
  letter-spacing: 0.04em; text-transform: uppercase;
}}

/* ── PAGE ── */
.page-wrap {{ padding: 30px 40px 80px; }}
.page-top {{
  display: flex; align-items: center; justify-content: space-between;
  padding-bottom: 20px; margin-bottom: 24px;
  border-bottom: 1.5px solid var(--border);
}}
.page-top-left {{ display: flex; align-items: center; gap: 14px; }}
.page-icon {{
  width: 44px; height: 44px; border-radius: var(--radius);
  background: var(--surface); border: 1.5px solid var(--border);
  display: flex; align-items: center; justify-content: center; overflow: hidden;
}}
.page-icon img {{ width: 26px; height: 26px; object-fit: contain; }}
.page-title {{ font-size: 22px; font-weight: 800; letter-spacing: -0.03em; }}
.page-sub {{ font-size: 12px; color: var(--text-muted); margin-top: 2px; }}

/* ── METRICS ── */
div[data-testid="metric-container"] {{
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 16px 18px !important;
  box-shadow: var(--shadow-sm) !important;
}}
div[data-testid="metric-container"] label {{
  font-size: 10px !important; font-weight: 700 !important;
  text-transform: uppercase !important; letter-spacing: 0.08em !important;
  color: var(--text-muted) !important;
}}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {{
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 26px !important; font-weight: 600 !important; color: var(--text) !important;
}}

/* ── RADIO ── */
.stRadio > div {{ flex-direction: row !important; gap: 8px !important; }}
.stRadio label {{
  background: var(--surface) !important; border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important; padding: 7px 18px !important;
  font-size: 12.5px !important; font-weight: 500 !important;
  cursor: pointer !important; transition: all 0.18s !important; color: var(--text-secondary) !important;
}}
.stRadio label:has(input:checked) {{
  background: var(--accent-soft) !important;
  border-color: var(--accent-border) !important; color: var(--accent) !important;
  font-weight: 600 !important;
}}

/* ── SELECTBOX ── */
div[data-testid="stSelectbox"] > div > div {{
  background: var(--surface) !important; border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important; color: var(--text) !important; font-size: 13px !important;
}}

/* ── TEXT INPUT ── */
.stTextInput > div > div {{
  background: var(--surface) !important; border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}}
.stTextInput input {{ color: var(--text) !important; font-size: 13px !important; }}

/* ── TEXT AREA ── */
.stTextArea > div > div {{
  background: var(--surface) !important; border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}}
.stTextArea textarea {{
  color: var(--text) !important; font-size: 12.5px !important;
  font-family: 'IBM Plex Mono', monospace !important;
}}

/* ── DATAFRAME ── */
div[data-testid="stDataFrame"] {{
  border-radius: var(--radius) !important;
  border: 1.5px solid var(--border) !important; overflow: hidden !important;
  box-shadow: var(--shadow-sm) !important;
}}

/* ── PROGRESS ── */
.stProgress > div > div {{ background: var(--surface-3) !important; border-radius: 3px !important; }}
.stProgress > div > div > div {{
  background: linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light)) !important;
  border-radius: 3px !important;
}}

/* ── BUTTONS ── */
button[kind="primary"] {{
  background: var(--accent) !important; border: none !important; color: #fff !important;
  font-family: 'Sora', sans-serif !important; font-weight: 600 !important;
  font-size: 13px !important; border-radius: var(--radius-sm) !important;
  transition: background 0.18s !important;
}}
button[kind="primary"]:hover {{ background: var(--accent-hover) !important; }}
button[kind="secondary"] {{
  background: var(--surface) !important; border: 1.5px solid var(--border) !important;
  color: var(--text-secondary) !important; font-family: 'Sora', sans-serif !important;
  font-weight: 500 !important; font-size: 13px !important;
  border-radius: var(--radius-sm) !important;
}}
button[kind="secondary"]:hover {{
  border-color: var(--border-mid) !important; color: var(--text) !important;
}}

/* ── ALERTS ── */
.stInfo, .stSuccess, .stWarning, .stError {{
  border-radius: var(--radius-sm) !important; font-size: 13px !important;
  font-family: 'Sora', sans-serif !important;
}}

/* ── CANDIDATE CARD ── */
.cand-hero {{
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius-lg); padding: 22px 26px;
  margin-bottom: 20px;
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 14px;
  box-shadow: var(--shadow-sm);
}}
.cand-hero-id {{ font-size: 21px; font-weight: 800; letter-spacing: -0.02em; }}
.cand-hero-label {{
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 3px;
}}

/* ── BADGE ── */
.badge {{
  display: inline-flex; align-items: center; gap: 6px;
  padding: 5px 13px; border-radius: 20px; font-size: 12px; font-weight: 600;
}}
.badge-dot {{ width: 6px; height: 6px; border-radius: 50%; background: currentColor; }}
.badge-open   {{ background: var(--amber-bg); color: var(--amber); }}
.badge-close  {{ background: var(--green-bg); color: var(--green); }}
.badge-failed {{ background: var(--red-bg); color: var(--red); }}

/* ── PROGRESS TRACKER ── */
.prog-box {{
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 18px 22px; margin-bottom: 18px;
  box-shadow: var(--shadow-sm);
}}
.prog-track {{ height: 5px; background: var(--surface-3); border-radius: 3px; overflow: hidden; margin: 8px 0 6px; }}
.prog-fill {{
  height: 100%;
  background: linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light));
  border-radius: 3px; transition: width 0.6s ease;
}}
.prog-meta {{ display: flex; justify-content: space-between; align-items: center; }}

/* ── STEPS LIST ── */
.steps-box {{
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius); overflow: hidden; margin-bottom: 18px;
  box-shadow: var(--shadow-sm);
}}
.step-row {{
  display: flex; align-items: center; gap: 14px;
  padding: 11px 18px; border-bottom: 1px solid var(--border);
  transition: background 0.14s;
}}
.step-row:last-child {{ border-bottom: none; }}
.step-row:hover {{ background: var(--surface-2); }}
.step-num {{
  width: 27px; height: 27px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; flex-shrink: 0;
  font-family: 'IBM Plex Mono', monospace;
}}
.step-num.done   {{ background: var(--green-bg); color: var(--green); }}
.step-num.active {{ background: var(--accent-soft); color: var(--accent); }}
.step-num.idle   {{ background: var(--surface-2); color: var(--text-muted); }}
.step-num.failed {{ background: var(--red-bg); color: var(--red); }}
.step-name {{ font-size: 12.5px; font-weight: 600; flex: 1; color: var(--text); }}
.step-dates {{
  font-size: 10.5px; color: var(--text-muted);
  font-family: 'IBM Plex Mono', monospace;
}}
.step-badge {{
  font-size: 10px; font-weight: 600; padding: 3px 9px; border-radius: 20px;
}}
.step-badge.done   {{ background: var(--green-bg); color: var(--green); }}
.step-badge.active {{ background: var(--accent-soft); color: var(--accent); }}
.step-badge.idle   {{ background: var(--surface-2); color: var(--text-muted); }}
.step-badge.failed {{ background: var(--red-bg); color: var(--red); }}

/* ── REC ROOM ── */
.rec-section {{
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius-lg); margin-bottom: 18px; overflow: hidden;
  box-shadow: var(--shadow-sm);
}}
.rec-section-hdr {{
  padding: 14px 20px; border-bottom: 1.5px solid var(--border);
  display: flex; align-items: center; gap: 11px;
  background: var(--surface-2);
}}
.rec-section-icon {{
  width: 32px; height: 32px; border-radius: var(--radius-sm);
  background: var(--surface); border: 1.5px solid var(--border);
  display: flex; align-items: center; justify-content: center; overflow: hidden;
}}
.rec-section-icon img {{ width: 20px; height: 20px; object-fit: contain; }}
.rec-section-title {{ font-size: 13px; font-weight: 700; color: var(--text); }}
.rec-section-sub {{ font-size: 11px; color: var(--text-muted); margin-top: 1px; }}
.rec-body {{ padding: 20px; }}

/* Tracking info grid */
.info-grid {{
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 20px;
}}
.info-item {{
  background: var(--surface-2); border-radius: var(--radius-sm);
  padding: 12px 14px;
}}
.info-item-label {{
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.07em; color: var(--text-muted); margin-bottom: 4px;
}}
.info-item-val {{ font-size: 13px; font-weight: 600; color: var(--text); }}

</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──
if "page" not in st.session_state:
    st.session_state.page = "home"

# ── TOPBAR ──
st.markdown(f"""
<div class="topbar">
  <div class="topbar-left">
    <img class="topbar-logo"
         src="{GITHUB_RAW}/logo_putih.png"
         onerror="this.style.display='none'"
         alt="PTDH" />
    <div class="topbar-sep"></div>
    <span class="topbar-text">HR Recruitment Portal</span>
  </div>
  <div class="topbar-right">
    <span class="topbar-date">{datetime.now().strftime('%d %b %Y')}</span>
    <span class="topbar-badge">Live</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ────────────────────────────────────────
# ① HOME
# ────────────────────────────────────────
def run_home():
    st.markdown('<div class="home-wrap">', unsafe_allow_html=True)

    # ── Dashboard section label ──
    st.markdown("""
    <div class="sec-label">
      <div class="sec-label-text"><div class="sec-label-dot"></div>Recruitment Dashboard · Live</div>
      <div class="sec-label-line"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Looker embed ──
    st.markdown(f"""
    <div class="dash-frame">
      <div class="dash-frame-header">
        <div class="dash-frame-title">
          <div class="dash-frame-live"></div>
          Looker Studio — Recruitment Overview
        </div>
        <div class="dash-chrome">
          <span style="background:#FF5F57;"></span>
          <span style="background:#FFBD2E;"></span>
          <span style="background:#28CA41;"></span>
        </div>
      </div>
      <iframe
        width="100%" height="700"
        src="https://datastudio.google.com/embed/reporting/a425625f-0af4-4b5c-8826-218a929b1333/page/YwLxF"
        frameborder="0" style="border:0;display:block;" allowfullscreen>
      </iframe>
    </div>
    """, unsafe_allow_html=True)

    # ── Tools section label ──
    st.markdown("""
    <div class="sec-label" style="margin-top:4px;">
      <div class="sec-label-line"></div>
      <div class="sec-label-text"><div class="sec-label-dot"></div>Recruitment Tools</div>
      <div class="sec-label-line"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Two nav cards ──
    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.markdown(f"""
        <div class="nav-card">
          <div class="nav-card-stripe"></div>
          <div class="nav-card-icon">
            <img src="{GITHUB_RAW}/Search.png"
                 onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2242%22 height=%2242%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><circle cx=%2211%22 cy=%2211%22 r=%228%22/><path d=%22m21 21-4.35-4.35%22/></svg>'"
                 alt="Search" />
          </div>
          <div class="nav-card-title">Candidate Tracking</div>
          <div class="nav-card-desc">Monitor candidate pipeline & recruitment stage progress in real-time. Search by position or candidate ID.</div>
          <div class="nav-card-cta">Open Tracking <span>→</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Open Candidate Tracking", key="btn_tracking", use_container_width=True, type="primary"):
            st.session_state.page = "tracking"
            st.rerun()

    with c2:
        st.markdown(f"""
        <div class="nav-card">
          <div class="nav-card-stripe"></div>
          <div class="nav-card-icon">
            <img src="{GITHUB_RAW}/home.png"
                 onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2242%22 height=%2242%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><path d=%22M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z%22/><polyline points=%229 22 9 12 15 12 15 22%22/></svg>'"
                 alt="Room" />
          </div>
          <div class="nav-card-title">Recruitment Room</div>
          <div class="nav-card-desc">Forms, spreadsheet links, and quick actions — all recruitment tools in one workspace.</div>
          <div class="nav-card-cta">Open Room <span>→</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Open Recruitment Room", key="btn_recroom", use_container_width=True, type="primary"):
            st.session_state.page = "rec_room"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────
# ② TRACKING SYSTEM
# ────────────────────────────────────────
def run_tracking():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    # Header
    col_hdr, col_back = st.columns([5, 1])
    with col_hdr:
        st.markdown(f"""
        <div class="page-top" style="border:none;padding-bottom:0;margin-bottom:0;">
          <div class="page-top-left">
            <div class="page-icon">
              <img src="{GITHUB_RAW}/Search.png"
                   onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><circle cx=%2211%22 cy=%2211%22 r=%228%22/><path d=%22m21 21-4.35-4.35%22/></svg>'"
                   alt="Tracking" />
            </div>
            <div>
              <div class="page-title">Candidate Tracking</div>
              <div class="page-sub">Monitor recruitment pipeline in real-time</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_back:
        st.markdown("<div style='padding-top:12px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_track"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1.5px;background:var(--border);margin:14px 0 22px;'></div>", unsafe_allow_html=True)

    # Load data
    @st.cache_data(ttl=60)
    def load_data():
        url = "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc/export?format=csv"
        try:
            df = pd.read_csv(url)
            df.columns = df.columns.str.lower()
            for c in ["candidate_id", "position_name", "departement", "level", "loc", "status1"]:
                if c in df.columns:
                    df[c] = df[c].fillna("Unknown")
            return df, None
        except Exception as e:
            return None, str(e)

    df, err = load_data()
    if err:
        st.error(f"⚠ Failed to load data: {err}")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    mode = st.radio("Search Mode", ["By Position", "By Candidate"], horizontal=True, key="m_track")
    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    # ── BY POSITION ──
    if mode == "By Position":
        pos_list = sorted(df["position_name"].dropna().unique())
        sel_pos = st.selectbox("Select Position", pos_list, key="s_pos")
        filtered = df[df["position_name"] == sel_pos].copy()

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        if "status1" in filtered.columns:
            su = filtered["status1"].str.upper()
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Candidates", len(filtered))
            m2.metric("On-Progress",      int((su == "OPEN").sum()))
            m3.metric("Hired",            int((su == "CLOSE").sum()))
            m4.metric("Failed",           int((su == "FAILED").sum()))

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        cols = [c for c in ["candidate_id","position_name","departement","level","loc","last_progress","total_lt","status1"] if c in filtered.columns]
        disp = filtered[cols].copy()
        if "total_lt" in disp.columns:
            disp["total_lt"] = pd.to_numeric(disp["total_lt"], errors="coerce").fillna(0).astype(int)
        if "status1" in disp.columns:
            disp = disp.rename(columns={"status1": "Status"})

        def color_status(val):
            v = str(val).upper()
            if v == "OPEN":   return "color: #92400E; font-weight: 700;"
            if v == "FAILED": return "color: #991B1B; font-weight: 700;"
            if v == "CLOSE":  return "color: #166534; font-weight: 700;"
            return ""

        st.dataframe(
            disp.style.map(color_status, subset=["Status"]) if "Status" in disp.columns else disp,
            use_container_width=True, height=380,
        )

    # ── BY CANDIDATE ──
    else:
        cand_list = sorted(df["candidate_id"].dropna().unique())
        sel_cand = st.selectbox("Select Candidate ID", cand_list, key="s_cand")
        filt = df[df["candidate_id"] == sel_cand]
        if filt.empty:
            st.warning("No data found for this candidate.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        row = filt.iloc[0]
        h_st = str(row.get("status1", "Unknown")).upper()
        b_cls = {"OPEN": "badge-open", "CLOSE": "badge-close", "FAILED": "badge-failed"}.get(h_st, "badge-open")
        b_lbl = {"OPEN": "On Progress", "CLOSE": "Hired", "FAILED": "Failed"}.get(h_st, "Unknown")
        is_failed = (h_st == "FAILED")

        # Candidate hero card
        st.markdown(f"""
        <div class="cand-hero">
          <div>
            <div class="cand-hero-label">Candidate ID</div>
            <div class="cand-hero-id">{sel_cand}</div>
          </div>
          <span class="badge {b_cls}"><span class="badge-dot"></span>{b_lbl}</span>
        </div>
        """, unsafe_allow_html=True)

        # Info grid instead of metrics row (cleaner layout)
        pos  = row.get("position_name", "—")
        dept = row.get("departement",   "—")
        lvl  = row.get("level",         "—")
        loc  = row.get("loc",           "—")
        sla  = row.get("total_lt",      "—")
        if isinstance(sla, float): sla = int(sla)
        last = row.get("last_progress", "—")

        st.markdown(f"""
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:20px;">
          <div class="info-item"><div class="info-item-label">Position</div><div class="info-item-val">{pos}</div></div>
          <div class="info-item"><div class="info-item-label">Department</div><div class="info-item-val">{dept}</div></div>
          <div class="info-item"><div class="info-item-label">Level</div><div class="info-item-val">{lvl}</div></div>
          <div class="info-item"><div class="info-item-label">Location</div><div class="info-item-val">{loc}</div></div>
          <div class="info-item"><div class="info-item-label">SLA (days)</div><div class="info-item-val">{sla}</div></div>
          <div class="info-item"><div class="info-item-label">Last Progress</div><div class="info-item-val">{last}</div></div>
        </div>
        """, unsafe_allow_html=True)

        # Recruitment steps
        steps = [
            ("Screening CV",   "start_screening_cv",   "complete_screening_cv"),
            ("HR Interview",   "start_interview_hr",   "complete_interview_hr"),
            ("User Interview", "start_interview_user", "complete_interview_user"),
            ("Psychotest",     "start_psychotest",     "complete_psychotest"),
            ("Offering",       "start_offering",       "complete_offering"),
            ("MCU",            "start_mcu",            "mcu_date"),
            ("Review MCU",     "start_review_mcu",     "review_mcu"),
            ("FU MCU",         "start_fu_mcu",         "complete_fu_mcu"),
            ("Onboarding",     "date_onboarding",      "date_onboarding"),
        ]

        p_data = []
        done_count = 0
        last_active_idx = -1
        for i, (name, s_col, e_col) in enumerate(steps):
            s_val = row.get(s_col)
            e_val = row.get(e_col)
            has_start = pd.notna(s_val) and str(s_val).strip() not in ("", "nan")
            has_end   = pd.notna(e_val) and str(e_val).strip() not in ("", "nan")
            if has_end:
                st_code = "done"; done_count += 1
            elif has_start:
                st_code = "active"; last_active_idx = i
            else:
                st_code = "idle"
            p_data.append({
                "name": name,
                "start": str(s_val) if has_start else "—",
                "end":   str(e_val) if has_end   else "—",
                "status": st_code,
                "idx": i
            })

        prog_pct = done_count / len(steps)
        prog_color = "var(--red)" if is_failed else "var(--accent)"

        # If failed: the last active step is the failure point
        if is_failed and last_active_idx >= 0:
            p_data[last_active_idx]["status"] = "failed"

        # Progress bar
        bar_gradient = "linear-gradient(90deg, #991B1B, #EF4444)" if is_failed else "linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light))"
        st.markdown(f"""
        <div class="prog-box">
          <div class="prog-meta">
            <span style="font-size:13px;font-weight:700;">Recruitment Progress</span>
            <span style="font-size:11px;color:var(--text-muted);font-family:'IBM Plex Mono',monospace;">{done_count}/{len(steps)} stages complete</span>
          </div>
          <div class="prog-track">
            <div style="height:100%;width:{prog_pct*100:.0f}%;background:{bar_gradient};border-radius:3px;transition:width 0.6s ease;"></div>
          </div>
          <div class="prog-meta">
            <span style="font-size:11px;color:var(--text-muted);">Overall completion</span>
            <span style="font-size:12px;font-weight:700;color:{prog_color};">{prog_pct*100:.0f}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Steps list — failed step shows ✕
        html = '<div class="steps-box">'
        for s in p_data:
            cls = s["status"]
            if cls == "done":
                icon = "✓"
                badge_txt = "Done"
            elif cls == "failed":
                icon = "✕"
                badge_txt = "Failed Here"
            elif cls == "active":
                icon = str(s["idx"] + 1)
                badge_txt = "In Progress"
            else:
                icon = str(s["idx"] + 1)
                badge_txt = "Pending"
            html += f"""
            <div class="step-row">
              <div class="step-num {cls}">{icon}</div>
              <div class="step-name">{s['name']}</div>
              <div class="step-dates">{s['start']} → {s['end']}</div>
              <span class="step-badge {cls}">{badge_txt}</span>
            </div>"""
        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────
# ③ RECRUITMENT ROOM
# ────────────────────────────────────────
def run_rec_room():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    col_hdr, col_back = st.columns([5, 1])
    with col_hdr:
        st.markdown(f"""
        <div class="page-top" style="border:none;padding-bottom:0;margin-bottom:0;">
          <div class="page-top-left">
            <div class="page-icon">
              <img src="{GITHUB_RAW}/home.png"
                   onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><path d=%22M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z%22/><polyline points=%229 22 9 12 15 12 15 22%22/></svg>'"
                   alt="Room" />
            </div>
            <div>
              <div class="page-title">Recruitment Room</div>
              <div class="page-sub">Forms, spreadsheets, and tools — all in one place</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_back:
        st.markdown("<div style='padding-top:12px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_rec"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1.5px;background:var(--border);margin:14px 0 22px;'></div>", unsafe_allow_html=True)

    # ── SECTION 1: RECRUITMENT FORM (embedded directly) ──
    st.markdown(f"""
    <div class="rec-section">
      <div class="rec-section-hdr">
        <div class="rec-section-icon">
          <img src="{GITHUB_RAW}/form.png"
               onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><path d=%22M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z%22/><polyline points=%2214 2 14 8 20 8%22/><line x1=%2216%22 y1=%2213%22 x2=%228%22 y2=%2213%22/><line x1=%2216%22 y1=%2217%22 x2=%228%22 y2=%2217%22/><polyline points=%2210 9 9 9 8 9%22/></svg>'"
               alt="Form" />
        </div>
        <div>
          <div class="rec-section-title">Recruitment Form</div>
          <div class="rec-section-sub">Powered by Google Apps Script</div>
        </div>
      </div>
      <div class="rec-body">
        <div style="background:var(--surface-2);border:1.5px solid var(--border);border-radius:var(--radius);overflow:hidden;">
          <div style="padding:9px 16px;border-bottom:1px solid var(--border);display:flex;gap:7px;align-items:center;background:var(--dh-black);">
            <span style="width:9px;height:9px;border-radius:50%;background:#FF5F57;display:inline-block;"></span>
            <span style="width:9px;height:9px;border-radius:50%;background:#FFBD2E;display:inline-block;"></span>
            <span style="width:9px;height:9px;border-radius:50%;background:#28CA41;display:inline-block;"></span>
            <span style="margin-left:8px;font-size:11px;color:rgba(255,255,255,0.5);font-family:'IBM Plex Mono',monospace;">Recruitment Form</span>
          </div>
          <iframe src="{APPS_SCRIPT_URL}" width="100%" height="780" frameborder="0" style="border:none;display:block;"></iframe>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 2: QUICK LINKS ──
    st.markdown(f"""
    <div class="rec-section">
      <div class="rec-section-hdr">
        <div class="rec-section-icon">
          <img src="{GITHUB_RAW}/dashboard.png"
               onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><rect x=%223%22 y=%223%22 width=%227%22 height=%227%22/><rect x=%2214%22 y=%223%22 width=%227%22 height=%227%22/><rect x=%2214%22 y=%2214%22 width=%227%22 height=%227%22/><rect x=%223%22 y=%2214%22 width=%227%22 height=%227%22/></svg>'"
               alt="Links" />
        </div>
        <div>
          <div class="rec-section-title">Quick Links</div>
          <div class="rec-section-sub">Spreadsheets &amp; connected resources</div>
        </div>
      </div>
      <div class="rec-body">
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-muted);margin-bottom:10px;">
    ⚠️ Note: Links are stored in session only — they reset on page refresh. To make links permanent, add them directly to the code.
    </div>
    """, unsafe_allow_html=True)

    if "rec_links" not in st.session_state:
        st.session_state.rec_links = [
            {"label": "Recruitment Progress DB", "url": "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc"},
            {"label": "MPP Tracker", "url": ""},
            {"label": "Backend / Position List", "url": ""},
        ]

    for i, link in enumerate(st.session_state.rec_links):
        ca, cb, cc = st.columns([2, 4, 1])
        with ca:
            nl = st.text_input("Label", value=link["label"], key=f"ll_{i}", label_visibility="collapsed")
        with cb:
            nu = st.text_input("URL", value=link["url"], key=f"lu_{i}", placeholder="https://docs.google.com/...", label_visibility="collapsed")
        with cc:
            if st.button("↗ Open", key=f"lo_{i}"):
                if link["url"]:
                    st.markdown(f'<script>window.open("{link["url"]}", "_blank");</script>', unsafe_allow_html=True)
        st.session_state.rec_links[i]["label"] = nl
        st.session_state.rec_links[i]["url"]   = nu

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    if st.button("＋ Add Link", key="add_link"):
        st.session_state.rec_links.append({"label": "New Link", "url": ""})
        st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ── SECTION 3: QUICK ACTIONS ──
    st.markdown(f"""
    <div class="rec-section">
      <div class="rec-section-hdr">
        <div class="rec-section-icon">
          <img src="{GITHUB_RAW}/dashboard.png"
               onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF5000%22 stroke-width=%222%22><polygon points=%2213 2 3 14 12 14 11 22 21 10 12 10 13 2%22/></svg>'"
               alt="Actions" />
        </div>
        <div>
          <div class="rec-section-title">Quick Actions</div>
          <div class="rec-section-sub">Shortcuts to common tasks</div>
        </div>
      </div>
      <div class="rec-body">
    """, unsafe_allow_html=True)

    qa1, qa2, qa3, qa4 = st.columns(4)
    with qa1:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <img src="{GITHUB_RAW}/ppt-open-file-format-with-pie-chart.png" style="width:22px;height:22px;object-fit:contain;" onerror="this.style.display='none'" />
          <span style="font-size:12px;color:var(--text-muted);">PPT Report</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Download Report PPT", use_container_width=True, key="qa_ppt"):
            st.info("⏳ On progress — PPT report feature is being developed.")
    with qa2:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <img src="{GITHUB_RAW}/dashboard.png" style="width:22px;height:22px;object-fit:contain;" onerror="this.style.display='none'" />
          <span style="font-size:12px;color:var(--text-muted);">Dashboard</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Recruitment Dashboard", use_container_width=True, key="qa_mpp"):
            st.session_state.page = "home"
            st.rerun()
    with qa3:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <img src="{GITHUB_RAW}/Search.png" style="width:22px;height:22px;object-fit:contain;" onerror="this.style.display='none'" />
          <span style="font-size:12px;color:var(--text-muted);">Tracking</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Tracking", use_container_width=True, key="qa_track"):
            st.session_state.page = "tracking"
            st.rerun()
    with qa4:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <span style="font-size:18px;">🔄</span>
          <span style="font-size:12px;color:var(--text-muted);">Cache</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Refresh Data Cache", use_container_width=True, key="qa_cache"):
            st.cache_data.clear()
            st.success("Cache cleared!")

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ── ROUTER ──
if st.session_state.page == "home":
    run_home()
elif st.session_state.page == "tracking":
    run_tracking()
elif st.session_state.page == "rec_room":
    run_rec_room()
