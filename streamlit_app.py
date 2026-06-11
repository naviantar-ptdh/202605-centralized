"""
HR Centralized System — Darma Henwa Brand
v5: Full redesign (professional, clean), fixed ✕ failed logic, inline-style-only HTML
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
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbytQh3jy8-MQ6UUHXmxOIAkx3au6SwgmXZM1NlN1iaP9GQaGCFOEqMy9QgrLwFeXHLs/exec"

# ── colour palette (for inline use in Python) ──
OR  = "#E8440A"          # DH orange
OR2 = "#FF6B35"          # lighter
BK  = "#1C1917"          # near black
GY1 = "#F7F5F3"          # page bg
GY2 = "#EFECE9"          # surface 2
GY3 = "#E2DDD8"          # border
TX  = "#1C1917"          # text
TX2 = "#6B6560"          # secondary
TX3 = "#A09890"          # muted
GR  = "#15803D"          # green
GRB = "rgba(21,128,61,.09)"
AM  = "#92400E"          # amber
AMB = "rgba(146,64,14,.09)"
RD  = "#B91C1C"          # red
RDB = "rgba(185,28,28,.09)"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html,body,.stApp{{font-family:'Inter',sans-serif!important;background:{GY1}!important;color:{TX}!important;}}
#MainMenu,footer,header,.stDeployButton{{display:none!important;}}
.block-container,.stMainBlockContainer{{padding:0!important;max-width:100%!important;}}
[data-testid="stAppViewBlockContainer"]{{padding:0!important;}}
.element-container{{margin:0!important;}}

/* scrollbar */
::-webkit-scrollbar{{width:4px;height:4px;}}
::-webkit-scrollbar-track{{background:{GY2};}}
::-webkit-scrollbar-thumb{{background:{GY3};border-radius:2px;}}

/* topbar */
.tb{{position:sticky;top:0;z-index:999;height:54px;background:{BK};
  display:flex;align-items:center;justify-content:space-between;
  padding:0 36px;border-bottom:2px solid {OR};}}
.tb-brand{{display:flex;align-items:center;gap:14px;}}
.tb-sep{{width:1px;height:20px;background:rgba(255,255,255,.12);}}
.tb-name{{font-size:12px;font-weight:600;color:rgba(255,255,255,.75);letter-spacing:.01em;}}
.tb-right{{display:flex;align-items:center;gap:12px;}}
.tb-date{{font-size:11px;color:rgba(255,255,255,.35);font-family:'JetBrains Mono',monospace;}}
.tb-pill{{font-size:9px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  background:{OR};color:#fff;padding:3px 10px;border-radius:20px;}}

/* page wrap */
.pw{{padding:28px 36px 72px;}}

/* section divider */
.sd{{height:1px;background:{GY3};margin:18px 0 22px;}}

/* page header */
.ph{{display:flex;align-items:center;gap:14px;margin-bottom:4px;}}
.ph-ico{{width:40px;height:40px;border-radius:8px;background:{GY2};
  border:1.5px solid {GY3};display:flex;align-items:center;justify-content:center;}}
.ph-title{{font-size:20px;font-weight:800;letter-spacing:-.03em;color:{TX};}}
.ph-sub{{font-size:11.5px;color:{TX3};margin-top:2px;}}

/* candidate hero */
.ch{{background:#fff;border:1.5px solid {GY3};border-radius:12px;
  padding:20px 24px;margin-bottom:16px;
  display:flex;align-items:center;justify-content:space-between;}}
.ch-id{{font-size:18px;font-weight:800;letter-spacing:-.02em;color:{TX};}}
.ch-lbl{{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:{TX3};margin-bottom:3px;}}

/* info grid */
.ig{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:16px;}}
.ig-item{{background:{GY2};border-radius:8px;padding:11px 14px;}}
.ig-lbl{{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:{TX3};margin-bottom:3px;}}
.ig-val{{font-size:12.5px;font-weight:600;color:{TX};}}

/* progress */
.pb-wrap{{background:#fff;border:1.5px solid {GY3};border-radius:10px;
  padding:16px 20px;margin-bottom:16px;}}
.pb-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;}}
.pb-label{{font-size:13px;font-weight:700;color:{TX};}}
.pb-count{{font-size:11px;color:{TX3};font-family:'JetBrains Mono',monospace;}}
.pb-track{{height:5px;background:{GY3};border-radius:3px;overflow:hidden;margin-bottom:6px;}}
.pb-bottom{{display:flex;justify-content:space-between;}}
.pb-hint{{font-size:10.5px;color:{TX3};}}

/* metrics */
div[data-testid="metric-container"]{{
  background:#fff!important;border:1.5px solid {GY3}!important;
  border-radius:9px!important;padding:14px 16px!important;}}
div[data-testid="metric-container"] label{{
  font-size:9px!important;font-weight:700!important;
  text-transform:uppercase!important;letter-spacing:.09em!important;color:{TX3}!important;}}
div[data-testid="metric-container"] [data-testid="stMetricValue"]{{
  font-family:'JetBrains Mono',monospace!important;
  font-size:24px!important;font-weight:600!important;color:{TX}!important;}}

/* radio */
.stRadio>div{{flex-direction:row!important;gap:6px!important;flex-wrap:wrap!important;}}
.stRadio label{{
  background:#fff!important;border:1.5px solid {GY3}!important;
  border-radius:7px!important;padding:6px 16px!important;
  font-size:12px!important;font-weight:500!important;cursor:pointer!important;color:{TX2}!important;}}
.stRadio label:has(input:checked){{
  background:rgba(232,68,10,.07)!important;
  border-color:rgba(232,68,10,.30)!important;color:{OR}!important;font-weight:600!important;}}

/* selectbox */
div[data-testid="stSelectbox"]>div>div{{
  background:#fff!important;border:1.5px solid {GY3}!important;
  border-radius:7px!important;color:{TX}!important;font-size:12.5px!important;}}

/* buttons */
button[kind="primary"]{{
  background:{OR}!important;border:none!important;color:#fff!important;
  font-family:'Inter',sans-serif!important;font-weight:600!important;
  font-size:12.5px!important;border-radius:7px!important;}}
button[kind="primary"]:hover{{background:{OR2}!important;}}
button[kind="secondary"]{{
  background:#fff!important;border:1.5px solid {GY3}!important;
  color:{TX2}!important;font-family:'Inter',sans-serif!important;
  font-weight:500!important;font-size:12.5px!important;border-radius:7px!important;}}

/* dataframe */
div[data-testid="stDataFrame"]{{
  border-radius:9px!important;border:1.5px solid {GY3}!important;
  overflow:hidden!important;}}

/* nav cards */
.nc{{background:#fff;border:1.5px solid {GY3};border-radius:12px;
  padding:22px 24px 18px;position:relative;overflow:hidden;cursor:pointer;}}
.nc-stripe{{position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,{OR},{OR2});}}
.nc-ico{{width:38px;height:38px;border-radius:7px;background:{GY2};
  border:1.5px solid {GY3};display:flex;align-items:center;justify-content:center;
  margin-bottom:12px;overflow:hidden;}}
.nc-ico img{{width:22px;height:22px;object-fit:contain;}}
.nc-title{{font-size:13.5px;font-weight:700;color:{TX};margin-bottom:4px;}}
.nc-desc{{font-size:11.5px;color:{TX3};line-height:1.6;}}
.nc-cta{{margin-top:14px;font-size:10px;font-weight:700;color:{OR};
  letter-spacing:.05em;text-transform:uppercase;}}

/* rec section */
.rs{{background:#fff;border:1.5px solid {GY3};border-radius:12px;
  margin-bottom:16px;overflow:hidden;}}
.rs-hdr{{padding:12px 18px;border-bottom:1.5px solid {GY3};background:{GY2};
  display:flex;align-items:center;gap:10px;}}
.rs-ico{{width:30px;height:30px;border-radius:7px;background:#fff;
  border:1.5px solid {GY3};display:flex;align-items:center;justify-content:center;overflow:hidden;}}
.rs-ico img{{width:18px;height:18px;object-fit:contain;}}
.rs-title{{font-size:12.5px;font-weight:700;color:{TX};}}
.rs-sub{{font-size:10.5px;color:{TX3};margin-top:1px;}}
.rs-body{{padding:18px;}}

/* dash embed */
.df{{background:{BK};border-radius:12px;overflow:hidden;margin-bottom:24px;
  border:1px solid rgba(255,255,255,.04);}}
.df-hdr{{padding:12px 18px;border-bottom:1px solid rgba(255,255,255,.07);
  display:flex;align-items:center;justify-content:space-between;}}
.df-title{{font-size:11px;font-weight:600;color:rgba(255,255,255,.65);
  display:flex;align-items:center;gap:7px;}}
.df-live{{width:6px;height:6px;border-radius:50%;background:#22C55E;
  box-shadow:0 0 4px #22C55E;animation:pulse 2s infinite;}}
@keyframes pulse{{0%,100%{{opacity:1;}}50%{{opacity:.4;}}}}
.df-dots{{display:flex;gap:5px;}}
.df-dots span{{width:9px;height:9px;border-radius:50%;display:block;}}

/* section label */
.sl{{display:flex;align-items:center;gap:10px;margin-bottom:14px;}}
.sl-line{{flex:1;height:1px;background:{GY3};}}
.sl-text{{font-size:9px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:{TX3};white-space:nowrap;display:flex;align-items:center;gap:6px;}}
.sl-dot{{width:4px;height:4px;border-radius:50%;background:{OR};}}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# session
if "page" not in st.session_state:
    st.session_state.page = "home"

# ── TOPBAR ──
st.markdown(f"""
<div class="tb">
  <div class="tb-brand">
    <img src="{GITHUB_RAW}/logo_putih.png" style="height:26px;width:auto;"
         onerror="this.style.display='none'" alt="PTDH"/>
    <div class="tb-sep"></div>
    <span class="tb-name">HR Recruitment Portal</span>
  </div>
  <div class="tb-right">
    <span class="tb-date">{datetime.now().strftime('%d %b %Y')}</span>
    <span class="tb-pill">Live</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════
