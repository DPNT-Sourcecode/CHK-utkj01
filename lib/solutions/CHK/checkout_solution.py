from typing import Dict, List, Generator
from .product import Product
from .errors import ProductNotFoundError


def calculate_getfree_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    discount = 0
    for offer in offers:
        product = offer['product']
        if isinstance(product, Product):
            if 'get_free' in offer and product in basket:
                free_product = offer["get_free"]
                if free_product in basket:
                    while basket[product] >= offer["count"] and basket[free_product] > 0:
                        discount += free_product.price
                        # TODO: This is quite hacky. To be refactored later.
                        if free_product is not product:
                            basket[free_product] -= 1
                        basket[product] -= offer["count"]
    return discount, basket 


def calculate_multiprice_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    discount = 0
    for offer in offers:
        product = offer['product']
        if isinstance(product, Product):
            if 'price' in offer and product in basket:
                while basket[product] >= offer["count"]:
                    discount += product.price * offer["count"] - offer['price']
                    basket[product] -= offer["count"]
    return discount, basket


def sort_pricier_first(products: List[Product]) -> List[Product]:
    return sorted(products, key=lambda product: product.price, reverse=True)


def calculate_groupbuy_discount(basket: Dict[str, int], offers: List[dict]) -> int: 
    discount = 0
    total = 0
    applied = 0
    for offer in offers:
        product_list = offer['product']
        if isinstance(product_list, list):
            for product in sort_pricier_first(product_list):
                if product in basket:
                    while basket[product] > 0:
                        total += product.price
                        applied += 1
                        basket[product] -= 1
            if applied >= offer['count']:
                discount += total - offer['price'] * applied / offer['count']
    return discount, basket


def calculate_discount(basket: Dict[str, int], offers: List[dict]) -> int:
    # TODO: Refactor this as the order seems to matter 
    groupbuy_discount, basket = calculate_groupbuy_discount(basket, offers) 
    getfree_discount, basket = calculate_getfree_discount(basket, offers) 
    multiprice_discount, basket = calculate_multiprice_discount(basket, offers) 
    return groupbuy_discount + getfree_discount + multiprice_discount 


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
        

    def _parse_skus(self, skus: str) -> Generator[Product, None, None]:
        for sku in list(skus):
            try:
                yield Product[sku]
            except:
                raise ProductNotFoundError(sku)


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





