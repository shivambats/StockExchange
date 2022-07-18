from abc import ABC
from typing import List

from interfaces.match_order_strategy_interface import MatchOrderStrategyInterface
from models.buy_order import BuyOrder
from models.sell_order import SellOrder


class DefaultMarketplaceStrategy(MatchOrderStrategyInterface, ABC):
    def matchBuyToSellOrder(self, buy_orders: List[BuyOrder], sell_orders: List[SellOrder]):
        for buy_order in buy_orders:
            for sell_order in sell_orders:
                quantity_available_to_sell = sell_order.getQuantity() - sell_order.getQuantitySold()
                quantity_available_to_buy = buy_order.getQuantity() - buy_order.getQuantityBought()
                if sell_order.getStock().getName() == buy_order.getStock().getName() and quantity_available_to_sell > 0 and \
                        quantity_available_to_buy > 0 and buy_order.price > sell_order.price:
                    quantity_to_be_matched = min(quantity_available_to_sell, quantity_available_to_buy)
                    sell_order.setQuantitySold(quantity_to_be_matched)
                    buy_order.setQuantityBought(quantity_to_be_matched)
                    sell_order.setBuyOrders(buy_order.getId(), quantity_to_be_matched, buy_order.getPrice())
                    buy_order.setSellOrders(sell_order.getId(), quantity_to_be_matched, sell_order.getPrice())