# SHARED HELPERS
# ═══════════════════════════════════════
def _badge(text, bg, fg, font="'Inter',sans-serif"):
    return (f'<span style="display:inline-block;padding:3px 11px;border-radius:20px;'
            f'background:{bg};color:{fg};font-size:10px;font-weight:600;'
            f'font-family:{font};">{text}</span>')

def _status_colors(cls):
    m = {
        "done":   (GRB, GR),
        "failed": (RDB, RD),
        "active": ("rgba(232,68,10,.08)", OR),
        "idle":   (GY2, TX3),
    }
    return m.get(cls, (GY2, TX3))

def _circle(cls, icon):
    bg, fg = _status_colors(cls)
    return (f'<td style="width:42px;padding:10px 4px 10px 14px;vertical-align:middle;">'
            f'<span style="display:inline-flex;align-items:center;justify-content:center;'
            f'width:26px;height:26px;border-radius:50%;background:{bg};color:{fg};'
            f'font-size:11px;font-weight:700;font-family:\'JetBrains Mono\',monospace;">'
            f'{icon}</span></td>')

def _td_badge(cls, txt):
    bg, fg = _status_colors(cls)
    return (f'<td style="width:120px;padding:10px 8px;vertical-align:middle;">'
            + _badge(txt, bg, fg) + '</td>')

