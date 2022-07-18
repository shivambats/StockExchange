from interfaces.output_formatter_interface import OutputFormatterInterface


class OutputFormatterController:
    def __init__(self, output_formatter_service: OutputFormatterInterface):
        self.output_formatter_service = output_formatter_service

    def format_response(self, buy_order_service):
        self.output_formatter_service.format_response(buy_order_service)
