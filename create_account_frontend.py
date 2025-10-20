import streamlit as st
import pagination as pg
import data_handler as dh
import shopping_frontend as shop
import login_frontend as login
from time import sleep
import create_account_backend as caccback

class Page:
    #create Page object
    def __init__(self):
        st.session_state.logged_in = False

    def render(self):
        page_container = st.container()
        with page_container:
          #display the starting elements and add necessary listeners
          col1, middleCol, col2 = st.columns(3)
          with middleCol:
            st.image("test.jpeg", width=200)
          
          st.markdown("<h1 style='text-align: center;'>Make New Account</h1>", unsafe_allow_html=True)
          username = st.text_input("Username")
          password = st.text_input("Password", type="password")

          leftButtonCol, rightButtonCol = st.columns(2)

          with leftButtonCol:
            create_acc_button_clicked = st.button("Create Account")

            # Event listener for Create Account button
            if create_acc_button_clicked:
                print("Create Account clicked")
                print(password)
                print(password.isalnum())

                # Input validation
                if len(username.strip()) <= 5 or username == "":
                    st.error("Username field must be at least 6 characters long.")
                elif len(password.strip()) <= 7 or password == "" or password.isalnum():
                    st.error("Password must be at least 8 characters long, and contain special characters.")
                else:
                    # Input verification + account creation
                    if caccback.verify_credentials(username):
                        dh.add_user( {'username': username.strip(), 'password': password.strip()} )
                        st.success("Account successfully made! Redirecting to login page...")
                        # Temporarily pauses so reader can see success message
                        sleep(0.8)
                        pg.change_page(login.Page)
                    else:
                        st.error("Account could not be made (username is already in use)")
          

          with rightButtonCol:
            login_button_clicked = st.button("Login to Existing Account")

            # Event listener for Login button
            if login_button_clicked:
              print("Login clicked")
              pg.change_page(login.Page)



        return page_container