def _td_sla(sla_str):
    sl = (sla_str or "").lower()
    if "ontime" in sl:
        bg, fg, lbl = GRB, GR, "Ontime"
    elif "late" in sl:
        bg, fg, lbl = RDB, RD, "Late"
    else:
        bg, fg, lbl = GY2, TX3, sla_str or "—"
    return (f'<td style="width:88px;padding:10px 14px 10px 8px;vertical-align:middle;">'
            + _badge(lbl, bg, fg) + '</td>')

def _td_lt(lt_actual_str, lt_budget_str, sla_val, st_code):
    base = ("display:inline-block;padding:3px 9px;border-radius:20px;"
            "font-size:10px;font-weight:600;font-family:'JetBrains Mono',monospace;"
            "white-space:nowrap;")
    grey = base + f"background:{GY2};color:{TX3};"
    if lt_actual_str is None:
        txt = "—" if st_code == "idle" else "In progress"
        return f'<td style="width:130px;padding:10px 8px;vertical-align:middle;"><span style="{grey}">{txt}</span></td>'
    sl = (sla_val or "").lower()
    if "ontime" in sl:
        chip = base + f"background:{GRB};color:{GR};"
    elif "late" in sl:
        chip = base + f"background:{RDB};color:{RD};"
    else:
        chip = grey
    bpart = f" / {lt_budget_str}d" if lt_budget_str else ""
    return (f'<td style="width:130px;padding:10px 8px;vertical-align:middle;">'
            f'<span style="{chip}">{lt_actual_str}d{bpart}</span></td>')

