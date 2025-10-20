import streamlit as st
import confirmation_backend as conf_back
import pagination as pg
import login_frontend as front
import shopping_frontend as shop

class Page:
  #create Page object
  def __init__(self):
    pass

  def render(self):
    st.title("🎉 Congratulations 🎉")
    st.markdown("## Your order has been placed!")
    st.markdown("It will arrive within **three to five days.**")

    st.subheader("Your items:")
    books = conf_back.get_books()

    for book in books:
      with st.container():
        st.markdown(f"**{book['title']}** by {book['author']}")

    restart_button = st.button("Return to Home")
    if restart_button:
      if st.session_state.logged_in:
        pg.change_page(shop.Page)
      else:
        pg.change_page(front.Page)
    
    logout_button = st.button("Log Out")
    if logout_button:
      st.session_state.logged_in = False
      pg.change_page(front.Page)