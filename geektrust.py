import sys
from controllers.buy_order_controller import BuyOrderController
from controllers.input_reader_controller import InputReaderController
from controllers.marketplace_controller import MarketplaceController
from controllers.output_formatter_controller import OutputFormatterController
from controllers.sell_order_controller import SellOrderController
from services.buy_order_service import BuyOrderService
from services.input_reader_service import InputReaderService
from services.marketplace_service import MarketplaceService
from services.output_formatter_service import OutputFormatterService
from services.sell_order_service import SellOrderService
from strategy.default_marketplace_strategy import DefaultMarketplaceStrategy


def main():
    input_file = sys.argv[1]

    input_reader_service = InputReaderService()
    input_reader_controller = InputReaderController(input_reader_service)

    output_formatter_service = OutputFormatterService()
    output_formatter_controller = OutputFormatterController(output_formatter_service)

    marketplace_strategy = DefaultMarketplaceStrategy()
    marketplace_service = MarketplaceService(marketplace_strategy)
    marketplace_controller = MarketplaceController(marketplace_service)

    buy_order_service = BuyOrderService()
    buy_order_controller = BuyOrderController(buy_order_service)

    sell_order_service = SellOrderService()
    sell_order_controller = SellOrderController(sell_order_service)

    input_reader_controller.read_file(buy_order_controller, sell_order_controller, input_file)
    marketplace_controller.place_orders(buy_order_service, sell_order_service)
    output_formatter_controller.format_response(buy_order_service)
    # sys.argv[1] should give the absolute path to the input file
    # parse the file and process the command
    # print the output


if __name__ == "__main__":
    main()
