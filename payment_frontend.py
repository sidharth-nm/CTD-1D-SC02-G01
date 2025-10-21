# Imports
import streamlit as st
import payment_backend as pay_back
import pagination as pg
import confirmation_frontend as conf_front #if user proceeds to pay
import shopping_frontend as shop_front #if user decides to edit their shopping cart or add something

class Page:
  #create page object
  def __init__(self):
    pass

  def render(self):
    st.title("Order Summary") #cannot show the execution of the payment methods as it is out of the scope of our code

    # Cannot proceed to payment if cart is empty
    if len(st.session_state.books_in_cart['book_ids']) == 0 or "books_in_cart" not in st.session_state:
      st.error("Your cart is empty. Please add items.")

    # Displays final price to be paid
    total_to_pay = pay_back.total_with_gst()
    st.markdown("Grand total with 9%% GST: %f" % round(total_to_pay[0], 2))
    # Displays a message if bill qualifies for a discount
    if total_to_pay[1]:
      st.success("Your bill was over $35, so a 10% discount was applied!")

    col1, col2 = st.columns(2)

    with col1:
      continue_shopping_btn = st.button("Continue Shopping")

    with col2:
      checkout_btn = st.button("Proceed to Checkout")

    # Event listener for Continue Shopping button
    if continue_shopping_btn:
      pg.change_page(shop_front.Page)

    # Event listener for Checkout button
    if checkout_btn:
      pg.change_page(conf_front.Page)

