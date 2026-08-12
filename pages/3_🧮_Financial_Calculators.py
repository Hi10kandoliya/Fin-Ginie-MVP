import streamlit as st

from utils.financial_calculators import (
    calculate_loan_payment,
    calculate_mortgage_payment,
    calculate_compound_interest,
    calculate_simple_interest,
    calculate_savings_goal,
    calculate_debt_payoff,
    calculate_investment_return,
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Financial Calculators",
    page_icon="🧮",
    layout="wide",
)


# =========================================================
# HEADER
# =========================================================

st.title(
    "🧮 Financial Calculators"
)

st.markdown(
    """
    Use FinGenie's calculators to estimate loan payments,
    savings requirements, interest growth, debt payoff,
    and other financial scenarios.
    """
)


# =========================================================
# DISCLAIMER
# =========================================================

st.warning(
    """
    **Financial Calculator Disclaimer**

    These calculators provide estimates for educational
    purposes only. Actual results may vary based on rates,
    fees, taxes, compounding methods, lender policies,
    account terms, and other factors.

    These calculations are not financial, investment,
    tax, or legal advice.
    """
)


# =========================================================
# CALCULATOR SELECTOR
# =========================================================

calculator = st.selectbox(
    "Select a Calculator",
    [
        "💳 Loan Payment",
        "🏠 Mortgage Payment",
        "💰 Compound Interest",
        "📈 Simple Interest",
        "🎯 Savings Goal",
        "💳 Debt Payoff",
        "📊 Investment Return",
    ],
)


st.markdown("---")


# =========================================================
# LOAN PAYMENT
# =========================================================

if calculator == "💳 Loan Payment":

    st.header(
        "💳 Loan Payment Calculator"
    )

    col1, col2 = st.columns(2)

    with col1:

        principal = st.number_input(
            "Loan Amount ($)",
            min_value=0.0,
            value=25000.0,
            step=1000.0,
        )

        annual_rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            value=7.0,
            step=0.1,
        )

    with col2:

        years = st.number_input(
            "Loan Term (Years)",
            min_value=1,
            max_value=50,
            value=5,
        )

    if st.button(
        "Calculate Loan Payment",
        type="primary",
    ):

        result = calculate_loan_payment(
            principal,
            annual_rate,
            years,
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Monthly Payment",
            f"${result['monthly_payment']:,.2f}",
        )

        col2.metric(
            "Total Payment",
            f"${result['total_payment']:,.2f}",
        )

        col3.metric(
            "Total Interest",
            f"${result['total_interest']:,.2f}",
        )


# =========================================================
# MORTGAGE
# =========================================================

elif calculator == "🏠 Mortgage Payment":

    st.header(
        "🏠 Mortgage Payment Calculator"
    )

    col1, col2 = st.columns(2)

    with col1:

        home_price = st.number_input(
            "Home Price ($)",
            min_value=0.0,
            value=400000.0,
            step=5000.0,
        )

        down_payment = st.number_input(
            "Down Payment ($)",
            min_value=0.0,
            value=80000.0,
            step=5000.0,
        )

        annual_rate = st.number_input(
            "Mortgage Rate (%)",
            min_value=0.0,
            value=6.5,
            step=0.1,
        )

    with col2:

        years = st.number_input(
            "Loan Term",
            min_value=1,
            max_value=50,
            value=30,
        )

        property_tax = st.number_input(
            "Annual Property Tax ($)",
            min_value=0.0,
            value=6000.0,
            step=500.0,
        )

        annual_insurance = st.number_input(
            "Annual Home Insurance ($)",
            min_value=0.0,
            value=1800.0,
            step=100.0,
        )


    if down_payment >= home_price:

        st.error(
            "Down payment must be less than the home price."
        )

    elif st.button(
        "Calculate Mortgage",
        type="primary",
    ):

        result = calculate_mortgage_payment(
            home_price,
            down_payment,
            annual_rate,
            years,
            property_tax,
            annual_insurance,
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Loan Amount",
            f"${result['loan_amount']:,.2f}",
        )

        col2.metric(
            "Principal + Interest",
            f"${result['principal_interest']:,.2f}/mo",
        )

        col3.metric(
            "Estimated Monthly Cost",
            f"${result['estimated_monthly_total']:,.2f}",
        )

        st.info(
            "This estimate does not include potential PMI, "
            "HOA fees, closing costs, or other expenses."
        )


# =========================================================
# COMPOUND INTEREST
# =========================================================

elif calculator == "💰 Compound Interest":

    st.header(
        "💰 Compound Interest Calculator"
    )

    col1, col2 = st.columns(2)

    with col1:

        principal = st.number_input(
            "Initial Amount ($)",
            min_value=0.0,
            value=10000.0,
            step=500.0,
        )

        annual_rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            value=5.0,
            step=0.1,
        )

    with col2:

        years = st.number_input(
            "Time Period (Years)",
            min_value=1,
            max_value=100,
            value=10,
        )

     compounding_options = {
    "Annually": 1,
    "Semi-annually": 2,
    "Quarterly": 4,
    "Monthly": 12,
    "Daily": 365,
}

compounding_label = st.selectbox(
    "Compounding Frequency",
    list(compounding_options.keys()),
)

