import streamlit as st
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FinGenie",
    page_icon="🧠",
    layout="wide",
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO = BASE_DIR / "assets" / "FinGenie_Logo.png"


# =========================================================
# BRANDING (SIDEBAR)
# =========================================================

with st.sidebar:

    st.image(str(LOGO), width=180)

    st.sidebar.markdown("### AI Financial Guide")


# =========================================================
# HEADER
# =========================================================

st.title("🧠 Welcome to FinGenie")

st.subheader(
    "Your AI-powered financial education and decision-support assistant."
)


# =========================================================
# FEATURE OVERVIEW
# =========================================================

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


# =========================================================
# DISCLAIMER
# =========================================================

st.markdown("---")

st.warning(
    """
    **Financial Disclaimer**

    FinGenie provides educational and informational content
    only. It is not a financial advisor and does not provide
    personalized financial, investment, tax, or legal advice.
    """
)
