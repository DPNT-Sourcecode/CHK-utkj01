from enum import Enum, auto
from typing import Dict, List


class Product(Enum):
    A = 50
    B = 30
    C = 20
    D = 15
    E = 40

    def __init__(self, price: int) -> None:
        self._value_ = auto()
        self.price = price


def calculate_getfree_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    discount = 0
    for offer in offers:
        product = offer['product']
        if 'get_free' in offer and product in basket:
            free_product = offer["get_free"]
            if free_product in basket:
                while basket[product] >= offer["count"] and basket[free_product] > 0:
                    discount += free_product.price
                    basket[free_product] -= 1
                    basket[product] -= offer["count"]
    return discount, basket 


def calculate_multiprice_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    discount = 0
    for offer in offers:
        product = offer['product']
        if 'price' in offer and product in basket:
            while basket[product] >= offer["count"]:
                discount += product.price * offer["count"] - offer['price']
                basket[product] -= offer["count"]
    return discount, basket


def calculate_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    getfree_discount, basket = calculate_getfree_discount(basket, offers) 
    multiprice_discount, basket = calculate_multiprice_discount(basket, offers) 
    return getfree_discount + multiprice_discount 


def get_offers() -> list:
    offers = [
        {"product": Product.A, "count": 3, "price": 130},
        {"product": Product.A, "count": 5, "price": 200},
        {"product": Product.B, "count": 2, "price": 45},
        {"product": Product.E, "count": 2, "get_free": Product.B},
    ]
    for offer in offers:
        if 'price' in offer:
            discount_per_item = offer['product'].price - offer['price'] / offer['count']
        else:
            discount_per_item = offer['get_free'].price
        offer.update({"discount_per_item": discount_per_item})
    offers.sort(reverse=True, key=lambda offer: offer['discount_per_item'])
    return offers


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    basket = {}
    total_price = 0
    for sku in list(skus):
        try:
            product = Product[sku]
        except:
            return -1
        if product in basket:
            basket[product] += 1
        else:
            basket[product] = 1

    for product, count in basket.items():
        total_price += product.price * count

    offers = get_offers()
    discount = calculate_discount(basket, offers)
    total_price = total_price - discount
    return total_price 

