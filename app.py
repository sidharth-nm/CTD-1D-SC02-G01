import streamlit as st
import pagination as pg
import shopping_frontend as shopping
import create_account_frontend as front

#initialise
pg.change_page(shopping.Page())

#Render the page based on the given page state in the arguement
# #TODO: Create the Navigation bar containing only the logo
# st.navigation({
#     pass
# })

#To display the container of the pages
#create the tab display
with st.container():
  st.set_page_config(page_title="The Reading Nook", page_icon="📖")
  #render page
  curr_page = st.session_state.curr_page_container
  curr_page.render()