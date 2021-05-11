import streamlit as st


def local_css(file_name):
      with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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


def learning_home():
	st.title("Innovation Hub")
	mm2 = st.empty()
	local_css("survey.css")

	col22,col23,col24,col25,col26=mm2.beta_columns(5)
	with col22:
		button_clicked1 = st.button("Project 1")
		
		  # mm.empty()
		  # mm2.empty()

	with col23:
		button_clicked2 = st.button("Project 2")
		

	with col24:
		button_clicked3 = st.button("Experiment Explore Evaluate")
	with col25:
		button_clicked4 = st.button("Open Source Projects")

	with col26:
		button_clicked5 = st.button("Submit an Idea")
		

	if button_clicked1:
		  project1()

	if button_clicked2:
		  project2()

	if button_clicked3:
		   eee()
	if button_clicked4:
		   osp()
	if button_clicked5:
		   sai()



		  # mm.empty()

def project1():
	c=st.beta_container()
	c.title("Project 1")


def project2():
	c=st.beta_container()
	c.title("Project 2")

def osp():
	c=st.beta_container()
	c.title("Open Source projects you can work on")
	c.write("Streamlit")


def eee():
	c=st.beta_container()
	c.title("Experience Tools in a whole new way")
	c.write("Pycharm for Python")
	c.write("OCR")

def sai():
	c=st.beta_container()
	form = st.form(key='my_form')
	c=form.selectbox('Choose a Field of Interest', ['AI', 'Blockchain','Others'], key=1)
	if c=="Others":
		form.text_input(label="Enter your desired field")
	form.text_area(label="Enter your Idea")
	submit = form.form_submit_button('Submit')
    
