import abc

from interfaces.order_service_interface import OrderServiceInterface


class OutputFormatterInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def format_response(self, buy_order_service: OrderServiceInterface):
        pass
