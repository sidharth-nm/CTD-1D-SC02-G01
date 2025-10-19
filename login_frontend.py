# Imports
import streamlit as st
import pagination as pg
import login_backend as logback
import create_account_frontend as create_acc
import shopping_frontend as shopping

class Page:
    # Initialize page's state
    def __init__(self):
        if 'logged_in' not in st.session_state:
          st.session_state.logged_in = False

    def render(self):
        page_container = st.container()
        with page_container:
          #display the starting elements and add necessary listeners
          col1, middleCol, col2 = st.columns(3)
          with middleCol:
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

          st.markdown("<h1 style='text-align: center;'>Login To Your Account</h1>", unsafe_allow_html=True)
          username = st.text_input("Username")
          password = st.text_input("Password", type="password")

          leftButtonCol, rightButtonCol = st.columns(2)
          with leftButtonCol:
            create_acc_button = st.button("Create Account")

            # Event listener for Create Account button
            if create_acc_button:
              print("Create Account clicked")
              pg.change_page(create_acc.Page)
          
          with rightButtonCol:
            login_button = st.button("Login")

            # Event listener for Login button
            if login_button:
              print("Login clicked")
              print(f"Credentials: {username}, {password}")

              if logback.verify_credentials(username, password):
                st.success("Successfully logged in! Redirecting...")
                st.session_state.logged_in = True
                pg.change_page(shopping.Page)
              
              # If invalid, user must try again with new, correct credentials
              else:
                st.error("Incorrect username or password, please try again.")
          
        return page_container

        


