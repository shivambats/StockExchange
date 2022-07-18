from exceptions.invalid_buy_quantity_error import InvalidBuyQuantityException
from models.order import Order


class BuyOrder(Order):
    def __init__(self):
        super().__init__()
        self.sold_orders = []
        self.quantity_bought = 0

    def getSellOrders(self):
        return self.sold_orders

    def setSellOrders(self, sell_order_id, quantity, sell_order_price):
        self.sold_orders.append({'sell_order_id': sell_order_id, 'quantity': quantity, 'sell_order_price': sell_order_price})

    def getQuantityBought(self):
        return self.quantity_bought

    def setQuantityBought(self, quantity_bought):
        if self.quantity_bought + quantity_bought <= self.quantity:
            self.quantity_bought = self.quantity_bought + quantity_bought
        else:
            raise InvalidBuyQuantityException(self.id)
