"""
FinGenie Budget Planner Helper
"""


def calculate_budget(
    monthly_income,
    housing,
    utilities,
    transportation,
    groceries,
    insurance,
    debt_payments,
    entertainment,
    other_expenses,
):

    expenses = {
        "Housing": housing,
        "Utilities": utilities,
        "Transportation": transportation,
        "Groceries": groceries,
        "Insurance": insurance,
        "Debt Payments": debt_payments,
        "Entertainment": entertainment,
        "Other": other_expenses,
    }

    total_expenses = sum(
        expenses.values()
    )

    remaining = (
        monthly_income - total_expenses
    )

    if monthly_income > 0:

        expense_ratio = (
            total_expenses
            / monthly_income
        ) * 100

        savings_ratio = (
            max(remaining, 0)
            / monthly_income
        ) * 100

    else:

        expense_ratio = 0
        savings_ratio = 0

    return {
        "expenses": expenses,
        "total_expenses": total_expenses,
        "remaining": remaining,
        "expense_ratio": expense_ratio,
        "savings_ratio": savings_ratio,
    }
