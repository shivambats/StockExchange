from services.marketplace_service import MarketplaceService


class MarketplaceController:
    def __init__(self, marketplace_service: MarketplaceService):
        self.marketplace_service = marketplace_service

    def place_orders(self, buy_order_service, sell_order_service):
        self.marketplace_service.start_matching(buy_order_service, sell_order_service)
