"""
HR Centralized System — Darma Henwa Brand
Redesign: Dashboard-first Home, professional DH orange theme
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="PTDH Recruitment Portal",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GLOBAL CSS — Darma Henwa Brand Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  /* Darma Henwa Brand Colors */
  --dh-orange:        #FF5000;
  --dh-orange-light:  #FF7501;
  --dh-yellow:        #FFDC1E;
  --dh-blue-soft:     #AEDDEC;
  --dh-black:         #211C1C;

  /* UI Palette */
  --bg:               #F7F6F4;
  --surface:          #FFFFFF;
  --surface-2:        #F2F0ED;
  --surface-3:        #E8E5E0;
  --border:           rgba(33,28,28,0.10);
  --border-mid:       rgba(33,28,28,0.18);
  --text:             #211C1C;
  --text-secondary:   #5C5652;
  --text-muted:       #8C8681;

  /* Accents */
  --accent:           #FF5000;
  --accent-hover:     #E04500;
  --accent-soft:      rgba(255,80,0,0.08);
  --accent-border:    rgba(255,80,0,0.25);

  /* Status */
  --green:            #1A7A4A;
  --green-bg:         rgba(26,122,74,0.08);
  --amber:            #B85C00;
  --amber-bg:         rgba(255,115,1,0.10);
  --red:              #C53030;
  --red-bg:           rgba(197,48,48,0.08);

  --radius:           10px;
  --radius-sm:        7px;
  --radius-lg:        14px;
  --shadow-sm:        0 1px 4px rgba(33,28,28,0.08);
  --shadow:           0 4px 16px rgba(33,28,28,0.10);
  --shadow-lg:        0 8px 32px rgba(33,28,28,0.12);
}

html, body, .stApp {
  background: var(--bg) !important;
  font-family: 'Sora', sans-serif !important;
  color: var(--text) !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewBlockContainer"] { padding: 0 !important; }
.element-container { margin: 0 !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--surface-2); }
::-webkit-scrollbar-thumb { background: var(--surface-3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* ── TOPBAR ── */
.topbar {
  position: sticky; top: 0; z-index: 999;
  background: var(--dh-black);
  height: 56px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 36px;
  border-bottom: 2px solid var(--dh-orange);
}
.topbar-logo-area {
  display: flex; align-items: center; gap: 14px;
}
.topbar-logo-placeholder {
  height: 28px; display: flex; align-items: center;
}
.topbar-logo-placeholder img { height: 28px; width: auto; }
.topbar-divider {
  width: 1px; height: 20px;
  background: rgba(255,255,255,0.15);
}
.topbar-title {
  font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.85);
  letter-spacing: 0.01em;
}
.topbar-right {
  display: flex; align-items: center; gap: 12px;
}
.topbar-date {
  font-size: 11px; color: rgba(255,255,255,0.45);
  font-family: 'IBM Plex Mono', monospace;
}
.topbar-badge {
  font-size: 10px; font-weight: 600;
  background: var(--dh-orange); color: #fff;
  padding: 3px 9px; border-radius: 20px;
  letter-spacing: 0.04em; text-transform: uppercase;
}

/* ── HOMEPAGE LAYOUT ── */
.home-wrap { padding: 32px 36px 60px; }

/* Dashboard hero */
.dash-hero {
  background: var(--dh-black);
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 20px;
  box-shadow: var(--shadow-lg);
}
.dash-hero-header {
  padding: 16px 22px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  display: flex; align-items: center; justify-content: space-between;
}
.dash-hero-title {
  font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.85);
  display: flex; align-items: center; gap: 8px;
}
.dash-hero-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--dh-orange);
  box-shadow: 0 0 6px var(--dh-orange);
}
.dash-chrome-dots { display: flex; gap: 6px; }
.dash-chrome-dot {
  width: 10px; height: 10px; border-radius: 50%;
}

/* ── NAV CARDS (below dashboard) ── */
.nav-cards-row {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.nav-card-wrap {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 22px 24px 18px;
  position: relative; overflow: hidden;
  transition: all 0.2s ease;
  cursor: pointer;
}
.nav-card-wrap:hover {
  border-color: var(--accent-border);
  box-shadow: var(--shadow);
  transform: translateY(-1px);
}
.nav-card-wrap::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light));
  opacity: 0; transition: opacity 0.2s;
}
.nav-card-wrap:hover::before { opacity: 1; }
.nav-card-icon {
  width: 38px; height: 38px; border-radius: var(--radius-sm);
  background: var(--accent-soft);
  border: 1px solid var(--accent-border);
  display: flex; align-items: center; justify-content: center;
  font-size: 17px; margin-bottom: 12px;
}
.nav-card-title {
  font-size: 14px; font-weight: 700; color: var(--text);
  margin-bottom: 5px; letter-spacing: -0.01em;
}
.nav-card-desc { font-size: 11.5px; color: var(--text-muted); line-height: 1.55; }
.nav-card-cta {
  margin-top: 14px; font-size: 11px; font-weight: 600;
  color: var(--accent); display: flex; align-items: center; gap: 4px;
  text-transform: uppercase; letter-spacing: 0.05em;
}

/* ── PAGE WRAPPER ── */
.page-wrap { padding: 32px 36px 80px; }

/* ── PAGE HEADER ── */
.page-header-bar {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 28px; padding-bottom: 20px;
  border-bottom: 1.5px solid var(--border);
}
.page-header-left { display: flex; align-items: center; gap: 14px; }
.page-header-icon {
  width: 44px; height: 44px; border-radius: var(--radius);
  background: var(--accent-soft); border: 1.5px solid var(--accent-border);
  display: flex; align-items: center; justify-content: center; font-size: 20px;
}
.page-header-title {
  font-size: 22px; font-weight: 800; letter-spacing: -0.03em; color: var(--text);
}
.page-header-sub { font-size: 12px; color: var(--text-muted); margin-top: 2px; }

/* Back button */
.stButton button[data-testid="baseButton-secondary"] {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  color: var(--text-secondary) !important;
  font-size: 12px !important; font-weight: 500 !important;
  border-radius: var(--radius-sm) !important;
  padding: 7px 14px !important;
  font-family: 'Sora', sans-serif !important;
}

/* ── METRICS ── */
div[data-testid="metric-container"] {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 16px 18px !important;
}
div[data-testid="metric-container"] label {
  font-size: 10px !important; font-weight: 600 !important;
  text-transform: uppercase !important; letter-spacing: 0.07em !important;
  color: var(--text-muted) !important;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 26px !important; font-weight: 600 !important;
  color: var(--text) !important;
}
div[data-testid="stMetricDelta"] { font-size: 11px !important; }

/* ── FILTER / RADIO ── */
.stRadio > div { flex-direction: row !important; gap: 8px !important; }
.stRadio label {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  padding: 7px 16px !important;
  font-size: 12px !important; font-weight: 500 !important;
  cursor: pointer !important; transition: all 0.18s !important;
  color: var(--text-secondary) !important;
}
.stRadio label:has(input:checked) {
  background: var(--accent-soft) !important;
  border-color: var(--accent-border) !important;
  color: var(--accent) !important;
}

/* ── SELECT BOX ── */
div[data-testid="stSelectbox"] > div > div {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text) !important;
  font-size: 13px !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within {
  border-color: var(--accent-border) !important;
  box-shadow: 0 0 0 3px rgba(255,80,0,0.08) !important;
}

/* ── TEXT INPUT ── */
.stTextInput > div > div {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--accent-border) !important;
  box-shadow: 0 0 0 3px rgba(255,80,0,0.08) !important;
}
.stTextInput input { color: var(--text) !important; font-size: 13px !important; }

/* ── TEXT AREA ── */
.stTextArea > div > div {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}
.stTextArea textarea {
  color: var(--text) !important;
  font-size: 12.5px !important;
  font-family: 'IBM Plex Mono', monospace !important;
}

/* ── DATAFRAME ── */
div[data-testid="stDataFrame"] {
  border-radius: var(--radius) !important;
  border: 1.5px solid var(--border) !important;
  overflow: hidden !important;
}

/* ── PROGRESS ── */
.stProgress > div > div {
  background: var(--surface-3) !important;
  border-radius: 3px !important;
}
.stProgress > div > div > div {
  background: linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light)) !important;
  border-radius: 3px !important;
}

/* ── BUTTONS (Streamlit native) ── */
button[kind="primary"] {
  background: var(--accent) !important;
  border: none !important; color: #fff !important;
  font-family: 'Sora', sans-serif !important;
  font-weight: 600 !important; font-size: 13px !important;
  border-radius: var(--radius-sm) !important;
}
button[kind="primary"]:hover {
  background: var(--accent-hover) !important;
}
button[kind="secondary"] {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  color: var(--text-secondary) !important;
  font-family: 'Sora', sans-serif !important;
  font-weight: 500 !important; font-size: 13px !important;
  border-radius: var(--radius-sm) !important;
}

/* ── ALERTS ── */
.stInfo, .stSuccess, .stWarning, .stError {
  border-radius: var(--radius-sm) !important;
  font-size: 13px !important;
  font-family: 'Sora', sans-serif !important;
}

/* ── EXPANDER ── */
div[data-testid="stExpander"] {
  background: var(--surface) !important;
  border: 1.5px solid var(--border) !important;
  border-radius: var(--radius) !important;
}
div[data-testid="stExpander"] summary {
  color: var(--text) !important; font-weight: 600 !important;
}

/* ── CANDIDATE CARD ── */
.cand-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  margin-bottom: 18px;
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 14px;
}
.cand-card-id {
  font-size: 20px; font-weight: 800;
  letter-spacing: -0.02em; color: var(--text);
}
.cand-card-label {
  font-size: 10px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 3px;
}

/* ── STATUS BADGES ── */
.badge {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 5px 12px; border-radius: 20px;
  font-size: 11.5px; font-weight: 600;
}
.badge-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
.badge-open   { background: var(--amber-bg); color: var(--amber); }
.badge-close  { background: var(--green-bg); color: var(--green); }
.badge-failed { background: var(--red-bg); color: var(--red); }

/* ── PROGRESS TRACKER ── */
.prog-wrap {
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 18px 22px; margin-bottom: 18px;
}
.prog-bar-track {
  height: 5px; background: var(--surface-3);
  border-radius: 3px; overflow: hidden; margin: 8px 0 6px;
}
.prog-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--dh-orange), var(--dh-orange-light));
  border-radius: 3px; transition: width 0.6s ease;
}
.prog-meta { display: flex; justify-content: space-between; }

/* ── STEPS ── */
.steps-container {
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius); overflow: hidden; margin-bottom: 18px;
}
.step-row {
  display: flex; align-items: center; gap: 14px;
  padding: 11px 18px; border-bottom: 1px solid var(--border);
  transition: background 0.15s;
}
.step-row:last-child { border-bottom: none; }
.step-row:hover { background: var(--surface-2); }
.step-num {
  width: 26px; height: 26px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 10px; font-weight: 700; flex-shrink: 0;
  font-family: 'IBM Plex Mono', monospace;
}
.step-num.done   { background: var(--green-bg); color: var(--green); }
.step-num.active { background: var(--accent-soft); color: var(--accent); }
.step-num.idle   { background: var(--surface-2); color: var(--text-muted); }
.step-name { font-size: 12.5px; font-weight: 600; flex: 1; color: var(--text); }
.step-dates {
  font-size: 10.5px; color: var(--text-muted);
  font-family: 'IBM Plex Mono', monospace;
}
.step-badge {
  font-size: 10px; font-weight: 600;
  padding: 3px 9px; border-radius: 20px;
}
.step-badge.done   { background: var(--green-bg); color: var(--green); }
.step-badge.active { background: var(--accent-soft); color: var(--accent); }
.step-badge.idle   { background: var(--surface-2); color: var(--text-muted); }

/* ── REC ROOM SECTIONS ── */
.rec-section {
  background: var(--surface); border: 1.5px solid var(--border);
  border-radius: var(--radius-lg); margin-bottom: 18px; overflow: hidden;
}
.rec-section-header {
  padding: 14px 20px; border-bottom: 1.5px solid var(--border);
  display: flex; align-items: center; gap: 10px;
  background: var(--surface-2);
}
.rec-section-icon {
  width: 30px; height: 30px; border-radius: var(--radius-sm);
  background: var(--accent-soft); border: 1px solid var(--accent-border);
  display: flex; align-items: center; justify-content: center; font-size: 14px;
}
.rec-section-title { font-size: 13px; font-weight: 700; color: var(--text); }
.rec-section-sub { font-size: 11px; color: var(--text-muted); margin-top: 1px; }
.rec-section-body { padding: 20px; }

/* ── SECTION HEADER ── */
.section-label {
  display: flex; align-items: center; gap: 10px;
  margin-bottom: 14px;
}
.section-label-line { flex: 1; height: 1px; background: var(--border); }
.section-label-text {
  font-size: 10px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--text-muted); white-space: nowrap;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"

# ─────────────────────────────────────────────
# TOPBAR
# ─────────────────────────────────────────────
logo_html = """
<img src="https://raw.githubusercontent.com/naviantar-ptdh/202605-centralized/main/logo_putih.png"
     onerror="this.style.display='none';this.nextElementSibling.style.display='flex';"
     style="height:26px;width:auto;" />
