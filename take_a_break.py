import random

import streamlit as st
from datetime import datetime, date,time
from random import randint
def local_css(file_name):
      with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def need_break():
    c=st.beta_container()
    c.header("Take a break")

    # c.header("Request for a break or change in timings")
    r=c.selectbox("Select below",options=['Flexi-Time','Change shift'])
    if r=="Flexi-Time":
        c.slider("Please select in hours the time you will be away from the keyboard",min_value=0.5,max_value=8.0,step=0.5)
        c.radio("Please check this box if you intend to use flexi-tine for more than a day",options=["Yes","No"])
    else:
        ck=c.radio("Please click here to change your shift",options=["Morning Shift (08:00-16:00)","Afternoon Shift (11:30-17:30)","Evening Shift (14:30-22:30)","Flexi-Shift"])
        if ck=="Flexi-Shift":
         h = c.time_input("Start time", key=str(random.randint(2, 10)))
         e = c.time_input("End Time", key=str(random.randint(100, 200)))
         duration = datetime.combine(date.min, e) - datetime.combine(date.min, h)
         if (duration.seconds // 3600) < 8:
          c.warning("Chose a minimum of 8 hours")
          cap = c.button("Submit", key="submit")
          if cap==True:
           c.success("Time submitted")
        else:
          cap = c.button("Submit", key="submit")
          if cap==True:
           c.success("Time submitted")
def need_break_home():
	st.title("Request for a break")
	mm2 = st.empty()
	local_css("survey.css")

	col22,col23=mm2.beta_columns(2)
	with col22:
		button_clicked1 = st.button("Request Time Off")
		
		  # mm.empty()
		  # mm2.empty()

	with col23:
		button_clicked2 = st.button("Time off Scheduler")
		

	

	if button_clicked1:
		  sai()

	if button_clicked2:
		  tos()





		  # mm.empty()


def sai():
	c=st.beta_container()
	form = st.form(key='my_form')
	form.text_input(label="Enter your time")
	c=form.selectbox('Reason for Leave', ['Illness', 'Vacction','Others'], key=1)
	if c=="Others":
		form.text_input(label="Enter your reason")
	form.text_area(label="Enter Description Optional")
	submit = form.form_submit_button('Submit')
	
def tos():
	st.title("To be devloped")
