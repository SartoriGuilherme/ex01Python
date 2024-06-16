from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, quantity, additionalTransport):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._additionalTransport = additionalTransport

    @abstractmethod
    def getFinalPrice(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @property
    def additionalTransport(self):
        return self._additionalTransport