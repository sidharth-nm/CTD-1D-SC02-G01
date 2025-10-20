import app
import create_account_frontend as front

#prevents potential circular import between page files and app.py
import streamlit as st

#page change
def change_page(new_page):
  st.session_state.curr_page = new_page
  st.rerun(scope="fragment")