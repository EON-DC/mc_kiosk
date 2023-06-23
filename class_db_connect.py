import sqlite3

import numpy as np
import pandas as pd

import common
from class_menu import Menu


class KioskDBConnector:
    _instance = None

    def __new__(cls, test_option=False):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=False):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        if self.test_option is False:
            self.conn = sqlite3.connect('mac_db.db')
        else:
            self.conn = sqlite3.connect('test_db.db')
        return self.conn.cursor()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def insert_menu_value(self):
        c = self.start_conn()
        df = pd.read_excel('excel_source/table_menu.xlsx', engine='openpyxl')
        self.conn: sqlite3.Connection
        for row in df.values:
            row: pd.Series
            result_row = list()
            temp_question_list = ['?' for _ in range(35)]
            for i in row:
                if isinstance(i, int) or isinstance(i, str):
                    result_row.append(i)
                else:
                    if np.isnan(i):
                        result_row.append(None)
                    else:
                        result_row.append(int(i))
            c.execute(
                f'insert into tb_menu({", ".join(common.tb_menu_col_name)}) values ({",".join(temp_question_list)})',
                result_row)
        self.conn.commit()
        self.end_conn()

    def delete_row_menu_table(self):
        self.start_conn()
        self.conn: sqlite3.Connection
        c = self.conn.cursor()
        c.execute(f'delete from tb_menu')
        self.conn.commit()
        self.end_conn()

    def insert_menu_detail_value(self):
        self.start_conn()
        df = pd.read_excel('excel_source/table_menu_detail.xlsx', engine='openpyxl')
        self.conn: sqlite3.Connection
        c = self.conn.cursor()
        for row in df.values:
            row: pd.Series
            result_row = list()
            temp_question_list = ['?' for _ in range(20)]
            for i in row:
                if isinstance(i, float):
                    result_row.append(None)
                else:
                    result_row.append(i)
            c.execute(
                f'insert into tb_menu_detail({", ".join(common.tb_menu_detail_col_name)}) values ({",".join(temp_question_list)})',
                result_row)
        self.conn.commit()
        self.end_conn()

    def get_menu_list(self):
        self.start_conn()
        menu_list = list()
        df = pd.read_sql('select * from tb_menu natural join tb_menu_detail', self.conn)
        df.drop(['menu_detail_id'], axis=1, inplace=True)
        for row in df.values:
            converted_data = list()
            for col_data in row:
                if isinstance(col_data, float) and np.isnan(col_data):
                    converted_data.append(None)
                elif isinstance(col_data, float):
                    converted_data.append(int(col_data))
                elif str(col_data).isdigit():
                    converted_data.append(int(col_data))
                else:
                    converted_data.append(col_data)
            menu_list.append(Menu(*converted_data))
        self.end_conn()
        return menu_list

    def get_ordinary_price_by_menu_id(self, menu_id):
        c = self.start_conn()
        result_price = c.execute('select ordinary_price from tb_menu where menu_id = (?)', (menu_id,)).fetchone()[0]
        self.end_conn()
        return result_price

    def get_menu_name_by_menu_id(self, menu_id):
        c = self.start_conn()
        result_name = c.execute('select name from tb_menu where menu_id = (?)', (menu_id,)).fetchone()[0]
        self.end_conn()
        return result_name

    # 주문번호 4자리 구하기
    def get_order_number(self, now_datetime):
        c = self.start_conn()
        date, time = now_datetime.split(' ')
        today_date = date
        statement = f'''select count(order_id) from tb_order where order_date like (?) || '%' '''
        result = c.execute(statement, (today_date,)).fetchone()[0]

        if result != 0:
            result_order_num = \
                int(c.execute('''select order_number from tb_order where order_date 
                like (?) || '%' order by order_number desc limit 1''',
                              (today_date,)).fetchone()[0]) + 1
        else:
            result_order_num = 1
        self.end_conn()
        return f'{result_order_num:04d}'

    def is_serving_lunch_set(self, menu_id):
        c = self.start_conn()
        result_bool = c.execute('select is_lunch_menu from tb_menu where menu_id = (?)', (menu_id,)).fetchone()[0]
        self.end_conn()
        if result_bool == 1:
            return True
        else:
            return False

    def commit_db(self):
        self.conn.commit()


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)

    connector = KioskDBConnector()
    df = connector.get_menu_list()

    # connector.insert_menu_value()
    # connector.delete_row_menu_table()
    # connector.insert_menu_detail_value()
