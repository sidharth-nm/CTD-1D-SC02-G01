import streamlit as st
import shopping_frontend as shopping
import login_frontend as login
import create_account_frontend as create_acc

#Render the page based on the given page state in the arguement
# #TODO: Create the Navigation bar containing only the logo
# st.navigation({
#     pass
# })

# Initializes current page
# If user has never opened application or signed out, they are directed to login page
if (not "curr_page" in st.session_state) or (not "logged_in" in st.session_state) or (not st.session_state.logged_in):
  st.session_state.curr_page = login.Page

#To display the container of the pages
#create the tab display
st.set_page_config(page_title="The Reading Nook", page_icon="📖")

@st.fragment
def render_current_page():
    current_page = st.session_state.curr_page()
    current_page.render()

render_current_page()
