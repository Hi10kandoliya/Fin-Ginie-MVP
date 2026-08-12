import streamlit as st

from utils.ai_helper import (
    generate_chat_response,
)

from utils.financial_data import products


st.set_page_config(
    page_title="FinGenie AI Assistant",
    page_icon="💬",
    layout="wide",
)


# =========================================================
# SESSION STATE
# =========================================================

if "chat_messages" not in st.session_state:

    st.session_state.chat_messages = []


if "pending_question" not in st.session_state:

    st.session_state.pending_question = None


# =========================================================
# HEADER
# =========================================================

st.title(
    "💬 FinGenie AI Financial Assistant"
)

st.markdown(
    """
    Ask questions about financial products, saving,
    borrowing, budgeting, debt, and personal finance.
    """
)


# =========================================================
# DISCLAIMER
# =========================================================

st.warning(
    """
    **Financial Education Disclaimer**

    FinGenie provides general educational information
    and estimates. It does not provide personalized
    financial, investment, tax, legal, or accounting advice.

    Do not enter sensitive information such as your Social
    Security number, bank account number, password,
    credit/debit card number, or authentication code.
    """
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header(
    "🎯 Conversation Context"
)


selected_product = st.sidebar.selectbox(
    "Financial Product",
    ["None"] + list(products.keys()),
)


st.sidebar.markdown("---")


st.sidebar.subheader(
    "👤 Optional Profile"
)


age_range = st.sidebar.selectbox(
    "Age Range",
    [
        "Prefer not to say",
        "18–24",
        "25–34",
        "35–44",
        "45–54",
        "55–64",
        "65+",
    ],
)


financial_goal = st.sidebar.selectbox(
    "Primary Financial Goal",
    [
        "General financial education",
        "Build emergency savings",
        "Buy a home",
        "Pay down debt",
        "Save for retirement",
        "Save for education",
        "Other",
    ],
)


risk_preference = st.sidebar.selectbox(
    "General Preference",
    [
        "Prefer not to say",
        "Focus on safety",
        "Balance safety and growth",
        "Focus on growth",
    ],
)


# =========================================================
# PRODUCT CONTEXT
# =========================================================

product_context = None


if selected_product != "None":

    product = products[
        selected_product
    ]

    features = product.get(
        "features",
        []
    )

    questions = product.get(
        "common_questions",
        []
    )

    product_context = (
        f"Product Name: {selected_product}\n"
        f"Features: {', '.join(features)}\n"
        f"Common Questions: "
        f"{', '.join(questions)}"
    )


# =========================================================
# USER CONTEXT
# =========================================================

user_profile_context = (
    f"Age Range: {age_range}\n"
    f"Primary Goal: {financial_goal}\n"
    f"General Preference: {risk_preference}"
)


# =========================================================
# CHAT HISTORY
# =========================================================

st.subheader(
    "💬 Conversation"
)


if not st.session_state.chat_messages:

    st.info(
        "👋 Hello! I'm FinGenie. "
        "What would you like to know about finance?"
    )


for message in (
    st.session_state.chat_messages
):

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =========================================================
# SUGGESTED QUESTIONS
# =========================================================

st.markdown(
    "### 💡 Suggested Questions"
)


if selected_product != "None":

    product_questions = products[
        selected_product
    ].get(
        "suggested_questions",
        []
    )

else:

    product_questions = []


if not product_questions:

    product_questions = [
        "What is the difference between a savings account and a CD?",
        "What are the advantages of a high-yield savings account?",
        "What are the risks of a CD?",
        "Which financial products are more liquid?",
    ]


columns = st.columns(2)


for index, question in enumerate(
    product_questions[:4]
):

    with columns[index % 2]:

        if st.button(
            question,
            key=f"suggestion_{index}",
            use_container_width=True,
        ):

            st.session_state.pending_question = (
                question
            )

            st.rerun()


# =========================================================
# CHAT INPUT
# =========================================================

user_question = st.chat_input(
    "Ask FinGenie a financial question..."
)


if st.session_state.pending_question:

    user_question = (
        st.session_state.pending_question
    )

    st.session_state.pending_question = None


# =========================================================
# AI RESPONSE
# =========================================================

if user_question:

    # -----------------------------------------------------
    # Save user message
    # -----------------------------------------------------

    st.session_state.chat_messages.append(
        {
            "role": "user",
            "content": user_question,
        }
    )


    # -----------------------------------------------------
    # Display user message
    # -----------------------------------------------------

    with st.chat_message(
        "user"
    ):

        st.markdown(
            user_question
        )


    # -----------------------------------------------------
    # Generate AI response
    # -----------------------------------------------------

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "FinGenie is thinking..."
        ):

            try:

                response = (
                    generate_chat_response(

                        user_question=(
                            user_question
                        ),

                        conversation_history=(
                            st.session_state
                            .chat_messages[-20:-1]
                        ),

                        product_context=(
                            product_context
                        ),

                        user_profile_context=(
                            user_profile_context
                        ),
                    )
                )

            except Exception:

                response = (
                    "I'm sorry, I couldn't process "
                    "your question right now. "
                    "Please try again."
                )


        st.markdown(
            response
        )


    # -----------------------------------------------------
    # Save AI response
    # -----------------------------------------------------

    st.session_state.chat_messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )


# =========================================================
# CLEAR CHAT
# =========================================================

st.markdown("---")


if st.button(
    "🗑️ Clear Conversation"
):

    st.session_state.chat_messages = []

    st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "FinGenie provides educational information only. "
    "Verify current rates, fees, terms, eligibility, "
    "and product availability with the relevant "
    "financial institution."
)
