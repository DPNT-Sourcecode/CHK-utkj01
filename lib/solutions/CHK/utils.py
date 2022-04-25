from typing import List

# typing only
from .product import Product


def sort_pricier_first(products: List[Product]) -> List[Product]:
    return sorted(products, key=lambda product: product.price, reverse=True)
