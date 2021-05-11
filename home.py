import streamlit as st
import SessionState
def first():
    st.title('EAP')
    m=st.empty()
    col1,col2,col3,col4=m.beta_columns(4)
    with col1:
        col1.header("Take a survey")
    with col2:
        col2.markdown("""<div class="card" style="width: relative;">
  <img class="card-img-top" src="..." alt="Card image cap">
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>""",unsafe_allow_html=True)
        c=col2.checkbox("Check here")
        while c:
            col2.empty()
    
    with col3:
        col3.markdown("""<div class="card" style="width: relative;">
  <img class="card-img-top" src="..." alt="Card image cap">
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>""",unsafe_allow_html=True)
    with col4:
        col4.markdown("""<div class="card" style="width: relative;">
  <img class="card-img-top" src="..." alt="Card image cap">
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>
""",unsafe_allow_html=True)
