"""
FinGenie AI Financial Chat Helper

Provides conversational AI responses with:
- Conversation history
- Product context
- User profile context
- Financial safety instructions
"""

from typing import List, Dict, Optional


FINANCIAL_SYSTEM_PROMPT = """
You are FinGenie, an AI financial education assistant.

Your role is to help users understand financial concepts,
financial products, budgeting, saving, borrowing, and
general personal finance.

IMPORTANT SAFETY RULES:

1. Provide educational information, not personalized
   financial, investment, tax, legal, or accounting advice.

2. Do not guarantee financial outcomes.

3. Do not tell users that a specific financial product,
   bank, investment, loan, or security is definitely the
   "best" choice for them.

4. When discussing financial products, explain important
   tradeoffs such as:
   - fees
   - interest rates
   - liquidity
   - risk
   - term
   - penalties
   - eligibility

5. If the answer depends on current rates, fees, regulations,
   bank policies, or market conditions, explicitly say that
   the information should be verified with the relevant
   financial institution or official source.

6. Never request highly sensitive information such as:
   - Social Security numbers
   - passwords
   - bank account numbers
   - credit/debit card numbers
   - authentication codes

7. Keep explanations clear and understandable.

8. When appropriate, provide examples.

9. If the user's question is ambiguous, ask a short
   clarification question.

10. Do not pretend to have access to the user's bank account,
    credit report, financial records, or other private data.

Always maintain a neutral, educational tone.
"""


def build_chat_prompt(
    user_question: str,
    conversation_history: Optional[List[Dict]] = None,
    product_context: Optional[str] = None,
    user_profile_context: Optional[str] = None,
) -> str:
    """
    Build the prompt sent to the AI model.
    """

    prompt_parts = [
        FINANCIAL_SYSTEM_PROMPT
    ]

    if product_context:

        prompt_parts.append(
            f"""
CURRENT FINANCIAL PRODUCT CONTEXT:

{product_context}

Use this context when it is relevant to the user's question.
Do not assume that this product is appropriate for the user.
"""
        )

    if user_profile_context:

        prompt_parts.append(
            f"""
USER PROFILE CONTEXT:

{user_profile_context}

Use this information only to make explanations more relevant.
Do not make unsupported assumptions about the user's finances.
"""
        )

    if conversation_history:

        history_text = ""

        for message in conversation_history:

            role = message.get("role", "user")
            content = message.get("content", "")

            history_text += (
                f"\n{role.upper()}: {content}\n"
            )

        prompt_parts.append(
            f"""
CONVERSATION HISTORY:

{history_text}
"""
        )

    prompt_parts.append(
        f"""
CURRENT USER QUESTION:

{user_question}

Respond directly to the user's question.
"""
    )

    return "\n".join(prompt_parts)
