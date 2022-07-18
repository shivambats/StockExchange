from abc import ABC

from models.order import Order
from interfaces.order_service_interface import OrderServiceInterface


class BuyOrderService(OrderServiceInterface, ABC):
    def __init__(self):
        self.orders = []

    def getOrders(self):
        return self.orders

    def addOrder(self, order: Order):
        self.orders.append(order)
