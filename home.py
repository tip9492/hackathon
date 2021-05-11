import streamlit as st
import SessionState
from survey import survey, survey_home
from learning import learning
from take_a_break import need_break
def first():
#     st.title('EAP')
#     m=st.empty()
#     col1,col2,col3,col4=m.beta_columns(4)
#     with col1:
#         col1.header("Take a survey")
#     with col2:
#         col2.markdown("""<div class="card" style="width: relative;">
#   <img class="card-img-top" src="..." alt="Card image cap">
#   <div class="card-body">
#     <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
#   </div>
# </div>""",unsafe_allow_html=True)
#         c=col2.checkbox("Check here")
#         while c:
#             col2.empty()
    
#     with col3:
#         col3.markdown("""<div class="card" style="width: relative;">
#   <img class="card-img-top" src="..." alt="Card image cap">
#   <div class="card-body">
#     <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
#   </div>
# </div>""",unsafe_allow_html=True)
#     with col4:
#         col4.markdown("""<div class="card" style="width: relative;">
#   <img class="card-img-top" src="..." alt="Card image cap">
#   <div class="card-body">
#     <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
#   </div>
# </div>
# """,unsafe_allow_html=True)


  def local_css(file_name):
      with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

  local_css("home.css")
  st.title("E.A.P")
  mm=st.empty()
  mm2=st.empty()
  col12,col13=mm.beta_columns(2)
  with col12:
    button_clicked1 = st.button("HOME")
    if button_clicked1:
      first()
      # mm.empty()

  with col13:
    button_clicked2 = st.button("SURVEY")
    if button_clicked2:
      survey_home()
      # mm.empty()
      # mm2.empty()



  col22,col23=mm2.beta_columns(2)
  with col22:
    button_clicked3 = st.button("LEARNING")
    if button_clicked3:
      learning()
      # mm.empty()
      # mm2.empty()
 
  with col23:
    button_clicked4 = st.button("TAKE A BREAK")
    if button_clicked4:
      need_break()
      # mm.empty()
