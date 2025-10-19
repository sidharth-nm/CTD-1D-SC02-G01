import streamlit as st
import pagination as pg
import create_account_frontend as front
import payment_frontend as payment
import login_frontend as login
import shopping_backend as shopback

class Page:
    #create Page object
    def __init__(self):
        pass

    #TODO: update the total and shopping list database and total in this script
    def update_payment(self):
        #get total
        total = 0
        books_to_buy = []

        for book_id in st.session_state.books_in_cart['book_ids']:
            book = shopback.get_book_by_id(book_id)
            total += book["price"]
            books_to_buy.append(book_id)

        #store total
        st.session_state.books_in_cart["total"] = round(total,2)
        #store book
        st.session_state.books_in_cart['book_ids'] = books_to_buy[:]

    #add only 1 book to cart (I got no time to make it so versatile)
    def add_to_cart(self,book_id):
        if  book_id not in st.session_state.books_in_cart['book_ids']:
            st.session_state.books_in_cart['book_ids'].append(book_id)
            self.update_payment()

    #remove only 1 book to cart (I got no time to make it so versatile)
    def remove_from_cart(self, book_id):
        if book_id in st.session_state.books_in_cart['book_ids']:
            st.session_state.books_in_cart['book_ids'].remove(book_id)
            self.update_payment()

    #show search results using the input keywoard by user
    def update_results(self):
        if not st.session_state.search_performed:
            return
        if st.session_state.curr_search_input:
            results_list = shopback.get_search_results(st.session_state.curr_search_input)

            #if nothing, give none
            if not results_list:
                st.session_state.book_cards_to_display = None
            #else store results from search
            else:
                st.session_state.book_cards_to_display = results_list
        else:
            st.session_state.book_cards_to_display = None
        st.session_state.search_performed = False

    #search btn listener that starts update results function
    def handle_search(self):
        st.session_state.search_performed = True
        self.update_results()

    def render(self):
        # Initialize session state for the book display elements if not already present
        if "book_cards_to_display" not in st.session_state:
            st.session_state.book_cards_to_display = []

        # Initialize session state for the input if not already present
        if "curr_search_input" not in st.session_state:
            st.session_state.curr_search_input = " "

        # Initialize session state for the search performed check if not already present
        if "search_performed" not in st.session_state:
            st.session_state.search_performed = False

        # Initialize session state for the books in cart if not already present
        if "books_in_cart" not in st.session_state:
            #storing the books in ids because of the add book btn that is returning ONLY the book id,
            #use the datahandler.py's get_book_by_id function to retrieve kill me
            st.session_state.books_in_cart = {'total':0,'book_ids':[]}

        #initialise book cards elements
        self.handle_search()

        #display the shopping container
        shopping_container = st.container()
        with shopping_container:
            with st.container(width = "stretch"):
                col1, col2 = st.columns([0.1, 0.9])
                with col1:
                    #the search icon
                    st.markdown('<p style="font-size: 30px; padding-left: 20px;">🔎</p>', unsafe_allow_html=True)
                with col2:
                    with st.form("search_form", enter_to_submit=False,border=False):
                        col1, col2 = st.columns([0.8, 0.2])
                        #a search bar
                        with col1:
                            st.text_input(
                                "",
                                placeholder="Search by genre, author or title",
                                label_visibility="collapsed",
                                key="curr_search_input"
                                )
                        # Search button
                        with col2:
                            st.form_submit_button("Search", on_click=self.handle_search)


            with st.container(width = "stretch"):
                col1, col2 = st.columns([0.7, 0.3])
                #the search results
                with col1:
                    if st.session_state.book_cards_to_display == None:
                        st.write("Search for books to see results")
                    else:
                        # Display the current book cards from session state
                        with st.container(height=800,border = False):
                          for book in st.session_state.book_cards_to_display:
                              with st.container(border=True):
                                  book_card_col1,book_card_col2 = st.columns([0.4,0.5])
                                  with book_card_col1:
                                    st.markdown(f'<b>{book["title"]}</b>', unsafe_allow_html=True)
                                    st.markdown(f'by {book["author"]}', unsafe_allow_html=True)
                                    st.markdown(f'<u>{book["genre"]}</u>', unsafe_allow_html=True)
                                    st.markdown(f'<span style="color: green;">{book["price"]}', unsafe_allow_html=True)
                                  with book_card_col2:
                                    if book['image'] != "":
                                      st.image(book["image"], width=200)
                                  st.button("Add to Cart", key=f"add_{book['id']}", on_click=self.add_to_cart, args=(book["id"],))
                #sidebar containing cart list
                with col2:
                    with st.container(height = 800, border = True):
                        st.header("Cart",anchor =False)
                        #Display all books addded to cart
                        books_displayed_in_cart = st.container(height = 450, border = False)
                        with books_displayed_in_cart:
                            if len(st.session_state.books_in_cart['book_ids']) == 0:
                                st.write("No books in cart")
                            else:
                                for book_id in st.session_state.books_in_cart['book_ids']:
                                    book = shopback.get_book_by_id(book_id)
                                    with st.container(border=True):
                                        st.markdown(f'<b>{book["title"]}</b>', unsafe_allow_html=True)
                                        st.markdown(f'by {book["author"]}', unsafe_allow_html=True)
                                        st.markdown(f'<span style="color: green;">{book["price"]}', unsafe_allow_html=True)
                                        st.button("Remove", key=f"remove_{book['id']}", on_click=self.remove_from_cart, args=(book["id"],))

                        st.divider()

                        #the total cost information and checkout btn at the bottom of the cart
                        with st.container():
                            st.markdown(f'Total: {st.session_state.books_in_cart["total"]}')
                            checkout_btn_clicked = st.button("Checkout")
                            if checkout_btn_clicked:
                                if len(st.session_state.books_in_cart['book_ids']) > 0:
                                    pg.change_page(login.Page)
                                else:
                                    st.error("Please add books to cart")

        return shopping_container