import streamlit as st

def local_css(file_name):
      with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def survey_home():
    # st.title('Take a survey')
    st.title("Survey")
    c=st.beta_container()
    c.slider("Please rate your last meet",min_value=0,max_value=5,step=1)
    c.slider("Please rate the participants",min_value=0,max_value=5,step=1)
    c.text_area("Do you have any other suggestions",max_chars=100,value="Please enter here",height=100)
    cap=c.button(label="Submit",key="Submit")
    if cap==True:
        c.success("Thank you for taking the survey")

def survey():
	st.title("Survey")
	mm2 = st.empty()
	local_css("survey.css")

	col22,col23, col24=mm2.beta_columns(3)
	with col22:
		button_clicked3 = st.button("Monthly")
		
		  # mm.empty()
		  # mm2.empty()

	with col23:
		button_clicked2 = st.button("Weekly")
		

	with col24:
		button_clicked4 = st.button("Daily")
		

	if button_clicked3:
		  monthly()

	if button_clicked4:
		  daily()

	if button_clicked2:
		  weekly()

		  # mm.empty()

def daily():

	c=st.beta_container()
	c.title("Daily Survey")
	c.slider("Please rate your last meet",min_value=0,max_value=5,step=1)
	c.slider("Please rate the participants",min_value=0,max_value=5,step=1)
	c.text_area("Do you have any other suggestions",max_chars=100,value="Please enter here",height=100)
	cap=c.button(label="Submit",key="Submit")
	if cap==True:
	    c.success("Thank you for taking the survey")

def monthly():
	c=st.beta_container()
	c.title("Monthly Survey")


def weekly():
	c=st.beta_container()
	c.title("Weekly Survey")