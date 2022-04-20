from enum import Enum, auto


class Product(Enum):
    A = 50
    B = 30
    C = 20
    D = 15

    def __init__(self, price: int) -> None:
        self._value_ = auto()
        self.price = price


def offer_applicable():
    .


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    total_price = 0
    for sku in list(skus):
        try:
            product = Product[sku]
        except:
            return -1
        total_price += product.price

    # Check if discount is applicable
    if offer_applicable(skus):

        # Apply discount

    return total_price 


