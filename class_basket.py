from class_db_connect import KioskDBConnector
from common import *


class Basket:
    def __init__(self, conn, total_menu_list=None):
        conn: KioskDBConnector
        self.now_time = datetime.datetime.now()
        self.menu_id_list = list()
        self.option_list = list()
        self.price_list = list()
        self.qr_code_id = None
        self.conn = conn
        self.eat_way = None
        self.total_menu_list = total_menu_list
        if self.total_menu_list is None:
            self.total_menu_list = self.conn.get_menu_list()

    def __repr__(self):
        # return f'Basket_obj| MENU_ID: {self.menu_id_list}\t| OPTION_LIST: {self.option_list}\t| PRICE_LIST: {self.price_list}'
        menu_name_list = list()
        for index, menu_id in enumerate(self.menu_id_list):
            name = self.conn.get_menu_name_by_menu_id(menu_id)
            item_quantity = self.option_list[index][0]
            residual_option = self.option_list[index][1:]
            menu_name_list.append((name, str(item_quantity) + '개', residual_option, f'{self.price_list[index]:,d}원'))
        return str(menu_name_list)


    def set_eat_way(self, eat_way):
        self.eat_way = eat_way

    def assert_same_option(self, list_1, list_2):
        if len(list_1) != len(list_2):
            return False
        for left, right in zip(list_1[1:], list_2[1:]):
            if left != right:
                return False
        return True

    def add_item(self, menu_id, option):
        assert isinstance(menu_id, int)
        assert isinstance(option, list)

        if menu_id in self.menu_id_list:
            # 기존 메뉴에 추가해야하는 경우임
            idx = self.menu_id_list.index(menu_id)
            if self.assert_same_option(self.option_list[idx], option):
                # 옵션이 같은 경우엔 수량만 추가, 그 외엔 다르게 리스트 구성해야함
                additional_count = option[0]
                self.option_list[idx][0] += additional_count
                self.refresh_price_list()
                return

        # 들어오는 옵션의 0번째는 수량, 1번째는 세트여부, -2번째는 사이드, -1번째는 음료
        self.menu_id_list.append(menu_id)
        self.option_list.append(option)
        now_price = self.get_price(menu_id, option)
        self.price_list.append(now_price)

    def update_qrcode(self, qr_code_id):
        self.qr_code_id = qr_code_id

    def refresh_price_list(self):
        self.price_list = list()
        for menu_id, option in zip(self.menu_id_list, self.option_list):
            self.price_list.append(self.get_price(menu_id, option))

    def delete_item(self, index_):
        assert isinstance(index_, int) and 0 <= index_ < len(self.menu_id_list)
        self.menu_id_list.pop(index_)
        self.option_list.pop(index_)

    def get_basket_as_zip(self):
        return self.menu_id_list, self.option_list, self.price_list

    def add_option(self, index, option_content):
        self.option_list[index].insert(1, option_content)
        self.refresh_price_list()

    def select_side_and_beverage(self, index, side_menu_id, beverage_menu_id):
        self.option_list[index].insert(-1, side_menu_id)
        self.option_list[index].insert(-1, beverage_menu_id)
        self.refresh_price_list()

    def select_beverage(self, index, beverage_menu_id):
        self.option_list[index].insert(-1, beverage_menu_id)
        self.refresh_price_list()

    def get_additional_price(self, idx):
        return self.total_menu_list[idx - 1].additional_price

    def get_price(self, menu_id, option):
        result_price = 0
        quantity = option[0]
        menu = self.total_menu_list[menu_id - 1]
        if 'set' in option:
            if menu.set_order_can_it_order_side_menu and option[-2] is not None and option[-2].isdigit():
                result_price += self.get_additional_price(int(option[-2]))
            if menu.set_order_can_it_order_beverage and option[-1] is not None and option[-1].isdigit():
                result_price += self.get_additional_price(int(option[-1]))

        if is_lunch() and menu.is_lunch_menu == 1:
            result_price += menu.lunch_price
        elif menu.is_happy_snack == 1:
            result_price += menu.happy_snack_price
        elif 'large' in option and 'set' in option:
            result_price += 700
        elif 'large' in option and 'set' not in option:
            result_price += menu.large_price
        elif 'medium' in option and 'set' not in option:
            result_price += menu.medium_price
        elif 'small' in option:
            result_price += menu.small_price
        else:
            result_price += menu.ordinary_price

        return result_price * quantity

    # def get_price(self, menu_id, option):
    #     c = self.conn.start_conn()
    #     result_price = 0
    #     quantity = option[0]
    #     if 'set' in option:
    #         has_side_opt, has_beverage_opt = c.execute('''select set_order_can_it_order_side_menu,
    #         set_order_can_it_order_beverage from tb_menu where menu_id = (?)''', (menu_id,)).fetchone()
    #         side_menu_id = None
    #         beverage_menu_id = None
    #         if has_side_opt:
    #             side_menu_id = int(option[-2])
    #         if has_beverage_opt:
    #             beverage_menu_id = int(option[-1])
    #         # lunch 확인
    #         if is_lunch(self.now_time) and self.conn.is_serving_lunch_set(menu_id):
    #             menu_price = c.execute('select lunch_price from tb_menu where menu_id = (?)', (menu_id,)).fetchone()[0]
    #         else:
    #             menu_price = c.execute('select set_price from tb_menu where menu_id = (?)', (menu_id,)).fetchone()[0]
    #         result_price = result_price + menu_price
    #
    #         if side_menu_id is not None and beverage_menu_id is not None:
    #             # additional_price_list = c.execute('select additional_price from tb_menu where menu_id in (?, ?)',
    #             #                                   (side_menu_id, beverage_menu_id,)).fetchall()
    #             # for i in additional_price_list:
    #             #     result_price = result_price + i[0]
    #             result_price += c.execute('select additional_price from tb_menu where menu_id = (?)',
    #                                       (side_menu_id,)).fetchone()[0]
    #             result_price += c.execute('select additional_price from tb_menu where menu_id = (?)',
    #                                       (beverage_menu_id,)).fetchone()[0]
    #
    #         elif side_menu_id is not None:
    #             result_price += c.execute('select additional_price from tb_menu where menu_id = (?)',
    #                                       (side_menu_id,)).fetchone()[0]
    #
    #         elif beverage_menu_id is not None:
    #             result_price += c.execute('select additional_price from tb_menu where menu_id = (?)',
    #                                       (beverage_menu_id,)).fetchone()[0]
    #
    #         # large 시 요금 추가
    #         if 'large' in option:
    #             result_price += 700  # 현재는 라지 세트가 700원 추가로 동일
    #
    #     else:  # 단품 메뉴시 일반 가격 가져옴
    #         menu_price = self.conn.get_ordinary_price_by_menu_id(menu_id)
    #         result_price = result_price + menu_price
    #
    #     return result_price * quantity

    def decrease_item(self, index):
        self.option_list[index][0] -= 1
        self.refresh_price_list()

    def increase_item(self, index):
        self.option_list[index][0] += 1
        self.refresh_price_list()

    def delete_item(self, index):
        self.menu_id_list.pop(index)
        self.option_list.pop(index)
        self.price_list.pop(index)

    def get_total_price(self):
        return sum(self.price_list)



