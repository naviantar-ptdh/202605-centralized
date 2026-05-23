"""
HR Centralized System — Streamlit App
Professional redesign dengan 3 section:
  1. Home: Looker Dashboard embed + 2 navigation buttons
  2. Tracking System (diprofesionalkan)
  3. Recruitment Room (baru)
"""

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="HR System Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GLOBAL CSS — Professional Dark-Accent Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & Root ── */
*, *::before, *::after { box-sizing: border-box; }

:root {
  --bg:           #0F1117;
  --surface:      #181C27;
  --surface-2:    #1E2435;
  --border:       rgba(255,255,255,0.07);
  --border-mid:   rgba(255,255,255,0.13);
  --text:         #E8EAF0;
  --text-muted:   #6B7280;
  --text-dim:     #9CA3AF;
  --accent:       #4F8EF7;
  --accent-glow:  rgba(79,142,247,0.18);
  --accent-soft:  rgba(79,142,247,0.10);
  --green:        #34D399;
  --green-bg:     rgba(52,211,153,0.10);
  --orange:       #F59E0B;
  --orange-bg:    rgba(245,158,11,0.10);
  --red:          #F87171;
  --red-bg:       rgba(248,113,113,0.10);
  --radius:       12px;
  --radius-sm:    8px;
  --radius-lg:    16px;
  --shadow:       0 4px 24px rgba(0,0,0,0.4);
}

/* ── Base ── */
html, body, .stApp {
  background: var(--bg) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  color: var(--text) !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewBlockContainer"] { padding: 0 !important; }

/* ── Remove default streamlit element margins ── */
.element-container { margin: 0 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--surface); }
::-webkit-scrollbar-thumb { background: var(--border-mid); border-radius: 3px; }

/* ── Topbar ── */
.topbar {
  position: sticky; top: 0; z-index: 999;
  background: rgba(15,17,23,0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 0 40px;
  height: 60px;
  display: flex; align-items: center; justify-content: space-between;
}
.topbar-brand {
  display: flex; align-items: center; gap: 10px;
  font-size: 15px; font-weight: 700; letter-spacing: -0.02em; color: var(--text);
}
.topbar-dot {
  width: 8px; height: 8px; background: var(--accent);
  border-radius: 50%; box-shadow: 0 0 8px var(--accent);
}
.topbar-badge {
  font-size: 11px; font-weight: 500;
  background: var(--accent-soft); color: var(--accent);
  border: 1px solid rgba(79,142,247,0.25);
  padding: 3px 10px; border-radius: 20px;
  font-family: 'JetBrains Mono', monospace;
}
.topbar-nav {
  display: flex; align-items: center; gap: 6px;
}
.topbar-nav-btn {
  padding: 7px 16px; border-radius: var(--radius-sm);
  font-size: 12px; font-weight: 500;
  background: none; border: 1px solid var(--border);
  color: var(--text-muted); cursor: pointer;
  transition: all 0.2s; font-family: 'Plus Jakarta Sans', sans-serif;
}
.topbar-nav-btn:hover, .topbar-nav-btn.active {
  background: var(--accent-soft); border-color: rgba(79,142,247,0.35);
  color: var(--accent);
}

/* ── Hero / Landing ── */
.hero-wrap {
  padding: 80px 60px 40px;
  background: radial-gradient(ellipse 70% 50% at 50% -10%, rgba(79,142,247,0.12) 0%, transparent 70%);
  text-align: center;
}
.hero-label {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 11px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 20px;
}
.hero-label-dot { width: 6px; height: 6px; background: var(--accent); border-radius: 50%; }
.hero-title {
  font-size: clamp(32px, 5vw, 52px); font-weight: 800;
  letter-spacing: -0.04em; line-height: 1.1;
  color: var(--text); margin-bottom: 14px;
}
.hero-title span { color: var(--accent); }
.hero-sub {
  font-size: 16px; color: var(--text-muted); max-width: 480px;
  margin: 0 auto 48px; line-height: 1.6; font-weight: 400;
}

/* ── Nav Cards ── */
.nav-cards {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 16px; max-width: 680px; margin: 0 auto 60px;
}
.nav-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 28px 28px;
  text-align: left; cursor: pointer; transition: all 0.25s;
  position: relative; overflow: hidden;
}
.nav-card::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, var(--accent-soft) 0%, transparent 60%);
  opacity: 0; transition: opacity 0.25s;
}
.nav-card:hover { border-color: rgba(79,142,247,0.35); transform: translateY(-2px); box-shadow: var(--shadow); }
.nav-card:hover::before { opacity: 1; }
.nav-card-icon {
  width: 40px; height: 40px; border-radius: var(--radius-sm);
  background: var(--accent-soft); border: 1px solid rgba(79,142,247,0.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; margin-bottom: 14px;
}
.nav-card-title {
  font-size: 15px; font-weight: 700; color: var(--text);
  margin-bottom: 6px; letter-spacing: -0.01em;
}
.nav-card-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }
.nav-card-arrow {
  position: absolute; right: 20px; top: 50%;
  transform: translateY(-50%); color: var(--text-muted);
  font-size: 18px; transition: all 0.2s;
}
.nav-card:hover .nav-card-arrow { color: var(--accent); transform: translateY(-50%) translateX(3px); }

