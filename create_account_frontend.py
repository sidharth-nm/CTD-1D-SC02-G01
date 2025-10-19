import streamlit as st

class Page:
    def __init__(self):
        self.container = st.container()

    def render(self):
        with self.container:
            st.write("## This is inside the container")
            st.write("Hello from the container!")
            name = st.text_input("Enter your name:")
            if name:
                st.success(f"Hello, {name}!")


