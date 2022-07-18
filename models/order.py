from models.stock import Stock


class Order:
    def __init__(self):
        self.id = None
        self.stock = None
        self.time = None
        self.price = None
        self.quantity = None

    def getId(self):
        return self.id

    def setId(self, id: str):
        self.id = id

    def getStock(self):
        return self.stock

    def setStock(self, stock: Stock):
        self.stock = stock

    def getTime(self):
        return self.time

    def setTime(self, time: str):
        self.time = time

    def getPrice(self):
        return self.price

    def setPrice(self, price: int):
        self.price = price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity
