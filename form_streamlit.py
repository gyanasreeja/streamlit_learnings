import streamlit as st
import re
st.title("Application Form")
name = st.text_input("Name")
gmail = st.text_input("Gmail")
gender = st.radio("Gender", ["Male","Female","Other"])
Resume = st.file_uploader("Resume", type =['csv','pdf','png'])
clgname = st.text_input("Clg Name")
pass_out = st.selectbox("Pass Out",['2024','2025','2026','2027'])
Branch = st.radio("Branch",['CSE','CSD','CSM','IT','ECE'])

age = st.text_input("Age")
skills = st.multiselect("Skills",["Python","SQL","Java","Spring","FastAPI"])
project = st.text_input("Name the project")
Describe_Abt_Project = st.text_area("Describe about your Project")
if st.button("Submit"):
    if Resume is not None:
        st.success("Resume uploaded : {Resume.name}")
        st.write("submitted")
    else:
        st.error("Submit crct Resume")   
        
         
        
    
