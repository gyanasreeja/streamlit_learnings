import streamlit as st

st.set_page_config(page_title="Layout Demo", layout="wide")
st.title("Layout Demo")

# --- Sidebar ---
st.sidebar.header("Settings")
theme = st.sidebar.radio("Choose mode", ["Light", "Dark"])
st.sidebar.write(f"You picked: {theme}")

# --- Tabs ---
tab1, tab2 = st.tabs(["Personal Info", "Academic Info"])

with tab1:
    st.subheader("Personal Details")
    # --- Columns inside a tab ---
    col1, col2 = st.columns([3,1])
    with col1:
        name = st.text_input("Name")
    with col2:
        age = st.number_input("Age", min_value=0, max_value=100)

with tab2:
    st.subheader("Academic Details")
    # --- Container with border, like a "card" ---
    with st.container(border=True):
        clg = st.text_input("College Name")
        branch = st.radio("Branch", ["CSE", "IT", "ECE"])

if st.button("Submit"):
    st.success(f"{name}, age {age}, from {clg} ({branch}) — submitted!")