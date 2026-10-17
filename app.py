
import streamlit as st
import random
import re
from datetime import date

st.set_page_config(
    page_title="CreatorFlow | AI Content Studio",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #100d1d 0%, #17132b 55%, #100f1b 100%);
    color: #f5f3ff;
}
section[data-testid="stSidebar"] {
    background: #100e1b;
    border-right: 1px solid #302648;
}
.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}
h1, h2, h3 {
    color: #f5f3ff !important;
}
p, label, .stMarkdown {
    color: #d5cfe8;
}
div[data-testid="stMetric"] {
    background: #211a35;
    border: 1px solid #40315e;
    border-radius: 16px;
    padding: 18px;
}
div[data-testid="stMetricValue"] {
    color: #c4a5ff;
}
.stButton > button, .stFormSubmitButton > button {
    background: linear-gradient(100deg, #8b5cf6, #a855f7);
    color: white;
    border: 0;
    border-radius: 12px;
    min-height: 44px;
    font-weight: 700;
    width: 100%;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: #7c3aed;
    color: white;
    border: 1px solid #c4b5fd;
}
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background: #1d1830;
    color: white;
    border: 1px solid #493866;
    border-radius: 10px;
}
div[data-baseweb="select"] > div {
    background: #1d1830;
    border-color: #493866;
    border-radius: 10px;
}
div[data-testid="stChatMessage"] {
    background: #211a35;
    border: 1px solid #40315e;
    border-radius: 16px;
    padding: 14px;
}
.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(120deg, #30204e, #201a36 65%, #19232e);
    border: 1px solid #574078;
    margin-bottom: 24px;
}
.hero-tag {
    color: #c4b5fd;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.hero-title {
    color: white;
    font-size: 38px;
    font-weight: 800;
    line-height: 1.2;
    margin: 10px 0;
}
.hero-subtitle {
    color: #d8d0eb;
    font-size: 16px;
}
.tool-card {
    background: #201a32;
    border: 1px solid #3c3054;
    border-radius: 17px;
    padding: 20px;
    min-height: 145px;
}
.tool-icon {
    font-size: 28px;
}
.tool-title {
    color: #f5f3ff;
    font-size: 18px;
    font-weight: 700;
    margin: 9px 0;
}
.tool-description {
    color: #bdb3d4;
    font-size: 13px;
}
.small-note {
    color: #a99cbe;
    font-size: 12px;
}
hr {
    border-color: #342845;
}
</style>
""", unsafe_allow_html=True)


# -------------------- CONTENT LOGIC --------------------

def make_story(topic, audience, style):
    hooks = {
        "Educational": f"Here's what you need to know about {topic}.",
        "Funny": f"POV: You thought you understood {topic} 😂",
        "Motivational": f"Your reminder to get better at {topic} starts now.",
        "Professional": f"Let's break down {topic} in a simple, practical way.",
        "Storytelling": f"I wish someone had told me this about {topic} earlier.",
    }

    scenes = [
        ("Scene 1 — The hook", hooks[style]),
        ("Scene 2 — Set the context",
         f"Introduce the main challenge related to {topic}. Connect it to {audience}."),
        ("Scene 3 — The value",
         f"Share one useful tip, example, or lesson about {topic}. Keep it clear and relatable."),
        ("Scene 4 — The takeaway",
         f"Give {audience} one practical action they can try today."),
    ]

    caption = (
        f"Let's talk about {topic}! 💡 "
        f"If you're interested in this, save this post and share your thoughts."
    )
    tags = ["#ContentCreator", "#LearnSomethingNew", "#CreatorFlow"]
    clean_topic = re.sub(r"[^a-zA-Z0-9]", "", topic.title().replace(" ", ""))
    if clean_topic:
        tags.insert(0, "#" + clean_topic)

    return {
        "hook": hooks[style],
        "scenes": scenes,
        "caption": caption,
        "hashtags": " ".join(tags),
        "cta": "Save this for later and comment your biggest takeaway!",
        "tips": [
            "Keep the opening 2–3 seconds engaging.",
            "Use readable on-screen text and clear visuals.",
            "End with one specific call to action.",
        ],
    }


def make_plan(niche, platform, goal, frequency):
    ideas = [
        ("Quick tip", f"Share one practical {niche} tip."),
        ("Myth vs fact", f"Clear up a common misconception about {niche}."),
        ("Behind the scenes", f"Show your process or routine related to {niche}."),
        ("Beginner guide", f"Explain one {niche} concept for beginners."),
        ("Common mistakes", f"List three mistakes people make with {niche}."),
        ("Personal story", f"Share a lesson you learned about {niche}."),
        ("Q&A", f"Answer a frequently asked question about {niche}."),
    ]

    if goal == "Engagement":
        ideas = [
            ("Ask the audience", f"Ask followers about their experience with {niche}."),
            ("This or that", f"Create a poll or comparison about {niche}."),
            ("Hot take", f"Share a thoughtful opinion about {niche}."),
            ("Q&A", f"Answer a question your audience often asks."),
            ("Challenge", f"Invite viewers to try a small {niche} challenge."),
            ("Myth vs fact", f"Ask viewers which belief about {niche} they agree with."),
            ("Community spotlight", "Highlight a useful audience comment or contribution."),
        ]
    elif goal == "Reach":
        ideas = [
            ("Trend with a twist", f"Adapt a relevant trend to {niche}."),
            ("Relatable moment", f"Show a relatable situation in {niche}."),
            ("Quick tips", f"Share three fast tips about {niche}."),
            ("Mistakes to avoid", f"Show a common mistake in {niche}."),
            ("Before and after", f"Show a process or progress related to {niche}."),
            ("Unexpected fact", f"Share a surprising fact about {niche}."),
            ("Beginner guide", f"Make {niche} easier for a first-time viewer."),
        ]

    plan = []
    for i in range(frequency):
        title, description = ideas[i % len(ideas)]
        plan.append({
            "day": f"Day {i + 1}",
            "title": title,
            "description": description,
            "platform": platform,
        })
    return plan


def analyse_performance(views, likes, comments, shares):
    interactions = likes + comments + shares
    rate = (interactions / views * 100) if views > 0 else 0

    if views == 0:
        suggestions = [
            "Enter a non-zero view count to calculate the interaction rate.",
            "Use a clear opening hook and a relevant caption.",
        ]
    else:
        suggestions = []
        if rate < 2:
            suggestions.append(
                "Interactions are relatively low compared with views. Try a clearer question or a stronger call to action."
            )
        elif rate < 5:
            suggestions.append(
                "There is room to improve engagement. Test a more specific hook and invite viewers to respond."
            )
        else:
            suggestions.append(
                "Your interaction rate is promising. Test similar topics and formats to see what keeps working."
            )

        if comments < likes * 0.1:
            suggestions.append(
                "Try a conversation starter to encourage more comments."
            )
        if shares < views * 0.01:
            suggestions.append(
                "Make the content more shareable with useful tips, checklists, or relatable examples."
            )
        if not suggestions:
            suggestions.append(
                "Keep testing content formats and compare results across several posts."
            )

    return interactions, rate, suggestions


def get_chat_reply(message):
    text = message.lower()

    if any(word in text for word in ["hello", "hi", "hey", "help"]):
        return (
            "Hey, creator! 💜 I'm your CreatorFlow assistant. "
            "I can help you brainstorm content, build a weekly plan, "
            "or understand post performance. Pick a tool from the sidebar, "
            "or tell me what you want to create."
        )

    if any(word in text for word in ["script", "story", "idea", "reel", "hook", "caption"]):
        return (
            "Let's turn that idea into content! ✨ Open **Idea-to-Story** "
            "in the sidebar. Enter your topic, target audience, and style "
            "to get a hook, scene outline, caption, hashtags, and CTA."
        )

    if any(word in text for word in ["plan", "calendar", "schedule", "week", "weekly"]):
        return (
            "Planning mode activated! 🗓️ Open **Smart Content Planner** "
            "in the sidebar. Choose your niche, platform, goal, and how "
            "many days you want to plan."
        )

    if any(word in text for word in ["views", "likes", "shares", "performance", "engagement", "analytics"]):
        return (
            "Let's inspect those numbers! 📊 Open **Performance Detective** "
            "and enter your views, likes, comments, and shares. "
            "I'll calculate the interaction rate and suggest improvements."
        )

    if any(word in text for word in ["instagram", "youtube", "creator", "content"]):
        return (
            "Nice! 💜 Start with your content goal. For a single post, "
            "use **Idea-to-Story**. For a multi-day schedule, use "
            "**Smart Content Planner**. To review metrics, use "
            "**Performance Detective**."
        )

    return (
        "I'm ready to help! 💜 Try asking about a content idea, a weekly plan, "
        "or post performance. You can also open any tool in the sidebar. "
        "I'm a rule-based assistant in this version, so I work best with these tasks."
    )


# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.markdown("# 💜 CreatorFlow")
    st.caption("YOUR SHORT-FORM CONTENT STUDIO")
    st.divider()

    page = st.radio(
        "WORKSPACE",
        [
            "🏠 Chatbot Home",
            "✨ Idea-to-Story",
            "🗓️ Smart Content Planner",
            "📊 Performance Detective",
        ],
        label_visibility="visible",
    )

    st.divider()
    st.markdown("**Made for creators**")
    st.caption("Plan smarter. Create consistently. Learn from your numbers.")
    st.markdown("---")
    st.caption("CreatorFlow · Rule-based prototype")


# -------------------- CHATBOT HOME --------------------

if page == "🏠 Chatbot Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">✦ Your creative workspace</div>
        <div class="hero-title">Create content.<br>Find your flow.</div>
        <div class="hero-subtitle">
            Brainstorm ideas, plan your next posts, and turn performance
            numbers into practical next steps.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">✨</div>
            <div class="tool-title">Idea-to-Story</div>
            <div class="tool-description">Turn a topic into a hook, scene outline, caption and hashtags.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🗓️</div>
            <div class="tool-title">Smart Planner</div>
            <div class="tool-description">Build a content schedule around your niche and goals.</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">📊</div>
            <div class="tool-title">Performance Detective</div>
            <div class="tool-description">Calculate interaction rates and get improvement suggestions.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 💬 Your creator assistant")
    st.caption("Ask for help with ideas, planning, captions, or performance.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": (
                    "Hey! Welcome to CreatorFlow 💜 What are we working on today? "
                    "I can guide you through content ideas, weekly planning, "
                    "or performance analysis."
                ),
            }
        ]

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Try: Help me plan a week of fitness content...")
    if prompt:
        st.session_state.chat_history.append(
            {"role": "user", "content": prompt}
        )
        reply = get_chat_reply(prompt)
        st.session_state.chat_history.append(
            {"role": "assistant", "content": reply}
        )
        st.rerun()

    st.markdown("**Quick prompts**")
    q1, q2, q3 = st.columns(3)
    with q1:
        if st.button("✨ Create a reel idea"):
            st.session_state.chat_history.append({
                "role": "user", "content": "Help me create a reel idea."
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": get_chat_reply("Help me create a reel idea.")
            })
            st.rerun()
    with q2:
        if st.button("🗓️ Plan my week"):
            st.session_state.chat_history.append({
                "role": "user", "content": "Help me plan my week."
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": get_chat_reply("Help me plan my week.")
            })
            st.rerun()
    with q3:
        if st.button("📊 Check performance"):
            st.session_state.chat_history.append({
                "role": "user", "content": "Help me analyse performance."
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": get_chat_reply("Help me analyse performance.")
            })
            st.rerun()


# -------------------- IDEA-TO-STORY --------------------

elif page == "✨ Idea-to-Story":
    st.title("✨ Idea-to-Story Assistant")
    st.write("Give your topic a direction. Get a practical short-form content outline.")

    with st.form("story_form"):
        topic = st.text_input("What's your topic?", placeholder="e.g. Study productivity")
        audience = st.text_input("Who is this for?", placeholder="e.g. College students")
        style = st.selectbox(
            "Choose your style",
            ["Educational", "Funny", "Motivational", "Professional", "Storytelling"],
        )
        submitted = st.form_submit_button("Generate my story ✨")

    if submitted:
        if not topic.strip() or not audience.strip():
            st.error("Please enter both a topic and a target audience.")
        else:
            result = make_story(topic.strip(), audience.strip(), style)
            st.success("Your content outline is ready!")
            st.markdown("### 🎯 Opening hook")
            st.info(result["hook"])

            st.markdown("### 🎬 Scene-by-scene outline")
            for title, description in result["scenes"]:
                with st.container(border=True):
                    st.markdown(f"**{title}**")
                    st.write(description)

            st.markdown("### ✍️ Caption")
            st.write(result["caption"])
            st.markdown("### #️⃣ Hashtags")
            st.code(result["hashtags"])
            st.markdown("### 📣 Call to action")
            st.write(result["cta"])
            st.markdown("### 💡 Creator tips")
            for tip in result["tips"]:
                st.markdown(f"- {tip}")


# -------------------- SMART PLANNER --------------------

elif page == "🗓️ Smart Content Planner":
    st.title("🗓️ Smart Content Planner")
    st.write("Build a simple content plan based on your niche, platform and goal.")

    with st.form("planner_form"):
        niche = st.text_input("Your niche", placeholder="e.g. Fitness, tech, student life")
        platform = st.selectbox(
            "Platform",
            ["Instagram Reels", "YouTube Shorts", "TikTok", "Facebook Reels"],
        )
        goal = st.selectbox("Main goal", ["Reach", "Engagement", "Consistency"])
        frequency = st.slider("How many days should we plan?", 1, 7, 5)
        submitted = st.form_submit_button("Build my content plan 🗓️")

    if submitted:
        if not niche.strip():
            st.error("Please enter your niche first.")
        else:
            plan = make_plan(niche.strip(), platform, goal, frequency)
            st.success(f"Your {frequency}-day plan is ready!")
            st.caption(f"Platform: {platform} · Goal: {goal}")
            for item in plan:
                with st.container(border=True):
                    st.markdown(f"**{item['day']} · {item['title']}**")
                    st.write(item["description"])
                    st.caption(f"Platform: {item['platform']}")


# -------------------- PERFORMANCE DETECTIVE --------------------

elif page == "📊 Performance Detective":
    st.title("📊 Performance Detective")
    st.write("Enter post metrics to calculate interaction rate and get practical suggestions.")

    with st.form("performance_form"):
        col1, col2 = st.columns(2)
        with col1:
            views = st.number_input("Views", min_value=0, value=1000, step=100)
            likes = st.number_input("Likes", min_value=0, value=80, step=10)
        with col2:
            comments = st.number_input("Comments", min_value=0, value=12, step=1)
            shares = st.number_input("Shares", min_value=0, value=8, step=1)
        submitted = st.form_submit_button("Analyse my post 📊")

    if submitted:
        if views == 0:
            st.warning("Views are zero, so an interaction rate cannot be calculated yet.")

        interactions, rate, suggestions = analyse_performance(
            int(views), int(likes), int(comments), int(shares)
        )

        col1, col2, col3 = st.columns(3)
        col1.metric("Total interactions", f"{interactions:,}")
        col2.metric("Interaction rate", f"{rate:.2f}%")
        col3.metric("Views", f"{int(views):,}")

        st.markdown("### 💡 What to try next")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

        st.caption(
            "Formula used: (likes + comments + shares) ÷ views × 100. "
            "These suggestions are general heuristics, not guaranteed predictions."
        )

# -------------------- FOOTER --------------------

st.markdown("---")
st.markdown(
    '<div class="small-note">CreatorFlow · A rule-based content assistant prototype</div>',
    unsafe_allow_html=True,
)
