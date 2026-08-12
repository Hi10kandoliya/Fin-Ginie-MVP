
import streamlit as st

from utils.goals_helper import (
    calculate_goal_progress,
    calculate_months_to_goal,
    calculate_required_monthly_savings,
)


st.set_page_config(
    page_title="Financial Goals",
    page_icon="🎯",
    layout="wide",
)


st.title("🎯 Financial Goal Planner")

st.markdown(
    """
    Set a financial goal and estimate how much
    you may need to save each month to reach it.
    """
)


goal_type = st.selectbox(
    "What is your financial goal?",
    [
        "Emergency Fund",
        "Buy a Home",
        "Buy a Car",
        "Education",
        "Vacation",
        "Debt-Free Goal",
        "Retirement",
        "Other",
    ],
)


col1, col2 = st.columns(2)


with col1:

    target_amount = st.number_input(
        "Target Amount ($)",
        min_value=100.0,
        value=10000.0,
        step=500.0,
    )

    current_savings = st.number_input(
        "Current Savings ($)",
        min_value=0.0,
        value=2000.0,
        step=500.0,
    )


with col2:

    monthly_contribution = st.number_input(
        "Current Monthly Contribution ($)",
        min_value=0.0,
        value=500.0,
        step=50.0,
    )

    target_months = st.number_input(
        "Target Timeframe (Months)",
        min_value=1,
        max_value=600,
        value=24,
        step=1,
    )


if st.button(
    "🎯 Analyze Goal",
    type="primary",
):

    progress = calculate_goal_progress(
        target_amount,
        current_savings,
    )

    months_needed = calculate_months_to_goal(
        target_amount,
        current_savings,
        monthly_contribution,
    )

    required_monthly = (
        calculate_required_monthly_savings(
            target_amount,
            current_savings,
            target_months,
        )
    )


    st.markdown("---")

    st.subheader(
        f"🎯 {goal_type}"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Goal",
            f"${target_amount:,.0f}",
        )


    with col2:

        st.metric(
            "Current Savings",
            f"${current_savings:,.0f}",
        )


    with col3:

        st.metric(
            "Remaining",
            f"${progress['remaining']:,.0f}",
        )


    st.progress(
        progress["progress"] / 100
    )


    st.write(
        f"**Goal Progress:** "
        f"{progress['progress']:.1f}%"
    )


    st.markdown("---")

    st.subheader("📅 Savings Plan")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Estimated Months at Current Contribution",
            (
                "Already reached"
                if months_needed == 0
                else (
                    "Not achievable"
                    if months_needed is None
                    else f"{months_needed} months"
                )
            ),
        )


    with col2:

        st.metric(
            "Required Monthly Savings",
            f"${required_monthly:,.2f}",
        )


    if months_needed is not None:

        if months_needed <= target_months:

            st.success(
                "Your current monthly contribution "
                "may be sufficient to reach the goal "
                "within your target timeframe."
            )

        else:

            st.warning(
                "Your current contribution may not be "
                "enough to reach the goal within the "
                "selected timeframe."
            )


st.markdown("---")

st.caption(
    "This planner provides estimates and does not "
    "account for taxes, investment returns, inflation, "
    "fees, or other factors."
)