compounds = compounding_options[
    compounding_label
]


    if st.button(
        "Calculate Compound Interest",
        type="primary",
    ):

        result = calculate_compound_interest(
            principal,
            annual_rate,
            years,
            compounds,
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Future Value",
            f"${result['future_value']:,.2f}",
        )

        col2.metric(
            "Interest Earned",
            f"${result['interest_earned']:,.2f}",
        )


# =========================================================
# SIMPLE INTEREST
# =========================================================

elif calculator == "📈 Simple Interest":

    st.header(
        "📈 Simple Interest Calculator"
    )

    principal = st.number_input(
        "Principal ($)",
        min_value=0.0,
        value=10000.0,
        step=500.0,
    )

    annual_rate = st.number_input(
        "Annual Interest Rate (%)",
        min_value=0.0,
        value=5.0,
        step=0.1,
    )

    years = st.number_input(
        "Time Period (Years)",
        min_value=1,
        max_value=100,
        value=5,
    )


    if st.button(
        "Calculate Simple Interest",
        type="primary",
    ):

        result = calculate_simple_interest(
            principal,
            annual_rate,
            years,
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Interest Earned",
            f"${result['interest']:,.2f}",
        )

        col2.metric(
            "Final Amount",
            f"${result['future_value']:,.2f}",
        )


# =========================================================
# SAVINGS GOAL
# =========================================================

elif calculator == "🎯 Savings Goal":

    st.header(
        "🎯 Savings Goal Calculator"
    )

    col1, col2 = st.columns(2)

    with col1:

        target_amount = st.number_input(
            "Savings Goal ($)",
            min_value=0.0,
            value=20000.0,
            step=1000.0,
        )

        current_savings = st.number_input(
            "Current Savings ($)",
            min_value=0.0,
            value=5000.0,
            step=500.0,
        )

    with col2:

        annual_rate = st.number_input(
            "Estimated Annual Rate (%)",
            min_value=0.0,
            value=4.0,
            step=0.1,
        )

        years = st.number_input(
            "Time to Goal (Years)",
            min_value=1,
            max_value=50,
            value=3,
        )


    if st.button(
        "Calculate Savings Requirement",
        type="primary",
    ):

        result = calculate_savings_goal(
            target_amount,
            current_savings,
            annual_rate,
            years,
        )

        if result.get("monthly_contribution") == 0:

            st.success(
                result["message"]
            )

        else:

            col1, col2 = st.columns(2)

            col1.metric(
                "Estimated Monthly Contribution",
                f"${result['monthly_contribution']:,.2f}",
            )

            col2.metric(
                "Remaining Amount",
                f"${result['remaining_amount']:,.2f}",
            )


# =========================================================
# DEBT PAYOFF
# =========================================================

elif calculator == "💳 Debt Payoff":

    st.header(
        "💳 Debt Payoff Calculator"
    )

    col1, col2 = st.columns(2)

    with col1:

        balance = st.number_input(
            "Current Balance ($)",
            min_value=0.0,
            value=10000.0,
            step=500.0,
        )

        annual_rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            value=20.0,
            step=0.5,
        )

    with col2:

        monthly_payment = st.number_input(
            "Monthly Payment ($)",
            min_value=0.0,
            value=400.0,
            step=25.0,
        )


    if st.button(
        "Calculate Debt Payoff",
        type="primary",
    ):

        result = calculate_debt_payoff(
            balance,
            annual_rate,
            monthly_payment,
        )

        if result.get("months") is None:

            st.error(
                result["message"]
            )

        else:

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Estimated Payoff",
                f"{result['months']} months",
            )

            col2.metric(
                "Total Paid",
                f"${result['total_paid']:,.2f}",
            )

            col3.metric(
                "Estimated Interest",
                f"${result['total_interest']:,.2f}",
            )


# =========================================================
# INVESTMENT RETURN
# =========================================================

elif calculator == "📊 Investment Return":

    st.header(
        "📊 Investment Return Calculator"
    )

    st.info(
        """
        This calculator provides a hypothetical compound-growth
        estimate. Actual investment returns are uncertain and
        can be higher or lower, including negative returns.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        initial_investment = st.number_input(
            "Initial Investment ($)",
            min_value=0.0,
            value=10000.0,
            step=500.0,
        )

        monthly_contribution = st.number_input(
            "Monthly Contribution ($)",
            min_value=0.0,
            value=500.0,
            step=50.0,
        )

    with col2:

        annual_rate = st.number_input(
            "Assumed Annual Return (%)",
            min_value=0.0,
            value=7.0,
            step=0.5,
        )

        years = st.number_input(
            "Investment Period (Years)",
            min_value=1,
            max_value=100,
            value=20,
        )


    if st.button(
        "Calculate Investment Growth",
        type="primary",
    ):

        result = calculate_investment_return(
            initial_investment,
            monthly_contribution,
            annual_rate,
            years,
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Estimated Future Value",
            f"${result['future_value']:,.2f}",
        )

        col2.metric(
            "Total Contributions",
            f"${result['total_contributed']:,.2f}",
        )

        col3.metric(
            "Estimated Growth",
            f"${result['estimated_growth']:,.2f}",
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "FinGenie calculators provide educational estimates only. "
    "Actual financial results may vary."
)
