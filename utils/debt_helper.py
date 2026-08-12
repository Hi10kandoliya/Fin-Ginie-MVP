"""
FinGenie Debt Payoff Helper
"""


def calculate_debt_payoff(
    balance,
    annual_rate,
    monthly_payment,
):
    """
    Estimate months required to pay off debt.
    """

    if balance <= 0:
        return {
            "months": 0,
            "total_paid": 0,
            "total_interest": 0,
        }

    if monthly_payment <= 0:
        return None

    monthly_rate = (
        annual_rate / 100 / 12
    )

    # If there is no interest
    if monthly_rate == 0:

        months = balance / monthly_payment

        months = int(months) + (
            1 if months % 1 else 0
        )

        return {
            "months": months,
            "total_paid": balance,
            "total_interest": 0,
        }

    # Payment must be greater than
    # the first month's interest
    first_month_interest = (
        balance * monthly_rate
    )

    if monthly_payment <= first_month_interest:

        return {
            "impossible": True,
            "reason": (
                "Monthly payment is not enough "
                "to cover the interest."
            ),
        }

    remaining_balance = balance
    total_interest = 0
    months = 0

    while (
        remaining_balance > 0
        and months < 1200
    ):

        interest = (
            remaining_balance
            * monthly_rate
        )

        principal_payment = (
            monthly_payment - interest
        )

        if principal_payment <= 0:

            return {
                "impossible": True,
                "reason": (
                    "Payment does not reduce "
                    "the principal."
                ),
            }

        total_interest += interest

        remaining_balance -= (
            principal_payment
        )

        months += 1

    total_paid = (
        balance + total_interest
    )

    return {
        "months": months,
        "total_paid": total_paid,
        "total_interest": total_interest,
    }


def calculate_extra_payment_impact(
    balance,
    annual_rate,
    current_payment,
    extra_payment,
):
    """
    Compare current payment vs increased payment.
    """

    current = calculate_debt_payoff(
        balance,
        annual_rate,
        current_payment,
    )

    accelerated = calculate_debt_payoff(
        balance,
        annual_rate,
        current_payment
        + extra_payment,
    )

    if (
        current is None
        or accelerated is None
        or current.get("impossible")
        or accelerated.get("impossible")
    ):
        return None

    return {
        "current": current,
        "accelerated": accelerated,
        "months_saved": (
            current["months"]
            - accelerated["months"]
        ),
        "interest_saved": (
            current["total_interest"]
            - accelerated["total_interest"]
        ),
    }
