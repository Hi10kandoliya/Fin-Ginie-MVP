
import streamlit as st

from utils.financial_data import products
from utils.comparison_helper import (
    find_common_features,
    find_unique_features,
)


st.set_page_config(
    page_title="Product Comparison",
    page_icon="⚖️",
    layout="wide",
)


st.title("⚖️ Financial Product Comparison")

st.markdown(
    """
    Compare two financial products side-by-side
    to understand their features and differences.
    """
)


product_names = list(products.keys())


col1, col2 = st.columns(2)


with col1:

    product_1_name = st.selectbox(
        "Select Product 1",
        product_names,
        index=0,
    )


with col2:

    product_2_options = [
        name
        for name in product_names
        if name != product_1_name
    ]

    product_2_name = st.selectbox(
        "Select Product 2",
        product_2_options,
        index=0,
    )


if st.button(
    "⚖️ Compare Products",
    type="primary",
):

    product_1 = products[product_1_name]
    product_2 = products[product_2_name]

    st.markdown("---")

    st.subheader(
        f"{product_1_name} vs {product_2_name}"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"### 💰 {product_1_name}"
        )

        st.write("**Features**")

        for feature in product_1.get(
            "features", []
        ):
            st.write(f"• {feature}")

    with col2:

        st.markdown(
            f"### 💰 {product_2_name}"
        )

        st.write("**Features**")

        for feature in product_2.get(
            "features", []
        ):
            st.write(f"• {feature}")


    st.markdown("---")

    common_features = find_common_features(
        {
            **product_1,
            "name": product_1_name,
        },
        {
            **product_2,
            "name": product_2_name,
        },
    )

    unique_features = find_unique_features(
        {
            **product_1,
            "name": product_1_name,
        },
        {
            **product_2,
            "name": product_2_name,
        },
    )


    st.subheader("🔍 Comparison Summary")


    if common_features:

        st.write("### Features shared by both")

        for feature in common_features:
            st.write(f"• {feature}")

    else:

        st.info(
            "No identical features were found."
        )


    st.write(
        f"### {product_1_name} — Unique Features"
    )

    if unique_features[product_1_name]:

        for feature in unique_features[
            product_1_name
        ]:
            st.write(f"• {feature}")

    else:

        st.write(
            "No unique features identified."
        )


    st.write(
        f"### {product_2_name} — Unique Features"
    )

    if unique_features[product_2_name]:

        for feature in unique_features[
            product_2_name
        ]:
            st.write(f"• {feature}")

    else:

        st.write(
            "No unique features identified."
        )


st.markdown("---")

st.caption(
    "FinGenie provides educational information only "
    "and does not provide personalized financial advice."
)
