

class ProductNotFoundError(Exception):
    def __init(self, product: str) -> None:
        super().__init__(f"Product not found: {product}")
