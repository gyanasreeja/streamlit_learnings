import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0   # only runs once, on first load

if st.button("Add 1"):
    st.session_state.count += 1

st.write(st.session_state.count)