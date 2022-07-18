from interfaces.input_reader_interface import InputReaderInterface


class InputReaderController:
    def __init__(self, input_reader_service: InputReaderInterface):
        self.input_reader_service = input_reader_service

    def read_file(self, buy_order_controller, sell_order_controller, filename):
        return self.input_reader_service.read_input(buy_order_controller, sell_order_controller, filename)
