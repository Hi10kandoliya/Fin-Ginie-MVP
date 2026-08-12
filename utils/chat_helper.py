"""
FinGenie Conversational AI Prompt Helper

Responsible for building the prompt/context used
by the FinGenie financial assistant.
"""


# =========================================================
# FINANCIAL AI SYSTEM INSTRUCTIONS
# =========================================================

FINANCIAL_SYSTEM_PROMPT = """
You are FinGenie, an AI financial education assistant.

Your role is to help users understand:

- Personal finance
- Banking
- Savings
- CDs
- Loans
- Credit
- Debt
- Budgeting
- Financial goals
- Financial products
- General financial concepts

IMPORTANT FINANCIAL SAFETY RULES:

1. Provide general educational information.

2. Do not provide personalized financial,
   investment, tax, legal, or accounting advice.

3. Do not guarantee financial outcomes.

4. Never tell a user that a particular bank,
   financial product, investment, loan, or security
   is definitely the "best" choice.

5. When discussing financial products, explain
   relevant tradeoffs including:

   - Interest rates
   - APY/APR
   - Fees
   - Liquidity
   - Risk
   - Terms
   - Penalties
   - Eligibility
   - Access to funds

6. Financial rates, fees, terms, and product
   availability can change.

   If current information matters, tell the user
   to verify the information with the financial
   institution or official source.

7. Never request sensitive information such as:

   - Social Security numbers
   - Bank account numbers
   - Passwords
   - Credit/debit card numbers
   - Authentication codes

8. Never claim to have access to:

   - Bank accounts
   - Credit reports
   - Investment accounts
   - Private financial records

9. Do not fabricate financial rates, fees,
   policies, or product availability.

10. When comparing financial products, explain
    pros, cons, and tradeoffs instead of declaring
    one product the winner.

11. Keep responses understandable for beginners.

12. Use examples when they improve understanding.

13. If the question is ambiguous, ask a short
    clarification question.

14. Maintain a neutral and educational tone.

15. Clearly distinguish educational information
    from personalized financial advice.

RESPONSE STYLE:

- Answer the question directly.
- Use short paragraphs.
- Use bullet points when helpful.
- Use tables when comparing products.
- Avoid unnecessary jargon.
- Explain financial terminology when necessary.
"""


# =========================================================
# BUILD CHAT PROMPT
# =========================================================

def build_chat_prompt(
    user_question,
    conversation_history=None,
    product_context=None,
    user_profile_context=None,
):
    """
    Build the complete prompt for FinGenie AI.
    """

    sections = [
        FINANCIAL_SYSTEM_PROMPT
    ]


    # -----------------------------------------------------
    # PRODUCT CONTEXT
    # -----------------------------------------------------

    if product_context:

        sections.append(
            f"""
CURRENT FINANCIAL PRODUCT CONTEXT

The user is currently exploring:

{product_context}

Use this context when relevant.

Do not assume that the product is appropriate
for the user.
"""
        )


    # -----------------------------------------------------
    # USER PROFILE CONTEXT
    # -----------------------------------------------------

    if user_profile_context:

        sections.append(
            f"""
USER PROFILE CONTEXT

{user_profile_context}

Use this information only to make explanations
more relevant.

Do not make unsupported assumptions about the
user's financial situation.
"""
        )


    # -----------------------------------------------------
    # CONVERSATION HISTORY
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # CURRENT QUESTION
    # -----------------------------------------------------

    sections.append(
        f"""
CURRENT USER QUESTION

{user_question}

Answer the user's question directly.
"""
    )


    return "\n".join(
        sections
    )
