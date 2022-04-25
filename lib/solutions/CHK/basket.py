from typing import List, Dict

from .product import Product
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
        products = self.products.copy()
        groupbuy_discount, products = calculate_groupbuy_discount(products, offers) 
        getfree_discount, products = calculate_getfree_discount(products, offers) 
        multiprice_discount, products = calculate_multiprice_discount(products, offers) 
        return groupbuy_discount + getfree_discount + multiprice_discount 

    def _parse_skus(self, skus: str) -> Generator[Product, None, None]:
        for sku in list(skus):
            try:
                yield Product[sku]
            except:
                raise ProductNotFoundError(sku)
