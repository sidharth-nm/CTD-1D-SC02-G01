import streamlit as st

# calculate gst and add it to the total cost of the books to find the total the user needs to pay
def total_with_gst():
  #get total book price from shopping cart
  total = st.session_state.books_in_cart.get("total",0)
  gst = total*0.09 # 9% gst
  grand_total = round(total + gst, 2) # rounded to two d.p. for payment

  return grand_total