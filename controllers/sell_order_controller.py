from interfaces.order_service_interface import OrderServiceInterface
from models.sell_order import SellOrder
from models.stock import Stock


class SellOrderController:
    def __init__(self, sell_order_service: OrderServiceInterface):
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
