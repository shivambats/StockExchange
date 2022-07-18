from abc import ABC

from interfaces.buy_order_service_interface import BuyOrderServiceInterface
from interfaces.output_formatter_interface import OutputFormatterInterface


class OutputFormatterService(OutputFormatterInterface, ABC):
    def format_response(self, buy_order_service: BuyOrderServiceInterface):
        for buy_order in buy_order_service.getOrders():
            for buy_order_audit in buy_order.getSellOrders():
                print(buy_order.getId(), buy_order_audit['sell_order_price'],
                      buy_order_audit['quantity'], buy_order_audit['sell_order_id'])
