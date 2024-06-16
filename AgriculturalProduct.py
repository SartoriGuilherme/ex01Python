from Product import Product

class AgriculturalProduct(Product):

    def __init__(self, name: str, price: float, quantity: float, additionalTransport: float):
        super().__init__(name, price, quantity, additionalTransport)
