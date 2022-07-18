import abc

from interfaces.buy_order_service_interface import BuyOrderServiceInterface


class OutputFormatterInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def format_response(self, buy_order_service: BuyOrderServiceInterface):
        pass
