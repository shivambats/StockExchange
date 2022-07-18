from interfaces.buy_order_service_interface import BuyOrderServiceInterface
from interfaces.output_formatter_interface import OutputFormatterInterface


class OutputFormatterController:
    def __init__(self, output_formatter_service: OutputFormatterInterface):
        self.output_formatter_service = output_formatter_service

    def format_response(self, buy_order_service: BuyOrderServiceInterface):
        self.output_formatter_service.format_response(buy_order_service)
