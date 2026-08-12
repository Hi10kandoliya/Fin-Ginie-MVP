"""
FinGenie Bank and Financial Product Data

MVP curated data.
Rates, fees, eligibility, and availability should be
verified with the financial institution before applying.
"""


banks = {

    "Chase": {
        "description": (
            "A large U.S. financial institution offering "
            "checking, savings, credit cards, mortgages, "
            "and other financial products."
        ),

        "website": "https://www.chase.com",

        "products": {

            "Checking Account": {
                "name": "Chase Checking Account",
                "category": "Checking",
                "type": "Deposit Account",

                "features": [
                    "Everyday banking",
                    "Debit card access",
                    "Online and mobile banking",
                    "ATM access",
                ],

                "considerations": [
                    "Monthly service fees may apply",
                    "Fee waivers may depend on account/activity",
                    "Verify current terms before opening",
                ],

                "best_for": [
                    "Everyday banking",
                    "Customers wanting branch access",
                    "Customers who want mobile banking",
                ],

                "official_url": "https://www.chase.com/personal/checking",
            },

            "Savings Account": {
                "name": "Chase Savings",
                "category": "Savings",
                "type": "Deposit Account",

                "features": [
                    "Savings account",
                    "Online and mobile banking",
                    "ATM access",
                    "Automatic savings options",
                ],

                "considerations": [
                    "Monthly service fees may apply",
                    "Interest rate can change",
                    "Verify current APY and fees",
                ],

                "best_for": [
                    "General savings",
                    "Emergency fund",
                    "Customers who want banking services in one place",
                ],

                "official_url": "https://www.chase.com/personal/savings",
            },

            "Mortgage": {
                "name": "Chase Home Lending",
                "category": "Mortgage",
                "type": "Home Loan",

                "features": [
                    "Home purchase financing",
                    "Refinancing options",
                    "Multiple mortgage options",
                    "Online application resources",
                ],

                "considerations": [
                    "Rates depend on borrower and market conditions",
                    "Credit and income requirements apply",
                    "Closing costs may apply",
                ],

                "best_for": [
                    "Home buyers",
                    "Homeowners considering refinancing",
                ],

                "official_url": "https://www.chase.com/personal/mortgage",
            },
        },
    },


    "Bank of America": {
        "description": (
            "A major U.S. financial institution offering "
            "banking, credit, lending, investment, and "
            "other financial services."
        ),

        "website": "https://www.bankofamerica.com",

        "products": {

            "Checking Account": {
                "name": "Bank of America Advantage Banking",
                "category": "Checking",
                "type": "Deposit Account",

                "features": [
                    "Everyday checking",
                    "Online and mobile banking",
                    "Debit card",
                    "ATM access",
                ],

                "considerations": [
                    "Monthly service fees may apply",
                    "Fee waivers may be available depending on circumstances",
                    "Verify current account terms",
                ],

                "best_for": [
                    "Everyday banking",
                    "Customers wanting a large banking network",
                ],

                "official_url": "https://www.bankofamerica.com/deposits/checking/",
            },

            "Savings Account": {
                "name": "Bank of America Advantage Savings",
                "category": "Savings",
                "type": "Deposit Account",

                "features": [
                    "Savings account",
                    "Online and mobile banking",
                    "Automatic savings tools",
                    "ATM access",
                ],

                "considerations": [
                    "Monthly service fees may apply",
                    "Interest rate can change",
                    "Verify current APY",
                ],

                "best_for": [
                    "General savings",
                    "Emergency savings",
                ],

                "official_url": "https://www.bankofamerica.com/deposits/savings/",
            },

            "Mortgage": {
                "name": "Bank of America Home Loans",
                "category": "Mortgage",
                "type": "Home Loan",

                "features": [
                    "Home purchase loans",
                    "Refinancing",
                    "Mortgage resources",
                    "Online application resources",
                ],

                "considerations": [
                    "Rates depend on market and borrower profile",
                    "Credit and income requirements apply",
                    "Closing costs may apply",
                ],

                "best_for": [
                    "Home buyers",
                    "Homeowners exploring refinancing",
                ],

                "official_url": "https://www.bankofamerica.com/mortgage/",
            },
        },
    },


    "Wells Fargo": {
        "description": (
            "A major U.S. financial institution offering "
            "deposit accounts, credit cards, loans, "
            "mortgages, and other financial services."
        ),

        "website": "https://www.wellsfargo.com",

        "products": {

            "Checking Account": {
                "name": "Wells Fargo Everyday Checking",
                "category": "Checking",
                "type": "Deposit Account",

                "features": [
                    "Everyday checking",
                    "Debit card",
                    "Online and mobile banking",
                    "ATM access",
                ],

                "considerations": [
                    "Monthly service fees may apply",
                    "Fee waiver requirements may apply",
                    "Verify current terms",
                ],

                "best_for": [
                    "Everyday banking",
                    "Customers wanting branch access",
                ],

                "official_url": "https://www.wellsfargo.com/checking/",
            },

            "Savings Account": {
                "name": "Wells Fargo Way2Save Savings",
                "category": "Savings",
                "type": "Deposit Account",

                "features": [
                    "Savings account",
                    "Automatic savings features",
                    "Online and mobile banking",
                    "ATM access",
                ],

                "considerations": [
                    "Monthly service fees may apply",
                    "Interest rate can change",
                    "Verify current APY",
                ],

                "best_for": [
                    "Beginning savers",
                    "Emergency savings",
                ],

                "official_url": "https://www.wellsfargo.com/savings-cds/",
            },
        },
    },


    "Capital One": {
        "description": (
            "A U.S. financial institution known for "
            "banking, credit cards, savings, and lending products."
        ),

        "website": "https://www.capitalone.com",

        "products": {

            "Checking Account": {
                "name": "Capital One 360 Checking",
                "category": "Checking",
                "type": "Deposit Account",

                "features": [
                    "Online checking",
                    "No monthly service fee",
                    "Mobile banking",
                    "ATM access",
                ],

                "considerations": [
                    "Verify current account terms",
                    "Branch availability varies by location",
                ],

                "best_for": [
                    "Online banking",
                    "Customers seeking low-fee checking",
                ],

                "official_url": "https://www.capitalone.com/bank/checking-accounts/",
            },

            "Savings Account": {
                "name": "Capital One 360 Performance Savings",
                "category": "Savings",
                "type": "Deposit Account",

                "features": [
                    "Online savings",
                    "No monthly service fee",
                    "Mobile banking",
                    "Automatic savings tools",
                ],

                "considerations": [
                    "APY can change",
                    "Verify current APY and terms",
                ],

                "best_for": [
                    "Online savings",
                    "Emergency funds",
                    "Customers focused on low fees",
                ],

                "official_url": "https://www.capitalone.com/bank/savings-accounts/",
            },
        },
    },


    "Discover": {
        "description": (
            "A U.S. financial services company offering "
            "banking, credit cards, and other financial products."
        ),

        "website": "https://www.discover.com",

        "products": {

            "Savings Account": {
                "name": "Discover Online Savings",
                "category": "Savings",
                "type": "Deposit Account",

                "features": [
                    "Online savings",
                    "No monthly maintenance fee",
                    "Online and mobile banking",
                    "Competitive savings features",
                ],

                "considerations": [
                    "APY can change",
                    "Primarily digital banking experience",
                    "Verify current terms",
                ],

                "best_for": [
                    "Online savings",
                    "Customers comfortable with digital banking",
                ],

                "official_url": "https://www.discover.com/online-banking/savings-account/",
            },
        },
    },
}


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_bank_names():

    return list(banks.keys())


def get_bank(bank_name):

    return banks.get(bank_name)


def get_bank_products(bank_name):

    bank = banks.get(bank_name)

    if not bank:
        return {}

    return bank.get("products", {})


def get_product_categories(bank_name):

    products = get_bank_products(bank_name)

    return sorted(
        set(
            product.get("category", "Other")
            for product in products.values()
        )
    )


def get_products_by_category(
    bank_name,
    category
):

    products = get_bank_products(bank_name)

    return {
        name: data
        for name, data in products.items()
        if data.get("category") == category
    }
