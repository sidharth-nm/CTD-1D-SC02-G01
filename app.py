'''Main application file. Run "streamlit run app.py" in root folder to execute the web application.'''

# Imports
import streamlit as st
import login_frontend as login

# Initializes current page
# If user has never opened application or signed out, they are directed to login page
if (not "curr_page" in st.session_state) or (not "logged_in" in st.session_state) or (not st.session_state.logged_in):
  st.session_state.curr_page = login.Page

# Configure browser tab
st.set_page_config(page_title="The Reading Nook", page_icon="📖")

# Loads current page
@st.fragment
def render_current_page():
    current_page = st.session_state.curr_page()
    current_page.render()

render_current_page()
