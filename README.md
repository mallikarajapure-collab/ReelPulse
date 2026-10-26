<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7F1D1D,45:EA580C,100:FBBF24&height=220&section=header&text=REELPULSE&fontSize=46&fontColor=FFFFFF&fontAlignY=38&desc=Plan%20the%20story.%20Learn%20from%20the%20numbers.&descAlignY=61&descSize=15" width="100%" alt="ReelPulse — Plan the story. Learn from the numbers." />

<p>
  <strong>A short-form content planning and engagement comparison toolkit.</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3B2F2F?style=for-the-badge&logo=python&logoColor=FBBF24" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-EA580C?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Analytics-F97316?style=for-the-badge&logo=googleanalytics&logoColor=white" alt="Analytics" />
  <img src="https://img.shields.io/badge/Status-Learning%20Project-92400E?style=for-the-badge" alt="Learning project" />
</p>

</div>

---

## 🎬 What is ReelPulse?

**ReelPulse** is a Python project for creators who want help shaping short-form video ideas, planning posts, and reviewing engagement figures in one place. It includes a terminal-based assistant, a Streamlit content workspace, and a separate dashboard for comparing video metrics.

The project currently uses **predefined rules and user-entered metrics**. It is a practical content-planning prototype—not an automatic social-media analytics service or a trained AI prediction model.

## ✨ What you can do

<table>
<tr>
<td width="50%" valign="top">

### 💡 Idea-to-Story Assistant
- Start with a topic and target audience.
- Choose a content style.
- Draft an opening hook and scene-by-scene outline.
- Get caption, hashtag, call-to-action, and creator-tip suggestions.

</td>
<td width="50%" valign="top">

### 🗓️ Content Planner
- Build a short plan around your niche.
- Select a platform and content goal.
- Choose how many days to plan.
- Use the output as a starting point, then adapt it to your audience.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 Performance Detective
- Enter views, likes, comments, and shares.
- Calculate recorded interactions and interaction rate.
- Receive simple, rule-based ideas for what to test next.
- Handle invalid values and zero-view cases.

</td>
<td width="50%" valign="top">

### 🔎 Video Comparison
- Add multiple videos and their metrics.
- View the data in a table and comparison chart.
- Compare interaction rates and find the highest rate among videos with views.
- Reset the comparison data when starting a new review.

</td>
</tr>
</table>

## 📈 Interaction-rate calculation

ReelPulse uses this simple formula:

`Interaction rate (%) = ((Likes + Comments + Shares) / Views) × 100`

**Example:** 20 likes, 40 comments, and 20 shares on a video with 1,000 views gives an interaction rate of **8%**.

This is a comparison metric, not a complete measure of content quality. Results depend on the accuracy and consistency of the metrics entered.

## 🧰 Built with

| Technology | Role in the project |
|---|---|
| Python | Application logic and content-planning rules |
| Streamlit | Interactive content and analytics dashboards |
| Pandas | Organizing video metrics for comparison |
| Streamlit charts | Visual comparison of interaction rates |
| Git & GitHub | Version control and project hosting |

## 🚀 Run it locally

### Requirements
- Python installed
- `pip`
- A terminal or command prompt

### 1. Clone the repository

```bash
git clone https://github.com/mallikarajapure-collab/ReelPulse.git
cd ReelPulse
```

### 2. Create and activate a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application you want to use

**Terminal-based assistant**
```bash
python main.py
```

**Main Streamlit dashboard**
```bash
streamlit run app.py
```

**Video comparison dashboard**
```bash
streamlit run compare.py
```

Streamlit prints a local address in the terminal; open it in your browser. Run the dashboards as separate commands in separate terminal sessions if you want to use both at the same time.

## 🗂️ Repository structure

```text
ReelPulse/
├── app.py             # Streamlit content assistant and planner
├── compare.py         # Video metrics comparison dashboard
├── main.py            # Terminal-based content assistant
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

## ⚠️ Current scope and limitations

- Content ideas, plans, and performance suggestions are generated with predefined rules.
- Video statistics are entered manually; the app does not currently connect to Instagram or YouTube analytics APIs.
- There is no trained machine-learning model or external LLM API powering the current content-generation logic.
- The interaction rate can be misleading when source metrics are missing or recorded differently across platforms.
- The output is intended as a planning aid; review topic-specific claims and recommendations before publishing.

## 🛣️ Possible next steps

- Add optional LLM-assisted drafts with clear user control.
- Save plans and comparison data between sessions.
- Support importing metrics from a CSV file.
- Add more chart types and comparisons over time.
- Add automated tests for core calculations and input validation.

## 👩‍💻 About

Built by **Mallika Rajapure** as a Python project exploring content planning, rule-based assistance, and interactive data visualization.

<div align="center">

**ReelPulse · Make the next post a more informed experiment.**

</div>
