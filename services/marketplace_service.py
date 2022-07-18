from interfaces.match_order_strategy_interface import MatchOrderStrategyInterface
from interfaces.order_service_interface import OrderServiceInterface


class MarketplaceService:
    def __init__(self, match_order_strategy: MatchOrderStrategyInterface):
        self.match_order_strategy = match_order_strategy

    def start_matching(self, buy_order_service: OrderServiceInterface, sell_order_service: OrderServiceInterface):
        buy_orders = buy_order_service.getOrders()
        sell_orders = sell_order_service.getOrders()
        self.match_order_strategy.matchBuyToSellOrder(buy_orders, sell_orders)
