from abc import ABC, abstractmethod
from typing import Dict, List

from .utils import sort_pricier_first

# typing only
from .product import Product


class Discount(ABC):
    @abstractmethod
    def apply(self, products: Dict[Product, int]) -> int: ...


def calculate_getfree_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    discount = 0
    for offer in offers:
        product = offer['product']
        if isinstance(product, Product):
            if 'get_free' in offer and product in basket:
                free_product = offer["get_free"]
                if free_product in basket:
                    while basket[product] >= offer["count"] and basket[free_product] > 0:
                        discount += free_product.price
                        # TODO: This is quite hacky. To be refactored later.
                        if free_product is not product:
                            basket[free_product] -= 1
                        basket[product] -= offer["count"]
    return discount, basket 


def calculate_multiprice_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    discount = 0
    for offer in offers:
        product = offer['product']
        if isinstance(product, Product):
            if 'price' in offer and product in basket:
                while basket[product] >= offer["count"]:
                    discount += product.price * offer["count"] - offer['price']
                    basket[product] -= offer["count"]
    return discount, basket



def calculate_groupbuy_discount(basket: Dict[str, int], offers: List[dict]) -> int: 
    discount = 0
    total = 0
    applied = 0
    for offer in offers:
        product_list = offer['product']
        if isinstance(product_list, list):
            for product in sort_pricier_first(product_list):
                if product in basket:
                    while basket[product] > 0:
                        total += product.price
                        applied += 1
                        basket[product] -= 1
            if applied >= offer['count']:
                discount += total - offer['price'] * applied / offer['count']
    return discount, basket

