# Imports
import streamlit as st
import confirmation_backend as conf_back
import pagination as pg
import login_frontend as login
import shopping_frontend as shop

class Page:
  #create Page object
  def __init__(self):
    pass

  def render(self):
    st.title("🎉 Congratulations 🎉")
    st.markdown("## Your order has been placed!")
    st.markdown("It will arrive within **three to five days.**")

    # Displays list of books purchased
    st.subheader("Your items:")
    books = conf_back.get_books()

    for book in books:
      with st.container():
        st.markdown(f"**{book['title']}** by {book['author']}")

    # Displays Continue Shopping Button
    restart_button = st.button("Return to Home")
    if restart_button:
      if st.session_state.logged_in:
        pg.change_page(shop.Page)
      
      # If user logs out, sends them to login page instead
      else:
        pg.change_page(login.Page)
    
    # Displays Logout button
    logout_button = st.button("Log Out")
    # Event listener for Logout button
    if logout_button:
      st.session_state.logged_in = False
      pg.change_page(login.Page)