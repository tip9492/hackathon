import streamlit as st

def survey():
    st.title('Take a survey')
    c=st.beta_container()
    c.slider("Please rate your last meet",min_value=0,max_value=5,step=1)
    c.slider("Please rate the participants",min_value=0,max_value=5,step=1)
    c.text_area("Do you have any other suggestions",max_chars=100,value="Please enter here",height=100)
    cap=c.button(label="Submit",key="Submit")
    if cap==True:
        c.success("Thank you for taking the survey")
