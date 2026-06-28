"""
HR Recruitment Portal — PT Dharma Henwa
v6: Full redesign — clean, professional, inspired by career.ptdh.co.id
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="PTDH HR Portal",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GITHUB_RAW = "https://raw.githubusercontent.com/naviantar-ptdh/202605-centralized/main"
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbytQh3jy8-MQ6UUHXmxOIAkx3au6SwgmXZM1NlN1iaP9GQaGCFOEqMy9QgrLwFeXHLs/exec"

# ── Colour tokens (mirrors career.ptdh.co.id visual DNA) ──
OR   = "#E8440A"
OR_L = "#FFF0EB"
OR_M = "#FFD0BD"
BK   = "#111111"
GY1  = "#FAFAFA"   # page bg
GY2  = "#F4F4F5"   # surface
GY3  = "#E4E4E7"   # border
GY4  = "#A1A1AA"   # muted text
TX   = "#18181B"   # primary text
TX2  = "#52525B"   # secondary text
GR   = "#16A34A"
GR_L = "#F0FDF4"
GR_M = "#BBF7D0"
RD   = "#DC2626"
RD_L = "#FEF2F2"
RD_M = "#FECACA"
AM   = "#D97706"
AM_L = "#FFFBEB"
AM_M = "#FDE68A"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html, body, .stApp {{
  font-family: 'Inter', -apple-system, sans-serif !important;
  background: {GY1} !important;
  color: {TX} !important;
}}

#MainMenu, footer, header, .stDeployButton {{ display: none !important; }}
.block-container, .stMainBlockContainer {{
  padding: 0 !important;
  max-width: 100% !important;
}}
[data-testid="stAppViewBlockContainer"] {{ padding: 0 !important; }}
.element-container {{ margin: 0 !important; }}

::-webkit-scrollbar {{ width: 5px; height: 5px; }}
::-webkit-scrollbar-track {{ background: {GY2}; }}
::-webkit-scrollbar-thumb {{ background: {GY3}; border-radius: 999px; }}

/* ── Top Navigation Bar ── */
.nav {{
  height: 60px;
  background: #fff;
  border-bottom: 1px solid {GY3};
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  position: sticky;
  top: 0;
  z-index: 999;
}}
.nav-brand {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.nav-divider {{
  width: 1px;
  height: 22px;
  background: {GY3};
}}
.nav-title {{
  font-size: 13px;
  font-weight: 600;
  color: {TX2};
  letter-spacing: -0.01em;
}}
.nav-right {{
  display: flex;
  align-items: center;
  gap: 16px;
}}
.nav-date {{
  font-size: 12px;
  color: {GY4};
}}
.nav-live {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 600;
  color: {GR};
  background: {GR_L};
  border: 1px solid {GR_M};
  padding: 4px 12px;
  border-radius: 999px;
  letter-spacing: 0.02em;
}}
.nav-live-dot {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: {GR};
  animation: blink 2s ease-in-out infinite;
}}
@keyframes blink {{
  0%, 100% {{ opacity: 1; }}
  50% {{ opacity: 0.3; }}
}}

/* ── Page wrapper ── */
.page {{
  max-width: 1160px;
  margin: 0 auto;
  padding: 40px 32px 80px;
}}

/* ── Page header ── */
.page-header {{
  margin-bottom: 32px;
}}
.page-eyebrow {{
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: {OR};
  margin-bottom: 6px;
}}
.page-title {{
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: {TX};
  margin: 0 0 6px 0;
}}
.page-subtitle {{
  font-size: 13.5px;
  color: {TX2};
  line-height: 1.6;
  margin: 0;
}}

/* ── Divider ── */
.divider {{
  height: 1px;
  background: {GY3};
  margin: 24px 0;
}}

/* ── Section label ── */
.section-label {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: {GY4};
  margin: 0 0 14px;
  display: flex;
  align-items: center;
  gap: 10px;
}}
.section-label::after {{
  content: '';
  flex: 1;
  height: 1px;
  background: {GY3};
}}

/* ── Nav Cards (Home) ── */
.nav-card {{
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 14px;
  padding: 28px;
  transition: box-shadow 0.15s, border-color 0.15s;
  position: relative;
  overflow: hidden;
}}
.nav-card:hover {{
  border-color: {OR_M};
  box-shadow: 0 4px 24px rgba(232,68,10,.08);
}}
.nav-card-top-stripe {{
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: {OR};
  border-radius: 14px 14px 0 0;
}}
.nav-card-icon {{
  width: 44px;
  height: 44px;
  background: {OR_L};
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  margin-bottom: 16px;
}}
.nav-card-title {{
  font-size: 15px;
  font-weight: 700;
  color: {TX};
  margin-bottom: 6px;
}}
.nav-card-desc {{
  font-size: 13px;
  color: {TX2};
  line-height: 1.65;
}}
.nav-card-cta {{
  margin-top: 18px;
  font-size: 12px;
  font-weight: 600;
  color: {OR};
  display: flex;
  align-items: center;
  gap: 4px;
}}

/* ── Dashboard frame ── */
.dash-frame {{
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 32px;
}}
.dash-frame-header {{
  padding: 14px 20px;
  border-bottom: 1px solid {GY3};
  background: {GY2};
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.dash-frame-title {{
  font-size: 12.5px;
  font-weight: 600;
  color: {TX2};
  display: flex;
  align-items: center;
  gap: 8px;
}}
.dash-frame-dots {{
  display: flex;
  gap: 5px;
}}
.dash-frame-dots span {{
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: block;
}}

/* ── Candidate Hero Card ── */
.cand-hero {{
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 14px;
  padding: 24px 28px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.cand-hero-left {{}}
.cand-hero-label {{
  font-size: 10.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: {GY4};
  margin-bottom: 4px;
}}
.cand-hero-id {{
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: {TX};
}}

/* ── Info Grid ── */
.info-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-bottom: 16px;
}}
.info-item {{
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 10px;
  padding: 14px 16px;
}}
.info-label {{
  font-size: 10.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: {GY4};
  margin-bottom: 4px;
}}
.info-val {{
  font-size: 13px;
  font-weight: 600;
  color: {TX};
}}

/* ── Progress bar ── */
.prog-wrap {{
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 12px;
  padding: 18px 22px;
  margin-bottom: 16px;
}}
.prog-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}}
.prog-label {{
  font-size: 13px;
  font-weight: 600;
  color: {TX};
}}
.prog-count {{
  font-size: 12px;
  color: {GY4};
}}
.prog-track {{
  height: 6px;
  background: {GY3};
  border-radius: 999px;
  overflow: hidden;
  margin-bottom: 8px;
}}
.prog-pct {{
  font-size: 12px;
  font-weight: 700;
  color: {OR};
  text-align: right;
}}

/* ── Metrics ── */
div[data-testid="metric-container"] {{
  background: #fff !important;
  border: 1px solid {GY3} !important;
  border-radius: 10px !important;
  padding: 16px 18px !important;
}}
div[data-testid="metric-container"] label {{
  font-size: 10.5px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.07em !important;
  color: {GY4} !important;
}}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {{
  font-size: 26px !important;
  font-weight: 700 !important;
  color: {TX} !important;
  letter-spacing: -0.02em !important;
}}

/* ── Radio pills ── */
.stRadio > div {{
  flex-direction: row !important;
  gap: 6px !important;
  flex-wrap: wrap !important;
}}
.stRadio label {{
  background: #fff !important;
  border: 1px solid {GY3} !important;
  border-radius: 8px !important;
  padding: 7px 18px !important;
  font-size: 12.5px !important;
  font-weight: 500 !important;
  cursor: pointer !important;
  color: {TX2} !important;
  transition: all 0.15s !important;
}}
.stRadio label:has(input:checked) {{
  background: {OR_L} !important;
  border-color: {OR_M} !important;
  color: {OR} !important;
  font-weight: 600 !important;
}}

/* ── Selectbox ── */
div[data-testid="stSelectbox"] > div > div {{
  background: #fff !important;
  border: 1px solid {GY3} !important;
  border-radius: 8px !important;
  color: {TX} !important;
  font-size: 13px !important;
}}

/* ── Buttons ── */
button[kind="primary"] {{
  background: {OR} !important;
  border: none !important;
  color: #fff !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 600 !important;
  font-size: 13px !important;
  border-radius: 8px !important;
  letter-spacing: -0.01em !important;
  transition: opacity 0.15s !important;
}}
button[kind="primary"]:hover {{ opacity: 0.88 !important; }}
button[kind="secondary"] {{
  background: #fff !important;
  border: 1px solid {GY3} !important;
  color: {TX2} !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 500 !important;
  font-size: 13px !important;
  border-radius: 8px !important;
}}
button[kind="secondary"]:hover {{
  border-color: {GY4} !important;
  color: {TX} !important;
}}

/* ── Dataframe ── */
div[data-testid="stDataFrame"] {{
  border-radius: 10px !important;
  border: 1px solid {GY3} !important;
  overflow: hidden !important;
}}

/* ── Panel (Rec Room sections) ── */
.panel {{
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 14px;
  margin-bottom: 20px;
  overflow: hidden;
}}
.panel-header {{
  padding: 14px 20px;
  border-bottom: 1px solid {GY3};
  display: flex;
  align-items: center;
  gap: 10px;
}}
.panel-icon {{
  font-size: 16px;
  color: {OR};
  width: 32px;
  height: 32px;
  background: {OR_L};
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.panel-title {{
  font-size: 13.5px;
  font-weight: 700;
  color: {TX};
}}
.panel-subtitle {{
  font-size: 11.5px;
  color: {GY4};
  margin-top: 1px;
}}
.panel-body {{
  padding: 20px;
}}

/* ── Steps table ── */
.steps-table {{
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border: 1px solid {GY3};
  border-radius: 12px;
  overflow: hidden;
  font-size: 12.5px;
}}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"


# ── Top Nav ──
st.markdown(f"""
<div class="nav">
  <div class="nav-brand">
    <img src="{GITHUB_RAW}/logo_putih.png"
         style="height:28px;width:auto;filter:brightness(0);"
         onerror="this.style.display='none'" alt="PTDH Logo"/>
    <div class="nav-divider"></div>
    <span class="nav-title">HR Recruitment Portal</span>
  </div>
  <div class="nav-right">
    <span class="nav-date">{datetime.now().strftime('%d %B %Y')}</span>
    <span class="nav-live">
      <span class="nav-live-dot"></span>Live
    </span>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════
