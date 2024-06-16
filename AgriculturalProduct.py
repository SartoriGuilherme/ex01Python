from Product import Product
class AgriculturalProduct(Product):
    def __init__(self, name: str, price: float, quantity: float, additionalTransport: float):
        super().__init__(name, price, quantity, additionalTransport)

    def getFinalPrice(self) -> float:
        if self.quantity > 0 and self.quantity <= 100:
            return (self.quantity * self.price) * 1.08 + (self.quantity * self.additionalTransport)
        elif self.quantity >= 100.01 and self.quantity <= 200:
            return (self.quantity * self.price) * 1.05 + (self.quantity * self.additionalTransport)
        else:
            return (self.quantity * self.price) * 1.035 + (self.quantity * self.additionalTransport)
