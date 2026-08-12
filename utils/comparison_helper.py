"""
FinGenie Product Comparison Helper
"""

from typing import Dict, List


def get_comparison_data(
    product_1: Dict,
    product_2: Dict,
) -> Dict:
    """
    Prepare two financial products for comparison.
    """

    return {
        "Product 1": product_1,
        "Product 2": product_2,
    }


def compare_product_features(
    product_1: Dict,
    product_2: Dict,
) -> Dict:
    """
    Compare common product attributes.
    """

    comparison = {
        "Features": {
            product_1["name"]: product_1.get("features", []),
            product_2["name"]: product_2.get("features", []),
        },
        "Common Questions": {
            product_1["name"]: product_1.get(
                "common_questions", []
            ),
            product_2["name"]: product_2.get(
                "common_questions", []
            ),
        },
    }

    return comparison


def find_common_features(
    product_1: Dict,
    product_2: Dict,
) -> List[str]:
    """
    Find features shared by both products.
    """

    features_1 = set(
        product_1.get("features", [])
    )

    features_2 = set(
        product_2.get("features", [])
    )

    return sorted(features_1.intersection(features_2))


def find_unique_features(
    product_1: Dict,
    product_2: Dict,
) -> Dict:

    features_1 = set(
        product_1.get("features", [])
    )

    features_2 = set(
        product_2.get("features", [])
    )

    return {
        product_1["name"]: sorted(
            features_1 - features_2
        ),
        product_2["name"]: sorted(
            features_2 - features_1
        ),
    }
