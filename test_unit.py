from unittest import TestCase

from class_basket import Basket
from class_db_connect import KioskDBConnector
from class_order import Order


class UnitTest(TestCase):
    def setUp(self):
        # 운영상 DB를 건들이지 않기위해 테스트용 db를 이용함
        self.conn = KioskDBConnector(test_option=True)
        c = self.conn.start_conn()
        c.execute("""delete from tb_order""")
        c.execute("""delete from tb_order_menu""")
        self.conn.commit_db()

    def test_장바구니에_담긴_상품들로_주문을_등록한다_그리고_주문테이블_주문메뉴테이블에_등록된다(self):
        basket = Basket(self.conn)
        basket.add_item(1, [1, 'set', 'large', 'lunch', 35, 65])
        basket.add_item(3, [2, 'set', 'large', 32, 65])
        basket.add_item(45, [2])
        order_1 = Order.create_order(basket, self.conn, True)
        c = self.conn.start_conn()
        fetched_list = c.execute('select * from tb_order').fetchall()
        self.assertEqual(len(fetched_list), 1)

    def test_주문이_담길_때마다_주문번호가_증가한다(self):
        basket = Basket(self.conn)
        basket.add_item(1, [1, 'set', 'large', 'lunch', 35, 65])
        basket.add_item(3, [2, 'set', 'large', 32, 65])
        basket.add_item(45, [2])
        order_1 = Order.create_order(basket, self.conn, True)
        basket.add_item(48, [2])
        order_2 = Order.create_order(basket, self.conn, True)
        order_3 = Order.create_order(basket, self.conn, True)
        order_4 = Order.create_order(basket, self.conn, True)
        c = self.conn.start_conn()
        fetched_list = c.execute('select * from tb_order').fetchall()
        self.assertEqual(len(fetched_list), 4)
        self.assertEqual('0001', str(order_1.order_number))
        self.assertEqual('0002', str(order_2.order_number))
        self.assertEqual('0003', str(order_3.order_number))
        self.assertEqual('0004', str(order_4.order_number))

    def test_00시에_주문번호가_리셋된다(self):
        basket = Basket(self.conn)
        today_day = basket.now_time.day
        basket.now_time = basket.now_time.replace(day=(today_day - 1))
        basket.add_item(1, [1, 'set', 'large', 'lunch', 35, 65])
        basket.add_item(3, [2, 'set', 'large', 32, 65])
        basket.add_item(45, [2])
        order_1 = Order.create_order(basket, self.conn, True)
        order_2 = Order.create_order(basket, self.conn, True)
        basket.now_time = basket.now_time.replace(day=today_day)
        order_3 = Order.create_order(basket, self.conn, True)
        order_4 = Order.create_order(basket, self.conn, True)
        c = self.conn.start_conn()
        fetched_list = c.execute('select * from tb_order').fetchall()
        self.assertEqual(len(fetched_list), 4)
        self.assertEqual('0001', str(order_1.order_number))
        self.assertEqual('0002', str(order_2.order_number))
        self.assertEqual('0001', str(order_3.order_number))
        self.assertEqual('0002', str(order_4.order_number))

    def test_핫케이크_3조각은_사이드메뉴를_안받는다(self):
        basket = Basket(self.conn)
        # 핫케이크 3조각(29), 콜라(65) 세트 주문시 4300원, 바닐라세이크(70)로 음료 주문시 5500원
        basket.add_item(29, [1, 'set', 65])
        order_1 = Order.create_order(basket, self.conn)
        self.assertEqual(order_1.total_price, 4300)

        basket_2 = Basket(self.conn)
        basket_2.add_item(29, [1, 'set', 70])
        order_2 = Order.create_order(basket_2, self.conn)
        self.assertEqual(order_2.total_price, 5500)

    def test_메뉴_리스트를_모두_갖고온다(self):
        menu_list = self.conn.get_menu_list()
        self.assertEqual(len(menu_list), 74)