/* ── Section Divider ── */
.section-sep {
  display: flex; align-items: center; gap: 16px;
  padding: 0 60px; margin-bottom: 20px;
}
.section-sep-line { flex: 1; height: 1px; background: var(--border); }
.section-sep-label {
  font-size: 11px; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--text-muted);
  white-space: nowrap;
}

/* ── Dashboard Embed Container ── */
.dash-container {
  margin: 0 60px 60px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius-lg); overflow: hidden;
  box-shadow: var(--shadow);
}
.dash-header {
  padding: 16px 24px; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: 10px;
}
.dash-header-dot { width: 8px; height: 8px; border-radius: 50%; }

/* ── Page Wrapper (subpages) ── */
.page-wrap { padding: 40px 60px 80px; }

/* ── Page Header ── */
.page-header {
  display: flex; align-items: flex-start; gap: 16px;
  margin-bottom: 36px; padding-bottom: 28px;
  border-bottom: 1px solid var(--border);
}
.page-header-icon {
  width: 48px; height: 48px; border-radius: var(--radius);
  background: var(--accent-soft); border: 1px solid rgba(79,142,247,0.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; flex-shrink: 0; margin-top: 2px;
}
.page-header-title {
  font-size: 26px; font-weight: 800; letter-spacing: -0.03em;
  color: var(--text); margin-bottom: 4px;
}
.page-header-sub { font-size: 13px; color: var(--text-muted); }
.back-btn {
  margin-left: auto; padding: 8px 16px;
  background: var(--surface-2); border: 1px solid var(--border);
  border-radius: var(--radius-sm); color: var(--text-muted);
  font-size: 12px; font-weight: 500; cursor: pointer;
  font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s;
  white-space: nowrap; align-self: flex-start;
}
.back-btn:hover { border-color: var(--border-mid); color: var(--text); }

/* ── Metric Card ── */
.metric-grid { display: grid; gap: 12px; margin-bottom: 28px; }
.metric-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px 22px;
  position: relative; overflow: hidden;
}
.metric-card::after {
  content: ''; position: absolute; top: 0; left: 0;
  right: 0; height: 2px;
}
.metric-card.blue::after  { background: var(--accent); }
.metric-card.green::after { background: var(--green); }
.metric-card.orange::after{ background: var(--orange); }
.metric-card.red::after   { background: var(--red); }
.metric-label { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 8px; }
.metric-value { font-size: 32px; font-weight: 800; letter-spacing: -0.04em; font-family: 'JetBrains Mono', monospace; }
.metric-card.blue .metric-value  { color: var(--accent); }
.metric-card.green .metric-value { color: var(--green); }
.metric-card.orange .metric-value{ color: var(--orange); }
.metric-card.red .metric-value   { color: var(--red); }

/* ── Filter Bar ── */
.filter-bar {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px 20px;
  margin-bottom: 20px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap;
}
.filter-label { font-size: 11px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--text-muted); }

