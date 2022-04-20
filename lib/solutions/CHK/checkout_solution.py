from enum import Enum, auto


class Product(Enum):
    A = 50
    B = 30
    C = 20
    D = 15

    def __init__(self, price: int):
        self._value_ = auto()
        self.price = price


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    raise NotImplementedError()



