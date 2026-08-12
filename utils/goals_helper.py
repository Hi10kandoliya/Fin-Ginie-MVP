"""
FinGenie Financial Goals Helper
"""


def calculate_goal_progress(
    target_amount,
    current_savings,
):
    """
    Calculate current progress toward a savings goal.
    """

    if target_amount <= 0:
        return {
            "progress": 0,
            "remaining": 0,
        }

    progress = (
        current_savings / target_amount
    ) * 100

    progress = min(progress, 100)

    remaining = max(
        target_amount - current_savings,
        0,
    )

    return {
        "progress": progress,
        "remaining": remaining,
    }


def calculate_months_to_goal(
    target_amount,
    current_savings,
    monthly_contribution,
):
    """
    Estimate months required to reach a goal
    without considering investment returns.
    """

    remaining = max(
        target_amount - current_savings,
        0,
    )

    if remaining == 0:
        return 0

    if monthly_contribution <= 0:
        return None

    months = (
        remaining / monthly_contribution
    )

    return int(months) + (
        1 if months % 1 else 0
    )


def calculate_required_monthly_savings(
    target_amount,
    current_savings,
    months,
):
    """
    Calculate required monthly savings
    to reach a target.
    """

    if months <= 0:
        return 0

    remaining = max(
        target_amount - current_savings,
        0,
    )

    return remaining / months