/* ── Data Table ── */
.table-wrap {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); overflow: hidden; margin-bottom: 24px;
}
.table-header {
  padding: 14px 20px; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; justify-content: space-between;
}
.table-title { font-size: 13px; font-weight: 600; color: var(--text); }
.table-count {
  font-size: 11px; font-weight: 500;
  background: var(--accent-soft); color: var(--accent);
  padding: 3px 10px; border-radius: 20px;
  font-family: 'JetBrains Mono', monospace;
}

/* ── Progress Steps ── */
.steps-wrap {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); overflow: hidden; margin-bottom: 20px;
}
.step-row {
  display: flex; align-items: center; gap: 16px;
  padding: 12px 20px; border-bottom: 1px solid var(--border);
  transition: background 0.15s;
}
.step-row:last-child { border-bottom: none; }
.step-row:hover { background: var(--surface-2); }
.step-num {
  width: 28px; height: 28px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; flex-shrink: 0;
  font-family: 'JetBrains Mono', monospace;
}
.step-num.done   { background: var(--green-bg); color: var(--green); }
.step-num.active { background: var(--accent-soft); color: var(--accent); }
.step-num.idle   { background: var(--surface-2); color: var(--text-muted); }
.step-name { font-size: 13px; font-weight: 600; flex: 1; }
.step-dates { font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }
.step-badge {
  font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px;
}
.step-badge.done   { background: var(--green-bg); color: var(--green); }
.step-badge.active { background: var(--accent-soft); color: var(--accent); }
.step-badge.idle   { background: var(--surface-2); color: var(--text-muted); }

/* ── Progress Bar ── */
.prog-bar-wrap {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px 24px; margin-bottom: 24px;
}
.prog-bar-track { height: 6px; background: var(--surface-2); border-radius: 3px; overflow: hidden; margin: 10px 0 8px; }
.prog-bar-fill  { height: 100%; background: linear-gradient(90deg, var(--accent), #7CB9FF); border-radius: 3px; transition: width 0.6s ease; }
.prog-bar-meta  { display: flex; justify-content: space-between; font-size: 12px; }

/* ── Status Badge ── */
.status-badge { display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; }
.status-badge.open   { background: var(--orange-bg); color: var(--orange); }
.status-badge.close  { background: var(--green-bg); color: var(--green); }
.status-badge.failed { background: var(--red-bg); color: var(--red); }
.status-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; }

/* ── Rec Room ── */
.rec-section {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius-lg); margin-bottom: 20px; overflow: hidden;
}
.rec-section-header {
  padding: 16px 22px; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: 10px;
}
.rec-section-icon {
  width: 32px; height: 32px; border-radius: var(--radius-sm);
  background: var(--accent-soft); display: flex; align-items: center; justify-content: center;
  font-size: 15px; flex-shrink: 0;
}
.rec-section-title { font-size: 14px; font-weight: 700; }
.rec-section-body { padding: 22px; }

/* ── Link Grid ── */
.link-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.link-card {
  background: var(--surface-2); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px 18px;
  display: flex; align-items: center; gap: 12px;
  text-decoration: none; transition: all 0.2s;
}
.link-card:hover { border-color: rgba(79,142,247,0.35); background: var(--accent-soft); transform: translateY(-1px); }
.link-card-icon { font-size: 20px; flex-shrink: 0; }
.link-card-label { font-size: 13px; font-weight: 600; color: var(--text); }
.link-card-sub   { font-size: 11px; color: var(--text-muted); margin-top: 2px; }

/* ── Input Field ── */
.inp-label { font-size: 11px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 6px; }
.inp-field {
  width: 100%; padding: 10px 14px;
  background: var(--surface-2); border: 1px solid var(--border);
  border-radius: var(--radius-sm); color: var(--text);
  font-size: 13px; font-family: 'JetBrains Mono', monospace;
  outline: none; transition: all 0.2s;
}
.inp-field:focus { border-color: rgba(79,142,247,0.5); box-shadow: 0 0 0 3px rgba(79,142,247,0.1); }

