from interfaces.sell_order_service_interface import SellOrderServiceInterface
from models.sell_order import SellOrder
from models.stock import Stock


class SellOrderController:
    def __init__(self, sell_order_service: SellOrderServiceInterface):
        self.sell_order_service = sell_order_service

    def addOrder(self, id, quantity, stock_name, time, price):
        order = SellOrder()
        order.setId(id)
        order.setTime(time)
        order.setPrice(price)
        order.setQuantity(quantity)
        stock = Stock()
        stock.name = stock_name
        order.setStock(stock)
        self.sell_order_service.addOrder(order)
