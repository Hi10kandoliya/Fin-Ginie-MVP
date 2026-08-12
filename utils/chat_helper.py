"""
FinGenie Conversational AI Prompt Helper

Builds the context used by the FinGenie AI assistant.
"""

from typing import List, Dict, Optional


FINANCIAL_SYSTEM_PROMPT = """
You are FinGenie, an AI financial education assistant.

Your purpose is to help users understand:

- Personal finance
- Saving
- Banking products
- Loans
- Credit
- Debt
- Budgeting
- Financial goals
- General financial concepts

IMPORTANT FINANCIAL SAFETY RULES:

1. Provide educational information only.

2. Do not provide personalized financial, investment,
   tax, legal, or accounting advice.

3. Do not guarantee financial outcomes.

4. Do not tell a user that a particular bank,
   financial product, investment, loan, or security
   is definitely the best choice for them.

5. When discussing financial products, explain relevant
   tradeoffs such as:

   - Interest rates
   - APY/APR
   - Fees
   - Liquidity
   - Risk
   - Term
   - Penalties
   - Eligibility
   - Access to funds

6. If information may change over time, such as:

   - Interest rates
   - APYs
   - Fees
   - Bank policies
   - Loan rates
   - Regulations

   tell the user that they should verify the current
   information with the financial institution or official
   source.

7. Never request or encourage users to provide:

   - Social Security numbers
   - Passwords
   - Bank account numbers
   - Credit/debit card numbers
   - Authentication codes
   - Other sensitive credentials

8. Never claim that you can access:

   - Bank accounts
   - Credit reports
   - Investment accounts
   - Financial records
   - Private customer information

9. Keep responses clear and understandable.

10. Use examples when they help explain a concept.

11. If the question is ambiguous, ask a short
    clarification question.

12. Remain neutral and educational.

13. When comparing products, present pros, cons,
    tradeoffs, and considerations rather than
    declaring a winner.

14. Do not fabricate current financial rates,
    fees, bank policies, or product availability.

RESPONSE STYLE:

- Start with a direct answer.
- Use short paragraphs.
- Use bullet points where appropriate.
- Use tables for useful comparisons.
- Avoid unnecessary jargon.
- Explain financial terminology when needed.
"""


def build_chat_prompt(
    user_question: str,
    conversation_history: Optional[List[Dict]] = None,
    product_context: Optional[str] = None,
    user_profile_context: Optional[str] = None,
) -> str:
    """
    Build the complete FinGenie prompt.
    """

    sections = [
        FINANCIAL_SYSTEM_PROMPT
    ]

    if product_context:

        sections.append(
            f"""
CURRENT PRODUCT CONTEXT

The user is currently exploring:

{product_context}

Use this information when relevant to the question.
Do not assume that this product is appropriate for the user.
"""
        )

    if user_profile_context:

        sections.append(
            f"""
USER PROFILE CONTEXT

{user_profile_context}

Use this information only to make the explanation
more relevant.

Do not make unsupported assumptions about the user's
financial situation.
"""
        )

    if conversation_history:

        history_text = ""

        for message in conversation_history:

            role = message.get(
                "role",
                "user"
            )

            content = message.get(
                "content",
                ""
            )

            history_text += (
                f"\n{role.upper()}: {content}\n"
            )

        sections.append(
            f"""
RECENT CONVERSATION

{history_text}
"""
        )

    sections.append(
        f"""
CURRENT USER QUESTION

{user_question}

Answer the user's question directly.
"""
    )

    return "\n".join(sections)