def _steps_table(p_data):
    TH = (f"font-size:9px;font-weight:700;text-transform:uppercase;"
          f"letter-spacing:.09em;color:{TX3};padding:9px 8px;text-align:left;"
          f"border-bottom:1.5px solid {GY3};background:{GY2};")
    table = (f'<table style="width:100%;border-collapse:collapse;background:#fff;'
             f'border-radius:10px;overflow:hidden;border:1.5px solid {GY3};">'
             f'<thead><tr>'
             f'<th style="{TH}width:42px;padding:9px 4px 9px 14px;"></th>'
             f'<th style="{TH}">Stage</th>'
             f'<th style="{TH}width:120px;">Status</th>'
             f'<th style="{TH}width:200px;">Start → End</th>'
             f'<th style="{TH}width:130px;">LT / Budget</th>'
             f'<th style="{TH}width:88px;padding:9px 14px 9px 8px;">SLA</th>'
             f'</tr></thead><tbody>')

    for i, s in enumerate(p_data):
        cls = s["status"]
        icon = {"done":"✓","failed":"✕","active":str(s["idx"]+1),"idle":str(s["idx"]+1)}.get(cls, str(s["idx"]+1))
        badge_txt = {"done":"Done","failed":"Failed Here","active":"In Progress","idle":"Pending"}.get(cls,"—")
        bb = f"border-bottom:1px solid {GY3};" if i < len(p_data)-1 else ""
        row_bg = "#fff" if i%2==0 else GY1

        # highlight failed row subtly
        if cls == "failed":
            row_bg = "rgba(185,28,28,.03)"

        name_style = f"font-size:12.5px;font-weight:600;color:{TX};"
        if cls == "failed":
            name_style = f"font-size:12.5px;font-weight:700;color:{RD};"

        table += (
            f'<tr style="background:{row_bg};{bb}">'
            + _circle(cls, icon)
            + f'<td style="padding:10px 8px;vertical-align:middle;{name_style}">{s["name"]}</td>'
            + _td_badge(cls, badge_txt)
            + (f'<td style="width:200px;padding:10px 8px;vertical-align:middle;'
               f'font-size:10.5px;color:{TX3};font-family:\'JetBrains Mono\',monospace;">'
               f'{s["start"]}<br>→ {s["end"]}</td>')
            + _td_lt(s["lt_actual"], s["lt_budget"], s["sla"], cls)
            + _td_sla(s["sla"])
            + '</tr>'
        )
    table += '</tbody></table>'
    return table


