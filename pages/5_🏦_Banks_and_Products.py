import streamlit as st

from utils.bank_data import (
    banks,
    get_bank_products,
    get_product_categories,
    get_products_by_category,
)
from utils.ai_helper import generate_chat_response



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

bank = banks[selected_bank]

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
        selected_category,
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

    with st.container(border=True):

        st.subheader(
            product["name"]
        )

        st.caption(
            f'{product["category"]} • '
            f'{product["type"]}'
        )

        col1, col2 = st.columns(2)

        # -------------------------------------------------
        # FEATURES
        # -------------------------------------------------

        with col1:

            st.markdown("### ⭐ Key Features")

            for feature in product.get("features", []):

                st.markdown(f"• {feature}")

        # -------------------------------------------------
        # CONSIDERATIONS
        # -------------------------------------------------

        with col2:

            st.markdown("### ⚠️ Things to Consider")

            for item in product.get("considerations", []):

                st.markdown(f"• {item}")

        # -------------------------------------------------
        # WHO MAY CONSIDER
        # -------------------------------------------------

        st.markdown("### 👤 Common Use Cases")

        best_for = product.get("best_for", [])

        st.write(" • ".join(best_for))

        # -------------------------------------------------
        # NEXT STEPS
        # -------------------------------------------------

        st.markdown("### 🚀 Next Steps")

        st.write(
            """
            Before applying, review the current
            product terms, fees, eligibility requirements,
            interest rate/APY, and access requirements.
            """
        )

        # -------------------------------------------------
        # ACTIONS
        # -------------------------------------------------

        button_col1, button_col2 = st.columns(2)

        with button_col1:

            st.link_button(
                "🌐 Visit Official Bank Website",
                product["official_url"],
                use_container_width=True,
            )

        with button_col2:

            if st.button(
                "💬 Ask FinGenie",
                use_container_width=True,
                key=f"ask_fingenie_{selected_bank}_{product_name}",
            ):

                # Store the product context
                st.session_state["chat_product"] = product_name
                st.session_state["chat_bank"] = selected_bank

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

# Build user profile context (same style as Financial Assistance page)
user_profile_context = """
The user is exploring financial products and may need guidance
based on general financial literacy, risk awareness, and product suitability.
"""
# =========================================================
# PRODUCT CHAT SECTION (BOTTOM OF PAGE)
# =========================================================

st.markdown("---")

# Only show chat if user clicked Ask FinGenie
if st.session_state.get("show_product_chat"):

    st.subheader("💬 Chat with FinGenie About This Product")

    # Build context from selected bank + product
    chat_bank = st.session_state.get("chat_bank")
    chat_product = st.session_state.get("chat_product")

    context_text = f"""
    The user is asking about the financial product:
    • Bank: {chat_bank}
    • Product: {chat_product}

    Provide helpful, clear, educational guidance.
    """

    # Show previous messages
    for msg in st.session_state["financial_chat_history"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # Chat input
    user_input = st.chat_input("Ask FinGenie…")

    if user_input:
        # Add user message
        st.session_state["financial_chat_history"].append(
            {"role": "user", "content": user_input}
        )

        # Call your existing LLM function from Financial Assistance page
        response = generate_chat_response(
        user_question=user_input,
        conversation_history=st.session_state["financial_chat_history"][-20:],
        product_context=context_text,
        user_profile_context=user_profile_context
        )
    
        st.session_state["financial_chat_history"].append(
        {"role": "assistant", "content": response}
        )
             

        st.rerun()



