from interfaces.input_reader_interface import InputReaderInterface


class InputReaderController:
    def __init__(self, input_reader_service: InputReaderInterface):
        self.input_reader_service = input_reader_service

    def read_file(self, file):
        return self.input_reader_service.read_input(file)
