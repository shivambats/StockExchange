from abc import ABC

from enums.order_actions import OrderAction
from interfaces.input_reader_interface import InputReaderInterface


class InputReaderService(InputReaderInterface, ABC):
    def read_input(self, buy_order_controller, sell_order_controller, filename):
        file = open(filename, "r")
        for input in file:
            order_data = input.strip().split()
            id = order_data[0]
            time = order_data[1]
            stock = order_data[2]
            order_action = order_data[3]
            price = order_data[4]
            quantity = int(order_data[5])
            if order_action == OrderAction.BUY.value:
                buy_order_controller.addOrder(id, quantity, stock, time, price)
            else:
                sell_order_controller.addOrder(id, quantity, stock, time, price)
