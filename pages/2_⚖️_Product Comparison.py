import streamlit as st

from utils.bank_data import (
    banks,
    get_bank_products,
)

from utils.comparison_helper import (
    find_common_features,
    find_unique_features,
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Compare Financial Products",
    page_icon="⚖️",
    layout="wide",
)


# =========================================================
# HEADER
# =========================================================

st.title(
    "⚖️ Compare Financial Products"
)

st.markdown(
    """
    Select two financial products side by side to compare
    features, considerations, and common use cases before
    deciding which one may fit your needs.
    """
)


# =========================================================
# DISCLAIMER
# =========================================================

st.warning(
    """
    **Important:** FinGenie provides general educational
    information. Product availability, interest rates,
    APYs, fees, eligibility requirements, and terms can
    change. Always verify current information directly
    with the financial institution before applying.
    """
)


# =========================================================
# PRODUCT SELECTION
# =========================================================

st.subheader(
    "🔎 Choose Two Products to Compare"
)

bank_names = list(banks.keys())

select_col1, select_col2 = st.columns(2)


with select_col1:

    st.markdown("#### Product 1")

    bank_1_name = st.selectbox(
        "Select a Bank",
        bank_names,
        key="bank_1",
    )

    products_1 = get_bank_products(
        bank_1_name
    )

    product_1_key = st.selectbox(
        "Select a Product",
        list(products_1.keys()),
        key="product_1",
    )

    product_1 = products_1[product_1_key]


with select_col2:

    st.markdown("#### Product 2")

    bank_2_name = st.selectbox(
        "Select a Bank",
        bank_names,
        index=min(1, len(bank_names) - 1),
        key="bank_2",
    )

    products_2 = get_bank_products(
        bank_2_name
    )

    product_2_key = st.selectbox(
        "Select a Product",
        list(products_2.keys()),
        key="product_2",
    )

    product_2 = products_2[product_2_key]


same_product = (
    bank_1_name == bank_2_name
    and product_1_key == product_2_key
)

if same_product:

    st.info(
        "You've selected the same product twice. "
        "Choose a different bank or product to see a "
        "meaningful comparison."
    )


# =========================================================
# COMPARISON
# =========================================================

st.markdown("---")

st.subheader(
    "📋 Side-by-Side Comparison"
)


header_col1, header_col2 = st.columns(2)

with header_col1:

    st.markdown(
        f"### 🏦 {bank_1_name}"
    )

    st.markdown(
        f"**{product_1['name']}**"
    )

    st.caption(
        f'{product_1["category"]} • '
        f'{product_1["type"]}'
    )

with header_col2:

    st.markdown(
        f"### 🏦 {bank_2_name}"
    )

    st.markdown(
        f"**{product_2['name']}**"
    )

    st.caption(
        f'{product_2["category"]} • '
        f'{product_2["type"]}'
    )


# -------------------------------------------------
# FEATURES
# -------------------------------------------------

st.markdown("#### ⭐ Key Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    for feature in product_1.get("features", []):

        st.markdown(f"• {feature}")

with feature_col2:

    for feature in product_2.get("features", []):

        st.markdown(f"• {feature}")


# -------------------------------------------------
# CONSIDERATIONS
# -------------------------------------------------

st.markdown("#### ⚠️ Things to Consider")

consideration_col1, consideration_col2 = st.columns(2)

with consideration_col1:

    for item in product_1.get("considerations", []):

        st.markdown(f"• {item}")

with consideration_col2:

    for item in product_2.get("considerations", []):

        st.markdown(f"• {item}")


# -------------------------------------------------
# BEST FOR
# -------------------------------------------------

st.markdown("#### 👤 Common Use Cases")

best_for_col1, best_for_col2 = st.columns(2)

with best_for_col1:

    st.write(
        " • ".join(
            product_1.get("best_for", [])
        )
    )

with best_for_col2:

    st.write(
        " • ".join(
            product_2.get("best_for", [])
        )
    )


# =========================================================
# FEATURE OVERLAP
# =========================================================

st.markdown("---")

st.subheader(
    "🧩 Feature Overlap"
)

common_features = find_common_features(
    product_1,
    product_2,
)

unique_features = find_unique_features(
    product_1,
    product_2,
)


if common_features:

    st.markdown("#### 🤝 Shared Features")

    for feature in common_features:

        st.markdown(f"• {feature}")

else:

    st.write(
        "These products don't share any listed features "
        "in common."
    )


unique_col1, unique_col2 = st.columns(2)

with unique_col1:

    st.markdown(
        f"#### 🔹 Only in {product_1['name']}"
    )

    unique_1 = unique_features.get(
        product_1["name"],
        [],
    )

    if unique_1:

        for feature in unique_1:

            st.markdown(f"• {feature}")

    else:

        st.write("No unique features listed.")

with unique_col2:

    st.markdown(
        f"#### 🔹 Only in {product_2['name']}"
    )

    unique_2 = unique_features.get(
        product_2["name"],
        [],
    )

    if unique_2:

        for feature in unique_2:

            st.markdown(f"• {feature}")

    else:

        st.write("No unique features listed.")


# =========================================================
# ACTIONS
# =========================================================

st.markdown("---")

action_col1, action_col2 = st.columns(2)

with action_col1:

    st.link_button(
        f"🌐 Visit {bank_1_name}",
        product_1["official_url"],
        use_container_width=True,
    )

with action_col2:

    st.link_button(
        f"🌐 Visit {bank_2_name}",
        product_2["official_url"],
        use_container_width=True,
    )


st.markdown("---")

st.caption(
    "Comparisons are based on the FinGenie MVP catalog "
    "and are for general educational purposes only. "
    "Always verify current rates, fees, and terms "
    "directly with each financial institution."
)
