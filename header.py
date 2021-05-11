from home import first
from survey import survey
from learning import learning_home
from take_a_break import need_break_home
import streamlit as st

def header():
	mapping = {
		"Home": first,
		"Survey": survey,
		"Learning": learning_home,
		"Take a Break": need_break_home
	}
	menu = [ "Home","Survey", "Learning", "Take a Break"]
	choice_st = st.sidebar
	choice = choice_st.selectbox("Menu",menu)
	mapping[choice]()
