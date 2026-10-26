<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:831843,50:DB2777,100:F472B6&height=210&section=header&text=REELPULSE&fontSize=42&fontColor=FFFFFF&fontAlignY=38&desc=Short-Form%20Content%20Intelligence&descAlignY=60&descSize=16" width="100%" />

</div>

---

# 💜 ReelPulse — Create Smarter. Compare Better.

**ReelPulse** is a Python-based content planning and video analytics application designed to help short-form content creators organize their ideas, plan their posting schedules, and compare video engagement performance.

It combines a command-line content assistant with interactive Streamlit dashboards to make content planning and performance analysis easier.

## ✨ Features

### 💡 1. Idea-to-Story Assistant
- Generate content ideas from a topic and target audience.
- Choose educational, funny, or storytelling styles.
- Create video hooks and scene-by-scene outlines.
- Generate on-screen text, captions, hashtags, and calls to action.
- Get practical creator tips for content development.

### 📅 2. Smart Content Planner
- Create a seven-day content plan.
- Customize plans based on niche, platform, content goal, and posting frequency.
- Support Instagram and YouTube.
- Choose education, growth, or engagement goals.
- Validate inputs and posting-frequency limits.

### 🔎 3. Performance Detective
- Enter video views, likes, comments, and shares.
- Calculate total recorded interactions and interaction rate.
- Receive rule-based suggestions for content experiments.
- Handle invalid numeric inputs and zero views.

### 📊 4. Video Comparison Dashboard
- Compare multiple videos using manually entered metrics.
- Calculate and compare interaction rates.
- Visualize performance through a comparison chart.
- Identify the highest interaction rate.
- Compare video views and engagement metrics through a Streamlit dashboard.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive dashboards |
| Rule-based logic | Content suggestions and planning |
| Data visualization | Comparing video performance |
| Git & GitHub | Version control and project hosting |

## 🧮 Interaction Rate Formula

ReelPulse calculates interaction rate using the following formula:

**Interaction Rate (%) = ((Likes + Comments + Shares) / Views) × 100**

**Example:**

For a video with 1,000 views, 20 likes, 40 comments, and 20 shares:

Interaction Rate = ((20 + 40 + 20) / 1,000) × 100

**Result: 8%**

This metric helps compare recorded interactions relative to video views. A higher rate does not automatically mean better overall content quality.

🚀 Getting Started

Prerequisites

Python 3.12 or a compatible Python 3 version

pip package installer

Terminal or command prompt

1. Clone the repository

Replace YOUR_USERNAME with your GitHub username.

git clone https://github.com/YOUR_USERNAME/ReelPulse.git
cd ReelPulse

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

3. Install dependencies

Install the packages required by the project. If a requirements.txt file is available, run:

pip install -r requirements.txt

4. Run the command-line application

python main.py

Follow the menu options to explore the content assistant features.

5. Launch the Streamlit dashboard

Run the main dashboard:

streamlit run app.py

To launch the video comparison dashboard separately:

streamlit run compare.py

Open the local URL displayed in the terminal.

📁 Project Structure

ReelPulse/
├── app.py
├── compare.py
├── main.py
├── README.md
├── .gitignore
└── requirements.txt  # Include if available

This is a simplified overview. Update it to match the files actually included in the repository.

🧪 Testing

The project has been manually tested for core content-assistant workflows, input validation, invalid numeric inputs, zero-view handling, and posting-frequency boundaries.

The comparison dashboard has also been tested with sample video metrics, interaction-rate calculations, performance summaries, and chart rendering.

⚠️ Limitations

Content suggestions are generated using predefined rules.

Video metrics are entered manually; automatic social media analytics integration is not currently included.

The current implementation does not claim to use a trained machine-learning model or an external LLM API.

Performance comparisons depend on the accuracy of the supplied metrics.

🔮 Future Enhancements

Optional LLM-powered content generation.

Persistent storage for content plans and video analytics.

Additional engagement charts and performance insights.

Automated tests and expanded error handling.

A more polished, responsive user interface.

👩‍💻 Author

Mallika Rajapure

A personal project exploring Python development, content planning, engagement analytics, and interactive dashboards.

ReelPulse — Create smarter. Compare better.