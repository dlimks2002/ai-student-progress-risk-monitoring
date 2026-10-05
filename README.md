# AI-Powered Student Progress & Risk Monitoring

## 1. Solution Summary
This project is a lightweight prototype for helping lecturers identify students who may require early academic support.

The dashboard combines four indicators:
- Attendance
- Assessment performance
- Engagement
- Assignment submission

An explainable weighted risk model produces a risk score and classifies students as **Low**, **Medium**, or **High** risk. The dashboard then highlights the contributing factors and suggests possible lecturer interventions.

> **Important:** This prototype uses synthetic data and is intended for demonstration/early-support triage. It does not make automated decisions about students.

## 2. Key Features
- Student monitoring dashboard
- High / Medium / Low risk classification
- Search and risk-level filters
- Risk distribution chart
- Individual student drill-down
- Explainable risk factors
- Suggested intervention actions
- Synthetic dataset for safe demonstration

## 3. Risk Model
The prototype uses an intentionally simple, explainable weighted formula:

**Risk Score =**
- 35% × (100 − Assessment Average)
- 30% × (100 − Attendance)
- 20% × (100 − Engagement)
- 15% × (100 − Assignment Submission)

Risk bands:
- **High:** 60% or above
- **Medium:** 35%–59.9%
- **Low:** below 35%

The model is deliberately transparent so a lecturer can understand why a student has been flagged.

## 4. Project Structure
```text
AI_Student_Progress_Risk_Monitoring/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── students.csv
├── docs/
│   ├── Project_Documentation.pptx
│   └── 3_Minute_Demo_Script.md
└── assets/
```

## 5. Setup Instructions

### Prerequisites
- Python 3.10 or newer
- Internet access for the initial package installation

### Install
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app.py
```

The terminal will provide a local URL, normally:
`http://localhost:8501`

## 6. Demonstration Flow
1. Open the dashboard.
2. Show the overall student monitoring KPIs.
3. Filter to **High Risk** students.
4. Select **Isaac Goh** or **Farah Ahmad**.
5. Show the risk score and indicators.
6. Explain why the student is flagged.
7. Show the recommended intervention.
8. Return to the overview and explain how a lecturer could use the dashboard for early intervention.

## 7. Project Link
Repository placeholder:
`https://github.com/dlimks2002/ai-student-progress-risk-monitoring`

Replace this with the final GitHub/GitLab repository URL before submission.

## 8. Future Enhancements
- Train a supervised ML model using historical anonymised student data.
- Add weekly progress trend charts.
- Integrate LMS/student information system data through APIs.
- Add lecturer notes and intervention tracking.
- Add model evaluation metrics and fairness monitoring.
- Add role-based access control and privacy safeguards.
- Use an LLM/RAG layer to generate personalised learning-resource recommendations.

## 9. Responsible AI Considerations
The prototype should support lecturers rather than replace professional judgement. Risk flags can be affected by incomplete data, contextual factors or bias. Any real deployment should use appropriate governance, access control, data minimisation, transparency, human review and model monitoring.
