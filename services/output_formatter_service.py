from abc import ABC

from interfaces.order_service_interface import OrderServiceInterface
from interfaces.output_formatter_interface import OutputFormatterInterface


class OutputFormatterService(OutputFormatterInterface, ABC):
    def format_response(self, buy_order_service: OrderServiceInterface):
        for buy_order in buy_order_service.getOrders():
            for buy_order_audit in buy_order.getSellOrders():
                print(buy_order.getId(), buy_order_audit['sell_order_price'],
                      buy_order_audit['quantity'], buy_order_audit['sell_order_id'])
