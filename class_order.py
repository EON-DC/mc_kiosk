import datetime
import re
import sqlite3
import time

from class_basket import Basket
from class_db_connect import KioskDBConnector
from class_order_menu import OrderMenu


class Order:

    def __init__(self, order_id, location, order_date, order_status, basket, total_price, order_number, connector,
                 update_to_db_=False):
        assert isinstance(order_date, str) and re.match(r'(\d{4}-\d{1,2}-\d{1,2}\b)', order_date)
        assert isinstance(location, str)
        assert isinstance(order_status, str)
        assert isinstance(basket, Basket)
        assert isinstance(total_price, int) and total_price >= 100
        assert isinstance(connector, KioskDBConnector)

        self.order_id = order_id
        self.order_date = order_date
        self.location = location
        self.order_status = order_status
        self.qr_code_id = basket.qr_code_id
        self.total_price = total_price
        self.order_menu_list = list()
        self.order_number = order_number
        self.conn = connector
        self.basket = basket
        if update_to_db_:
            self.update_on_DB()

    def update_on_DB(self):
        self.conn: KioskDBConnector
        # 로케이션 인덱스 얻기
        c = self.conn.start_conn()
        try:
            location_id = c.execute('select location_id from tb_location').fetchone()[0]
        except Exception:
            location_id = 999
        # 이미 자기 ID가 있는 경우엔 update를 하고 없는 경우엔 Insert를 한다
        if self.order_id is None:
            # 마지막 인덱스 얻기
            try:
                last_index = c.execute('select count(order_id) from tb_order').fetchone()[0]
            except Exception:
                last_index = 1
            self.order_id = last_index + 1
            c.execute(
                'insert into tb_order(order_id, order_date, location_id, ' +
                'order_status_id, qr_code_id, order_number,total_price) values (?, ?, ?, ?, ?, ?, ?)',
                (self.order_id, self.order_date, location_id, 1, self.qr_code_id, self.order_number, self.total_price,))
        else:
            c.execute(
                'update tb_order ' +
                'set order_id = (?), order_date = (?), location_id = (?), ' +
                'order_status_id = (?), qr_code_id =(?), order_number = (?), total_price= (?))',
                (self.order_id, self.order_date, location_id, 1, self.qr_code_id, self.order_number, self.total_price,))
        # TODO: basket 정보 DB에 업데이트하는 로직 필요
        self.conn.commit_db()
        self.conn.end_conn()
        order_menu_list = list()
        menu_list, option_list, price_list = self.basket.get_basket_as_zip()
        for menu_id, option, price in zip(menu_list, option_list, price_list):
            order_menu_list.append(OrderMenu(self.order_id, menu_id, option, price, self.conn))
        for order_menu in order_menu_list:
            order_menu.update_on_DB()

    def apply_qr_code(self, code_):
        self.qr_code_id = code_

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def create_order(cls, basket, connector, update_to_db_=False):
        # 타임스탬프 저장
        now_time_str = basket.now_time.strftime('%Y-%m-%d %H:%M:%S')

        # 총액 구하기
        total_price = 0
        menu_id, option_list, item_price = basket.get_basket_as_zip()
        total_price = sum(item_price)

        # 주문번호가져오기
        order_number = connector.get_order_number(now_time_str)

        return cls(None, '광주인력개발원점', now_time_str, "ORDERED", basket, total_price, order_number, connector,
                   update_to_db_)

    @classmethod
    def get_one_from_db_by_id(cls, order_id, connector):
        connector: KioskDBConnector
        c = connector.start_conn()

        order_data = c.execute('''
            select order_id,order_date,location_id,order_status_id,qr_code_id,order_number,total_price
            from tb_order where order_id = (?)''', order_id).fetchall()
        connector.end_conn()

        # basket 조립

        return cls(*order_data)


if __name__ == '__main__':
    pass
