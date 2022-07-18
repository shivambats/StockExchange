import abc

from models.order import Order


class SellOrderServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addOrder(self, order: Order):
        pass

    @abc.abstractmethod
    def getOrders(self):
        pass
