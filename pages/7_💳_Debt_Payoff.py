
import streamlit as st

from utils.debt_helper import (
    calculate_debt_payoff,
    calculate_extra_payment_impact,
)


st.set_page_config(
    page_title="Debt Payoff Planner",
    page_icon="💳",
    layout="wide",
)


st.title("💳 Debt Payoff Planner")

st.markdown(
    """
    Estimate how long it may take to pay off a debt
    and explore the potential impact of making extra
    monthly payments.
    """
)


debt_type = st.selectbox(
    "Debt Type",
    [
        "Credit Card",
        "Auto Loan",
        "Personal Loan",
        "Student Loan",
        "Other",
    ],
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
        "Annual Interest Rate / APR (%)",
        min_value=0.0,
        max_value=100.0,
        value=18.0,
        step=0.1,
    )


with col2:

    monthly_payment = st.number_input(
        "Current Monthly Payment ($)",
        min_value=0.0,
        value=300.0,
        step=25.0,
    )

    extra_payment = st.number_input(
        "Additional Monthly Payment ($)",
        min_value=0.0,
        value=50.0,
        step=25.0,
    )


if st.button(
    "💳 Analyze Debt",
    type="primary",
):

    result = calculate_debt_payoff(
        balance,
        annual_rate,
        monthly_payment,
    )


    st.markdown("---")

    st.subheader(
        f"📊 {debt_type} Payoff Estimate"
    )


    if result is None:

        st.error(
            "Please enter a valid monthly payment."
        )


    elif result.get("impossible"):

        st.error(
            result["reason"]
        )


    else:

        years = result["months"] // 12
        remaining_months = (
            result["months"] % 12
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Payoff Time",
                f"{years}y {remaining_months}m",
            )


        with col2:

            st.metric(
                "Total Interest",
                f"${result['total_interest']:,.2f}",
            )


        with col3:

            st.metric(
                "Total Paid",
                f"${result['total_paid']:,.2f}",
            )


        st.markdown("---")

        st.subheader(
            "🚀 Impact of Extra Payments"
        )


        impact = calculate_extra_payment_impact(
            balance,
            annual_rate,
            monthly_payment,
            extra_payment,
        )


        if impact:

            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "Months Saved",
                    impact["months_saved"],
                )


            with col2:

                st.metric(
                    "Potential Interest Saved",
                    f"${impact['interest_saved']:,.2f}",
                )


            st.info(
                f"By paying an additional "
                f"${extra_payment:,.2f} per month, "
                f"the estimated payoff period could "
                f"be reduced by approximately "
                f"{impact['months_saved']} months."
            )


st.markdown("---")

st.caption(
    "Debt calculations are estimates. Actual payoff "
    "results can vary based on compounding, payment "
    "dates, fees, and lender policies."
)
