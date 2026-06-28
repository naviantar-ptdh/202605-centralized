"""
HR Recruitment Portal — PT Dharma Henwa
v7: Sidebar layout + filter bulan/tahun/site + technical test step + recruitment room link cards
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
DATA_URL    = "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc/export?format=csv"
LOOKER_URL  = "https://datastudio.google.com/embed/reporting/a425625f-0af4-4b5c-8826-218a929b1333/page/YwLxF"

SITES = {
    "HO": {
        "form":  "https://script.google.com/macros/s/AKfycbytQh3jy8-MQ6UUHXmxOIAkx3au6SwgmXZM1NlN1iaP9GQaGCFOEqMy9QgrLwFeXHLs/exec",
        "sheet": "https://docs.google.com/spreadsheets/d/1WxPctId12ETTmELrkC6NGUJxKMW45R8llENqTtRt1hU/edit?pli=1&gid=593032148#gid=593032148",
    },
    "ACP": {
        "form":  "https://script.google.com/macros/s/AKfycbwyF4rVWA016TGZgKm2GE3NLjLqPFsdpm8tVISeKLbjrL0qZdFXXRiowwpjfeeW6sC6UA/exec",
        "sheet": "https://docs.google.com/spreadsheets/d/1ijLgBLvNJVG4VrSBwEaWLw7GfyYb7ck3tmuctE3I8Oo/edit?gid=0#gid=0",
    },
    "KCP": {
        "form":  "https://script.google.com/macros/s/AKfycbx2-5kNGHHj-qqAKmV0kHbXiN1VQ0KUu9Gw5nqXnYTXuRho3BSeWrgWodNWzVne4mC7MA/exec",
        "sheet": "https://docs.google.com/spreadsheets/d/1TZ91xddvt5718knaxDqAIlFadGSUvFjd67KDAx33VKA/edit?gid=0#gid=0",
    },
    "BCP": {
        "form":  "https://script.google.com/macros/s/AKfycbwYNMV7x1qjFr6CcVE2QF30iqeg-RjJb2uUIkD8oh69fmN5ZEvkyrnU41Td-sMp4ZqTyQ/exec",
        "sheet": "https://docs.google.com/spreadsheets/d/1Zqcs7d497_8kvoCDcFMSSRrfdxw5XBgD3pshIQhZWhg/edit?gid=29237685#gid=29237685",
    },
}

MONTHS_ID = {
    1:"Januari",2:"Februari",3:"Maret",4:"April",5:"Mei",6:"Juni",
    7:"Juli",8:"Agustus",9:"September",10:"Oktober",11:"November",12:"Desember"
}

OR   = "#E8440A"; OR_L = "#FFF0EB"; OR_M = "#FFD0BD"
BK   = "#111111"
GY1  = "#F7F7F8"; GY2  = "#F0F0F2"; GY3  = "#E2E2E6"; GY4  = "#9B9BA8"
TX   = "#18181B"; TX2  = "#52525B"
GR   = "#16A34A"; GR_L = "#F0FDF4"; GR_M = "#BBF7D0"
RD   = "#DC2626"; RD_L = "#FEF2F2"; RD_M = "#FECACA"
AM   = "#D97706"; AM_L = "#FFFBEB"; AM_M = "#FDE68A"
BL   = "#2563EB"; BL_L = "#EFF6FF"; BL_M = "#BFDBFE"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
*,*::before,*::after{{box-sizing:border-box}}
html,body,.stApp{{font-family:'Inter',-apple-system,sans-serif!important;background:{GY1}!important;color:{TX}!important}}
#MainMenu,footer,header,.stDeployButton{{display:none!important}}
.block-container,.stMainBlockContainer{{padding:0!important;max-width:100%!important}}
[data-testid="stAppViewBlockContainer"]{{padding:0!important}}
.element-container{{margin:0!important}}
section[data-testid="stSidebar"]{{display:none!important}}
::-webkit-scrollbar{{width:4px}}
::-webkit-scrollbar-track{{background:{GY2}}}
::-webkit-scrollbar-thumb{{background:{GY3};border-radius:99px}}

/* topnav */
.topnav{{height:56px;background:#fff;border-bottom:1px solid {GY3};display:flex;align-items:center;
  justify-content:space-between;padding:0 32px;position:sticky;top:0;z-index:999}}
.topnav-left{{display:flex;align-items:center;gap:12px}}
.logo-box{{width:30px;height:30px;background:{OR};border-radius:7px;display:flex;align-items:center;
  justify-content:center;font-size:11px;font-weight:700;color:#fff;letter-spacing:-.01em}}
.nav-sep{{width:1px;height:20px;background:{GY3}}}
.nav-brand{{font-size:13.5px;font-weight:600;color:{TX}}}
.topnav-right{{display:flex;align-items:center;gap:12px}}
.nav-date{{font-size:11.5px;color:{GY4}}}
.live-badge{{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:600;
  color:{GR};background:{GR_L};border:1px solid {GR_M};padding:3px 11px;border-radius:99px}}
.live-dot{{width:6px;height:6px;border-radius:50%;background:{GR};animation:pulse 2s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}

/* shell */
.shell{{display:flex;min-height:calc(100vh - 56px)}}

/* sidebar */
.sidebar{{width:220px;flex-shrink:0;background:#fff;border-right:1px solid {GY3};padding:20px 0;
  position:sticky;top:56px;height:calc(100vh - 56px);overflow-y:auto}}
.sb-section{{padding:0 14px;margin-bottom:22px}}
.sb-label{{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;
  color:{GY4};padding:0 8px;margin-bottom:6px}}
.sb-item{{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:8px;cursor:pointer;
  font-size:13px;color:{TX2};font-weight:500;margin-bottom:2px;text-decoration:none}}
.sb-item.active{{background:{OR_L};color:{OR};font-weight:600;border:1px solid {OR_M}}}
.sb-dot{{width:6px;height:6px;border-radius:50%;background:{OR};margin-left:auto}}
.sb-stat{{display:flex;justify-content:space-between;align-items:center;padding:5px 8px;border-radius:6px;font-size:12px}}

/* main */
.main{{flex:1;padding:28px 32px 64px;min-width:0}}

/* section heading */
.sec-hd{{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:{GY4};
  display:flex;align-items:center;gap:10px;margin-bottom:14px}}
.sec-hd::after{{content:'';flex:1;height:1px;background:{GY3}}}

/* embed frame */
.embed-frame{{background:#fff;border:1px solid {GY3};border-radius:14px;overflow:hidden;margin-bottom:28px}}
.embed-titlebar{{background:{GY2};border-bottom:1px solid {GY3};padding:10px 18px;
  display:flex;align-items:center;justify-content:space-between}}
.embed-title{{font-size:12px;font-weight:600;color:{TX2};display:flex;align-items:center;gap:7px}}
.embed-dots{{display:flex;gap:5px}}
.embed-dots span{{width:9px;height:9px;border-radius:50%;display:block}}

/* tool cards */
.tool-grid{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
.tool-card{{background:#fff;border:1px solid {GY3};border-radius:14px;padding:22px 24px;
  position:relative;overflow:hidden;transition:border-color .15s}}
.tool-card:hover{{border-color:{OR_M}}}
.tool-card-stripe{{position:absolute;top:0;left:0;right:0;height:3px;background:{OR}}}
.tool-card-ico{{width:40px;height:40px;background:{OR_L};border-radius:9px;
  display:flex;align-items:center;justify-content:center;margin-bottom:14px}}
.tool-card-title{{font-size:14px;font-weight:700;color:{TX};margin-bottom:5px}}
.tool-card-desc{{font-size:12.5px;color:{TX2};line-height:1.6}}
.tool-card-cta{{margin-top:14px;font-size:11.5px;font-weight:600;color:{OR}}}

/* filter bar */
.filter-bar{{background:#fff;border:1px solid {GY3};border-radius:10px;
  padding:14px 18px;margin-bottom:18px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}}
.filter-label{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:{GY4};white-space:nowrap}}

/* candidate list panel */
.cand-panel{{background:#fff;border:1px solid {GY3};border-radius:12px;overflow:hidden}}
.cand-panel-hd{{padding:12px 16px;border-bottom:1px solid {GY3};background:{GY2};
  font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:{GY4}}}
.cand-list{{max-height:540px;overflow-y:auto}}
.cand-row{{display:flex;align-items:center;gap:10px;padding:11px 14px;
  border-bottom:1px solid {GY3};cursor:pointer;transition:background .1s}}
.cand-row:last-child{{border-bottom:none}}
.cand-row:hover{{background:{GY1}}}
.cand-avatar{{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;font-size:11px;font-weight:700;flex-shrink:0}}
.cand-info{{flex:1;min-width:0}}
.cand-id{{font-size:12.5px;font-weight:600;color:{TX};white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.cand-pos{{font-size:11px;color:{TX2};white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}

/* hero */
.hero-card{{background:#fff;border:1px solid {GY3};border-radius:12px;padding:20px 22px;
  margin-bottom:12px;display:flex;align-items:center;justify-content:space-between}}
.hero-label{{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:{GY4};margin-bottom:4px}}
.hero-id{{font-size:20px;font-weight:700;letter-spacing:-.02em;color:{TX}}}

/* info grid */
.info-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px}}
.info-cell{{background:#fff;border:1px solid {GY3};border-radius:8px;padding:11px 13px}}
.info-cell-lbl{{font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:{GY4};margin-bottom:3px}}
.info-cell-val{{font-size:12.5px;font-weight:600;color:{TX}}}

/* progress card */
.prog-card{{background:#fff;border:1px solid {GY3};border-radius:10px;padding:14px 18px;margin-bottom:12px}}
.prog-top{{display:flex;justify-content:space-between;margin-bottom:8px}}
.prog-lbl{{font-size:12.5px;font-weight:600;color:{TX}}}
.prog-cnt{{font-size:11.5px;color:{GY4}}}
.prog-track{{height:5px;background:{GY3};border-radius:99px;overflow:hidden;margin-bottom:6px}}
.prog-pct{{font-size:11.5px;font-weight:700;text-align:right}}

/* pipeline table */
.pipe-wrap{{overflow-x:auto;border-radius:12px;border:1px solid {GY3}}}
.pipe-table{{width:100%;border-collapse:collapse;background:#fff;font-size:12px;min-width:600px}}
.pipe-table th{{background:{GY2};padding:9px 14px;text-align:left;font-size:10px;font-weight:700;
  text-transform:uppercase;letter-spacing:.07em;color:{GY4};border-bottom:1px solid {GY3};white-space:nowrap}}
.pipe-table td{{padding:9px 14px;border-bottom:1px solid {GY3};vertical-align:middle}}
.pipe-table tr:last-child td{{border-bottom:none}}
.step-circle{{width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;
  justify-content:center;font-size:10.5px;font-weight:700}}

/* pills */
.pill{{display:inline-block;padding:3px 11px;border-radius:99px;font-size:10.5px;font-weight:600;white-space:nowrap}}
.pill-open {{background:{AM_L};color:{AM};border:1px solid {AM_M}}}
.pill-close{{background:{GR_L};color:{GR};border:1px solid {GR_M}}}
.pill-fail {{background:{RD_L};color:{RD};border:1px solid {RD_M}}}
.pill-idle {{background:{GY2};color:{GY4};border:1px solid {GY3}}}
.pill-active{{background:{OR_L};color:{OR};border:1px solid {OR_M}}}

/* site cards grid */
.site-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.site-card{{background:#fff;border:1px solid {GY3};border-radius:14px;overflow:hidden}}
.site-card-hd{{padding:14px 18px;border-bottom:1px solid {GY3};display:flex;align-items:center;gap:10px}}
.site-badge{{font-size:11px;font-weight:700;letter-spacing:.04em;color:{OR};
  background:{OR_L};border:1px solid {OR_M};padding:3px 10px;border-radius:6px}}
.site-card-name{{font-size:14px;font-weight:700;color:{TX}}}
.site-link-row{{display:flex;align-items:center;justify-content:space-between;
  padding:13px 18px;border-bottom:1px solid {GY3}}}
.site-link-row:last-child{{border-bottom:none}}
.site-link-info{{display:flex;align-items:center;gap:10px}}
.site-link-ico{{width:30px;height:30px;border-radius:7px;display:flex;align-items:center;
  justify-content:center;font-size:14px;flex-shrink:0}}
.site-link-name{{font-size:12.5px;font-weight:600;color:{TX}}}
.site-link-desc{{font-size:11px;color:{GY4};margin-top:1px}}
.site-link-actions{{display:flex;align-items:center;gap:6px}}
.btn-copy{{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:600;
  color:{TX2};background:{GY2};border:1px solid {GY3};padding:5px 12px;
  border-radius:7px;cursor:pointer;text-decoration:none;white-space:nowrap}}
.btn-open{{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:600;
  color:{OR};background:{OR_L};border:1px solid {OR_M};padding:5px 12px;
  border-radius:7px;cursor:pointer;text-decoration:none;white-space:nowrap}}

/* streamlit widget overrides */
div[data-testid="metric-container"]{{background:#fff!important;border:1px solid {GY3}!important;
  border-radius:9px!important;padding:14px 16px!important}}
div[data-testid="metric-container"] label{{font-size:10px!important;font-weight:700!important;
  text-transform:uppercase!important;letter-spacing:.08em!important;color:{GY4}!important}}
div[data-testid="metric-container"] [data-testid="stMetricValue"]{{font-size:24px!important;
  font-weight:700!important;color:{TX}!important;letter-spacing:-.02em!important}}
.stRadio>div{{flex-direction:row!important;gap:6px!important;flex-wrap:wrap!important}}
.stRadio label{{background:#fff!important;border:1px solid {GY3}!important;border-radius:8px!important;
  padding:7px 18px!important;font-size:12.5px!important;font-weight:500!important;
  cursor:pointer!important;color:{TX2}!important}}
.stRadio label:has(input:checked){{background:{OR_L}!important;border-color:{OR_M}!important;
  color:{OR}!important;font-weight:600!important}}
div[data-testid="stSelectbox"]>div>div{{background:#fff!important;border:1px solid {GY3}!important;
  border-radius:8px!important;color:{TX}!important;font-size:13px!important}}
div[data-testid="stTextInput"] input{{background:#fff!important;border:1px solid {GY3}!important;
  border-radius:8px!important;color:{TX}!important;font-size:13px!important}}
button[kind="primary"]{{background:{OR}!important;border:none!important;color:#fff!important;
  font-family:'Inter',sans-serif!important;font-weight:600!important;font-size:13px!important;
  border-radius:8px!important}}
button[kind="primary"]:hover{{opacity:.88!important}}
button[kind="secondary"]{{background:#fff!important;border:1px solid {GY3}!important;
  color:{TX2}!important;font-family:'Inter',sans-serif!important;font-weight:500!important;
  font-size:13px!important;border-radius:8px!important}}
div[data-testid="stDataFrame"]{{border-radius:10px!important;border:1px solid {GY3}!important;overflow:hidden!important}}
</style>
"""