def badge(text, bg, fg):
    return (f'<span style="display:inline-flex;align-items:center;padding:3px 12px;'
            f'border-radius:999px;background:{bg};color:{fg};font-size:11px;font-weight:600;">'
            f'{text}</span>')

def _status_cfg(cls):
    return {
        "done":   (GR_L,  GR,  GR_M),
        "failed": (RD_L,  RD,  RD_M),
        "active": (OR_L,  OR,  OR_M),
        "idle":   (GY2,   GY4, GY3),
    }.get(cls, (GY2, GY4, GY3))

def _steps_table(p_data):
    TH = (f"font-size:10.5px;font-weight:600;text-transform:uppercase;letter-spacing:.07em;"
          f"color:{GY4};padding:10px 14px;text-align:left;border-bottom:1px solid {GY3};"
          f"background:{GY2};white-space:nowrap;")
    t = (f'<table style="width:100%;border-collapse:collapse;background:#fff;'
         f'border:1px solid {GY3};border-radius:12px;overflow:hidden;font-size:12.5px;">'
         f'<thead><tr>'
         f'<th style="{TH}width:44px;padding:10px 4px 10px 16px;"></th>'
         f'<th style="{TH}">Stage</th>'
         f'<th style="{TH}width:130px;">Status</th>'
         f'<th style="{TH}width:210px;">Start → End</th>'
         f'<th style="{TH}width:140px;">LT / Budget</th>'
         f'<th style="{TH}width:90px;padding-right:16px;">SLA</th>'
         f'</tr></thead><tbody>')

    for i, s in enumerate(p_data):
        cls = s["status"]
        bg, fg, bd = _status_cfg(cls)
        icon_map = {"done": "✓", "failed": "✕", "active": str(s["idx"]+1), "idle": str(s["idx"]+1)}
        icon = icon_map.get(cls, str(s["idx"]+1))
        badge_map = {"done": "Done", "failed": "Failed Here", "active": "In Progress", "idle": "Pending"}
        badge_txt = badge_map.get(cls, "—")
        row_bg = "#fff" if i % 2 == 0 else GY1
        bb = f"border-bottom:1px solid {GY3};" if i < len(p_data) - 1 else ""

        name_color = RD if cls == "failed" else TX
        name_weight = "700" if cls == "failed" else "600"

        # LT cell
        lt_a = s["lt_actual"]
        lt_b = s["lt_budget"]
        sla = (s["sla"] or "").lower()
        if lt_a is None:
            lt_chip = (f'<span style="display:inline-block;padding:3px 10px;border-radius:999px;'
                       f'background:{GY2};color:{GY4};font-size:11px;font-weight:500;">'
                       f'{"—" if cls == "idle" else "In progress"}</span>')
        else:
            c_bg = GR_L if "ontime" in sla else (RD_L if "late" in sla else GY2)
            c_fg = GR   if "ontime" in sla else (RD   if "late" in sla else GY4)
            bpart = f" / {lt_b}d" if lt_b else ""
            lt_chip = (f'<span style="display:inline-block;padding:3px 10px;border-radius:999px;'
                       f'background:{c_bg};color:{c_fg};font-size:11px;font-weight:600;">'
                       f'{lt_a}d{bpart}</span>')

        # SLA cell
        if "ontime" in sla:
            s_bg, s_fg, s_lbl = GR_L, GR, "On time"
        elif "late" in sla:
            s_bg, s_fg, s_lbl = RD_L, RD, "Late"
        else:
            s_bg, s_fg, s_lbl = GY2, GY4, s["sla"] or "—"
        sla_chip = (f'<span style="display:inline-block;padding:3px 10px;border-radius:999px;'
                    f'background:{s_bg};color:{s_fg};font-size:11px;font-weight:600;">'
                    f'{s_lbl}</span>')

        t += (
            f'<tr style="background:{row_bg};{bb}">'
            # circle
            f'<td style="width:44px;padding:10px 4px 10px 16px;vertical-align:middle;">'
            f'<span style="display:inline-flex;align-items:center;justify-content:center;'
            f'width:26px;height:26px;border-radius:50%;background:{bg};color:{fg};'
            f'font-size:11px;font-weight:700;border:1px solid {bd};">{icon}</span></td>'
            # name
            f'<td style="padding:10px 14px;vertical-align:middle;font-weight:{name_weight};color:{name_color};">{s["name"]}</td>'
            # status badge
            f'<td style="padding:10px 14px;vertical-align:middle;">'
            f'<span style="display:inline-block;padding:3px 12px;border-radius:999px;'
            f'background:{bg};color:{fg};font-size:11px;font-weight:600;">{badge_txt}</span></td>'
            # start → end
            f'<td style="padding:10px 14px;vertical-align:middle;font-size:11.5px;color:{TX2};">'
            f'{s["start"]}<br>→ {s["end"]}</td>'
            # LT
            f'<td style="padding:10px 14px;vertical-align:middle;">{lt_chip}</td>'
            # SLA
            f'<td style="padding:10px 16px 10px 14px;vertical-align:middle;">{sla_chip}</td>'
            f'</tr>'
        )
    t += '</tbody></table>'
    return t


