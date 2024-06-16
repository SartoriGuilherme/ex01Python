from Product import Product


class IndustrializedProduct(Product):
    def __init__(self, name: str, price: float, quantity: float, additionalTransport: float, icms: float, ipi: float):
        super().__init__(name, price, quantity, additionalTransport)
        self._icms = icms
        self._ipi = ipi

    def getFinalPrice(self) -> float:
        if self.quantity > 0 and self.quantity <= 50:
            return (self.quantity * self.price) * 1.12 * self._icms * self._ipi + (self.quantity * self.additionalTransport)
        elif self.quantity >= 51 and self.quantity <= 200:
            return (self.quantity * self.price) * 1.105 * self._icms * self._ipi + (self.quantity * self.additionalTransport)
        else:
            return (self.quantity * self.price) * 1.09 * self._icms * self._ipi + (self.quantity * self.additionalTransport)

    @property
    def icms(self):
        return self._icms

    @property
    def ipi(self):
        return self._ipi
