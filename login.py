import streamlit as st
from header import header
from db import *
import SessionState

def login():

 login=False
 tit = st.empty()
 tit.title("Welcome to our App")
 menu = ["Login","SignUp"]
 choice_st = st.sidebar.empty()
 choice = choice_st.selectbox("Menu",menu)
 username_st = st.empty()
 password_st = st.empty()
 checkbox = st.empty()
 session_state = SessionState.get(user_name='')

 if choice == "Login":
  username=username_st.text_input("User Name")
  password=password_st.text_input("Password",type='password')
  login_btn = checkbox.button("Login")
  if login_btn:
   create_usertable()
   hashed_pswd = make_hashes(password)
   result = login_user(username,check_hashes(password,hashed_pswd))
   if result:
    # st.success("Logged In as {}".format(username))
    session_state.user_name = username
    username_st.empty()
    password_st.empty()
    checkbox.empty()
    tit.empty()
    choice_st.empty()
    header()

   else:
    st.warning("Incorrect Username/Password")
 elif choice == "SignUp":
  st.subheader("Create New Account")
  new_user = st.text_input("Username")
  new_password = st.text_input("Password",type='password')
  if st.button("Signup"):
   create_usertable()
   add_userdata(new_user,make_hashes(new_password))
   st.success("You have successfully created a valid Account")
   st.info("Go to Login Menu to login")


# main()
