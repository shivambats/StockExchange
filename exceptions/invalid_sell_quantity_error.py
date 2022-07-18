class InvalidSellQuantityException(Exception):
    def __init__(self, sell_order_id):
        self.msg = f'Not enough sell quantity available for {sell_order_id}'

    def __repr__(self):
        return self.msg
