from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, quantity, additionalTransport):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__additionalTransport = additionalTransport

    @abstractmethod
    def getFinalPrice(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def additionalTransport(self):
        return self.__additionalTransport
