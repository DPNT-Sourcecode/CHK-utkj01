from enum import Enum, auto


class Product(Enum):
    A = 50
    B = 30
    C = 20
    D = 15

    def __init__(self, price: int) -> None:
        self._value_ = auto()
        self.price = price


def calculate_discount(basket, offers):
    discount = 0
    for product, count in basket.items():
        if product in offers:
            if count >= offers[product]["count"]:
                offer = offers[product]
                price_per_item = offer['price'] / offer['count']
                discount_count = count // offer['count']
                discount += (product.price - price_per_item) * offer["count"] * discount_count
    return discount


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    offers = {
        Product.A: {"count": 3, "price": 130},
        Product.B: {"count": 2, "price": 45},
    }
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

    discount = calculate_discount(basket, offers)
    total_price = total_price - discount
    return total_price 




