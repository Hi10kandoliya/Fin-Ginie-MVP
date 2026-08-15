import streamlit as st



st.set_page_config(
    page_title="FinGenie",
    page_icon="🧠",
    layout="wide",
)



st.sidebar.title("🧠 FinGenie")
st.sidebar.markdown("### AI Financial Guide")

st.title("🧠 Welcome to FinGenie")

st.subheader(
    "Your AI-powered financial education and decision-support assistant."
)

st.markdown(
    """
    FinGenie helps you:

    - 💰 Explore financial products
    - ⚖️ Compare financial products
    - 🧮 Calculate loan and savings estimates
    - 🎯 Plan financial goals
    - 📊 Create a personal budget
    - 💳 Build a debt payoff strategy
    - 💬 Ask financial questions using AI
    """
)

st.info(
    "Select a feature from the sidebar to get started."
)

st.markdown("---")

st.warning(
    """
    **Financial Disclaimer**

    FinGenie provides educational and informational content only.
    It is not a financial advisor and does not provide personalized
    financial, investment, tax, or legal advice.
    """
)
