"""
FinGenie Financial Calculators

All calculations are performed deterministically using Python.
AI should be used only to explain results, not calculate them.
"""

import math


# =========================================================
# LOAN PAYMENT
# =========================================================

def calculate_loan_payment(
    principal,
    annual_rate,
    years,
):
    """
    Calculate monthly loan payment.

    Uses standard amortizing loan formula.
    """

    monthly_rate = (
        annual_rate / 100 / 12
    )

    number_of_payments = (
        years * 12
    )

    if monthly_rate == 0:

        monthly_payment = (
            principal /
            number_of_payments
        )

    else:

        monthly_payment = (
            principal
            * monthly_rate
            * (1 + monthly_rate)
            ** number_of_payments
            /
            (
                (1 + monthly_rate)
                ** number_of_payments
                - 1
            )
        )

    total_payment = (
        monthly_payment
        * number_of_payments
    )

    total_interest = (
        total_payment
        - principal
    )

    return {
        "monthly_payment": monthly_payment,
        "total_payment": total_payment,
        "total_interest": total_interest,
    }


# =========================================================
# MORTGAGE PAYMENT
# =========================================================

def calculate_mortgage_payment(
    home_price,
    down_payment,
    annual_rate,
    years,
    property_tax=0,
    annual_insurance=0,
):
    """
    Estimate monthly mortgage payment.

    Includes:
        Principal + Interest
        Property tax
        Home insurance

    Does not include PMI, HOA, closing costs,
    or other potential expenses.
    """

    loan_amount = (
        home_price - down_payment
    )

    loan_result = calculate_loan_payment(
        principal=loan_amount,
        annual_rate=annual_rate,
        years=years,
    )

    monthly_property_tax = (
        property_tax / 12
    )

    monthly_insurance = (
        annual_insurance / 12
    )

    estimated_monthly_total = (
        loan_result["monthly_payment"]
        + monthly_property_tax
        + monthly_insurance
    )

    return {
        "loan_amount": loan_amount,
        "principal_interest":
            loan_result["monthly_payment"],
        "property_tax":
            monthly_property_tax,
        "insurance":
            monthly_insurance,
        "estimated_monthly_total":
            estimated_monthly_total,
        "total_interest":
            loan_result["total_interest"],
    }


# =========================================================
# COMPOUND INTEREST
# =========================================================

def calculate_compound_interest(
    principal,
    annual_rate,
    years,
    compounds_per_year=12,
):
    """
    Calculate compound growth.

    Formula:

    A = P(1 + r/n)^(nt)
    """

    rate = annual_rate / 100

    amount = (
        principal
        * (
            1
            + rate / compounds_per_year
        )
        ** (
            compounds_per_year
            * years
        )
    )

    interest_earned = (
        amount - principal
    )

    return {
        "future_value": amount,
        "interest_earned": interest_earned,
        "principal": principal,
    }


# =========================================================
# SIMPLE INTEREST
# =========================================================

def calculate_simple_interest(
    principal,
    annual_rate,
    years,
):
    """
    Calculate simple interest.

    Formula:

    I = PRT
    """

    interest = (
        principal
        * (annual_rate / 100)
        * years
    )

    future_value = (
        principal + interest
    )

    return {
        "interest": interest,
        "future_value": future_value,
        "principal": principal,
    }


# =========================================================
# SAVINGS GOAL
# =========================================================

def calculate_savings_goal(
    target_amount,
    current_savings,
    annual_rate,
    years,
):
    """
    Estimate the monthly contribution needed
    to reach a savings goal.
    """

    remaining_amount = (
        target_amount
        - current_savings
    )

    if remaining_amount <= 0:

        return {
            "monthly_contribution": 0,
            "remaining_amount": 0,
            "message":
                "Your current savings already "
                "meet the target."
        }

    months = years * 12

    monthly_rate = (
        annual_rate / 100 / 12
    )

    if monthly_rate == 0:

        monthly_contribution = (
            remaining_amount / months
        )

    else:

        monthly_contribution = (
            remaining_amount
            * monthly_rate
            /
            (
                (1 + monthly_rate)
                ** months
                - 1
            )
        )

    return {
        "monthly_contribution":
            monthly_contribution,

        "remaining_amount":
            remaining_amount,

        "months":
            months,
    }


# =========================================================
# DEBT PAYOFF
# =========================================================

def calculate_debt_payoff(
    balance,
    annual_rate,
    monthly_payment,
):
    """
    Estimate debt payoff period using a fixed
    monthly payment.
    """

    monthly_rate = (
        annual_rate / 100 / 12
    )

    if monthly_payment <= 0:

        return {
            "months": None,
            "total_paid": None,
            "total_interest": None,
            "message":
                "Monthly payment must be greater than zero."
        }

    if monthly_rate == 0:

        months = math.ceil(
            balance / monthly_payment
        )

        total_paid = (
            months * monthly_payment
        )

        return {
            "months": months,
            "total_paid": total_paid,
            "total_interest": 0,
        }

    minimum_payment = (
        balance * monthly_rate
    )

    if monthly_payment <= minimum_payment:

        return {
            "months": None,
            "total_paid": None,
            "total_interest": None,
            "message":
                "Payment is too low to pay down "
                "the debt at this interest rate."
        }

    months = math.ceil(
        -math.log(
            1
            - (
                balance
                * monthly_rate
                / monthly_payment
            )
        )
        / math.log(
            1 + monthly_rate
        )
    )

    total_paid = (
        months * monthly_payment
    )

    total_interest = (
        total_paid - balance
    )

    return {
        "months": months,
        "total_paid": total_paid,
        "total_interest": total_interest,
    }


# =========================================================
# INVESTMENT RETURN
# =========================================================

def calculate_investment_return(
    initial_investment,
    monthly_contribution,
    annual_rate,
    years,
):
    """
    Estimate future investment value using
    compound growth and regular monthly contributions.

    This is an educational estimate and does not
    account for taxes, fees, volatility, or actual
    investment performance.
    """

    months = years * 12

    monthly_rate = (
        annual_rate / 100 / 12
    )

    if monthly_rate == 0:

        future_value = (
            initial_investment
            + monthly_contribution * months
        )

    else:

        initial_growth = (
            initial_investment
            * (1 + monthly_rate)
            ** months
        )

        contribution_growth = (
            monthly_contribution
            *
            (
                (1 + monthly_rate)
                ** months
                - 1
            )
            / monthly_rate
        )

        future_value = (
            initial_growth
            + contribution_growth
        )

    total_contributed = (
        initial_investment
        + monthly_contribution * months
    )

    estimated_growth = (
        future_value
        - total_contributed
    )

    return {
        "future_value": future_value,
        "total_contributed": total_contributed,
        "estimated_growth": estimated_growth,
    }
