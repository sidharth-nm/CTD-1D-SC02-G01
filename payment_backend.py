import streamlit as st

# calculate gst and add it to the total cost of the books to find the total the user needs to pay
def total_with_gst():
  #get total book price from shopping cart
  total = st.session_state.books_in_cart.get("total",0)
  discount_applied = False
  gst = total*0.09 # 9% gst
  if total >= 35:
    discount = 0.1*total #10% discount for users who spend over $35
    discount_applied = True
  grand_total = round(total + gst - discount, 2) # rounded to two d.p. for payment

  return (grand_total, discount_applied)