# ═══════════════════════════════════════
# ① HOME
# ═══════════════════════════════════════
def run_home():
    st.markdown('<div class="pw">', unsafe_allow_html=True)

    st.markdown(f'<div class="sl"><div class="sl-text"><div class="sl-dot"></div>Recruitment Dashboard · Live</div><div class="sl-line"></div></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="df">
      <div class="df-hdr">
        <div class="df-title"><div class="df-live"></div>Looker Studio — Recruitment Overview</div>
        <div class="df-dots">
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

    st.markdown(f'<div class="sl"><div class="sl-line"></div><div class="sl-text"><div class="sl-dot"></div>Recruitment Tools</div><div class="sl-line"></div></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(f"""
        <div class="nc">
          <div class="nc-stripe"></div>
          <div class="nc-ico"><img src="{GITHUB_RAW}/Search.png" onerror="this.style.display='none'" alt=""/></div>
          <div class="nc-title">Candidate Tracking</div>
          <div class="nc-desc">Monitor candidate pipeline & recruitment stage progress in real-time.</div>
          <div class="nc-cta">Open Tracking →</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        if st.button("Open Candidate Tracking", key="btn_tracking", use_container_width=True, type="primary"):
            st.session_state.page = "tracking"; st.rerun()
    with c2:
        st.markdown(f"""
        <div class="nc">
          <div class="nc-stripe"></div>
          <div class="nc-ico"><img src="{GITHUB_RAW}/home.png" onerror="this.style.display='none'" alt=""/></div>
          <div class="nc-title">Recruitment Room</div>
          <div class="nc-desc">Forms, spreadsheet links, and quick actions — all in one workspace.</div>
          <div class="nc-cta">Open Room →</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        if st.button("Open Recruitment Room", key="btn_recroom", use_container_width=True, type="primary"):
            st.session_state.page = "rec_room"; st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════
# ② TRACKING
# ═══════════════════════════════════════
def run_tracking():
    st.markdown('<div class="pw">', unsafe_allow_html=True)

    col_hdr, col_back = st.columns([6, 1])
    with col_hdr:
        st.markdown(f"""
        <div class="ph">
          <div class="ph-ico"><img src="{GITHUB_RAW}/Search.png" style="width:20px;height:20px;object-fit:contain;" onerror="this.style.display='none'"/></div>
          <div><div class="ph-title">Candidate Tracking</div><div class="ph-sub">Monitor recruitment pipeline in real-time</div></div>
        </div>""", unsafe_allow_html=True)
    with col_back:
        st.markdown("<div style='padding-top:10px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_track"):
            st.session_state.page = "home"; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sd"></div>', unsafe_allow_html=True)

    @st.cache_data(ttl=60)
    def load_data():
        url = "https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc/export?format=csv"
        try:
            df = pd.read_csv(url)
            df.columns = df.columns.str.lower().str.strip()
            for c in ["candidate_id","position_name","departement","level","loc","status1"]:
                if c in df.columns: df[c] = df[c].fillna("Unknown")
            return df, None
        except Exception as e:
            return None, str(e)

    df, err = load_data()
    if err:
        st.error(f"⚠ Failed to load data: {err}")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    mode = st.radio("Search Mode", ["By Position", "By Candidate"], horizontal=True, key="m_track")
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # ── BY POSITION ──
    if mode == "By Position":
        pos_list = sorted(df["position_name"].dropna().unique())
        sel_pos  = st.selectbox("Select Position", pos_list, key="s_pos")
        filtered = df[df["position_name"] == sel_pos].copy()
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        if "status1" in filtered.columns:
            su = filtered["status1"].str.upper()
            m1,m2,m3,m4 = st.columns(4)
            m1.metric("Total Candidates", len(filtered))
            m2.metric("On-Progress",  int((su=="OPEN").sum()))
            m3.metric("Hired",        int((su=="CLOSE").sum()))
            m4.metric("Failed",       int((su=="FAILED").sum()))

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        cols = [c for c in ["candidate_id","position_name","departement","level","loc","last_progress","tot_lt","status1"] if c in filtered.columns]
        disp = filtered[cols].copy()
        if "tot_lt" in disp.columns:
            disp["tot_lt"] = pd.to_numeric(disp["tot_lt"], errors="coerce").fillna(0).astype(int)
        if "status1" in disp.columns:
            disp = disp.rename(columns={"status1":"Status","tot_lt":"Total LT (days)"})

        def color_st(val):
            v = str(val).upper()
            if v=="OPEN":   return f"color:{AM};font-weight:700;"
            if v=="FAILED": return f"color:{RD};font-weight:700;"
            if v=="CLOSE":  return f"color:{GR};font-weight:700;"
            return ""

        st.dataframe(
            disp.style.map(color_st, subset=["Status"]) if "Status" in disp.columns else disp,
            use_container_width=True, height=380)

    # ── BY CANDIDATE ──
    else:
        cand_list = sorted(df["candidate_id"].dropna().unique())
        sel_cand  = st.selectbox("Select Candidate ID", cand_list, key="s_cand")
        filt = df[df["candidate_id"] == sel_cand]
        if filt.empty:
            st.warning("No data found."); st.markdown("</div>", unsafe_allow_html=True); return

        row = filt.iloc[0]
        h_st     = str(row.get("status1","Unknown")).upper()
        is_failed = (h_st == "FAILED")
        is_close  = (h_st == "CLOSE")
        b_cls_map = {"OPEN":"amber","CLOSE":"green","FAILED":"red"}
        b_lbl_map = {"OPEN":"On Progress","CLOSE":"Hired","FAILED":"Failed"}

        badge_cfg = {
            "amber": (AMB, AM, "On Progress"),
            "green": (GRB, GR, "Hired"),
            "red":   (RDB, RD, "Failed"),
        }.get(b_cls_map.get(h_st,"amber"), (AMB, AM, h_st))

        # ── Hero ──
        st.markdown(f"""
        <div class="ch">
          <div>
            <div class="ch-lbl">Candidate ID</div>
            <div class="ch-id">{sel_cand}</div>
          </div>
          {_badge(badge_cfg[2], badge_cfg[0], badge_cfg[1])}
        </div>""", unsafe_allow_html=True)

        # ── Info grid ──
        pos      = row.get("position_name","—")
        dept     = row.get("departement","—")
        divisi   = row.get("divisi","—")
        lvl      = row.get("level","—")
        loc      = row.get("loc","—")
        last     = row.get("last_progress","—")
        tot_lt   = row.get("tot_lt", row.get("total_lt","—"))
        bgt_lt   = row.get("budget_lt","—")
        stat_lt  = row.get("status_lt","—")
        if isinstance(tot_lt,  float): tot_lt  = int(tot_lt)
        if isinstance(bgt_lt, float): bgt_lt  = int(bgt_lt)

        lt_color = GR if str(stat_lt).lower()=="onbudget" else (RD if str(stat_lt).lower()=="overbudget" else TX)

        st.markdown(f"""
        <div class="ig">
          <div class="ig-item"><div class="ig-lbl">Position</div><div class="ig-val">{pos}</div></div>
          <div class="ig-item"><div class="ig-lbl">Department</div><div class="ig-val">{dept}</div></div>
          <div class="ig-item"><div class="ig-lbl">Division</div><div class="ig-val">{divisi}</div></div>
          <div class="ig-item"><div class="ig-lbl">Level</div><div class="ig-val">{lvl}</div></div>
          <div class="ig-item"><div class="ig-lbl">Location</div><div class="ig-val">{loc}</div></div>
          <div class="ig-item"><div class="ig-lbl">Last Progress</div><div class="ig-val">{last}</div></div>
          <div class="ig-item"><div class="ig-lbl">Total LT (days)</div><div class="ig-val">{tot_lt}</div></div>
          <div class="ig-item"><div class="ig-lbl">Budget LT (days)</div><div class="ig-val">{bgt_lt}</div></div>
          <div class="ig-item"><div class="ig-lbl">LT Status</div><div class="ig-val" style="color:{lt_color};font-weight:700;">{stat_lt}</div></div>
        </div>""", unsafe_allow_html=True)

        # ── Steps definition ──
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
        if pd.notna(tech_start) and str(tech_start).strip() not in ("","nan"):
            steps_def.insert(4,("Technical Test","start_technical_test","complete_technical_test","lt_tech_test","b_lt_tech","sla11"))

        # ── Build p_data ──
        p_data = []
        done_count = 0
        last_data_idx = -1   # index of last step that has ANY data (start or end)

        for i,(name,s_col,e_col,lt_col,b_lt_col,sla_col) in enumerate(steps_def):
            s_val = row.get(s_col)
            e_val = row.get(e_col)
            has_start = pd.notna(s_val) and str(s_val).strip() not in ("","nan")
            has_end   = pd.notna(e_val) and str(e_val).strip() not in ("","nan")

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
            sla_v     = str(row.get(sla_col,"")).strip()
            lt_a_str  = str(int(float(lt_actual))) if pd.notna(lt_actual) and str(lt_actual).strip() not in ("","nan") else None
            lt_b_str  = str(int(float(lt_budget))) if pd.notna(lt_budget) and str(lt_budget).strip() not in ("","nan") else None

            p_data.append({"name":name,"start":str(s_val) if has_start else "—",
                           "end":str(e_val) if has_end else "—","status":st_code,
                           "idx":i,"lt_actual":lt_a_str,"lt_budget":lt_b_str,"sla":sla_v})

        # ── Fix: mark failure ──
        # If FAILED, the last step that has any data is where it failed
        if is_failed and last_data_idx >= 0:
            p_data[last_data_idx]["status"] = "failed"
            # If it was counted as done, subtract
            if p_data[last_data_idx]["end"] != "—":
                done_count -= 1

        prog_pct = done_count / len(p_data) if p_data else 0

        # ── Progress bar ──
        if is_failed:
            bar_grad  = f"linear-gradient(90deg,{RD},#EF4444)"
            pct_color = RD
        else:
            bar_grad  = f"linear-gradient(90deg,{OR},{OR2})"
            pct_color = OR

        st.markdown(f"""
        <div class="pb-wrap">
          <div class="pb-top">
            <span class="pb-label">Recruitment Progress</span>
            <span class="pb-count">{done_count}/{len(p_data)} stages complete</span>
          </div>
          <div class="pb-track">
            <div style="height:100%;width:{prog_pct*100:.0f}%;background:{bar_grad};border-radius:3px;"></div>
          </div>
          <div class="pb-bottom">
            <span class="pb-hint">Overall completion</span>
            <span style="font-size:12px;font-weight:700;color:{pct_color};">{prog_pct*100:.0f}%</span>
          </div>
        </div>""", unsafe_allow_html=True)

        # ── Steps table ──
        st.markdown(_steps_table(p_data), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════
# ③ RECRUITMENT ROOM
# ═══════════════════════════════════════
def run_rec_room():
    st.markdown('<div class="pw">', unsafe_allow_html=True)

    col_hdr, col_back = st.columns([6,1])
    with col_hdr:
        st.markdown(f"""
        <div class="ph">
          <div class="ph-ico"><img src="{GITHUB_RAW}/home.png" style="width:20px;height:20px;object-fit:contain;" onerror="this.style.display='none'"/></div>
          <div><div class="ph-title">Recruitment Room</div><div class="ph-sub">Forms, spreadsheets, and tools — all in one place</div></div>
        </div>""", unsafe_allow_html=True)
    with col_back:
        st.markdown("<div style='padding-top:10px;'>", unsafe_allow_html=True)
        if st.button("← Home", key="back_rec"):
            st.session_state.page = "home"; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sd"></div>', unsafe_allow_html=True)

    # Form
    st.markdown(f"""
    <div class="rs">
      <div class="rs-hdr">
        <div class="rs-ico"><img src="{GITHUB_RAW}/form.png" onerror="this.style.display='none'" alt=""/></div>
        <div><div class="rs-title">Recruitment Form</div><div class="rs-sub">Powered by Google Apps Script</div></div>
      </div>
      <div class="rs-body">
        <div style="background:{GY2};border:1.5px solid {GY3};border-radius:9px;overflow:hidden;">
          <div style="padding:8px 14px;border-bottom:1px solid {GY3};background:{BK};display:flex;gap:6px;align-items:center;">
            <span style="width:8px;height:8px;border-radius:50%;background:#FF5F57;display:inline-block;"></span>
            <span style="width:8px;height:8px;border-radius:50%;background:#FFBD2E;display:inline-block;"></span>
            <span style="width:8px;height:8px;border-radius:50%;background:#28CA41;display:inline-block;"></span>
            <span style="margin-left:8px;font-size:10px;color:rgba(255,255,255,.45);font-family:'JetBrains Mono',monospace;">Recruitment Form</span>
          </div>
          <iframe src="{APPS_SCRIPT_URL}" width="100%" height="780" frameborder="0" style="border:none;display:block;"></iframe>
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

    # Quick Links
    st.markdown(f"""
    <div class="rs">
      <div class="rs-hdr">
        <div class="rs-ico"><img src="{GITHUB_RAW}/dashboard.png" onerror="this.style.display='none'" alt=""/></div>
        <div><div class="rs-title">Quick Links</div><div class="rs-sub">Spreadsheets & connected resources</div></div>
      </div>
      <div class="rs-body">""", unsafe_allow_html=True)

    st.caption("⚠️ Links reset on page refresh. To make permanent, add them in the code.")

    if "rec_links" not in st.session_state:
        st.session_state.rec_links = [
            {"label":"Recruitment Progress DB","url":"https://docs.google.com/spreadsheets/d/1eysrca2wIWsx2LZeP3z2qlRawLzdRBYxsDf6JizcaZc"},
            {"label":"MPP Tracker","url":""},
            {"label":"Backend / Position List","url":""},
        ]
    for i,link in enumerate(st.session_state.rec_links):
        ca,cb,cc = st.columns([2,4,1])
        with ca: nl = st.text_input("Label",value=link["label"],key=f"ll_{i}",label_visibility="collapsed")
        with cb: nu = st.text_input("URL",value=link["url"],key=f"lu_{i}",placeholder="https://...",label_visibility="collapsed")
        with cc:
            if st.button("↗",key=f"lo_{i}") and link["url"]:
                st.markdown(f'<script>window.open("{link["url"]}","_blank");</script>',unsafe_allow_html=True)
        st.session_state.rec_links[i]["label"]=nl
        st.session_state.rec_links[i]["url"]=nu

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    if st.button("＋ Add Link", key="add_link"):
        st.session_state.rec_links.append({"label":"New Link","url":""}); st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Quick Actions
    st.markdown(f"""
    <div class="rs">
      <div class="rs-hdr">
        <div class="rs-ico"><img src="{GITHUB_RAW}/dashboard.png" onerror="this.style.display='none'" alt=""/></div>
        <div><div class="rs-title">Quick Actions</div><div class="rs-sub">Shortcuts to common tasks</div></div>
      </div>
      <div class="rs-body">""", unsafe_allow_html=True)

    qa1,qa2,qa3,qa4 = st.columns(4)
    with qa1:
        if st.button("📊 Download PPT",use_container_width=True,key="qa_ppt"):
            st.info("⏳ PPT feature coming soon.")
    with qa2:
        if st.button("📈 Dashboard",use_container_width=True,key="qa_mpp"):
            st.session_state.page="home"; st.rerun()
    with qa3:
        if st.button("🔍 Tracking",use_container_width=True,key="qa_track"):
            st.session_state.page="tracking"; st.rerun()
    with qa4:
        if st.button("🔄 Refresh Cache",use_container_width=True,key="qa_cache"):
            st.cache_data.clear(); st.success("Cache cleared!")

    st.markdown("</div></div></div>", unsafe_allow_html=True)


# ── ROUTER ──
if   st.session_state.page == "home":     run_home()
elif st.session_state.page == "tracking": run_tracking()
elif st.session_state.page == "rec_room": run_rec_room()
