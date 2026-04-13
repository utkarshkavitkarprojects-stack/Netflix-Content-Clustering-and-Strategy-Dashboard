import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Netflix Content Strategy Dashboard",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Custom CSS (FINAL POLISH)
# -----------------------------
st.markdown("""
<style>

/* ============================= */
/* GLOBAL TEXT FIX */
/* ============================= */
html, body, [class*="css"]  {
    color: white !important;
}

/* App Background */
.stApp {
    background-color: #0e1117;
    color: white !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161a23;
    border-right: 1px solid #2a2f3a;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ============================= */
/* HEADINGS FIX */
/* ============================= */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
}

/* Section Headers */
.section-header {
    color: #ffffff !important;
}

/* ============================= */
/* METRICS FIX */
/* ============================= */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1c1f26, #111827);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #2a2f3a;
}

/* Metric labels (Total Titles etc.) */
[data-testid="stMetricLabel"] {
    color: #9ca3af !important;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

/* ============================= */
/* INPUTS FIX */
/* ============================= */
label, .stSelectbox label, .stTextInput label {
    color: white !important;
}

input, textarea {
    color: white !important;
}

/* Dropdown text */
div[data-baseweb="select"] * {
    color: white !important;
}

/* ============================= */
/* TABLE FIX */
/* ============================= */
.stDataFrame {
    color: white !important;
}

/* ============================= */
/* BUTTON FIX */
/* ============================= */
.stDownloadButton > button {
    background-color: #e50914;
    color: white !important;
}

/* ============================= */
/* CLUSTER CARD */
/* ============================= */
.cluster-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 25px;
    border-radius: 14px;
    border-left: 6px solid #e50914;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    color: white !important;
}

/* ============================= */
/* FIX DROPDOWN VISIBILITY */
/* ============================= */

/* Dropdown selected value (visible box) */
div[data-baseweb="select"] > div {
    background-color: #1f2937 !important;
    color: white !important;
}

/* Dropdown menu (when opened) */
ul[role="listbox"] {
    background-color: white !important;
}

/* Dropdown options text */
ul[role="listbox"] li {
    color: black !important;
}

/* Hover effect */
ul[role="listbox"] li:hover {
    background-color: #e5e7eb !important;
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("artifacts/clustered_netflix_data.csv")

df = load_data()

# -----------------------------
# Cleaning
# -----------------------------
cols = ["title", "type", "duration", "listed_in", "country", "rating", "description"]
for col in cols:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎯 Filter Content")

cluster_options = sorted(df["cluster_label"].dropna().unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", cluster_options)

search_title = st.sidebar.text_input("🔍 Search Title")

type_options = ["All"] + sorted(df["type"].dropna().unique())
selected_type = st.sidebar.selectbox("Filter by Type", type_options)

rating_options = ["All"] + sorted(df["rating"].dropna().unique())
selected_rating = st.sidebar.selectbox("Filter by Rating", rating_options)

# -----------------------------
# Filtering
# -----------------------------
cluster_df = df[df["cluster_label"] == selected_cluster].copy()

if search_title:
    cluster_df = cluster_df[
        cluster_df["title"].str.contains(search_title, case=False, na=False)
    ]

if selected_type != "All":
    cluster_df = cluster_df[cluster_df["type"] == selected_type]

if selected_rating != "All":
    cluster_df = cluster_df[cluster_df["rating"] == selected_rating]

summary_df = df[df["cluster_label"] == selected_cluster]

# -----------------------------
# Helper Functions
# -----------------------------
def avg_year(data):
    return round(data["release_year"].mean(), 1)

def cluster_desc(name):
    mapping = {
        "Modern Streaming-Era Content (Series + Mature Films)":
        "Netflix-era binge content. Dominated by TV shows, global content, and mature storytelling.",
        "Classic & Legacy Cinema":
        "Older archival content focused on nostalgia and classic storytelling.",
        "Mature & Independent Adult Content (Movies + Series)":
        "Serious, indie, and darker themed content targeting niche audiences.",
        "Mainstream Global Feature Films":
        "Commercial cinema with broad appeal across genres and regions."
    }
    return mapping.get(name, "")

# -----------------------------
# Title
# -----------------------------
st.markdown(
    """
    <div style='text-align: center; padding: 10px 0 20px 0;'>
        <h1 style='font-size: 40px; font-weight: 800; color: white; margin-bottom: 10px;'>
            🎬 Netflix Content Strategy Dashboard
        </h1>
        <p style='font-size: 15px; color: #9ca3af;'>
            AI-powered clustering to understand content strategy & audience segmentation
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# -----------------------------
# Tabs (🔥 BIG UPGRADE)
# -----------------------------
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Insights", "📺 Explore Data"])

# =============================
# TAB 1: OVERVIEW
# =============================
with tab1:

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Titles", len(df))
    col2.metric("Clusters", df["cluster_label"].nunique())
    col3.metric("Titles in Cluster", len(summary_df))
    col4.metric("Avg Release Year", avg_year(summary_df))

    st.markdown(
        f"""
        <div class="cluster-card">
            <h2>📌 {selected_cluster}</h2>
            <p>{cluster_desc(selected_cluster)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =============================
# TAB 2: INSIGHTS
# =============================
with tab2:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="section-header">🎭 Top Genres</div>', unsafe_allow_html=True)
        st.dataframe(summary_df["listed_in"].value_counts().head(5))

    with col2:
        st.markdown('<div class="section-header">🌍 Top Countries</div>', unsafe_allow_html=True)
        st.dataframe(summary_df["country"].value_counts().head(5))

    with col3:
        st.markdown('<div class="section-header">⭐ Top Ratings</div>', unsafe_allow_html=True)
        st.dataframe(summary_df["rating"].value_counts().head(5))

    st.markdown('<div class="section-header">📊 Content Type Distribution</div>', unsafe_allow_html=True)
    st.bar_chart(summary_df["type"].value_counts(), use_container_width=True)

# =============================
# TAB 3: EXPLORE
# =============================
with tab3:

    st.markdown('<div class="section-header">📺 Browse Titles</div>', unsafe_allow_html=True)

    table_cols = [
        "title", "type", "country", "listed_in",
        "rating", "release_year", "duration", "description"
    ]

    if cluster_df.empty:
        st.warning("No results found.")
    else:
        st.dataframe(cluster_df[table_cols], height=500)

    st.markdown("### 📥 Download Data")

    csv = cluster_df[table_cols + ["cluster_label"]].to_csv(index=False).encode("utf-8")

    st.download_button("Download CSV", csv, "filtered_data.csv")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🚀 Built by Utkarsh | Netflix Clustering ML Project | 2026 Portfolio")