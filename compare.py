
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CreatorFlow | Video Comparison",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #100d1d, #19132b, #10121d);
    color: #f5f3ff;
}
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}
section[data-testid="stSidebar"] {
    background: #100e1b;
}
div[data-testid="stMetric"] {
    background: #211a35;
    border: 1px solid #40315e;
    border-radius: 14px;
    padding: 16px;
}
div[data-testid="stMetricValue"] {
    color: #c4a5ff;
}
.stButton > button, .stFormSubmitButton > button {
    background: #8b5cf6;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 42px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Video Comparison Dashboard")
st.write("Compare video metrics and discover which video performed best.")
st.caption("CreatorFlow · Comparative analytics prototype")

st.info(
    "Enter public video metrics manually. Use real figures where available "
    "and label estimates clearly. This tool does not fetch data automatically."
)

if "videos" not in st.session_state:
    st.session_state.videos = [
        {
            "Video": "Abhijeet Kain - Test Video",
            "Views": 4900000,
            "Likes": 103000,
            "Comments": 0,
            "Shares": 0,
        }
    ]

st.subheader("➕ Add a video")

with st.form("add_video_form", clear_on_submit=True):
    name = st.text_input(
        "Video name",
        placeholder="e.g. Python tips Reel",
    )

    c1, c2 = st.columns(2)

    with c1:
        views = st.number_input(
            "Views",
            min_value=0,
            value=0,
            step=100,
        )
        likes = st.number_input(
            "Likes",
            min_value=0,
            value=0,
            step=10,
        )

    with c2:
        comments = st.number_input(
            "Comments",
            min_value=0,
            value=0,
            step=1,
        )
        shares = st.number_input(
            "Shares",
            min_value=0,
            value=0,
            step=1,
        )

    submitted = st.form_submit_button("Add video ➕")

if submitted:
    if not name.strip():
        st.error("Please enter a video name.")
    elif any(v["Video"].casefold() == name.strip().casefold()
             for v in st.session_state.videos):
        st.error("A video with this name already exists. Use a different name.")
    else:
        st.session_state.videos.append({
            "Video": name.strip(),
            "Views": int(views),
            "Likes": int(likes),
            "Comments": int(comments),
            "Shares": int(shares),
        })
        st.success(f"{name.strip()} added successfully!")
        st.rerun()

st.divider()
st.subheader("🎬 Video performance")

rows = []

for video in st.session_state.videos:
    interactions = video["Likes"] + video["Comments"] + video["Shares"]
    rate = interactions / video["Views"] * 100 if video["Views"] > 0 else 0

    rows.append({
        "Video": video["Video"],
        "Views": video["Views"],
        "Likes": video["Likes"],
        "Comments": video["Comments"],
        "Shares": video["Shares"],
        "Total interactions": interactions,
        "Interaction rate (%)": round(rate, 2),
    })

df = pd.DataFrame(rows)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
)

if len(df) >= 1:
    st.subheader("🏆 Performance summary")

    eligible = df[df["Views"] > 0]

    if not eligible.empty:
        best_index = eligible["Interaction rate (%)"].idxmax()
        best = eligible.loc[best_index]

        col1, col2, col3 = st.columns(3)

        col1.metric("Videos compared", len(df))
        col2.metric("Highest interaction rate", f'{best["Interaction rate (%)"]:.2f}%')
        col3.metric("Most-viewed video", f'{df.loc[df["Views"].idxmax(), "Video"]}')

        st.success(
            f'🏆 Highest interaction rate: **{best["Video"]}** '
            f'({best["Interaction rate (%)"]:.2f}%)'
        )

        st.caption(
            "Ranking is based on interaction rate, not total views. "
            "Comments and shares affect the rate, so enter them when available."
        )
    else:
        st.warning("Add at least one video with more than zero views to compare performance.")

if len(df) >= 2:
    st.subheader("📈 Compare interaction rates")

    chart_data = df.set_index("Video")[["Interaction rate (%)"]]
    st.bar_chart(chart_data)

    st.subheader("💡 What the comparison tells you")

    eligible = df[df["Views"] > 0]

    if len(eligible) >= 2:
        best_rate = eligible["Interaction rate (%)"].max()
        lowest_rate = eligible["Interaction rate (%)"].min()

        if best_rate == lowest_rate:
            st.write(
                "The videos have the same interaction rate. "
                "Compare their topics, formats and audience response for further insights."
            )
        else:
            best_video = eligible.loc[
                eligible["Interaction rate (%)"].idxmax(), "Video"
            ]
            lowest_video = eligible.loc[
                eligible["Interaction rate (%)"].idxmin(), "Video"
            ]

            st.write(
                f"**{best_video}** has the highest interaction rate, while "
                f"**{lowest_video}** has the lowest among videos with views. "
                "Review their hooks, topics and calls to action to identify possible differences."
            )

st.divider()

if st.button("🗑️ Reset comparison data"):
    st.session_state.videos = []
    st.rerun()

st.caption(
    "Note: Interaction rate = (likes + comments + shares) ÷ views × 100. "
    "This is a rule-based comparison, not a guarantee of content quality."
)
