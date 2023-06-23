from class_db_connect import KioskDBConnector
from class_order import Order


class KioskController:
    def __init__(self, connector):
        assert isinstance(connector, KioskDBConnector)
        self.connector = connector

    def get_menu_data(self):
        menu_list = self.connector.get_menu_list()
        for menu in menu_list:
            if '맥너겟' in menu.name:
                menu.set_menu_disable()
        return menu_list

    def add_order(self, basket):
        order = Order.create_order(basket, self.connector, True)
        print(f"updated on DB (logged by controller) : {order}")
        return order.order_number

    def match_qr_code(self, code):
        assert isinstance(code, str)
        replaced_code = code.replace(' ', '')
        if replaced_code == 'M123456':
            return True
        else:
            return False