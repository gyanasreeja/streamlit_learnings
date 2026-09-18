import streamlit as st
import pandas as pd

st.set_page_config(page_title="Job Application Form", page_icon="📝", layout="wide")

st.title("📝 Job Application Form")

# --- Session state to track submission ---
if "submitted" not in st.session_state:
    st.session_state.submitted = False

tab1, tab2, tab3 = st.tabs(["Personal Info", "Academic Info", "Skills & Resume"])

with tab1:
    st.subheader("Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
    with col2:
        age = st.number_input("Age", min_value=15, max_value=100, step=1)
        email = st.text_input("Email")

with tab2:
    st.subheader("Academic Details")
    with st.container(border=True):
        clg = st.text_input("College Name")
        branch = st.radio("Branch", ["CSE", "CSD", "CSM", "IT", "ECE"])
        pass_out = st.selectbox("Pass Out Year", ["2024", "2025", "2026", "2027"])

with tab3:
    st.subheader("Skills & Resume")
    skills = st.multiselect("Skills", ["Python", "SQL", "Java", "Spring", "FastAPI"])
    project = st.text_input("Project Name")
    project_desc = st.text_area("Describe your Project")
    resume = st.file_uploader("Upload Resume", type=["pdf", "doc", "docx"])

st.divider()

if st.button("Submit Application"):
    if not name or not email or resume is None:
        st.error("Please fill Name, Email, and upload your Resume before submitting.")
    else:
        st.session_state.submitted = True

if st.session_state.submitted:
    st.success(f"✅ Application submitted for {name} — Resume: {resume.name}")
    with st.expander("View submitted details"):
        st.write({
            "Name": name, "Age": age, "Gender": gender, "Email": email,
            "College": clg, "Branch": branch, "Pass Out": pass_out,
            "Skills": skills, "Project": project
        })
        