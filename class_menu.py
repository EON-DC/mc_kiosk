from common import *


class Menu:
    def __init__(self, name, menu_id, classification_id, marketing_priority, is_mcmorning_service, is_ordinary_service,
                 is_lunch_menu, is_happy_snack, is_new_menu, is_asked_additional_side, is_asked_additional_beverage,
                 is_asked_happy_meal, is_asked_set_service, has_combo_service, set_order_can_it_order_side_menu,
                 set_order_can_it_order_beverage, has_size_distribution, ordinary_price, set_price, lunch_price,
                 combo_price, ordinary_size_detail, happy_snack_price, happy_snack_size_detail, small_price,
                 small_size_detail, medium_price, medium_size_detail, large_price, large_size_detail, additional_price,
                 basic_img_path, set_img_path, combo_img_path, description, weight, volume, calory,
                 glucose, protein, lipid, natrium, caffeine, level_1, level_2, level_3, level_4, level_5, level_6,
                 level_7, level_8, allergy_info, country_info):
        self.name = name
        self.menu_id = menu_id
        self.classification_id = classification_id
        self.marketing_priority = marketing_priority
        self.is_mcmorning_service = is_mcmorning_service
        self.is_ordinary_service = is_ordinary_service
        self.is_lunch_menu = is_lunch_menu
        self.is_happy_snack = is_happy_snack
        self.is_new_menu = is_new_menu
        self.is_asked_additional_side = is_asked_additional_side
        self.is_asked_additional_beverage = is_asked_additional_beverage
        self.is_asked_happy_meal = is_asked_happy_meal
        self.is_asked_set_service = is_asked_set_service
        self.has_combo_service = has_combo_service
        self.set_order_can_it_order_side_menu = set_order_can_it_order_side_menu
        self.set_order_can_it_order_beverage = set_order_can_it_order_beverage
        self.has_size_distribution = has_size_distribution
        self.ordinary_price = ordinary_price
        self.set_price = set_price
        self.lunch_price = lunch_price
        self.combo_price = combo_price
        self.ordinary_size_detail = ordinary_size_detail
        self.happy_snack_price = happy_snack_price
        self.happy_snack_size_detail = happy_snack_size_detail
        self.small_price = small_price
        self.small_size_detail = small_size_detail
        self.medium_price = medium_price
        self.medium_size_detail = medium_size_detail
        self.large_price = large_price
        self.large_size_detail = large_size_detail
        self.additional_price = additional_price
        self.basic_img_path = basic_img_path
        self.set_img_path = set_img_path
        self.combo_img_path = combo_img_path
        self.description = description
        self.weight = weight
        self.volume = volume
        self.calory = calory
        self.glucose = glucose
        self.protein = protein
        self.lipid = lipid
        self.natrium = natrium
        self.caffeine = caffeine
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_4 = level_4
        self.level_5 = level_5
        self.level_6 = level_6
        self.level_7 = level_7
        self.level_8 = level_8
        self.allergy_info = allergy_info
        self.country_info = country_info
        self.is_enable = True

    def __repr__(self):
        return f'{self.menu_id:02d}:{self.name}_객체'

    def get_calories(self):
        if self.calory is None or self.calory == 0:
            return ''
        else:
            return self.calory

    def set_menu_disable(self):
        self.is_enable = False

    def now_price(self, option):
        if is_lunch() and self.is_lunch_menu == 1:
            return self.lunch_price

        if self.is_happy_snack == 1:
            return self.happy_snack_price

        if (isinstance(option, str) and option == 'set') or \
                (isinstance(option, list) and 'set' in option):
            return self.set_price

        if (isinstance(option, str) and option == 'combo') or \
                (isinstance(option, list) and 'combo' in option):
            return self.combo_price

        if (isinstance(option, str) and option == 'small') or \
                (isinstance(option, list) and 'small' in option):
            return self.small_price

        if (isinstance(option, str) and option == 'medium') or \
                (isinstance(option, list) and 'medium' in option):
            return self.medium_price

        if (isinstance(option, str) and option == 'large') or \
                (isinstance(option, list) and 'large' in option):
            return self.large_price

        return self.ordinary_price

    def get_set_img_path(self):
        if self.set_img_path is not None:
            return f"{self.set_img_path:03d}"
        else:
            return f"{self.basic_img_path:03d}"

    def get_combo_img_path(self):
        if self.combo_img_path is not None:
            return f"{self.combo_img_path:03d}"
        else:
            return f"{self.basic_img_path:03d}"

    def get_basic_img_path(self):
        return f"{self.basic_img_path:03d}"
