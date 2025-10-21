'''Auxilliary file; used to handle page changes in application'''

# Prevents potential circular import between page files and app.py
import streamlit as st

# Changes page currently seen by the user
def change_page(new_page):
  st.session_state.curr_page = new_page
  st.rerun(scope="fragment")