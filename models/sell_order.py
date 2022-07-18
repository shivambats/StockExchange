from exceptions.invalid_sell_quantity_error import InvalidSellQuantityException
from models.order import Order


class SellOrder(Order):
    def __init__(self):
        super().__init__()
        self.sold_orders = []
        self.quantity_sold = 0

    def getBuyOrders(self):
        return self.sold_orders

    def setBuyOrders(self, buy_order_id, quantity, buy_price):
        self.sold_orders.append({'buy_order_id': buy_order_id, 'quantity': quantity, 'buy_price': buy_price})

    def getQuantitySold(self):
        return self.quantity_sold

    def setQuantitySold(self, quantity_sold):
        if self.quantity_sold + quantity_sold <= self.quantity:
            self.quantity_sold += quantity_sold
        else:
            raise InvalidSellQuantityException(self.id)
