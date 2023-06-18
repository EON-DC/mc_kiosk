from class_db_connect import KioskDBConnector
from class_order import Order


class KioskController:
    def __init__(self, connector):
        assert isinstance(connector, KioskDBConnector)
        self.connector = connector

    def get_menu_data(self):
        return self.connector.get_menu_list()

    def add_order(self, basket):
        order = Order.create_order(basket, self.connector, True)
        return order.order_id