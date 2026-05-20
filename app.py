import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-rec-466x.onrender.com"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="CineVerse",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================
# CINEMATIC 3D STYLES
# =============================
st.markdown(
    """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;500;600;700&display=swap');

/* ── Root Variables ── */
:root {
    --gold:     #e8b86d;
    --gold-dim: #a07840;
    --bg:       #080c14;
    --bg2:      #0d1220;
    --bg3:      #131929;
    --glass:    rgba(255,255,255,0.04);
    --glass-b:  rgba(255,255,255,0.09);
    --text:     #e8eaf0;
    --muted:    #7a839a;
    --accent:   #4a9eff;
    --red:      #e85555;
    --r:        14px;
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

/* ── Animated starfield background ── */
.main > .block-container::before {
    content: '';
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image:
        radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 30% 70%, rgba(255,255,255,0.3) 0%, transparent 100%),
        radial-gradient(1px 1px at 50% 10%, rgba(255,255,255,0.35) 0%, transparent 100%),
        radial-gradient(1px 1px at 70% 40%, rgba(255,255,255,0.25) 0%, transparent 100%),
        radial-gradient(1px 1px at 85% 80%, rgba(255,255,255,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 20% 90%, rgba(255,255,255,0.2) 0%, transparent 100%),
        radial-gradient(1px 1px at 95% 50%, rgba(255,255,255,0.3) 0%, transparent 100%),
        radial-gradient(1px 1px at 60% 95%, rgba(255,255,255,0.25) 0%, transparent 100%);
    z-index: 0;
}

/* ── Top ambient glow ── */
.main > .block-container::after {
    content: '';
    position: fixed;
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    width: 900px;
    height: 400px;
    background: radial-gradient(ellipse, rgba(74,158,255,0.07) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ── Main container ── */
.main > .block-container {
    padding: 1.5rem 2rem 4rem !important;
    max-width: 1500px !important;
    position: relative;
    z-index: 1;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0b1020 0%, #060910 100%) !important;
    border-right: 1px solid rgba(232,184,109,0.12) !important;
}
[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.25rem !important;
}

/* ── HERO TITLE ── */
.hero-title {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: clamp(3.5rem, 7vw, 6rem) !important;
    letter-spacing: 6px;
    background: linear-gradient(135deg, #fff 0%, var(--gold) 50%, #e06060 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin: 0;
    text-shadow: none;
}
.hero-sub {
    font-size: 0.85rem;
    color: var(--muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0.4rem;
}

/* ── Divider ── */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(232,184,109,0.3), transparent) !important;
    margin: 1.2rem 0 !important;
}

/* ── Search input ── */
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(232,184,109,0.25) !important;
    border-radius: 50px !important;
    color: var(--text) !important;
    padding: 0.6rem 1.4rem !important;
    font-size: 1rem !important;
    font-family: 'Outfit', sans-serif !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(232,184,109,0.15), 0 0 30px rgba(232,184,109,0.08) !important;
    outline: none !important;
}
[data-testid="stTextInput"] input::placeholder {
    color: var(--muted) !important;
}
[data-testid="stTextInput"] label {
    color: var(--gold) !important;
    font-size: 0.78rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(232,184,109,0.2) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
}
[data-testid="stSelectbox"] label {
    color: var(--gold) !important;
    font-size: 0.75rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}

/* ── Slider ── */
[data-testid="stSlider"] label {
    color: var(--gold) !important;
    font-size: 0.75rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}
[data-testid="stSlider"] .st-ae {
    background: var(--gold) !important;
}
[data-testid="stSlider"] .st-af {
    background: rgba(255,255,255,0.1) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, rgba(232,184,109,0.12), rgba(232,184,109,0.05)) !important;
    border: 1px solid rgba(232,184,109,0.35) !important;
    border-radius: 50px !important;
    color: var(--gold) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    padding: 0.35rem 1rem !important;
    transition: all 0.25s ease !important;
    cursor: pointer !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(232,184,109,0.22), rgba(232,184,109,0.1)) !important;
    border-color: var(--gold) !important;
    box-shadow: 0 4px 20px rgba(232,184,109,0.2), 0 0 0 1px rgba(232,184,109,0.15) !important;
    transform: translateY(-1px) !important;
    color: #fff !important;
}
.stButton > button:active {
    transform: translateY(0px) scale(0.97) !important;
}

/* ── 3D MOVIE CARD GRID ── */
.movie-card-wrap {
    perspective: 800px;
    margin-bottom: 0.5rem;
}
.movie-card {
    background: linear-gradient(160deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: var(--r);
    overflow: hidden;
    transform: rotateY(0deg) rotateX(0deg) scale(1);
    transform-style: preserve-3d;
    transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
    position: relative;
}
.movie-card:hover {
    transform: rotateY(-4deg) rotateX(3deg) scale(1.03) translateY(-4px);
    box-shadow: 8px 12px 40px rgba(0,0,0,0.6), 0 0 25px rgba(232,184,109,0.15);
    border-color: rgba(232,184,109,0.3);
}
.movie-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, transparent 60%);
    pointer-events: none;
    border-radius: var(--r);
}
.movie-poster img {
    border-radius: var(--r) var(--r) 0 0;
    display: block;
    width: 100%;
    transition: filter 0.3s;
}
.movie-card:hover .movie-poster img {
    filter: brightness(1.1) saturate(1.15);
}
.movie-card-title {
    font-size: 0.78rem;
    font-weight: 500;
    color: var(--text);
    padding: 6px 8px 2px;
    line-height: 1.2;
    height: 2.2rem;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}

/* ── Section headings ── */
.section-heading {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.8rem;
    letter-spacing: 4px;
    color: var(--gold);
    margin: 1.5rem 0 0.8rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(232,184,109,0.3), transparent);
}

/* ── Sidebar menu labels ── */
.sidebar-label {
    font-size: 0.7rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--muted);
    margin: 1.2rem 0 0.4rem;
    font-weight: 600;
}

/* ── Detail page ── */
.detail-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 2rem;
    backdrop-filter: blur(10px);
}
.detail-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2rem, 4vw, 3.5rem);
    letter-spacing: 3px;
    background: linear-gradient(135deg, #fff 0%, var(--gold) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.5rem;
    line-height: 1.1;
}
.detail-meta-pill {
    display: inline-block;
    background: rgba(232,184,109,0.12);
    border: 1px solid rgba(232,184,109,0.25);
    border-radius: 50px;
    padding: 3px 14px;
    font-size: 0.76rem;
    color: var(--gold);
    letter-spacing: 1px;
    margin: 0 6px 6px 0;
    font-weight: 500;
}
.detail-overview {
    font-size: 0.95rem;
    line-height: 1.75;
    color: rgba(232,234,240,0.85);
    margin-top: 1rem;
}

/* ── Poster 3D frame ── */
.poster-3d-wrap {
    perspective: 1000px;
}
.poster-3d {
    border-radius: 16px;
    border: 2px solid rgba(232,184,109,0.25);
    box-shadow: 20px 20px 60px rgba(0,0,0,0.7), -4px -4px 20px rgba(232,184,109,0.08);
    transform: rotateY(-6deg) rotateX(2deg);
    transition: transform 0.4s ease;
    overflow: hidden;
}
.poster-3d:hover {
    transform: rotateY(0deg) rotateX(0deg);
}

/* ── Backdrop ── */
.backdrop-wrap {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.07);
    margin-top: 1rem;
    position: relative;
}
.backdrop-wrap::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to right, rgba(8,12,20,0.5), transparent 40%, transparent 60%, rgba(8,12,20,0.5));
    pointer-events: none;
}

/* ── Info/error messages ── */
.stAlert {
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    background: rgba(255,255,255,0.04) !important;
}

/* ── Streamlit image tweaks ── */
[data-testid="stImage"] img {
    border-radius: 12px;
}

/* ── Caption ── */
.stCaption {
    color: var(--muted) !important;
    font-size: 0.78rem !important;
}

/* ── Markdown text ── */
.stMarkdown p, .stMarkdown div {
    color: var(--text);
}

/* ── No poster placeholder ── */
.no-poster {
    background: linear-gradient(135deg, #0d1425, #141d30);
    border: 1px dashed rgba(255,255,255,0.1);
    border-radius: var(--r);
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--muted);
    font-size: 2rem;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: rgba(232,184,109,0.25); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(232,184,109,0.45); }

/* ── Sidebar home button ── */
[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(135deg, rgba(232,184,109,0.18), rgba(232,184,109,0.06)) !important;
    border: 1px solid rgba(232,184,109,0.4) !important;
    font-size: 0.82rem !important;
    padding: 0.5rem 1.2rem !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


# =============================
# CARD RENDERERS
# =============================
def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return
    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols, gap="small")
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1
            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")
            with colset[c]:
                # Card wrapper with 3D hover via CSS
                st.markdown("<div class='movie-card-wrap'><div class='movie-card'>", unsafe_allow_html=True)
                if poster:
                    st.markdown(f"<div class='movie-poster'><img src='{poster}' style='width:100%;border-radius:14px 14px 0 0;'/></div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='no-poster'>🎬</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='movie-card-title'>{title}</div>", unsafe_allow_html=True)
                st.markdown("</div></div>", unsafe_allow_html=True)
                if st.button("▶ Open", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}"):
                    if tmdb_id:
                        goto_details(tmdb_id)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append({
                "tmdb_id": tmdb["tmdb_id"],
                "title": tmdb.get("title") or x.get("title") or "Untitled",
                "poster_url": tmdb.get("poster_url"),
            })
    return cards


def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()
    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append({
                "tmdb_id": int(tmdb_id),
                "title": title,
                "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                "release_date": m.get("release_date", ""),
            })
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append({
                "tmdb_id": int(tmdb_id),
                "title": title,
                "poster_url": poster_url,
                "release_date": m.get("release_date", ""),
            })
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 0.5rem 0 1.5rem;'>
            <div style='font-family:"Bebas Neue",sans-serif; font-size:2rem; letter-spacing:5px;
                        background:linear-gradient(135deg,#fff,#e8b86d);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
                CINEVERSE
            </div>
            <div style='font-size:0.65rem; letter-spacing:3px; color:#4a9eff; text-transform:uppercase; margin-top:2px;'>
                Your Cinema Universe
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🏠  Home"):
        goto_home()

    st.markdown("<div class='sidebar-label'>Browse Category</div>", unsafe_allow_html=True)
    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
        label_visibility="collapsed",
    )

    st.markdown("<div class='sidebar-label'>Grid Columns</div>", unsafe_allow_html=True)
    grid_cols = st.slider("Columns", 4, 8, 6, label_visibility="collapsed")

    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("""
        <div style='font-size:0.7rem; color:#3a4260; text-align:center; margin-top:1rem; letter-spacing:1px;'>
            Powered by TMDB · TF-IDF Engine
        </div>
    """, unsafe_allow_html=True)


# =============================
# HERO HEADER
# =============================
col_hero, _ = st.columns([3, 1])
with col_hero:
    st.markdown("""
        <div style='padding: 0.5rem 0 0.8rem;'>
            <div class='hero-title'>CINEVERSE</div>
            <div class='hero-sub'>✦ Discover · Explore · Experience ✦</div>
        </div>
    """, unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)


# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    typed = st.text_input(
        "🔍  Search Movies",
        placeholder="Search by title — avenger, inception, love...",
    )

    st.markdown("<hr/>", unsafe_allow_html=True)

    # SEARCH MODE
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters to search.")
        else:
            with st.spinner("Searching the universe..."):
                data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

                if suggestions:
                    labels = ["— Select a title —"] + [s[0] for s in suggestions]
                    selected = st.selectbox("Matching Titles", labels, index=0)
                    if selected != "— Select a title —":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.info("No matching titles found. Try another keyword.")

                st.markdown(
                    f"<div class='section-heading'>🔎 Search Results</div>",
                    unsafe_allow_html=True,
                )
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")
        st.stop()

    # HOME FEED
    cat_display = home_category.replace("_", " ").upper()
    st.markdown(
        f"<div class='section-heading'>✦ {cat_display}</div>",
        unsafe_allow_html=True,
    )

    with st.spinner("Loading..."):
        home_cards, err = api_get_json("/home", params={"category": home_category, "limit": 24})

    if err or not home_cards:
        st.error(f"Could not load feed: {err or 'Unknown error'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")


# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    # Back button
    back_col, _ = st.columns([1, 5])
    with back_col:
        if st.button("← Back"):
            goto_home()

    with st.spinner("Loading movie details..."):
        data, err = api_get_json(f"/movie/id/{tmdb_id}")

    if err or not data:
        st.error(f"Could not load movie: {err or 'Unknown error'}")
        st.stop()

    # ── Backdrop ──
    if data.get("backdrop_url"):
        st.markdown("<div class='backdrop-wrap'>", unsafe_allow_html=True)
        st.image(data["backdrop_url"], use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Poster + Details ──
    left, right = st.columns([1, 2.6], gap="large")

    with left:
        if data.get("poster_url"):
            st.markdown("<div class='poster-3d-wrap'><div class='poster-3d'>", unsafe_allow_html=True)
            st.image(data["poster_url"], use_column_width=True)
            st.markdown("</div></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='no-poster' style='height:350px;'>🎬</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='detail-card'>", unsafe_allow_html=True)

        title_text = data.get("title", "Unknown Title")
        st.markdown(f"<div class='detail-title'>{title_text}</div>", unsafe_allow_html=True)

        # Meta pills
        pills = ""
        release = (data.get("release_date") or "")[:4]
        if release:
            pills += f"<span class='detail-meta-pill'>📅 {release}</span>"

        genres = data.get("genres", [])
        for g in genres[:4]:
            pills += f"<span class='detail-meta-pill'>{g['name']}</span>"

        if data.get("vote_average"):
            score = round(data["vote_average"], 1)
            pills += f"<span class='detail-meta-pill'>⭐ {score}</span>"

        if pills:
            st.markdown(f"<div style='margin-bottom:0.5rem;'>{pills}</div>", unsafe_allow_html=True)

        st.markdown("<hr/>", unsafe_allow_html=True)

        overview = data.get("overview") or "No overview available."
        st.markdown(
            f"<div class='detail-overview'>{overview}</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Recommendations ──
    st.markdown("<hr/>", unsafe_allow_html=True)
    title = (data.get("title") or "").strip()

    if title:
        with st.spinner("Finding similar movies..."):
            bundle, err2 = api_get_json(
                "/movie/search",
                params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
            )

        if not err2 and bundle:
            tfidf_cards = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            genre_cards = bundle.get("genre_recommendations", [])

            if tfidf_cards:
                st.markdown(
                    "<div class='section-heading'>🔎 Similar Movies</div>",
                    unsafe_allow_html=True,
                )
                poster_grid(tfidf_cards, cols=grid_cols, key_prefix="details_tfidf")

            if genre_cards:
                st.markdown(
                    "<div class='section-heading'>🎭 More Like This</div>",
                    unsafe_allow_html=True,
                )
                poster_grid(genre_cards, cols=grid_cols, key_prefix="details_genre")
        else:
            st.info("Showing genre-based recommendations.")
            with st.spinner("Loading..."):
                genre_only, err3 = api_get_json(
                    "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
                )
            if not err3 and genre_only:
                st.markdown(
                    "<div class='section-heading'>🎭 You May Also Like</div>",
                    unsafe_allow_html=True,
                )
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")