import streamlit as st
from multiapp import MultiApp
from home import first
from survey import survey
from learning import learning
from take_a_break import need_break
from login import login
import SessionState
from header import header


session_state = SessionState.get(user_name='')
print("==============>",session_state.user_name)
if session_state.user_name:
	header()
else:
	login()
# mapping = {
# 	"Home": first,
# 	"Take a survey": survey,
# 	"I want to Learn": learning,
# 	"Take a break": need_break,
# 	"Login": login
# }

# def run(app):
# 	mapping[app]()

# run("Login")
