import streamlit as st
from openai import OpenAI

from utils.chat_helper import build_chat_prompt


# =========================================================
# CONFIGURATION
# =========================================================

MODEL_NAME = "gpt-5-mini"


# =========================================================
# OPENAI CLIENT
# =========================================================

def get_openai_client():
    """
    Create and return an OpenAI client using Streamlit secrets.
    """

    return OpenAI(
        api_key=st.secrets["Fin-Genie-Key"]
    )


# =========================================================
# REAL AI FINANCIAL CHAT
# =========================================================

def generate_chat_response(
    user_question,
    conversation_history=None,
    product_context=None,
    user_profile_context=None,
):
    """
    Generate a conversational financial AI response.

    Parameters:
        user_question:
            Current question from the user.

        conversation_history:
            Previous messages in the conversation.

        product_context:
            Information about the selected financial product.

        user_profile_context:
            Optional user profile information.

    Returns:
        AI-generated response as a string.
    """

    try:

        client = get_openai_client()

        prompt = build_chat_prompt(
            user_question=user_question,
            conversation_history=conversation_history,
            product_context=product_context,
            user_profile_context=user_profile_context,
        )

        response = client.responses.create(
            model=MODEL_NAME,
            input=prompt,
        )

        return response.output_text

    except Exception as e:

        # Log the actual error for development/debugging.
        print(f"OpenAI Chat Error: {e}")

        return (
            "I'm sorry, I couldn't process your question "
            "right now. Please try again."
        )

#=========================================
# Product Chat Details
#========================================
def generate_financial_chat_response(
    product_name,
    bank_name,
    user_question,
    chat_history=None,
):
    """
    Generate a conversational financial response using OpenAI.

    The AI receives:
    - Bank context
    - Product context
    - User question
    - Previous conversation history
    """

    if chat_history is None:
        chat_history = []


    system_prompt = f"""
You are FinGenie, an AI financial education assistant.

The user is asking about:

Bank:
{bank_name}

Financial Product:
{product_name}

Your responsibilities:

1. Explain financial concepts clearly.
2. Use simple language suitable for beginners.
3. Keep the bank and product context in mind.
4. Do not invent current rates, fees, eligibility requirements,
   promotions, or product terms.
5. If current product information is required, tell the user
   to verify the information on the bank's official website.
6. Do not claim to be a human financial advisor.
7. Do not provide guaranteed financial outcomes.
8. Explain risks and important considerations when relevant.
9. Encourage users to compare products before making decisions.

IMPORTANT FINANCIAL DISCLAIMER:

Your response is for educational purposes only and is not
financial, investment, tax, or legal advice.

Keep responses concise and easy to understand.
"""


    messages = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]


    # -----------------------------------------------------
    # ADD PREVIOUS CONVERSATION
    # -----------------------------------------------------

    for message in chat_history[-10:]:

        role = message.get("role")

        content = message.get("content")

        if role in ["user", "assistant"] and content:

            messages.append(
                {
                    "role": role,
                    "content": content,
                }
            )


    # -----------------------------------------------------
    # ADD CURRENT QUESTION
    # -----------------------------------------------------

    messages.append(
        {
            "role": "user",
            "content": user_question,
        }
    )


    try:

        client = get_openai_client()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=500,
        )

        return response.choices[0].message.content


    except Exception as e:

        return (
            "I’m unable to connect to the AI service right now. "
            "Please try again later."
        )


# =========================================================
# FAQ GENERATION
# =========================================================

def generate_faq(
    product_name,
    user_profile="general"
):
    """
    Generate personalized FAQ based on product
    and user profile.
    """

    profile_context = {

        "student":
            "You are a college student looking for "
            "low-cost options.",

        "professional":
            "You are a working professional seeking "
            "premium benefits.",

        "retiree":
            "You are a retiree focused on safety "
            "and fixed returns.",

        "general":
            "You are a general customer."
    }

    prompt = f"""
You are FinGenie, an AI financial education assistant.

A {profile_context.get(
    user_profile,
    profile_context["general"]
)} is interested in {product_name}.

Generate 3 frequently asked questions and answers
about {product_name} that are:

- Easy to understand for a beginner
- Tailored to the user's profile
- Include one practical example
- Educational rather than personalized financial advice

Do not claim that this product is the best option
for the user.

Format your response as:

Q1: [Question]
A1: [Answer]

Q2: [Question]
A2: [Answer]

Q3: [Question]
A3: [Answer]
"""

    try:

        client = get_openai_client()

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_tokens=500,

            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:

        print(
            f"OpenAI FAQ Error: {e}"
        )

        return (
            f"Unable to generate FAQ: {str(e)}"
        )


# =========================================================
# PERSONALIZED PRODUCT CONTENT
# =========================================================

def personalize_content(
    product_name,
    user_info
):
    """
    Generate personalized product explanation
    based on user details.
    """

    prompt = f"""
You are FinGenie, an AI financial education assistant.

User details:

- Age: {user_info.get('age', 'Not provided')}
- Income: {user_info.get('income', 'Not provided')}
- Goal: {user_info.get('goal', 'saving for future')}

Explain the {product_name} in simple terms.

Highlight:

1. Important characteristics of the product
2. One key benefit the user may want to consider
3. One important risk, limitation, or tradeoff

Keep it under 150 words.

Use friendly, non-technical language.

Do not state that this product is definitely
appropriate for the user.

This is educational information, not personalized
financial advice.
"""

    try:

        client = get_openai_client()

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_tokens=300,

            temperature=0.8
        )

        return response.choices[0].message.content

    except Exception as e:

        print(
            f"OpenAI Personalization Error: {e}"
        )

        return (
            f"Unable to personalize content: {str(e)}"
        )


# =========================================================
# OFFLINE FAQ FALLBACK
# =========================================================

def fallback_faq(
    product_name,
    user_profile="general"
):
    """
    Generate an offline FAQ without using
    the OpenAI API.
    """

    # Import here to preserve your existing
    # project structure and avoid unnecessary
    # circular imports.
    from utils.financial_data import products

    data = products.get(
        product_name,
        {}
    )

    questions = data.get(
        "common_questions",
        [
            "What is this product?"
        ]
    )

    answers = [

        (
            f"This product offers "
            f"{', '.join(
                data.get(
                    "features",
                    ["various benefits"]
                )
            )}."
        ),

        (
            f"Check with your financial institution "
            f"for {user_profile}-specific options."
        ),

        (
            "Contact the financial institution's "
            "customer support for detailed information."
        )
    ]

    return "\n\n".join(

        [
            f"Q{i + 1}: {q}\nA: {a}"
            for i, (q, a) in enumerate(
                zip(
                    questions[:3],
                    answers
                )
            )
        ]
    )
