import gradio as gr
import pickle
import numpy as np

# Load model and scaler
with open("resume.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

education_dict = {
    "High School": 0,
    "Bachelors": 1,
    "Masters": 2,
    "PhD": 3
}

def predict_resume(education_label, years_experience, skills_match_score,
                   project_count, resume_length, github_activity):

    education_level = education_dict[education_label]

    input_data = np.array([[years_experience,
                            skills_match_score,
                            education_level,
                            project_count,
                            resume_length,
                            github_activity]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        return "✅ Resume Shortlisted"
    else:
        return "❌ Resume Not Shortlisted"


interface = gr.Interface(
    fn=predict_resume,
    inputs=[
        gr.Dropdown(list(education_dict.keys()), label="Education Level"),
        gr.Number(label="Years of Experience"),
        gr.Number(label="Skills Match Score"),
        gr.Number(label="Project Count"),
        gr.Number(label="Resume Length"),
        gr.Number(label="GitHub Activity")
    ],
    outputs="text",
    title="📄 Resume Shortlisting System",
    description="This system predicts whether a resume will be shortlisted or not."
)

interface.launch()