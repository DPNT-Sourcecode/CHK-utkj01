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
        return discount


class MultiPrice(Discount):
    def __init__(self, offer: List[dict]) -> None:
        self.offer = offer

    def apply(self, products: Dict[Product, int]) -> int:
        discount = 0
        product = self.offer['product']
        if isinstance(product, Product):
            if 'price' in self.offer and product in products:
                while products[product] >= self.offer["count"]:
                    discount += product.price * self.offer["count"] - self.offer['price']
                    products[product] -= self.offer["count"]
        return discount


class GroupPrice(Discount):
    def __init__(self, offer: List[dict]) -> None:
        self.offer = offer

    def apply(self, products: Dict[Product, int]) -> int:
        discount = 0
        product = self.offer['product']
        total = 0
        applied = 0
        for product in sort_pricier_first(product):
            if product in products:
                while products[product] > 0:
                    total += product.price
                    applied += 1
                    products[product] -= 1
        if applied >= self.offer['count']:
            print(applied, self.offer['count'], applied // self.offer['count'])
            discount += total - self.offer['price'] * applied // self.offer['count']
        return discount 

