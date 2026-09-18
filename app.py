import streamlit as st

st.title("Vote Validator")
age= st.text_input("Enter your age")
if st.button("validate"):
    if age.isdigit():
        if int(age)>=18:
            st.success("Eligible")
        else:
            st.error("Not Eligible") 
    else:
        st.error("Enter a valid number")
                   