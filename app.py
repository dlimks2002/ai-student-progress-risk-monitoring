import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="AI Student Progress & Risk Monitoring",
                   page_icon="🎓", layout="wide")

DATA_PATH = Path(__file__).parent / "data" / "students.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def recommendation(row):
    actions = []
    if row["attendance_pct"] < 75:
        actions.append("Discuss attendance and identify barriers.")
    if row["assessment_avg"] < 60:
        actions.append("Recommend targeted revision and a consultation session.")
    if row["engagement_pct"] < 60:
        actions.append("Provide a short check-in and engagement activity.")
    if row["submission_pct"] < 75:
        actions.append("Set a catch-up plan for missed assignments.")
    if not actions:
        actions.append("Continue normal monitoring and provide enrichment opportunities.")
    return actions

df = load_data()

st.title("🎓 AI-Powered Student Progress & Risk Monitoring")
st.caption("Prototype dashboard for early identification of students who may need academic support.")

# Sidebar
st.sidebar.header("Filters")
risk_filter = st.sidebar.multiselect(
    "Risk level",
    ["High", "Medium", "Low"],
    default=["High", "Medium", "Low"]
)
search = st.sidebar.text_input("Search student")

view = df[df["risk_level"].isin(risk_filter)].copy()
if search:
    view = view[view["student_name"].str.contains(search, case=False, na=False) |
                view["student_id"].str.contains(search, case=False, na=False)]

# KPIs
c1,c2,c3,c4 = st.columns(4)
c1.metric("Students monitored", len(df))
c2.metric("High risk", int((df.risk_level=="High").sum()))
c3.metric("Medium risk", int((df.risk_level=="Medium").sum()))
c4.metric("Average risk score", f"{df.risk_score.mean():.1f}%")

st.divider()

left, right = st.columns([1.5, 1])
with left:
    st.subheader("Student Risk Overview")
    display = view[["student_id","student_name","attendance_pct","assessment_avg",
                    "engagement_pct","submission_pct","risk_score","risk_level"]].copy()
    display.columns = ["ID","Student","Attendance","Assessment Avg",
                       "Engagement","Submission","Risk Score","Risk Level"]
    st.dataframe(
        display.style.format({
            "Attendance":"{:.0f}%",
            "Assessment Avg":"{:.1f}%",
            "Engagement":"{:.0f}%",
            "Submission":"{:.0f}%",
            "Risk Score":"{:.1f}%"
        }),
        use_container_width=True, hide_index=True
    )

with right:
    st.subheader("Risk Distribution")
    counts = df["risk_level"].value_counts().reindex(["High","Medium","Low"]).fillna(0)
    st.bar_chart(counts)

st.divider()

st.subheader("🔎 Student Detail & AI-Assisted Intervention")
student_options = list(df["student_name"])
selected = st.selectbox("Select a student", student_options)
row = df[df.student_name == selected].iloc[0]

a,b,c = st.columns(3)
a.metric("Risk Score", f"{row.risk_score:.1f}%")
b.metric("Risk Level", row.risk_level)
c.metric("Assessment Average", f"{row.assessment_avg:.1f}%")

st.markdown("### Key indicators")
m1,m2,m3,m4 = st.columns(4)
m1.metric("Attendance", f"{row.attendance_pct:.0f}%")
m2.metric("Engagement", f"{row.engagement_pct:.0f}%")
m3.metric("Assignments", f"{row.assignments_submitted}/{row.assignments_total}")
m4.metric("Assessment 4", f"{row.assessment_4:.0f}%")

st.markdown("### Why is this student flagged?")
reasons = []
if row.attendance_pct < 75: reasons.append(f"Attendance is {row.attendance_pct:.0f}%, below the 75% monitoring threshold.")
if row.assessment_avg < 60: reasons.append(f"Average assessment performance is {row.assessment_avg:.1f}%, indicating academic difficulty.")
if row.engagement_pct < 60: reasons.append(f"Engagement is {row.engagement_pct:.0f}%, suggesting reduced participation.")
if row.submission_pct < 75: reasons.append(f"Only {row.assignments_submitted} of {row.assignments_total} assignments were submitted.")
if not reasons: reasons.append("No major risk indicator crossed the prototype thresholds.")

for r in reasons:
    st.write("• " + r)

st.markdown("### 💡 Recommended intervention")
for action in recommendation(row):
    st.write("• " + action)

st.info(
    "Prototype note: the risk score is an explainable weighted model using attendance, "
    "assessment performance, engagement and assignment submission. It is intended for "
    "early-support triage, not automated decisions about students."
)

st.caption("Synthetic demonstration data — no real student records are used.")
