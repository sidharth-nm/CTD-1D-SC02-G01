#prevents potential circular import between page files and app.py
import streamlit as st

#initialise current page holder
if "curr_page_container" not in st.session_state:
  st.session_state.curr_page_container = st.container

#page change
def change_page(new_page):
  st.session_state.curr_page_container = new_page

