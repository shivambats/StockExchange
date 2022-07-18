import abc


class InputReaderInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read_input(self, buy_order_controller, sell_order_controller):
        pass
