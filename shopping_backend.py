import data_handler as dh
import streamlit as st

#get a book by id
def get_book_by_id(id):
  return dh.get_book_by_id(id)

#Get results based on keyword
def get_search_results(keyword):
    filtered_results = []

    #get books where title contains keyword
    for book in dh.get_filtered_books_list("title", keyword):
        if book not in filtered_results:
            filtered_results.append(book)

    #get books where genre contains keyword
    for book in dh.get_filtered_books_list("genre", keyword):
        if book not in filtered_results:
            filtered_results.append(book)

    #get books where author contains keyword
    for book in dh.get_filtered_books_list("author", keyword):
        if book not in filtered_results:
            filtered_results.append(book)

    return filtered_results