# ══════════════════════════════════════════
# ① HOME
# ══════════════════════════════════════════
def run_home():
    st.markdown('<div class="page">', unsafe_allow_html=True)

    # Hero / Page Header
    st.markdown(f"""
    <div class="page-header">
      <div class="page-eyebrow">PT Dharma Henwa — Internal</div>
      <h1 class="page-title">Recruitment Overview</h1>
      <p class="page-subtitle">Monitor pipeline metrics, track candidates, and manage recruitment workflows.</p>
    </div>
    """, unsafe_allow_html=True)

    # Dashboard embed
    st.markdown('<div class="section-label">Live Analytics</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="dash-frame">
      <div class="dash-frame-header">
        <div class="dash-frame-title">
          <span style="width:7px;height:7px;border-radius:50%;background:{GR};display:inline-block;
            box-shadow:0 0 5px {GR};animation:blink 2s ease-in-out infinite;"></span>
          Looker Studio — Recruitment Dashboard
        </div>
        <div class="dash-frame-dots">
          <span style="background:#FF5F57;"></span>
          <span style="background:#FFBD2E;"></span>
          <span style="background:#28CA41;"></span>
        </div>
      </div>
      <iframe width="100%" height="680"
        src="https://datastudio.google.com/embed/reporting/a425625f-0af4-4b5c-8826-218a929b1333/page/YwLxF"
        frameborder="0" style="border:0;display:block;" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # Tool Cards
    st.markdown('<div class="section-label" style="margin-top:32px;">Recruitment Tools</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown(f"""
        <div class="nav-card">
          <div class="nav-card-top-stripe"></div>
          <div class="nav-card-icon">🔍</div>
          <div class="nav-card-title">Candidate Tracking</div>
          <div class="nav-card-desc">Monitor individual candidate progress and view their full recruitment pipeline — stage by stage.</div>
          <div class="nav-card-cta">Open Tracking →</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Open Candidate Tracking", key="btn_tracking", use_container_width=True, type="primary"):
            st.session_state.page = "tracking"
            st.rerun()

    with c2:
        st.markdown(f"""
        <div class="nav-card">
          <div class="nav-card-top-stripe"></div>
          <div class="nav-card-icon">📋</div>
          <div class="nav-card-title">Recruitment Room</div>
          <div class="nav-card-desc">Submit and manage recruitment forms, access spreadsheets, and use quick actions — all in one workspace.</div>
          <div class="nav-card-cta">Open Room →</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Open Recruitment Room", key="btn_recroom", use_container_width=True, type="primary"):
            st.session_state.page = "rec_room"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════
# ② TRACKING
# ══════════════════════════════════════════
def run_tracking():
    st.markdown('<div class="page">', unsafe_allow_html=True)

    col_h, col_b = st.columns([5, 1])
    with col_h:
        st.markdown(f"""
        <div class="page-header" style="margin-bottom:20px;">
          <div class="page-eyebrow">Recruitment</div>
          <h1 class="page-title">Candidate Tracking</h1>
          <p class="page-subtitle">Monitor pipeline status and stage-by-stage progress in real time.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("<div style='padding-top:40px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_track"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    @st.cache_data(ttl=60)
    def load_data():
        url = "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc/export?format=csv"
        try:
            df = pd.read_csv(url)
            df.columns = df.columns.str.lower().str.strip()
            for c in ["candidate_id", "position_name", "departement", "level", "loc", "status1"]:
                if c in df.columns:
                    df[c] = df[c].fillna("Unknown")
            return df, None
        except Exception as e:
            return None, str(e)

    df, err = load_data()
    if err:
        st.error(f"Failed to load data: {err}")
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
            m1.metric("Total", len(filtered))
            m2.metric("On Progress", int((su == "OPEN").sum()))
            m3.metric("Hired", int((su == "CLOSE").sum()))
            m4.metric("Failed", int((su == "FAILED").sum()))

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
        cols = [c for c in ["candidate_id", "position_name", "departement", "level", "loc", "last_progress", "tot_lt", "status1"] if c in filtered.columns]
        disp = filtered[cols].copy()
        if "tot_lt" in disp.columns:
            disp["tot_lt"] = pd.to_numeric(disp["tot_lt"], errors="coerce").fillna(0).astype(int)
        if "status1" in disp.columns:
            disp = disp.rename(columns={"status1": "Status", "tot_lt": "Total LT (days)"})

        def color_st(val):
            v = str(val).upper()
            if v == "OPEN":   return f"color:{AM};font-weight:600;"
            if v == "FAILED": return f"color:{RD};font-weight:600;"
            if v == "CLOSE":  return f"color:{GR};font-weight:600;"
            return ""

        st.dataframe(
            disp.style.map(color_st, subset=["Status"]) if "Status" in disp.columns else disp,
            use_container_width=True, height=380
        )

    # ── BY CANDIDATE ──
    else:
        cand_list = sorted(df["candidate_id"].dropna().unique())
        sel_cand = st.selectbox("Select Candidate ID", cand_list, key="s_cand")
        filt = df[df["candidate_id"] == sel_cand]
        if filt.empty:
            st.warning("No data found.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        row = filt.iloc[0]
        h_st = str(row.get("status1", "Unknown")).upper()
        is_failed = (h_st == "FAILED")
        is_close  = (h_st == "CLOSE")

        badge_map = {
            "OPEN":   (AM_L,  AM,  "On Progress"),
            "CLOSE":  (GR_L,  GR,  "Hired"),
            "FAILED": (RD_L,  RD,  "Failed"),
        }
        b_bg, b_fg, b_txt = badge_map.get(h_st, (AM_L, AM, h_st))

        # Hero
        st.markdown(f"""
        <div class="cand-hero">
          <div>
            <div class="cand-hero-label">Candidate ID</div>
            <div class="cand-hero-id">{sel_cand}</div>
          </div>
          {badge(b_txt, b_bg, b_fg)}
        </div>
        """, unsafe_allow_html=True)

        # Info grid
        pos    = row.get("position_name", "—")
        dept   = row.get("departement", "—")
        divisi = row.get("divisi", "—")
        lvl    = row.get("level", "—")
        loc    = row.get("loc", "—")
        last   = row.get("last_progress", "—")
        tot_lt = row.get("total_lt", "—")
        bgt_lt = row.get("budget_lt1", "—")
        stat_lt = row.get("status_lt1", "—")

        if pd.notna(tot_lt):
            tot_lt = int(float(tot_lt))
        
        if pd.notna(bgt_lt):
            bgt_lt = int(float(bgt_lt))        
    

        lt_color = GR if str(stat_lt).lower() == "onbudget" else (RD if str(stat_lt).lower() == "overbudget" else TX)

        st.markdown(f"""
        <div class="info-grid">
          <div class="info-item"><div class="info-label">Position</div><div class="info-val">{pos}</div></div>
          <div class="info-item"><div class="info-label">Department</div><div class="info-val">{dept}</div></div>
          <div class="info-item"><div class="info-label">Division</div><div class="info-val">{divisi}</div></div>
          <div class="info-item"><div class="info-label">Level</div><div class="info-val">{lvl}</div></div>
          <div class="info-item"><div class="info-label">Location</div><div class="info-val">{loc}</div></div>
          <div class="info-item"><div class="info-label">Last Progress</div><div class="info-val">{last}</div></div>
          <div class="info-item"><div class="info-label">Total LT (days)</div><div class="info-val">{tot_lt}</div></div>
          <div class="info-item"><div class="info-label">Budget LT (days)</div><div class="info-val">{bgt_lt}</div></div>
          <div class="info-item"><div class="info-label">LT Status</div><div class="info-val" style="color:{lt_color};">{stat_lt}</div></div>
        </div>
        """, unsafe_allow_html=True)

        # Steps
        steps_def = [
            ("PRF Routing",    "start_prf_routing",    "complete_prf_routing",    "lt_prf",            "b_lt_prf",            "sla1"),
            ("Screening CV",   "start_screening_cv",   "complete_screening_cv",   "lt_screening",      "b_lt_screening",      "sla2"),
            ("HR Interview",   "start_interview_hr",   "complete_interview_hr",   "lt_hr_interview",   "b_lt_hr_interview",   "sla3"),
            ("User Interview", "start_interview_user", "complete_interview_user", "lt_user_interview", "b_lt_user_interview", "sla4"),
            ("Psychotest",     "start_psychotest",     "complete_psychotest",     "lt_psikotest",      "b_lt_psikotest",      "sla5"),
            ("Offering",       "start_offering",       "complete_offering",       "lt_offering",       "b_lt_offering",       "sla6"),
            ("MCU",            "start_mcu",            "mcu_date",                "lt_mcu",            "b_lt_mcu",            "sla7"),
            ("Review MCU",     "start_review_mcu",     "review_mcu",              "lt_review_mcu",     "b_lt_review_mcu",     "sla8"),
            ("FU MCU",         "start_fu_mcu",         "complete_fu_mcu",         "lt_fu_mcu",         "b_lt_fu_mcu",         "sla9"),
            ("Onboarding",     "date_onboarding",      "date_onboarding",         "lt_omn",            "b_lt_omn",            "sla10"),
        ]
        tech_start = row.get("start_technical_test")
        if pd.notna(tech_start) and str(tech_start).strip() not in ("", "nan"):
            steps_def.insert(4, ("Technical Test", "start_technical_test", "complete_technical_test", "lt_tech_test", "b_lt_tech", "sla11"))

        p_data = []
        done_count = 0
        last_data_idx = -1

        for i, (name, s_col, e_col, lt_col, b_lt_col, sla_col) in enumerate(steps_def):
            s_val = row.get(s_col)
            e_val = row.get(e_col)
            has_start = pd.notna(s_val) and str(s_val).strip() not in ("", "nan")
            has_end   = pd.notna(e_val) and str(e_val).strip() not in ("", "nan")

            if has_end:
                st_code = "done"; done_count += 1
            elif has_start:
                st_code = "active"
            else:
                st_code = "idle"

            if has_start or has_end:
                last_data_idx = i

            lt_actual = row.get(lt_col)
            lt_budget = row.get(b_lt_col)
            sla_v     = str(row.get(sla_col, "")).strip()
            lt_a_str  = str(int(float(lt_actual))) if pd.notna(lt_actual) and str(lt_actual).strip() not in ("", "nan") else None
            lt_b_str  = str(int(float(lt_budget))) if pd.notna(lt_budget) and str(lt_budget).strip() not in ("", "nan") else None

            p_data.append({
                "name": name,
                "start": str(s_val) if has_start else "—",
                "end":   str(e_val) if has_end   else "—",
                "status": st_code,
                "idx": i,
                "lt_actual": lt_a_str,
                "lt_budget": lt_b_str,
                "sla": sla_v,
            })

        if is_failed and last_data_idx >= 0:
            p_data[last_data_idx]["status"] = "failed"
            if p_data[last_data_idx]["end"] != "—":
                done_count -= 1

        prog_pct = done_count / len(p_data) if p_data else 0
        bar_color = RD if is_failed else OR
        pct_color = RD if is_failed else OR

        # Progress bar
        st.markdown(f"""
        <div class="prog-wrap">
          <div class="prog-top">
            <span class="prog-label">Recruitment Progress</span>
            <span class="prog-count">{done_count} of {len(p_data)} stages complete</span>
          </div>
          <div class="prog-track">
            <div style="height:100%;width:{prog_pct*100:.0f}%;background:{bar_color};border-radius:999px;"></div>
          </div>
          <div class="prog-pct" style="color:{pct_color};">{prog_pct*100:.0f}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(_steps_table(p_data), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════
# ③ RECRUITMENT ROOM
# ══════════════════════════════════════════
def run_rec_room():
    st.markdown('<div class="page">', unsafe_allow_html=True)

    col_h, col_b = st.columns([5, 1])
    with col_h:
        st.markdown(f"""
        <div class="page-header" style="margin-bottom:20px;">
          <div class="page-eyebrow">Workspace</div>
          <h1 class="page-title">Recruitment Room</h1>
          <p class="page-subtitle">Forms, spreadsheets, and tools — all in one workspace.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("<div style='padding-top:40px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_rec"):
            st.session_state.page = "home"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Form Panel ──
    st.markdown(f"""
    <div class="panel">
      <div class="panel-header">
        <div class="panel-icon">📝</div>
        <div>
          <div class="panel-title">Recruitment Form</div>
          <div class="panel-subtitle">Powered by Google Apps Script</div>
        </div>
      </div>
      <div class="panel-body" style="padding:0;">
        <div style="background:{GY2};border-top:none;">
          <div style="padding:9px 16px;background:{BK};display:flex;gap:6px;align-items:center;">
            <span style="width:9px;height:9px;border-radius:50%;background:#FF5F57;display:inline-block;"></span>
            <span style="width:9px;height:9px;border-radius:50%;background:#FFBD2E;display:inline-block;"></span>
            <span style="width:9px;height:9px;border-radius:50%;background:#28CA41;display:inline-block;"></span>
            <span style="margin-left:10px;font-size:11px;color:rgba(255,255,255,.4);">Recruitment Form · Google Apps Script</span>
          </div>
          <iframe src="{APPS_SCRIPT_URL}" width="100%" height="800" frameborder="0" style="border:none;display:block;background:#fff;"></iframe>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Links Panel ──
    st.markdown(f"""
    <div class="panel">
      <div class="panel-header">
        <div class="panel-icon">🔗</div>
        <div>
          <div class="panel-title">Quick Links</div>
          <div class="panel-subtitle">Spreadsheets and connected resources</div>
        </div>
      </div>
      <div class="panel-body">
    """, unsafe_allow_html=True)

    st.caption("Links reset on page refresh. Update the code to make them permanent.")

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
            nu = st.text_input("URL", value=link["url"], key=f"lu_{i}", placeholder="https://...", label_visibility="collapsed")
        with cc:
            if st.button("↗", key=f"lo_{i}") and link["url"]:
                st.markdown(f'<script>window.open("{link["url"]}","_blank");</script>', unsafe_allow_html=True)
        st.session_state.rec_links[i]["label"] = nl
        st.session_state.rec_links[i]["url"] = nu

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    if st.button("+ Add Link", key="add_link"):
        st.session_state.rec_links.append({"label": "New Link", "url": ""})
        st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ── Quick Actions Panel ──
    st.markdown(f"""
    <div class="panel">
      <div class="panel-header">
        <div class="panel-icon">⚡</div>
        <div>
          <div class="panel-title">Quick Actions</div>
          <div class="panel-subtitle">Shortcuts to common tasks</div>
        </div>
      </div>
      <div class="panel-body">
    """, unsafe_allow_html=True)

    qa1, qa2, qa3, qa4 = st.columns(4)
    with qa1:
        if st.button("📊  Export PPT", use_container_width=True, key="qa_ppt"):
            st.info("PPT export feature coming soon.")
    with qa2:
        if st.button("📈  Dashboard", use_container_width=True, key="qa_mpp"):
            st.session_state.page = "home"
            st.rerun()
    with qa3:
        if st.button("🔍  Tracking", use_container_width=True, key="qa_track"):
            st.session_state.page = "tracking"
            st.rerun()
    with qa4:
        if st.button("🔄  Refresh Cache", use_container_width=True, key="qa_cache"):
            st.cache_data.clear()
            st.success("Cache cleared!")

    st.markdown("</div></div></div>", unsafe_allow_html=True)


# ── ROUTER ──
if   st.session_state.page == "home":     run_home()
elif st.session_state.page == "tracking": run_tracking()
elif st.session_state.page == "rec_room": run_rec_room()
