# Imports
import streamlit as st
import app

# Event listeners for buttons
def on_signup():
  # TODO: signal to app.py to switch page
  app.open_page(app.page_state.CREATE_ACCOUNT)
  pass

# Setup visual elements
def render_page():
  col1, middleCol, col2 = st.columns(3)
  with middleCol:
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

  st.markdown("<h1 style='text-align: center;'>Login To Your Account</h1>", unsafe_allow_html=True)
  username = st.text_input("Username")
  password = st.text_input("Password", type="password")

  leftButton, rightButton = st.columns(2)
  with leftButton:
    signup_button = st.button("Sign Up for Account", on_click=on_signup)
  with rightButton:
    login_button = st.button("Login")

