import streamlit as st
import shopping_backend as shop_back

def get_books():
  book_list = []
  if "books_in_cart" in st.session_state:
    for book_id in st.session_state.books_in_cart['book_ids']:
      book = shop_back.get_book_by_id(book_id)
      if book:
        book_list.append(book)
  return book_list