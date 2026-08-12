
import streamlit as st

from utils.budget_helper import (
    calculate_budget,
)


st.set_page_config(
    page_title="Budget Planner",
    page_icon="📊",
    layout="wide",
)


st.title("📊 Budget Planner")

st.markdown(
    """
    Enter your estimated monthly income and expenses
    to understand your monthly cash flow.
    """
)


monthly_income = st.number_input(
    "Monthly Take-Home Income ($)",
    min_value=0.0,
    value=5000.0,
    step=250.0,
)


st.subheader("🏠 Monthly Expenses")


col1, col2 = st.columns(2)


with col1:

    housing = st.number_input(
        "Housing",
        min_value=0.0,
        value=1500.0,
        step=100.0,
    )

    utilities = st.number_input(
        "Utilities",
        min_value=0.0,
        value=300.0,
        step=50.0,
    )

    transportation = st.number_input(
        "Transportation",
        min_value=0.0,
        value=400.0,
        step=50.0,
    )

    groceries = st.number_input(
        "Groceries",
        min_value=0.0,
        value=500.0,
        step=50.0,
    )


with col2:

    insurance = st.number_input(
        "Insurance",
        min_value=0.0,
        value=250.0,
        step=50.0,
    )

    debt_payments = st.number_input(
        "Debt Payments",
        min_value=0.0,
        value=300.0,
        step=50.0,
    )

    entertainment = st.number_input(
        "Entertainment",
        min_value=0.0,
        value=200.0,
        step=50.0,
    )

    other_expenses = st.number_input(
        "Other Expenses",
        min_value=0.0,
        value=200.0,
        step=50.0,
    )


if st.button(
    "📊 Analyze Budget",
    type="primary",
):

    result = calculate_budget(
        monthly_income,
        housing,
        utilities,
        transportation,
        groceries,
        insurance,
        debt_payments,
        entertainment,
        other_expenses,
    )


    st.markdown("---")

    st.subheader("📊 Monthly Budget Summary")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Monthly Income",
            f"${monthly_income:,.2f}",
        )


    with col2:

        st.metric(
            "Total Expenses",
            f"${result['total_expenses']:,.2f}",
        )


    with col3:

        st.metric(
            "Remaining",
            f"${result['remaining']:,.2f}",
        )


    st.markdown("---")


    st.subheader("📈 Budget Breakdown")


    for category, amount in result[
        "expenses"
    ].items():

        percentage = (
            amount / monthly_income * 100
            if monthly_income > 0
            else 0
        )

        st.write(
            f"**{category}:** "
            f"${amount:,.2f} "
            f"({percentage:.1f}%)"
        )

        st.progress(
            min(percentage / 100, 1.0)
        )


    st.markdown("---")


    if result["remaining"] > 0:

        st.success(
            f"You have approximately "
            f"${result['remaining']:,.2f} "
            "remaining after the listed expenses."
        )

    elif result["remaining"] == 0:

        st.warning(
            "Your listed expenses equal your monthly income."
        )

    else:

        st.error(
            f"Your listed expenses exceed income by "
            f"${abs(result['remaining']):,.2f}."
        )


st.markdown("---")

st.caption(
    "Budget estimates are educational and may not "
    "represent your complete financial situation."
)
