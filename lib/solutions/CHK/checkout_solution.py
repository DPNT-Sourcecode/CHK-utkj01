from .offers import get_offers
from .basket import Basket
from .errors import ProductNotFoundError


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket = Basket(skus) 
    except ProductNotFoundError:
        return -1
    offers = get_offers()
    return basket.checkout(offers)
