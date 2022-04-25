from typing import List, Dict, Generator

from .product import Product
from .discount import Discount
from .errors import ProductNotFoundError



class Basket:
    def __init__(self, skus: str) -> None:
        self.skus: str = skus
        self.products: Dict[Product, int] = {}
        self.total_price: int = 0
        for product in self._parse_skus(self.skus):
            self.add_item(product)
    
    def add_item(self, product: Product) -> None:
        if product in self.products:
            self.products[product] += 1
        else:
            self.products[product] = 1
        self.total_price += product.price 

    def checkout(self, offers: List[dict]) -> int:
        return self.total_price - self._calculate_discount(offers)

    def _calculate_discount(self, offers: List[dict]) -> int:
        total_discount = 0
        products = self.products.copy()
        for offer in offers:
            total_discount += offer["type"](offer).apply(products)
        return total_discount    

    def _parse_skus(self, skus: str) -> Generator[Product, None, None]:
        for sku in list(skus):
            try:
                yield Product[sku]
            except:
                raise ProductNotFoundError(sku)