<div style="display:none;align-items:center;gap:6px;">
  <div style="width:22px;height:22px;background:var(--dh-orange);border-radius:4px;"></div>
  <span style="font-size:14px;font-weight:800;color:#fff;letter-spacing:-0.01em;">PTDH</span>
</div>
"""

st.markdown(f"""
<div class="topbar">
  <div class="topbar-logo-area">
    <div class="topbar-logo-placeholder">{logo_html}</div>
    <div class="topbar-divider"></div>
    <span class="topbar-title">HR Recruitment Portal</span>
  </div>
  <div class="topbar-right">
    <span class="topbar-date">{datetime.now().strftime('%d %b %Y')}</span>
    <span class="topbar-badge">Live</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ① HOME PAGE — Dashboard first, then 2 cards
# ─────────────────────────────────────────────
def run_home():
    st.markdown('<div class="home-wrap">', unsafe_allow_html=True)

    # ── Section label: Dashboard ──
    st.markdown("""
    <div class="section-label">
      <div class="section-label-text">📊 Recruitment Dashboard · Live</div>
      <div class="section-label-line"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Dashboard Embed ──
    st.markdown("""
    <div class="dash-hero">
      <div class="dash-hero-header">
        <div class="dash-hero-title">
          <div class="dash-hero-dot"></div>
          Recruitment Dashboard — Looker Studio
        </div>
        <div class="dash-chrome-dots">
          <div class="dash-chrome-dot" style="background:#FF5F57;"></div>
          <div class="dash-chrome-dot" style="background:#FFBD2E;"></div>
          <div class="dash-chrome-dot" style="background:#28CA41;"></div>
        </div>
      </div>
      <iframe
        width="100%" height="700"
        src="https://datastudio.google.com/embed/reporting/a425625f-0af4-4b5c-8826-218a929b1333/page/YwLxF"
        frameborder="0" style="border:0;display:block;" allowfullscreen>
      </iframe>
    </div>
    """, unsafe_allow_html=True)

    # ── Section label: Tools ──
    st.markdown("""
    <div class="section-label" style="margin-top:28px;">
      <div class="section-label-line"></div>
      <div class="section-label-text">⚡ Recruitment Tools</div>
      <div class="section-label-line"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Two Nav Cards ──
    st.markdown('<div class="nav-cards-row">', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.markdown("""
        <div class="nav-card-wrap">
          <div class="nav-card-icon">🔍</div>
          <div class="nav-card-title">Candidate Tracking</div>
          <div class="nav-card-desc">Monitor candidate pipeline & recruitment stage progress in real-time. Search by position or candidate ID.</div>
          <div class="nav-card-cta">Open Tracking <span>→</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Open Tracking System", key="btn_tracking", use_container_width=True, type="primary"):
            st.session_state.page = "tracking"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="nav-card-wrap">
          <div class="nav-card-icon">🏠</div>
          <div class="nav-card-title">Recruitment Room</div>
          <div class="nav-card-desc">Forms, spreadsheet links, quick actions, and team notes — all recruitment tools in one workspace.</div>
          <div class="nav-card-cta">Open Room <span>→</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Open Recruitment Room", key="btn_recroom", use_container_width=True, type="primary"):
            st.session_state.page = "rec_room"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ② TRACKING SYSTEM
# ─────────────────────────────────────────────
def run_tracking():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    # Header row
    col_hdr, col_back = st.columns([5, 1])
    with col_hdr:
        st.markdown("""
        <div class="page-header-bar" style="border-bottom:none;margin-bottom:0;padding-bottom:0;">
          <div class="page-header-left">
            <div class="page-header-icon">🔍</div>
            <div>
              <div class="page-header-title">Candidate Tracking</div>
              <div class="page-header-sub">Monitor recruitment pipeline in real-time</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_back:
        st.markdown("<div style='padding-top:14px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_track"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="height:1.5px;background:var(--border);margin:16px 0 24px;"></div>
    """, unsafe_allow_html=True)

    # Load Data
    @st.cache_data(ttl=60)
    def load_tracking_data():
        url = "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc/export?format=csv"
        try:
            df = pd.read_csv(url)
            df.columns = df.columns.str.lower()
            for col in ["candidate_id", "position_name", "departement", "level", "loc", "status1"]:
                if col in df.columns:
                    df[col] = df[col].fillna("Unknown")
            return df, None
        except Exception as e:
            return None, str(e)

    df, err = load_tracking_data()

    if err:
        st.error(f"⚠ Failed to load data: {err}")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    # Search Mode
    mode = st.radio("Search Mode", ["By Position", "By Candidate"], horizontal=True, key="m_track")
    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    # ── BY POSITION ──
    if mode == "By Position":
        pos_list = sorted(df["position_name"].dropna().unique())
        sel_pos = st.selectbox("Select Position", pos_list, key="s_pos")
        filtered = df[df["position_name"] == sel_pos].copy()

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        if "status1" in filtered.columns:
            status_s = filtered["status1"].str.upper()
            total    = len(filtered)
            open_c   = (status_s == "OPEN").sum()
            close_c  = (status_s == "CLOSE").sum()
            failed_c = (status_s == "FAILED").sum()

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Candidates", total)
            m2.metric("On-Progress",      int(open_c))
            m3.metric("Hired",            int(close_c))
            m4.metric("Failed",           int(failed_c))

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        cols_to_show = [c for c in ["candidate_id", "position_name", "departement", "level", "loc", "last_progress", "total_lt", "status1"] if c in filtered.columns]
        disp = filtered[cols_to_show].copy()
        if "total_lt" in disp.columns:
            disp["total_lt"] = pd.to_numeric(disp["total_lt"], errors="coerce").fillna(0).astype(int)
        if "status1" in disp.columns:
            disp = disp.rename(columns={"status1": "Hiring Status"})

        def color_status(val):
            v = str(val).upper()
            if v == "OPEN":   return "color: #B85C00; font-weight: 700;"
            if v == "FAILED": return "color: #C53030; font-weight: 700;"
            if v == "CLOSE":  return "color: #1A7A4A; font-weight: 700;"
            return ""

        st.dataframe(
            disp.style.map(color_status, subset=["Hiring Status"]) if "Hiring Status" in disp.columns else disp,
            use_container_width=True, height=360,
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
        badge_class = {"OPEN": "badge-open", "CLOSE": "badge-close", "FAILED": "badge-failed"}.get(h_st, "badge-open")
        badge_label = {"OPEN": "On Progress", "CLOSE": "Hired", "FAILED": "Failed"}.get(h_st, "Unknown")

        st.markdown(f"""
        <div class="cand-card">
          <div>
            <div class="cand-card-label">Candidate ID</div>
            <div class="cand-card-id">{sel_cand}</div>
          </div>
          <span class="badge {badge_class}"><span class="badge-dot"></span>{badge_label}</span>
        </div>
        """, unsafe_allow_html=True)

        # Metrics
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Position",   row.get("position_name", "—"))
        m2.metric("Department", row.get("departement", "—"))
        m3.metric("Level",      row.get("level", "—"))
        m4.metric("Location",   row.get("loc", "—"))
        sla = row.get("total_lt", "—")
        if isinstance(sla, float): sla = int(sla)
        m5.metric("SLA (days)", sla)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        # Steps data
        steps = [
            ("Screening CV",    "start_screening_cv",   "complete_screening_cv"),
            ("HR Interview",    "start_interview_hr",   "complete_interview_hr"),
            ("User Interview",  "start_interview_user", "complete_interview_user"),
            ("Psychotest",      "start_psychotest",     "complete_psychotest"),
            ("Offering",        "start_offering",       "complete_offering"),
            ("MCU",             "start_mcu",            "mcu_date"),
            ("Review MCU",      "start_review_mcu",     "review_mcu"),
            ("FU MCU",          "start_fu_mcu",         "complete_fu_mcu"),
            ("Onboarding",      "date_onboarding",      "date_onboarding"),
        ]

        p_data = []
        done_count = 0
        for name, s_col, e_col in steps:
            s_val = row.get(s_col)
            e_val = row.get(e_col)
            has_start = pd.notna(s_val) and str(s_val).strip() not in ("", "nan")
            has_end   = pd.notna(e_val) and str(e_val).strip() not in ("", "nan")
            if has_end:
                status = "done"; done_count += 1
            elif has_start:
                status = "active"
            else:
                status = "idle"
            p_data.append({
                "name": name,
                "start": str(s_val) if has_start else "—",
                "end": str(e_val) if has_end else "—",
                "status": status
            })

        prog_pct = done_count / len(steps)

        # Progress bar
        st.markdown(f"""
        <div class="prog-wrap">
          <div class="prog-meta">
            <span style="font-size:12.5px;font-weight:700;color:var(--text);">Recruitment Progress</span>
            <span style="font-size:11px;color:var(--text-muted);font-family:'IBM Plex Mono',monospace;">{done_count}/{len(steps)} stages complete</span>
          </div>
          <div class="prog-bar-track">
            <div class="prog-bar-fill" style="width:{prog_pct*100:.0f}%;"></div>
          </div>
          <div class="prog-meta">
            <span style="font-size:11px;color:var(--text-muted);">Overall completion</span>
            <span style="font-size:12px;font-weight:700;color:var(--accent);">{prog_pct*100:.0f}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Steps list
        steps_html = '<div class="steps-container">'
        for i, s in enumerate(p_data):
            cls = s["status"]
            icon = "✓" if cls == "done" else str(i + 1)
            badge_txt = {"done": "Done", "active": "In Progress", "idle": "Pending"}[cls]
            steps_html += f"""
            <div class="step-row">
              <div class="step-num {cls}">{icon}</div>
              <div class="step-name">{s['name']}</div>
              <div class="step-dates">{s['start']} → {s['end']}</div>
              <span class="step-badge {cls}">{badge_txt}</span>
            </div>"""
        steps_html += "</div>"
        st.markdown(steps_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ③ RECRUITMENT ROOM
# ─────────────────────────────────────────────
def run_rec_room():
    st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

    # Header
    col_hdr, col_back = st.columns([5, 1])
    with col_hdr:
        st.markdown("""
        <div class="page-header-bar" style="border-bottom:none;margin-bottom:0;padding-bottom:0;">
          <div class="page-header-left">
            <div class="page-header-icon">🏠</div>
            <div>
              <div class="page-header-title">Recruitment Room</div>
              <div class="page-header-sub">Forms, spreadsheets, and tools — all in one place</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_back:
        st.markdown("<div style='padding-top:14px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_rec"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="height:1.5px;background:var(--border);margin:16px 0 24px;"></div>
    """, unsafe_allow_html=True)

    # ── SECTION 1: RECRUITMENT FORM ──
    st.markdown("""
    <div class="rec-section">
      <div class="rec-section-header">
        <div class="rec-section-icon">📋</div>
        <div>
          <div class="rec-section-title">Recruitment Form</div>
          <div class="rec-section-sub">Powered by Google Apps Script</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    apps_url = st.text_input(
        "Apps Script Web App URL",
        placeholder="https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec",
        key="apps_url",
        help="Paste the deployed URL of your Google Apps Script Web App here."
    )

    if apps_url and apps_url.startswith("https://"):
        st.markdown(f"""
        <div style="margin-top:14px;background:var(--surface-2);border:1.5px solid var(--border);border-radius:var(--radius);overflow:hidden;">
          <div style="padding:8px 14px;border-bottom:1px solid var(--border);display:flex;gap:7px;align-items:center;">
            <div style="width:9px;height:9px;border-radius:50%;background:#FF5F57;"></div>
            <div style="width:9px;height:9px;border-radius:50%;background:#FFBD2E;"></div>
            <div style="width:9px;height:9px;border-radius:50%;background:#28CA41;"></div>
            <span style="margin-left:6px;font-size:11px;color:var(--text-muted);">Recruitment Form</span>
          </div>
          <iframe src="{apps_url}" width="100%" height="750" frameborder="0" style="border:none;display:block;"></iframe>
        </div>
        """, unsafe_allow_html=True)
    elif apps_url:
        st.warning("Please enter a valid URL starting with https://")
    else:
        st.markdown("""
        <div style="background:var(--surface-2);border:1.5px dashed var(--accent-border);border-radius:var(--radius);padding:44px;text-align:center;margin-top:8px;">
          <div style="font-size:28px;margin-bottom:10px;">📋</div>
          <div style="font-size:13px;font-weight:600;color:var(--text);margin-bottom:5px;">No Form Connected</div>
          <div style="font-size:12px;color:var(--text-muted);">Paste your Apps Script URL above to embed the recruitment form.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ── SECTION 2: QUICK LINKS ──
    st.markdown("""
    <div class="rec-section">
      <div class="rec-section-header">
        <div class="rec-section-icon">🔗</div>
        <div>
          <div class="rec-section-title">Quick Links</div>
          <div class="rec-section-sub">Spreadsheets & connected resources</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    if "rec_links" not in st.session_state:
        st.session_state.rec_links = [
            {"label": "Recruitment Progress DB", "url": "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc", "icon": "📊"},
            {"label": "MPP Tracker", "url": "", "icon": "📈"},
            {"label": "Backend / Position List", "url": "", "icon": "🗂"},
        ]

    for i, link in enumerate(st.session_state.rec_links):
        ca, cb, cc = st.columns([2, 4, 1])
        with ca:
            new_label = st.text_input("Label", value=link["label"], key=f"link_label_{i}", label_visibility="collapsed")
        with cb:
            new_url = st.text_input("URL", value=link["url"], key=f"link_url_{i}", placeholder="https://docs.google.com/...", label_visibility="collapsed")
        with cc:
            if st.button("Open ↗", key=f"link_open_{i}"):
                if link["url"]:
                    st.markdown(f'<script>window.open("{link["url"]}", "_blank");</script>', unsafe_allow_html=True)
        st.session_state.rec_links[i]["label"] = new_label
        st.session_state.rec_links[i]["url"] = new_url

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    if st.button("＋ Add Link", key="add_link"):
        st.session_state.rec_links.append({"label": "New Link", "url": "", "icon": "🔗"})
        st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ── SECTION 3: QUICK ACTIONS ──
    st.markdown("""
    <div class="rec-section">
      <div class="rec-section-header">
        <div class="rec-section-icon">⚡</div>
        <div>
          <div class="rec-section-title">Quick Actions</div>
          <div class="rec-section-sub">Shortcuts to common tasks</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    qa1, qa2, qa3, qa4 = st.columns(4)
    with qa1:
        if st.button("📥 Download Report PPT", use_container_width=True, key="qa_ppt"):
            st.info("Connect to Report module to generate PPT.")
    with qa2:
        if st.button("📊 Open MPP Dashboard", use_container_width=True, key="qa_mpp"):
            st.session_state.page = "home"
            st.rerun()
    with qa3:
        if st.button("🔍 Go to Tracking", use_container_width=True, key="qa_track"):
            st.session_state.page = "tracking"
            st.rerun()
    with qa4:
        if st.button("🔄 Refresh Data Cache", use_container_width=True, key="qa_cache"):
            st.cache_data.clear()
            st.success("Cache cleared!")

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ── SECTION 4: TEAM NOTES ──
    st.markdown("""
    <div class="rec-section">
      <div class="rec-section-header">
        <div class="rec-section-icon">📝</div>
        <div>
          <div class="rec-section-title">Team Notes</div>
          <div class="rec-section-sub">Shared notes for the recruitment team</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    if "rec_notes" not in st.session_state:
        st.session_state.rec_notes = ""

    st.session_state.rec_notes = st.text_area(
        "Notes",
        value=st.session_state.rec_notes,
        height=130,
        placeholder="Write team notes, reminders, or updates here...",
        label_visibility="collapsed",
        key="rec_notes_input"
    )

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────
if st.session_state.page == "home":
    run_home()
elif st.session_state.page == "tracking":
    run_tracking()
elif st.session_state.page == "rec_room":
    run_rec_room()
