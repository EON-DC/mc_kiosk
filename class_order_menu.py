from class_db_connect import KioskDBConnector


class OrderMenu:
    def __init__(self, order_id, menu_id, option, price, conn=None):
        self.order_id = order_id
        self.menu_id = menu_id
        self.option = option
        self.price = price
        self.conn = conn
        conn: KioskDBConnector

    def update_on_DB(self):
        self.conn: KioskDBConnector
        c = self.conn.start_conn()
        option_str = f'{str(self.option)}'
        c.execute('insert into tb_order_menu(order_id, menu_id, option, price) values (?, ?, ?, ?)',
                  (self.order_id, self.menu_id, option_str, self.price))
        self.conn.commit_db()
        self.conn.end_conn()
