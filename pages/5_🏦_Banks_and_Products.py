import streamlit as st

from utils.bank_data import (
    banks,
    get_bank_products,
    get_product_categories,
    get_products_by_category,
)

from utils.ai_helper import generate_financial_chat_response

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Banks & Financial Products",
    page_icon="🏦",
    layout="wide",
)


# =========================================================
# HEADER
# =========================================================

st.title(
    "🏦 Banks & Financial Products"
)

st.markdown(
    """
    Explore financial products offered by selected
    financial institutions and learn what to consider
    before contacting a bank.
    """
)


# =========================================================
# DISCLAIMER
# =========================================================

st.warning(
    """
    **Important:** FinGenie provides general educational
    information. Product availability, interest rates,
    APYs, fees, eligibility requirements, and terms can
    change. Always verify current information directly
    with the financial institution before applying.
    """
)



# =========================================================
# SEARCH / FILTER
# =========================================================

st.subheader(
    "🔎 Find a Financial Product"
)


col1, col2 = st.columns(2)


with col1:

    selected_bank = st.selectbox(
        "Select a Bank",
        list(banks.keys()),
    )


with col2:

    categories = get_product_categories(
        selected_bank
    )

    selected_category = st.selectbox(
        "Product Category",
        ["All"] + categories,
    )


# =========================================================
# BANK INFORMATION
# =========================================================

bank = banks[
    selected_bank
]


st.markdown("---")

st.subheader(
    f"🏦 {selected_bank}"
)

st.write(
    bank["description"]
)


# =========================================================
# PRODUCT FILTER
# =========================================================

if selected_category == "All":

    products = get_bank_products(
        selected_bank
    )

else:

    products = get_products_by_category(
        selected_bank,
        selected_category
    )


# =========================================================
# PRODUCT COUNT
# =========================================================

st.caption(
    f"{len(products)} product(s) available in "
    f"the FinGenie MVP catalog."
)


# =========================================================
# PRODUCT CARDS
# =========================================================

for product_name, product in products.items():

    with st.container(
        border=True
    ):

        st.subheader(
            product["name"]
        )

        st.caption(
            f'{product["category"]} • '
            f'{product["type"]}'
        )


        col1, col2 = st.columns(2)

# =========================================================
# PRODUCT-SPECIFIC FINANCIAL CHAT
# =========================================================

if st.session_state.get("show_product_chat", False):

    st.markdown("---")

    st.subheader("💬 Ask FinGenie")

    chat_product = st.session_state.get(
        "chat_product",
        product_name,
    )

    chat_bank = st.session_state.get(
        "chat_bank",
        bank_name,
    )

    st.info(
        f"""
        You are asking about **{chat_product}**
        from **{chat_bank}**.

        FinGenie will use this product as context when
        answering your questions.
        """
    )

    # -----------------------------------------------------
    # DISPLAY CHAT HISTORY
    # -----------------------------------------------------

    if "financial_chat_history" not in st.session_state:

        st.session_state["financial_chat_history"] = []


    for message in st.session_state[
        "financial_chat_history"
    ]:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


    # -----------------------------------------------------
    # CHAT INPUT
    # -----------------------------------------------------

    user_question = st.chat_input(
        f"Ask a question about {chat_product}..."
    )


    if user_question:

        # Add user question
        st.session_state[
            "financial_chat_history"
        ].append(
            {
                "role": "user",
                "content": user_question,
            }
        )


        # Display user message immediately
        with st.chat_message("user"):

            st.markdown(
                user_question
            )


        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner(
                "FinGenie is thinking..."
            ):

                try:

                    response = (
                        generate_financial_chat_response(
                            product_name=chat_product,
                            bank_name=chat_bank,
                            user_question=user_question,
                            chat_history=st.session_state[
                                "financial_chat_history"
                            ],
                        )
                    )

                except Exception as e:

                    response = (
                        "I'm sorry, I couldn't generate "
                        "a response right now. "
                        "Please try again."
                    )

                    st.error(
                        f"AI error: {e}"
                    )


                st.markdown(
                    response
                )


        # Save AI response
        st.session_state[
            "financial_chat_history"
        ].append(
            {
                "role": "assistant",
                "content": response,
            }
        )


    # -----------------------------------------------------
    # CLEAR CHAT
    # -----------------------------------------------------

    if st.session_state.get(
        "financial_chat_history"
    ):

        if st.button(
            "🗑️ Clear Conversation",
            key=f"clear_chat_{chat_product}",
        ):

            st.session_state[
                "financial_chat_history"
            ] = []

            st.rerun()


        
        # -------------------------------------------------
        # FEATURES
        # -------------------------------------------------

        with col1:

            st.markdown(
                "### ⭐ Key Features"
            )

            for feature in product.get(
                "features",
                []
            ):

                st.markdown(
                    f"• {feature}"
                )


        # -------------------------------------------------
        # CONSIDERATIONS
        # -------------------------------------------------

        with col2:

            st.markdown(
                "### ⚠️ Things to Consider"
            )

            for item in product.get(
                "considerations",
                []
            ):

                st.markdown(
                    f"• {item}"
                )


        # -------------------------------------------------
        # WHO MAY CONSIDER
        # -------------------------------------------------

        st.markdown(
            "### 👤 Common Use Cases"
        )

        best_for = product.get(
            "best_for",
            []
        )

        st.write(
            " • ".join(best_for)
        )


        # -------------------------------------------------
        # NEXT STEPS
        # -------------------------------------------------

        st.markdown(
            "### 🚀 Next Steps"
        )

        st.write(
            """
            Before applying, review the current
            product terms, fees, eligibility requirements,
            interest rate/APY, and access requirements.
            """
        )


        button_col1, button_col2 = st.columns(2)


        with button_col1:

            st.link_button(
                "🌐 Visit Official Bank Website",
                product["official_url"],
                use_container_width=True,
            )


col1, col2 = st.columns(2)

with col1:

    st.link_button(
        "🌐 Visit Official Bank Website",
        bank_url,
        use_container_width=True,
    )


with col2:

    if st.button(
        "💬 Ask FinGenie",
        use_container_width=True,
        key=f"ask_fingenie_{bank_name}_{product_name}",
    ):

        # Store the product context
        st.session_state["chat_product"] = product_name
        st.session_state["chat_bank"] = bank_name

        # Open the chat section
        st.session_state["show_product_chat"] = True

        # Initialize chat history
        if "financial_chat_history" not in st.session_state:
            st.session_state["financial_chat_history"] = []

        st.rerun()


# =========================================================
# BANK WEBSITE
# =========================================================

st.markdown("---")

st.subheader(
    "🌐 Contact / Learn More"
)

st.write(
    f"Visit the official {selected_bank} website "
    "to verify current product information."
)

st.link_button(
    f"Visit {selected_bank}",
    bank["website"],
)
