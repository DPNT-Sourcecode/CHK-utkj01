from enum import Enum, auto


class Product(Enum):
    A = 50
    B = 30
    C = 20
    D = 15
    E = 40

    def __init__(self, price: int) -> None:
        self._value_ = auto()
        self.price = price


def calculate_discount(basket, offers):
    discount = 0
    # Discount needs to favor the customer to pick lowest
    for product, count in basket.items():
        if product in offers:
            if count >= offers[product]["count"]:
                offer = offers[product]
                if 'buy_free' in offer:
                    discount_count = count // offer['count']
                    free_product = offers[product]["buy_free"]
                    if free_product in basket:
                        free_product_count = basket.get(free_product)
                        if free_product_count:
                            print(free_product_count, free_product.price)
                            discount += free_product.price * free_product_count
                else:
                    price_per_item = offer['price'] / offer['count']
                    discount_count = count // offer['count']
                    print(product)
                    discount += (product.price - price_per_item) * offer["count"] * discount_count
    print(discount)
    return discount


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    offers = {
        Product.A: {"count": 3, "price": 130},
        Product.B: {"count": 2, "price": 45},
        Product.E: {"count": 2, "buy_free": Product.B}
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



