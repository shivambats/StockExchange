class InvalidBuyQuantityException(Exception):
    def __init__(self, buy_order_id):
        self.msg = f"Not enough buy quantity available for {buy_order_id}"

    def __repr__(self):
        return self.msg