# ── SVG icons ──
ICO_DASH   = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>'
ICO_SEARCH = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.35-4.35"/></svg>'
ICO_CLIP   = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg>'
ICO_CHK    = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
ICO_X      = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
ICO_FORM   = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="13" y2="17"/></svg>'
ICO_SHEET  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/></svg>'
ICO_EXT    = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'
ICO_COPY   = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>'

st.markdown(CSS, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

# nav via query param
params = st.query_params
if "nav" in params:
    st.session_state.page = params["nav"]


# ══════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════
def pill(text, cls="idle"):
    return f'<span class="pill pill-{cls}">{text}</span>'

def step_circle(cls, label):
    cfg = {
        "done":   (GR_L, GR, GR_M),
        "failed": (RD_L, RD, RD_M),
        "active": (OR_L, OR, OR_M),
        "idle":   (GY2,  GY4, GY3),
    }.get(cls, (GY2, GY4, GY3))
    if cls == "done":
        inner = f'<span style="color:{cfg[1]};display:inline-flex;">{ICO_CHK}</span>'
    elif cls == "failed":
        inner = f'<span style="color:{cfg[1]};display:inline-flex;">{ICO_X}</span>'
    else:
        inner = f'<span style="color:{cfg[1]};">{label}</span>'
    return (f'<span class="step-circle" style="background:{cfg[0]};color:{cfg[1]};border:1px solid {cfg[2]};">'
            f'{inner}</span>')

def _steps_table(p_data):
    TH = (f"background:{GY2};padding:9px 14px;text-align:left;font-size:10px;font-weight:700;"
          f"text-transform:uppercase;letter-spacing:.07em;color:{GY4};border-bottom:1px solid {GY3};white-space:nowrap;")
    t = (f'<div class="pipe-wrap"><table class="pipe-table">'
         f'<thead><tr>'
         f'<th style="{TH}width:40px;padding-left:16px;"></th>'
         f'<th style="{TH}">Stage</th>'
         f'<th style="{TH}width:130px;">Status</th>'
         f'<th style="{TH}width:200px;">Start → End</th>'
         f'<th style="{TH}width:130px;">LT / Budget</th>'
         f'<th style="{TH}width:90px;padding-right:16px;">SLA</th>'
         f'</tr></thead><tbody>')

    for i, s in enumerate(p_data):
        cls = s["status"]
        badge_map = {"done":"Done","failed":"Failed Here","active":"In Progress","idle":"Pending"}
        badge_cls = {"done":"close","failed":"fail","active":"active","idle":"idle"}
        row_bg = GY1 if i % 2 else "#fff"
        bb = f"border-bottom:1px solid {GY3};" if i < len(p_data)-1 else ""
        name_style = f"color:{RD};font-weight:700;" if cls=="failed" else f"color:{TX};font-weight:600;"

        sla = (s["sla"] or "").lower()
        lt_a, lt_b = s["lt_actual"], s["lt_budget"]
        if lt_a is None:
            lt_html = f'<span class="pill pill-idle">{"—" if cls=="idle" else "In progress"}</span>'
        else:
            lt_cls = "close" if "ontime" in sla else ("fail" if "late" in sla else "idle")
            bpart  = f" / {lt_b}d" if lt_b else ""
            lt_html = f'<span class="pill pill-{lt_cls}">{lt_a}d{bpart}</span>'

        if "ontime" in sla:   sla_html = '<span class="pill pill-close">On time</span>'
        elif "late"  in sla:  sla_html = '<span class="pill pill-fail">Late</span>'
        else:                 sla_html = f'<span class="pill pill-idle">{s["sla"] or "—"}</span>'

        t += (
            f'<tr style="background:{row_bg};{bb}">'
            f'<td style="padding:9px 4px 9px 16px;">{step_circle(cls, str(s["idx"]+1))}</td>'
            f'<td style="padding:9px 14px;{name_style}">{s["name"]}</td>'
            f'<td style="padding:9px 14px;">{pill(badge_map.get(cls,"—"), badge_cls.get(cls,"idle"))}</td>'
            f'<td style="padding:9px 14px;font-size:11.5px;color:{TX2};">{s["start"]}<br>→ {s["end"]}</td>'
            f'<td style="padding:9px 14px;">{lt_html}</td>'
            f'<td style="padding:9px 16px 9px 14px;">{sla_html}</td>'
            f'</tr>'
        )
    t += '</tbody></table></div>'
    return t


# ══════════════════════════════════════════
# SHARED SHELL
# ══════════════════════════════════════════
def render_shell(active_page):
    st.markdown(f"""
    <div class="topnav">
      <div class="topnav-left">
        <div class="logo-box">DH</div>
        <div class="nav-sep"></div>
        <span class="nav-brand">HR Recruitment Portal</span>
      </div>
      <div class="topnav-right">
        <span class="nav-date">{datetime.now().strftime('%d %B %Y')}</span>
        <span class="live-badge"><span class="live-dot"></span>Live</span>
      </div>
    </div>
    <div class="shell">
    """, unsafe_allow_html=True)

    nav_items = [
        ("home",     ICO_DASH,   "Dashboard"),
        ("tracking", ICO_SEARCH, "Candidate Tracking"),
        ("rec_room", ICO_CLIP,   "Recruitment Room"),
    ]
    sb = '<div class="sidebar"><div class="sb-section"><div class="sb-label">Menu</div>'
    for key, ico, label in nav_items:
        a = " active" if active_page == key else ""
        dot = '<span class="sb-dot"></span>' if active_page == key else ""
        c = OR if active_page == key else TX2
        sb += (f'<div class="sb-item{a}" onclick="window.location.href=\'?nav={key}\'">'
               f'<span style="color:{c};">{ico}</span>{label}{dot}</div>')
    sb += '</div></div>'
    st.markdown(sb, unsafe_allow_html=True)
    st.markdown('<div class="main">', unsafe_allow_html=True)


def close_shell():
    st.markdown('</div></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════
# DATA LOADER
# ══════════════════════════════════════════
@st.cache_data(ttl=60)
def load_data():
    try:
        df = pd.read_csv(DATA_URL)
        df.columns = df.columns.str.lower().str.strip()
        for c in ["candidate_id","position_name","departement","level","loc","status1"]:
            if c in df.columns:
                df[c] = df[c].fillna("Unknown")
        # parse start_interview_user sebagai datetime untuk filter
        if "start_interview_user" in df.columns:
            df["_iu_dt"] = pd.to_datetime(df["start_interview_user"], dayfirst=True, errors="coerce")
        return df, None
    except Exception as e:
        return None, str(e)


# ══════════════════════════════════════════
# ① HOME
# ══════════════════════════════════════════
def run_home():
    render_shell("home")

    st.markdown('<div class="sec-hd">Live Analytics</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="embed-frame">
      <div class="embed-titlebar">
        <div class="embed-title">
          <span style="width:7px;height:7px;border-radius:50%;background:{GR};display:inline-block;
            animation:pulse 2s ease-in-out infinite;"></span>
          Looker Studio — Recruitment Overview
        </div>
        <div class="embed-dots">
          <span style="background:#FF5F57;"></span>
          <span style="background:#FFBD2E;"></span>
          <span style="background:#28CA41;"></span>
        </div>
      </div>
      <iframe width="100%" height="680" src="{LOOKER_URL}"
        frameborder="0" style="border:0;display:block;" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-hd">Recruitment Tools</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="tool-grid">
      <div class="tool-card">
        <div class="tool-card-stripe"></div>
        <div class="tool-card-ico">{ICO_SEARCH}</div>
        <div class="tool-card-title">Candidate Tracking</div>
        <div class="tool-card-desc">Monitor individual candidate progress and view their full recruitment pipeline — stage by stage in real time.</div>
        <div class="tool-card-cta">Open tracking →</div>
      </div>
      <div class="tool-card">
        <div class="tool-card-stripe"></div>
        <div class="tool-card-ico">{ICO_CLIP}</div>
        <div class="tool-card-title">Recruitment Room</div>
        <div class="tool-card-desc">Access forms and spreadsheets for all sites — HO, ACP, KCP, dan BCP — dalam satu tempat.</div>
        <div class="tool-card-cta">Open room →</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
    c1, c2, _ = st.columns([1, 1, 2])
    with c1:
        if st.button("Open Candidate Tracking", key="btn_tracking", use_container_width=True, type="primary"):
            st.query_params["nav"] = "tracking"
            st.session_state.page = "tracking"
            st.rerun()
    with c2:
        if st.button("Open Recruitment Room", key="btn_recroom", use_container_width=True, type="primary"):
            st.query_params["nav"] = "rec_room"
            st.session_state.page = "rec_room"
            st.rerun()

    close_shell()


# ══════════════════════════════════════════
# ② TRACKING
# ══════════════════════════════════════════
def run_tracking():
    render_shell("tracking")

    df, err = load_data()
    if err:
        st.error(f"Failed to load data: {err}")
        close_shell()
        return

    mode = st.radio("View mode", ["By Candidate", "By Position"], horizontal=True, key="m_track")
    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

    # ── SHARED FILTER BAR ──
    all_sites  = sorted(df["loc"].dropna().unique().tolist()) if "loc" in df.columns else []
    all_years  = []
    all_months = []
    if "_iu_dt" in df.columns:
        valid_dt = df["_iu_dt"].dropna()
        all_years  = sorted(valid_dt.dt.year.unique().tolist(), reverse=True)
        all_months = sorted(valid_dt.dt.month.unique().tolist())

    fc1, fc2, fc3 = st.columns([1, 1, 1])
    with fc1:
        site_opts = ["Semua Site"] + all_sites
        f_site = st.selectbox("Site / Lokasi", site_opts, key="f_site")
    with fc2:
        year_opts = ["Semua Tahun"] + [str(y) for y in all_years]
        f_year = st.selectbox("Tahun", year_opts, key="f_year")
    with fc3:
        month_opts = ["Semua Bulan"] + [MONTHS_ID[m] for m in all_months]
        f_month = st.selectbox("Bulan", month_opts, key="f_month")

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    # apply filters
    dff = df.copy()
    if f_site != "Semua Site":
        dff = dff[dff["loc"] == f_site]
    if f_year != "Semua Tahun" and "_iu_dt" in dff.columns:
        yr = int(f_year)
        mask = dff["_iu_dt"].dt.year == yr
        dff = dff[mask | dff["_iu_dt"].isna()]
    if f_month != "Semua Bulan" and "_iu_dt" in dff.columns:
        mo = [k for k,v in MONTHS_ID.items() if v == f_month][0]
        mask = dff["_iu_dt"].dt.month == mo
        dff = dff[mask | dff["_iu_dt"].isna()]

    # filter ketat bulan/tahun: sembunyikan baris yg _iu_dt tidak match jika filter aktif
    if f_year != "Semua Tahun" or f_month != "Semua Bulan":
        if "_iu_dt" in dff.columns:
            yr_ok  = (dff["_iu_dt"].dt.year  == int(f_year))  if f_year  != "Semua Tahun"  else pd.Series(True, index=dff.index)
            mo_ok  = (dff["_iu_dt"].dt.month == [k for k,v in MONTHS_ID.items() if v==f_month][0]) if f_month != "Semua Bulan" else pd.Series(True, index=dff.index)
            has_dt = dff["_iu_dt"].notna()
            dff = dff[~has_dt | (yr_ok & mo_ok)]

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ── BY CANDIDATE ──
    if mode == "By Candidate":
        cand_list = sorted(dff["candidate_id"].dropna().unique())
        if not cand_list:
            st.info("Tidak ada kandidat yang sesuai filter.")
            close_shell()
            return

        col_list, col_detail = st.columns([1, 2], gap="medium")

        with col_list:
            search = st.text_input("Search", placeholder="Cari candidate ID…", key="cand_search", label_visibility="collapsed")
            filtered_list = [c for c in cand_list if search.lower() in c.lower()] if search else cand_list

            av_map = {"OPEN":(OR_L,OR), "CLOSE":(GR_L,GR), "FAILED":(RD_L,RD)}
            sc_map = {"OPEN":"active","CLOSE":"close","FAILED":"fail"}
            st_lbl = {"OPEN":"Open","CLOSE":"Hired","FAILED":"Failed"}

            rows = '<div class="cand-panel"><div class="cand-panel-hd">Kandidat ({n})</div><div class="cand-list">'.replace("{n}", str(len(filtered_list)))
            for c in filtered_list[:80]:
                r   = dff[dff["candidate_id"]==c].iloc[0]
                st1 = str(r.get("status1","")).upper()
                ab, af = av_map.get(st1,(GY2,GY4))
                init = c[:2].upper()
                pos  = str(r.get("position_name",""))[:26]
                rows += (
                    f'<div class="cand-row">'
                    f'<div class="cand-avatar" style="background:{ab};color:{af};">{init}</div>'
                    f'<div class="cand-info"><div class="cand-id">{c}</div><div class="cand-pos">{pos}</div></div>'
                    f'<span class="pill pill-{sc_map.get(st1,"idle")}" style="font-size:10px;">{st_lbl.get(st1,st1)}</span>'
                    f'</div>'
                )
            rows += '</div></div>'
            st.markdown(rows, unsafe_allow_html=True)
            sel_cand = st.selectbox("Pilih kandidat", filtered_list, key="sel_cand", label_visibility="collapsed")

        with col_detail:
            filt = dff[dff["candidate_id"]==sel_cand]
            if filt.empty:
                st.info("Pilih kandidat dari daftar.")
                close_shell(); return

            row  = filt.iloc[0]
            h_st = str(row.get("status1","Unknown")).upper()
            b_cls = {"OPEN":"active","CLOSE":"close","FAILED":"fail"}.get(h_st,"idle")
            b_txt = {"OPEN":"On Progress","CLOSE":"Hired","FAILED":"Failed"}.get(h_st, h_st)

            st.markdown(f"""
            <div class="hero-card">
              <div><div class="hero-label">Candidate ID</div><div class="hero-id">{sel_cand}</div></div>
              {pill(b_txt, b_cls)}
            </div>""", unsafe_allow_html=True)

            pos     = row.get("position_name","—")
            dept    = row.get("departement","—")
            divisi  = row.get("divisi","—")
            lvl     = row.get("level","—")
            loc     = row.get("loc","—")
            last    = row.get("last_progress","—")
            tot_lt  = row.get("total_lt","—")
            bgt_lt  = row.get("budget_lt1","—")
            stat_lt = row.get("status_lt1","—")
            if pd.notna(tot_lt) and str(tot_lt) not in ("","nan"): tot_lt = int(float(tot_lt))
            if pd.notna(bgt_lt) and str(bgt_lt) not in ("","nan"): bgt_lt = int(float(bgt_lt))
            lt_col = GR if str(stat_lt).lower()=="onbudget" else (RD if str(stat_lt).lower()=="overbudget" else TX)

            st.markdown(f"""
            <div class="info-grid">
              <div class="info-cell"><div class="info-cell-lbl">Position</div><div class="info-cell-val">{pos}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Department</div><div class="info-cell-val">{dept}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Division</div><div class="info-cell-val">{divisi}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Level</div><div class="info-cell-val">{lvl}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Location</div><div class="info-cell-val">{loc}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Last Progress</div><div class="info-cell-val">{last}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Total LT (days)</div><div class="info-cell-val">{tot_lt}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">Budget LT (days)</div><div class="info-cell-val">{bgt_lt}</div></div>
              <div class="info-cell"><div class="info-cell-lbl">LT Status</div><div class="info-cell-val" style="color:{lt_col};">{stat_lt}</div></div>
            </div>""", unsafe_allow_html=True)

            # ── Pipeline steps ──
            steps_def = [
                ("PRF Routing",    "start_prf_routing",    "complete_prf_routing",    "lt_prf",            "b_lt_prf",    "sla1"),
                ("Screening CV",   "start_screening_cv",   "complete_screening_cv",   "lt_screening",      "b_lt_screening","sla2"),
                ("HR Interview",   "start_interview_hr",   "complete_interview_hr",   "lt_hr_interview",   "b_lt_hr_interview","sla3"),
                ("User Interview", "start_interview_user", "complete_interview_user", "lt_user_interview", "b_lt_user_interview","sla4"),
                ("Psychotest",     "start_psychotest",     "complete_psychotest",     "lt_psikotest",      "b_lt_psikotest","sla5"),
                ("Offering",       "start_offering",       "complete_offering",       "lt_offering",       "b_lt_offering","sla6"),
                ("MCU",            "start_mcu",            "mcu_date",                "lt_mcu",            "b_lt_mcu",    "sla7"),
                ("Review MCU",     "start_review_mcu",     "review_mcu",              "lt_review_mcu",     "b_lt_review_mcu","sla8"),
                ("FU MCU",         "start_fu_mcu",         "complete_fu_mcu",         "lt_fu_mcu",         "b_lt_fu_mcu", "sla9"),
                ("Onboarding",     "date_onboarding",      "date_onboarding",         "lt_omn",            "b_lt_omn",    "sla10"),
            ]
            # Technical Test: insert setelah User Interview (index 4) jika ada data
            tech_s = row.get("start_technical_test")
            if pd.notna(tech_s) and str(tech_s).strip() not in ("","nan"):
                steps_def.insert(4, (
                    "Technical Test",
                    "start_technical_test",
                    "complete_technical_test",
                    "lt_tech_test",
                    "b_lt_tech",
                    "sla11",
                ))

            p_data = []
            done_count = 0
            last_data_idx = -1

            for i,(name,s_col,e_col,lt_col2,b_lt_col,sla_col) in enumerate(steps_def):
                s_val = row.get(s_col); e_val = row.get(e_col)
                has_s = pd.notna(s_val) and str(s_val).strip() not in ("","nan")
                has_e = pd.notna(e_val) and str(e_val).strip() not in ("","nan")
                st_code = "done" if has_e else ("active" if has_s else "idle")
                if has_e: done_count += 1
                if has_s or has_e: last_data_idx = i
                lt_a  = row.get(lt_col2); lt_b = row.get(b_lt_col)
                sla_v = str(row.get(sla_col,"")).strip()
                lt_a_s = str(int(float(lt_a))) if pd.notna(lt_a) and str(lt_a).strip() not in ("","nan") else None
                lt_b_s = str(int(float(lt_b))) if pd.notna(lt_b) and str(lt_b).strip() not in ("","nan") else None
                p_data.append({
                    "name":name,"start":str(s_val) if has_s else "—","end":str(e_val) if has_e else "—",
                    "status":st_code,"idx":i,"lt_actual":lt_a_s,"lt_budget":lt_b_s,"sla":sla_v,
                })

            if h_st=="FAILED" and last_data_idx>=0:
                if p_data[last_data_idx]["end"] != "—": done_count -= 1
                p_data[last_data_idx]["status"] = "failed"

            prog_pct = done_count / len(p_data) if p_data else 0
            bar_col  = RD if h_st=="FAILED" else OR
            pct_col  = RD if h_st=="FAILED" else OR

            st.markdown(f"""
            <div class="prog-card">
              <div class="prog-top">
                <span class="prog-lbl">Recruitment Progress</span>
                <span class="prog-cnt">{done_count} of {len(p_data)} stages complete</span>
              </div>
              <div class="prog-track">
                <div style="height:100%;width:{prog_pct*100:.0f}%;background:{bar_col};border-radius:99px;"></div>
              </div>
              <div class="prog-pct" style="color:{pct_col};">{prog_pct*100:.0f}%</div>
            </div>""", unsafe_allow_html=True)

            st.markdown(_steps_table(p_data), unsafe_allow_html=True)

            # result Technical Test (extra info jika ada)
            res_tt = row.get("result_technical_test")
            if pd.notna(res_tt) and str(res_tt).strip() not in ("","nan"):
                st.markdown(f"""
                <div style="margin-top:10px;background:{BL_L};border:1px solid {BL_M};
                  border-radius:8px;padding:10px 14px;font-size:12.5px;color:{BL};">
                  <strong>Technical Test Result:</strong> {res_tt}
                </div>""", unsafe_allow_html=True)

    # ── BY POSITION ──
    else:
        pos_list = sorted(dff["position_name"].dropna().unique())
        if not pos_list:
            st.info("Tidak ada posisi yang sesuai filter.")
            close_shell(); return

        sel_pos  = st.selectbox("Pilih Posisi", pos_list, key="s_pos")
        filtered = dff[dff["position_name"]==sel_pos].copy()
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        if "status1" in filtered.columns:
            su = filtered["status1"].str.upper()
            m1,m2,m3,m4 = st.columns(4)
            m1.metric("Total",       len(filtered))
            m2.metric("On Progress", int((su=="OPEN").sum()))
            m3.metric("Hired",       int((su=="CLOSE").sum()))
            m4.metric("Failed",      int((su=="FAILED").sum()))

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        cols = [c for c in ["candidate_id","position_name","departement","level","loc",
                             "last_progress","total_lt","status1"] if c in filtered.columns]
        disp = filtered[cols].copy()
        if "total_lt" in disp.columns:
            disp["total_lt"] = pd.to_numeric(disp["total_lt"], errors="coerce").fillna(0).astype(int)
        if "status1" in disp.columns:
            disp = disp.rename(columns={"status1":"Status","total_lt":"Total LT (days)"})

        def color_st(val):
            v = str(val).upper()
            if v=="OPEN":   return f"color:{AM};font-weight:600;"
            if v=="FAILED": return f"color:{RD};font-weight:600;"
            if v=="CLOSE":  return f"color:{GR};font-weight:600;"
            return ""

        st.dataframe(
            disp.style.map(color_st, subset=["Status"]) if "Status" in disp.columns else disp,
            use_container_width=True, height=420
        )

    close_shell()


# ══════════════════════════════════════════
# ③ RECRUITMENT ROOM
# ══════════════════════════════════════════
def run_rec_room():
    render_shell("rec_room")

    st.markdown('<div class="sec-hd">Links per Site</div>', unsafe_allow_html=True)

    # copy toast via JS
    copy_js = """
    <script>
    function copyLink(txt, btnId) {
      navigator.clipboard.writeText(txt).then(function() {
        var btn = document.getElementById(btnId);
        var orig = btn.innerHTML;
        btn.innerHTML = '✓ Tersalin';
        btn.style.color = '#16A34A';
        btn.style.background = '#F0FDF4';
        btn.style.borderColor = '#BBF7D0';
        setTimeout(function(){ btn.innerHTML = orig;
          btn.style.color=''; btn.style.background=''; btn.style.borderColor=''; }, 1800);
      });
    }
    </script>
    """
    st.markdown(copy_js, unsafe_allow_html=True)

    site_html = '<div class="site-grid">'
    for site, urls in SITES.items():
        links = [
            ("Form Input",   ICO_FORM,  urls["form"],  f"form_{site}"),
            ("Spreadsheet",  ICO_SHEET, urls["sheet"], f"sheet_{site}"),
        ]
        site_html += f'<div class="site-card"><div class="site-card-hd"><span class="site-badge">{site}</span><span class="site-card-name">Site {site}</span></div>'
        for lname, ico, url, uid in links:
            site_html += f"""
            <div class="site-link-row">
              <div class="site-link-info">
                <div class="site-link-ico" style="background:{'#EFF6FF' if 'sheet' in uid else '#FFF0EB'};
                  color:{'#2563EB' if 'sheet' in uid else '#E8440A'};">{ico}</div>
                <div>
                  <div class="site-link-name">{lname}</div>
                  <div class="site-link-desc">{'Google Sheets' if 'sheet' in uid else 'Google Apps Script'}</div>
                </div>
              </div>
              <div class="site-link-actions">
                <button class="btn-copy" id="btn_{uid}"
                  onclick="copyLink('{url}', 'btn_{uid}')">{ICO_COPY} Salin Link</button>
                <a class="btn-open" href="{url}" target="_blank">{ICO_EXT} Buka</a>
              </div>
            </div>"""
        site_html += '</div>'
    site_html += '</div>'

    st.markdown(site_html, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    if st.button("🔄 Refresh Data Cache", key="qa_cache"):
        st.cache_data.clear()
        st.success("Cache cleared.")

    close_shell()


# ── ROUTER ──
p = st.session_state.page
if   p == "home":     run_home()
elif p == "tracking": run_tracking()
elif p == "rec_room": run_rec_room()
