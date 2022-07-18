from abc import ABC

from models.order import Order
from interfaces.sell_order_service_interface import SellOrderServiceInterface


class SellOrderService(SellOrderServiceInterface, ABC):
    def __init__(self):
        self.orders = []

    def addOrder(self, order: Order):
        self.orders.append(order)

    def getOrders(self):
        return self.orders
