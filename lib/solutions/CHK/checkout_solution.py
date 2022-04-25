from typing import Dict, List

from .product import Product
from .basket import Basket
from .errors import ProductNotFoundError


def get_offers() -> list:
    offers = [
        {"product": Product.A, "count": 3, "price": 130},
        {"product": Product.A, "count": 5, "price": 200},
        {"product": Product.B, "count": 2, "price": 45},
        {"product": Product.E, "count": 2, "get_free": Product.B},
        {"product": Product.F, "count": 3, "get_free": Product.F},
        {"product": Product.H, "count": 5, "price": 45},
        {"product": Product.H, "count": 10, "price": 80},
        {"product": Product.K, "count": 2, "price": 120},
        {"product": Product.N, "count": 3, "get_free": Product.M},
        {"product": Product.P, "count": 5, "price": 200},
        {"product": Product.Q, "count": 3, "price": 80},
        {"product": Product.R, "count": 3, "get_free": Product.Q},
        {"product": Product.U, "count": 4, "get_free": Product.U},
        {"product": Product.V, "count": 2, "price": 90},
        {"product": Product.V, "count": 3, "price": 130},
        {"product": [Product.S, Product.T, Product.X, Product.Y, Product.Z], "count": 3, "price": 45},
    ]
    for offer in offers:
        if 'get_free' in offer:
            discount_per_item = offer['get_free'].price
        elif isinstance(offer['product'], list):
            priciest_product = max([product.price for product in offer['product']])
            discount_per_item = priciest_product - offer['price'] / offer['count']
        else:
            discount_per_item = offer['product'].price - offer['price'] / offer['count']
        offer.update({"discount_per_item": discount_per_item})
    offers.sort(reverse=True, key=lambda offer: offer['discount_per_item'])
    return offers



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket = Basket(skus) 
    except ProductNotFoundError:
        return -1
    offers = get_offers()
    return basket.checkout(offers)
