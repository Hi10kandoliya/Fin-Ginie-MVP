import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="FinGenie",
    page_icon="🧠",
    layout="wide",
)

# ==========================================
# Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

LOGO = BASE_DIR / "assets" / "FinGenie_Logo.png"

# ==========================================
# Branding
# ==========================================

with st.sidebar:

    st.image(str(LOGO), width=180)

    st.markdown(
        "<h2 style='text-align:center;'>FinGenie</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>AI Financial Guide</p>",
        unsafe_allow_html=True
    )

    st.divider()

# ==========================================
# Navigation
# ==========================================

pages = [
    st.Page(
        "pages/1_💬_Financial_Assistant.py",
        title="Financial Assistant",
        icon="💬"
    ),

    st.Page(
        "pages/2_📊_Product_Comparison.py",
        title="Product Comparison",
        icon="📊"
    ),

    st.Page(
        "pages/3_🧮_Calculators.py",
        title="Calculators",
        icon="🧮"
    ),

    st.Page(
        "pages/4_🎯_Financial_Goals.py",
        title="Financial Goals",
        icon="🎯"
    ),

    st.Page(
        "pages/5_🏦_Banks_Products.py",
        title="Banks & Products",
        icon="🏦"
    ),

    st.Page(
        "pages/6_💰_Budget_Planner.py",
        title="Budget Planner",
        icon="💰"
    ),

    st.Page(
        "pages/7_💳_Debt_Payoff.py",
        title="Debt Payoff",
        icon="💳"
    ),
]

pg = st.navigation(pages)

pg.run()

    
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
