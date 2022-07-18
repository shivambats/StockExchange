from interfaces.buy_order_service_interface import BuyOrderServiceInterface
from models.buy_order import BuyOrder
from models.stock import Stock


class BuyOrderController:
    def __init__(self, buy_order_service: BuyOrderServiceInterface):
        self.buy_order_service = buy_order_service

    def addOrder(self, id, quantity, stock_name, time, price):
        order = BuyOrder()
        order.setId(id)
        order.setTime(time)
        order.setPrice(price)
        order.setQuantity(quantity)
        stock = Stock()
        stock.name = stock_name
        order.setStock(stock)
        self.buy_order_service.addOrder(order)
