import streamlit as st

def learning():
    # st.title('Welcome to the e-learning Portal')
    st.title("Learning")
    c=st.beta_container()

    sel=c.selectbox("Choose the topic you wish to learn today",options=['AI','Blockchain','Python'],index=0)
    val=c.slider("Rate your skill in"+sel, min_value=0, max_value=5, step=1)
    
    if val<3:
        c.write("Sharpen your skills with")
        link='[Udemy](https://www.udemy.com/course/learn-python/)'
        c.markdown(link,unsafe_allow_html=True)
    else:
        c.write("Your Idea could change the world click here to join the innovators")
    c.empty()