/* ── Buttons ── */
.btn-primary {
  padding: 10px 20px; border-radius: var(--radius-sm);
  background: var(--accent); border: none; color: #fff;
  font-size: 13px; font-weight: 600; cursor: pointer;
  font-family: 'Plus Jakarta Sans', sans-serif;
  transition: all 0.2s; box-shadow: 0 2px 12px rgba(79,142,247,0.3);
  display: inline-flex; align-items: center; gap: 7px;
}
.btn-primary:hover { background: #6BA4FF; box-shadow: 0 4px 16px rgba(79,142,247,0.45); }
.btn-ghost {
  padding: 10px 20px; border-radius: var(--radius-sm);
  background: var(--surface-2); border: 1px solid var(--border);
  color: var(--text-dim); font-size: 13px; font-weight: 500; cursor: pointer;
  font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s;
  display: inline-flex; align-items: center; gap: 7px;
}
.btn-ghost:hover { border-color: var(--border-mid); color: var(--text); }

/* ── Streamlit widget overrides ── */
.stRadio > div { flex-direction: row !important; gap: 8px !important; }
.stRadio label { background: var(--surface-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-sm) !important; padding: 7px 16px !important; font-size: 13px !important; font-weight: 500 !important; cursor: pointer !important; transition: all 0.2s !important; color: var(--text-muted) !important; }
.stRadio label:has(input:checked) { background: var(--accent-soft) !important; border-color: rgba(79,142,247,0.4) !important; color: var(--accent) !important; }
div[data-testid="stSelectbox"] > div > div { background: var(--surface-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-sm) !important; color: var(--text) !important; }
div[data-testid="stDataFrame"] { border-radius: var(--radius) !important; overflow: hidden !important; border: 1px solid var(--border) !important; }
div[data-testid="stDataFrame"] iframe { border-radius: var(--radius) !important; }
div[data-testid="metric-container"] { background: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: var(--radius) !important; padding: 16px 20px !important; }
div[data-testid="metric-container"] label { color: var(--text-muted) !important; font-size: 11px !important; font-weight: 600 !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] { color: var(--text) !important; font-family: 'JetBrains Mono', monospace !important; font-size: 28px !important; font-weight: 700 !important; }
.stProgress > div > div { background: var(--surface-2) !important; border-radius: 3px !important; }
.stProgress > div > div > div { background: linear-gradient(90deg, var(--accent), #7CB9FF) !important; border-radius: 3px !important; }
.stTextInput > div > div { background: var(--surface-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-sm) !important; color: var(--text) !important; }
.stTextInput > div > div > input { color: var(--text) !important; font-family: 'JetBrains Mono', monospace !important; }
.stTextArea > div > div { background: var(--surface-2) !important; border: 1px solid var(--border) !important; border-radius: var(--radius-sm) !important; }
.stTextArea textarea { color: var(--text) !important; font-family: 'JetBrains Mono', monospace !important; font-size: 12px !important; }
div[data-testid="stExpander"] { background: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: var(--radius) !important; }
div[data-testid="stExpander"] summary { color: var(--text) !important; font-weight: 600 !important; }
button[kind="primary"], button[kind="secondary"] {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-weight: 600 !important; border-radius: var(--radius-sm) !important;
}
button[kind="primary"] { background: var(--accent) !important; border: none !important; }
button[kind="secondary"] { background: var(--surface-2) !important; border: 1px solid var(--border) !important; color: var(--text) !important; }
.stInfo, .stSuccess, .stWarning, .stError {
  border-radius: var(--radius-sm) !important;
  font-size: 13px !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"

# ─────────────────────────────────────────────
# TOPBAR (always visible)
# ─────────────────────────────────────────────
page_map = {"home": "Home", "tracking": "Tracking", "rec_room": "Rec Room"}

st.markdown(f"""
<div class="topbar">
  <div class="topbar-brand">
    <div class="topbar-dot"></div>
    HR System Portal
  </div>
  <div style="display:flex;align-items:center;gap:10px;">
    <span class="topbar-badge">Centralized v2</span>
    <span style="font-size:12px;color:var(--text-muted);">{datetime.now().strftime('%d %b %Y')}</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ① HOME PAGE
# ─────────────────────────────────────────────
def run_home():
    # Hero
    st.markdown("""
    <div class="hero-wrap">
      <div class="hero-label"><div class="hero-label-dot"></div>HR Centralized System</div>
      <div class="hero-title">Recruitment <span>Intelligence</span><br>at Your Fingertips</div>
      <div class="hero-sub">One platform for dashboards, candidate tracking, and recruitment operations.</div>
    </div>
    """, unsafe_allow_html=True)

    # Nav Cards — using Streamlit columns for button functionality
    st.markdown('<div style="max-width:680px;margin:0 auto 48px;">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;margin-bottom:4px;">
          <div style="width:40px;height:40px;border-radius:8px;background:var(--accent-soft);border:1px solid rgba(79,142,247,0.2);display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:14px;">🔍</div>
          <div style="font-size:15px;font-weight:700;color:var(--text);margin-bottom:6px;">Tracking System</div>
          <div style="font-size:12px;color:var(--text-muted);line-height:1.6;">Monitor candidate progress & pipeline status by position or individual.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Tracking →", key="btn_tracking", use_container_width=True):
            st.session_state.page = "tracking"
            st.rerun()

    with c2:
        st.markdown("""
        <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;margin-bottom:4px;">
          <div style="width:40px;height:40px;border-radius:8px;background:var(--accent-soft);border:1px solid rgba(79,142,247,0.2);display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:14px;">🏠</div>
          <div style="font-size:15px;font-weight:700;color:var(--text);margin-bottom:6px;">Recruitment Room</div>
          <div style="font-size:12px;color:var(--text-muted);line-height:1.6;">Access forms, spreadsheets, and recruitment tools in one workspace.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Rec Room →", key="btn_recroom", use_container_width=True):
            st.session_state.page = "rec_room"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Dashboard Section Divider
    st.markdown("""
    <div class="section-sep">
      <div class="section-sep-line"></div>
      <div class="section-sep-label">📊 Recruitment Dashboard · Looker Studio</div>
      <div class="section-sep-line"></div>
    </div>
    """, unsafe_allow_html=True)

    # Looker Embed
    st.markdown("""
    <div class="dash-container">
      <div class="dash-header">
        <div class="dash-header-dot" style="background:#F87171;"></div>
        <div class="dash-header-dot" style="background:#F59E0B;"></div>
        <div class="dash-header-dot" style="background:#34D399;"></div>
        <span style="margin-left:8px;font-size:12px;color:var(--text-muted);font-weight:500;">Recruitment Dashboard — Live Data</span>
      </div>
      <iframe
        width="100%" height="750"
        src="https://datastudio.google.com/embed/reporting/a425625f-0af4-4b5c-8826-218a929b1333/page/YwLxF"
        frameborder="0" style="border:0;display:block;" allowfullscreen>
      </iframe>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ② TRACKING SYSTEM
# ─────────────────────────────────────────────
def run_tracking():
    import streamlit.components.v1 as components

    # Header
    col_hdr, col_back = st.columns([6, 1])
    with col_hdr:
        st.markdown("""
        <div style="padding:40px 60px 0;">
          <div class="page-header" style="margin-bottom:0;">
            <div class="page-header-icon">🔍</div>
            <div>
              <div class="page-header-title">Tracking System</div>
              <div class="page-header-sub">Monitor candidate pipeline in real-time</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_back:
        st.markdown('<div style="padding-top:44px;padding-right:60px;">', unsafe_allow_html=True)
        if st.button("← Back to Home", key="back_track"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div style="padding:20px 60px 80px;">', unsafe_allow_html=True)

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

    # Search Mode Toggle
    mode = st.radio("Search Mode", ["By Position", "By Candidate"], horizontal=True, key="m_track")

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # ── BY POSITION ──────────────────────────────────────
    if mode == "By Position":
        pos_list = sorted(df["position_name"].dropna().unique())
        sel_pos = st.selectbox("Select Position", pos_list, key="s_pos")
        filtered = df[df["position_name"] == sel_pos].copy()

        # Metrics
        if "status1" in filtered.columns:
            status_s = filtered["status1"].str.upper()
            total = len(filtered)
            open_c = (status_s == "OPEN").sum()
            close_c = (status_s == "CLOSE").sum()
            failed_c = (status_s == "FAILED").sum()

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Candidates", total)
            m2.metric("🟠 On-Progress", int(open_c))
            m3.metric("🟢 Hired", int(close_c))
            m4.metric("🔴 Failed", int(failed_c))

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        # Table
        cols_to_show = [c for c in ["candidate_id", "position_name", "departement", "level", "loc", "last_progress", "total_lt", "status1"] if c in filtered.columns]
        disp = filtered[cols_to_show].copy()
        if "total_lt" in disp.columns:
            disp["total_lt"] = pd.to_numeric(disp["total_lt"], errors="coerce").fillna(0).astype(int)
        if "status1" in disp.columns:
            disp = disp.rename(columns={"status1": "Hiring Status"})

        def color_status(val):
            v = str(val).upper()
            if v == "OPEN":   return "color: #F59E0B; font-weight: 700;"
            if v == "FAILED": return "color: #F87171; font-weight: 700;"
            if v == "CLOSE":  return "color: #34D399; font-weight: 700;"
            return ""

        st.dataframe(
            disp.style.map(color_status, subset=["Hiring Status"]) if "Hiring Status" in disp.columns else disp,
            use_container_width=True,
            height=360,
        )

    # ── BY CANDIDATE ──────────────────────────────────────
    else:
        cand_list = sorted(df["candidate_id"].dropna().unique())
        sel_cand = st.selectbox("Select Candidate ID", cand_list, key="s_cand")
        filt = df[df["candidate_id"] == sel_cand]
        if filt.empty:
            st.warning("No data found for this candidate.")
            st.markdown("</div>", unsafe_allow_html=True)
            return
        row = filt.iloc[0]

        # Candidate header
        h_st = str(row.get("status1", "Unknown")).upper()
        badge_class = {"OPEN": "open", "CLOSE": "close", "FAILED": "failed"}.get(h_st, "open")
        badge_label = {"OPEN": "● On Progress", "CLOSE": "● Hired", "FAILED": "● Failed"}.get(h_st, "● Unknown")

        st.markdown(f"""
        <div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px 28px;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
          <div>
            <div style="font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:var(--text-muted);margin-bottom:4px;">Candidate</div>
            <div style="font-size:22px;font-weight:800;letter-spacing:-0.02em;">{sel_cand}</div>
          </div>
          <span class="status-badge {badge_class}"><span class="status-badge-dot"></span>{badge_label}</span>
        </div>
        """, unsafe_allow_html=True)

        # Metrics row
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Position",   row.get("position_name", "—"))
        m2.metric("Department", row.get("departement", "—"))
        m3.metric("Level",      row.get("level", "—"))
        m4.metric("Location",   row.get("loc", "—"))
        sla = row.get("total_lt", "—")
        if isinstance(sla, float): sla = int(sla)
        m5.metric("SLA (days)", sla)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # Recruitment steps
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
                "name": name, "start": str(s_val) if has_start else "—",
                "end": str(e_val) if has_end else "—", "status": status
            })

        prog_pct = done_count / len(steps)

        # Progress bar
        st.markdown(f"""
        <div class="prog-bar-wrap">
          <div class="prog-bar-meta">
            <span style="font-size:13px;font-weight:700;">Recruitment Progress</span>
            <span style="font-size:12px;color:var(--text-muted);font-family:'JetBrains Mono',monospace;">{done_count}/{len(steps)} stages complete</span>
          </div>
          <div class="prog-bar-track">
            <div class="prog-bar-fill" style="width:{prog_pct*100:.0f}%;"></div>
          </div>
          <div class="prog-bar-meta">
            <span style="font-size:11px;color:var(--text-muted);">Progress</span>
            <span style="font-size:12px;font-weight:700;color:var(--accent);">{prog_pct*100:.0f}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Steps
        steps_html = '<div class="steps-wrap">'
        for i, s in enumerate(p_data):
            cls = s["status"]
            icon = "✓" if cls == "done" else str(i + 1)
            badge_txt = {"done": "Done", "active": "In Progress", "idle": "Not Started"}[cls]
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
    import streamlit.components.v1 as components

    # Header
    col_hdr, col_back = st.columns([6, 1])
    with col_hdr:
        st.markdown("""
        <div style="padding:40px 60px 0;">
          <div class="page-header" style="margin-bottom:0;">
            <div class="page-header-icon">🏠</div>
            <div>
              <div class="page-header-title">Recruitment Room</div>
              <div class="page-header-sub">Forms, spreadsheets, and tools — all in one place</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_back:
        st.markdown('<div style="padding-top:44px;padding-right:60px;">', unsafe_allow_html=True)
        if st.button("← Back to Home", key="back_rec"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div style="padding:20px 60px 80px;">', unsafe_allow_html=True)

    # ── SECTION 1: RECRUITMENT FORM (AppScript Embed) ──
    st.markdown("""
    <div class="rec-section">
      <div class="rec-section-header">
        <div class="rec-section-icon">📋</div>
        <div>
          <div class="rec-section-title">Recruitment Form</div>
          <div style="font-size:11px;color:var(--text-muted);margin-top:2px;">Powered by Google Apps Script</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    # AppScript URL Input
    apps_url = st.text_input(
        "AppScript Web App URL",
        placeholder="https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec",
        key="apps_url",
        label_visibility="visible",
        help="Paste the deployed URL of your Google Apps Script Web App here."
    )

    if apps_url and apps_url.startswith("https://"):
        st.markdown(f"""
        <div style="margin-top:16px;background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;">
          <div style="padding:10px 16px;border-bottom:1px solid var(--border);display:flex;gap:8px;align-items:center;">
            <div style="width:10px;height:10px;border-radius:50%;background:#F87171;"></div>
            <div style="width:10px;height:10px;border-radius:50%;background:#F59E0B;"></div>
            <div style="width:10px;height:10px;border-radius:50%;background:#34D399;"></div>
            <span style="margin-left:6px;font-size:11px;color:var(--text-muted);">Recruitment Form</span>
          </div>
          <iframe src="{apps_url}" width="100%" height="750" frameborder="0" style="border:none;display:block;"></iframe>
        </div>
        """, unsafe_allow_html=True)
    elif apps_url:
        st.warning("Please enter a valid URL starting with https://")
    else:
        st.markdown("""
        <div style="background:var(--surface-2);border:1px solid var(--border);border:1px dashed rgba(79,142,247,0.3);border-radius:var(--radius);padding:48px;text-align:center;">
          <div style="font-size:32px;margin-bottom:12px;">📋</div>
          <div style="font-size:14px;font-weight:600;color:var(--text);margin-bottom:6px;">No Form Connected</div>
          <div style="font-size:12px;color:var(--text-muted);">Paste your Apps Script URL above to embed the recruitment form here.</div>
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
          <div style="font-size:11px;color:var(--text-muted);margin-top:2px;">Spreadsheets & connected resources</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    # Spreadsheet Links
    st.markdown("**Spreadsheet Links**")
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # Initialize session state for links
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
                st.markdown(f'<script>window.open("{link["url"]}", "_blank");</script>', unsafe_allow_html=True)
        st.session_state.rec_links[i]["label"] = new_label
        st.session_state.rec_links[i]["url"] = new_url

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
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
          <div style="font-size:11px;color:var(--text-muted);margin-top:2px;">Shortcuts to common tasks</div>
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

    # ── SECTION 4: NOTES ──
    st.markdown("""
    <div class="rec-section">
      <div class="rec-section-header">
        <div class="rec-section-icon">📝</div>
        <div>
          <div class="rec-section-title">Team Notes</div>
          <div style="font-size:11px;color:var(--text-muted);margin-top:2px;">Shared notes for the recruitment team</div>
        </div>
      </div>
      <div class="rec-section-body">
    """, unsafe_allow_html=True)

    if "rec_notes" not in st.session_state:
        st.session_state.rec_notes = ""

    st.session_state.rec_notes = st.text_area(
        "Notes",
        value=st.session_state.rec_notes,
        height=140,
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
