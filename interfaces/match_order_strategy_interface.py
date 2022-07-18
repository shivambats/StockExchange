import abc
from typing import List

from models.buy_order import BuyOrder
from models.sell_order import SellOrder


class MatchOrderStrategyInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def matchBuyToSellOrder(self, buy_orders: List[BuyOrder], sell_orders: List[SellOrder]):
        pass
