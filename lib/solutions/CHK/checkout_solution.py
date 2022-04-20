from enum import Enum, auto


class Product(Enum):
    A = 50
    B = 30
    C = 20
    D = 15

    def __init__(self, price: int) -> None:
        self._value_ = auto()
        self.price = price


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
    return total_price 






