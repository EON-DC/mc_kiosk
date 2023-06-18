import datetime
import sqlite3

import pandas as pd

tb_menu_col_name = ['name', 'menu_id', 'classification_id', 'marketing_priority', 'is_mcmorning_service',
                    'is_ordinary_service', 'is_lunch_menu', 'is_happy_snack', 'is_new_menu', 'is_asked_additional_side',
                    'is_asked_additional_beverage', 'is_asked_happy_meal', 'is_asked_set_service', 'has_combo_service',
                    'set_order_can_it_order_side_menu', 'set_order_can_it_order_beverage', 'has_size_distribution',
                    'ordinary_price', 'set_price', 'lunch_price', 'combo_price', 'ordinary_size_detail',
                    'happy_snack_price', 'happy_snack_size_detail', 'small_price', 'small_size_detail', 'medium_price',
                    'medium_size_detail', 'large_price', 'large_size_detail', 'additional_price', 'basic_img_path',
                    'set_img_path', 'combo_img_path', 'menu_detail_id']

tb_menu_detail_col_name = ['menu_detail_id', 'description', 'weight', 'volume', 'calory',
                           'glucose', 'protein', 'lipid', 'natrium', 'caffeine', 'level_1', 'level_2',
                           'level_3', 'level_4', 'level_5', 'level_6', 'level_7', 'level_8',
                           'allergy_info', 'country_info']

tb_order_col_name = ['order_id', 'order_date', 'location_id', 'order_status_id',
                     'qr_code_id', 'order_number', 'total_price']


def is_morning(input_datetime=None):
    if input_datetime is None:
        now_time = datetime.datetime.now()
    else:
        now_time = input_datetime
    if (now_time.hour == 4 and now_time.minute >= 30) or (5 <= now_time.hour <= 9) or (
            now_time.hour == 10 and now_time.minute < 30):
        return True
    else:
        return False


def is_lunch(input_datetime=None):
    if input_datetime is None:
        now_time = datetime.datetime.now()
    else:
        now_time = input_datetime
    if (now_time.hour == 10 and now_time.minute >= 30) or (11 <= now_time.hour <= 13) or (
            now_time.hour == 14 and now_time.minute < 30):
        return True
    else:
        return False


if __name__ == '__main__':
    # conn = sqlite3.connect('mac_db.db')
    # df = pd.read_sql('select * from tb_order', conn)
    # print(df.columns)
    print(','.join(tb_order_col_name))
    pass
