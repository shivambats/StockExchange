import abc

from models.order import Order


class OrderServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addOrder(self, order: Order):
        pass

    @abc.abstractmethod
    def getOrders(self):
        pass
