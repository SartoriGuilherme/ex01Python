from Product import Product


class IndustrializedProduct(Product):
    def __init__(self, name: str, price: float, quantity: float, additionalTransport: float, icms: float, ipi: float):
        super().__init__(name, price, quantity, additionalTransport)
        self.__icms = icms
        self.__ipi = ipi

    def getFinalPrice(self) -> float:
        if self.quantity > 0 and self.quantity <= 50:
            return (self.quantity * self.price) * 1.12 * self.__icms * self.__ipi + (self.quantity * self.additionalTransport)
        elif self.quantity >= 51 and self.quantity <= 200:
            return (self.quantity * self.price) * 1.105 * self.__icms * self.__ipi + (self.quantity * self.additionalTransport)
        else:
            return (self.quantity * self.price) * 1.09 * self.__icms * self.__ipi + (self.quantity * self.additionalTransport)

    @property
    def icms(self):
        return self.__icms

    @property
    def ipi(self):
        return self.__ipi
