from abc import ABC, abstractmethod
from typing import Dict, List

from .utils import sort_pricier_first

# typing only
from .product import Product


class Discount(ABC):
    @abstractmethod
    def apply(self, products: Dict[Product, int]) -> int: ...


class GetFree(Discount):
    def __init__(self, offer: List[dict]) -> None:
        self.offer = offer

    def apply(self, products: Dict[Product, int]) -> int:
        discount = 0
        product = self.offer['product']
        free_product = self.offer["get_free"]
        if product in products and free_product in products:
            while products[product] >= self.offer["count"] and products[free_product] > 0:
                discount += free_product.price
                if free_product is not product:
                    products[free_product] -= 1
                products[product] -= self.offer["count"]


class MultiPrice(Discount):
    def __init__(self, offer: List[dict]) -> None:
        self.offer = offer
    def apply(self, products: Dict[Product, int]) -> int:
        discount = 0
        for offer in offers:
            product = offer['product']
            if isinstance(product, Product):
                if 'price' in offer and product in basket:
                    while basket[product] >= offer["count"]:
                        discount += product.price * offer["count"] - offer['price']
                        basket[product] -= offer["count"]
        return discount, basket


class GroupPrice(Discount):
    def __init__(self, offer: List[dict]) -> None:
        self.offer = offer

    def apply(self, products: Dict[Product, int]) -> int:
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



