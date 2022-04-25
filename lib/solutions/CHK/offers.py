from .discount import GetFree, MultiPrice, GroupPrice
from .product import Product


def get_offers() -> list:
    offers = [
        {"product": Product.A, "type": MultiPrice, "count": 3, "price": 130},
        {"product": Product.A, "type": MultiPrice, "count": 5, "price": 200},
        {"product": Product.B, "type": MultiPrice, "count": 2, "price": 45},
        {"product": Product.E, "type": GetFree, "count": 2, "get_free": Product.B},
        {"product": Product.F, "type": GetFree, "count": 3, "get_free": Product.F},
        {"product": Product.H, "type": MultiPrice, "count": 5, "price": 45},
        {"product": Product.H, "type": MultiPrice, "count": 10, "price": 80},
        {"product": Product.K, "type": MultiPrice, "count": 2, "price": 120},
        {"product": Product.N, "type": GetFree, "count": 3, "get_free": Product.M},
        {"product": Product.P, "type": MultiPrice, "count": 5, "price": 200},
        {"product": Product.Q, "type": MultiPrice, "count": 3, "price": 80},
        {"product": Product.R, "type": GetFree, "count": 3, "get_free": Product.Q},
        {"product": Product.U, "type": GetFree, "count": 4, "get_free": Product.U},
        {"product": Product.V, "type": MultiPrice, "count": 2, "price": 90},
        {"product": Product.V, "type": MultiPrice, "count": 3, "price": 130},
        {"product": [Product.S, Product.T, Product.X, Product.Y, Product.Z], 
         "type": GroupPrice, "count": 3, "price": 45},
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

