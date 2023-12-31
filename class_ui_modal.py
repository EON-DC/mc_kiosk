from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

import common
from class_carusel_option import CaruselOption
from class_menu import Menu
from ui_nutrition_form import Ui_NutritionForm
from ui_pay_finish import Ui_Modal_finish
from ui_set_option_modal import Ui_Modal_set_option
from ui_widget_list_item import Ui_WidgetConfirmItem


class ModalFinish(QtWidgets.QWidget, Ui_Modal_finish):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.timer = QtCore.QTimer(self)
        self.timer.singleShot(2000, lambda: self.close())


class ModalNutrition(QtWidgets.QWidget, Ui_NutritionForm):
    def __init__(self, grand_parent, parent, menu_info, pixmap_dict, total_menu_list):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(50, 230, 500, 500)
        self.grand_parent = grand_parent
        self.parent = parent
        self.menu_info = menu_info
        self.pixmap_dict = pixmap_dict
        self.total_menu_list = total_menu_list
        self.setStyleSheet(self.grand_parent.styleSheet())
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(lambda state: self.close())
        self.widget.setStyleSheet('background-color: white;')

    def show(self):
        self._reset_labels()
        super().show()

    def _reset_labels(self):
        self.label_table_header_11.setText(f'{self.menu_info.weight}')
        self.label_table_header_12.setText(f'{self.menu_info.volume}')
        self.label_table_header_13.setText(f'{self.menu_info.calory}')
        self.label_table_header_14.setText(f'{self.menu_info.glucose}')
        self.label_table_header_15.setText(f'{self.menu_info.protein}')
        self.label_table_header_16.setText(f'{self.menu_info.lipid}')
        self.label_table_header_17.setText(f'{self.menu_info.natrium}')
        self.label_table_header_18.setText(f'{self.menu_info.caffeine}')
        self.label_table_header_20.setText(f'{self.menu_info.level_1}')
        self.label_table_header_21.setText(f'{self.menu_info.level_2}')
        self.label_table_header_22.setText(f'{self.menu_info.level_3}')
        self.label_table_header_23.setText(f'{self.menu_info.level_4}')
        self.label_table_header_24.setText(f'{self.menu_info.level_5}')
        self.label_table_header_25.setText(f'{self.menu_info.level_6}')
        self.label_table_header_26.setText(f'{self.menu_info.level_7}')
        self.label_table_header_27.setText(f'{self.menu_info.level_8}')
        self.label_allergy_info.setText(f'{self.menu_info.allergy_info}')
        self.label_food_origin_info.setText(f'{self.menu_info.country_info}')


class ListConfirmItem(QtWidgets.QWidget, Ui_WidgetConfirmItem):
    def __init__(self, parent, menu_info, pixmap_dict, total_menu_list, option, price, row_index):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.menu_info = menu_info
        self.pixmap_dict = pixmap_dict
        self.total_menu_list = total_menu_list
        self.option = option
        self.price = price
        self.item_row_index = row_index
        self._initialize_labels()
        self._set_btn_triggered()

    def _initialize_labels(self):
        self.label_option_list.hide()
        self.btn_detail_menu_info.hide()
        title = f"""{self.menu_info.name}"""
        if 'large' in self.option:
            title = title + ' 라지'
        if 'set' in self.option:
            self.label_option_list.show()
            self.btn_detail_menu_info.show()
            title = title + '세트'

            option_info = list()
            if isinstance(self.option[-2], str) and self.option[-2].isdigit():
                side_menu_id = int(self.option[-2])
                option_info.append(f'{self.total_menu_list[side_menu_id - 1].name}')
            if isinstance(self.option[-1], str) and self.option[-1].isdigit():
                beverage_menu_id = int(self.option[-1])
                option_info.append(f'{self.total_menu_list[beverage_menu_id - 1].name}')
            self.label_option_list.setText(','.join(option_info))
            self.label_img.setPixmap(self.pixmap_dict[self.menu_info.get_set_img_path()])
        else:
            if self.menu_info.classification_id == 1:
                title = title + '버거 단품'
            else:
                title = title + '\n'
            self.label_img.setPixmap(self.pixmap_dict[self.menu_info.get_basic_img_path()])
        title = title + f' {self.menu_info.get_calories()}'
        self.label_menu_name_and_calories.setText(title)

        self.label_price.setText(f'￦{self.price:,d}')

        # stepper 초기화
        self.label_item_count.setText(f'{self.option[0]}')  # menu count
        # 1과 같아지면 버튼 비활성화
        if self.option[0] <= 1:
            self.btn_minus.setEnabled(False)
            self.btn_minus.setStyleSheet('background-color:#e3e3e3')
        # 2, 9부터는 둘다 활성화
        if self.option[0] == 2 or self.option[0] == 9:
            self.btn_minus.setEnabled(True)
            self.btn_minus.setStyleSheet('background-color:white')
            self.btn_plus.setEnabled(True)
            self.btn_plus.setStyleSheet('background-color:white')
        # 10과 같아지면 버튼 비활성화
        if self.option[0] >= 10:
            self.btn_plus.setEnabled(False)
            self.btn_plus.setStyleSheet('background-color:#e3e3e3')

    def _set_btn_triggered(self):
        self.btn_delete.clicked.connect(lambda state: self._delete_row())
        self.btn_plus.clicked.connect(lambda state: self._stepper_add(1))
        self.btn_minus.clicked.connect(lambda state: self._stepper_add(-1))

    def _stepper_add(self, value):
        if self.parent.is_refractory_period is True:
            return
        label_counter = self.label_item_count
        int_value = int(label_counter.text())
        int_value += value

        label_counter.setText(str(int_value))

        if value == -1:
            self.parent.update_stepper_value_btn_minus(self.item_row_index)
        elif value == 1:
            self.parent.update_stepper_value_btn_plus(self.item_row_index)
        self.parent.set_refractory_period()

    def _delete_row(self):
        self.parent.delete_basket_item(self.item_row_index)


class ModalOption(QtWidgets.QWidget, Ui_Modal_set_option):
    def __init__(self, parent, menu_info, pixmap_dict, total_menu_list):
        assert isinstance(menu_info, Menu)
        super().__init__()
        self.setupUi(self)
        self.setGeometry(30, 30, 540, 960)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.parent = parent
        self.menu_info = menu_info
        self.pixmap_dict = pixmap_dict
        self.total_menu_list = total_menu_list
        self.banner_list = self._set_banner_groups()
        self.now_index = 0
        self._option_list = None
        self._reset_option_list()
        self._config_labels()
        self._set_btn_triggered()
        self._stepper_add(self.label_item_count_1, 0)
        self.parent.set_enable_button()
        self._stepper_add(self.label_item_count_2, 0)
        self._initialize_widget_select_area()
        self._hide_banners()
        self._showing_banners(0)
        self.nutrition_modal = None

    def _reset_option_list(self):
        self._option_list = list()
        self._option_list.append(1)  # 기본 수량 1부터 시작하게함
        # stepper 초기화
        self.btn_minus_1.setStyleSheet('background-color:#e3e3e3')
        self.btn_plus_1.setStyleSheet('background-color:white')
        self.btn_minus_2.setStyleSheet('background-color:#e3e3e3')
        self.btn_plus_2.setStyleSheet('background-color:white')
        self.label_item_count_1.setText('1')
        self.label_item_count_2.setText('1')

    def _initialize_widget_select_area(self):
        grid_layout_1 = QtWidgets.QGridLayout(self.widget_select_area_1)
        grid_layout_1.setContentsMargins(0, 0, 0, 0)
        self.widget_select_area_1.setLayout(grid_layout_1)
        grid_layout_1.addWidget(CaruselOption(self, self.pixmap_dict, self.menu_info, ['medium', 'set']), 0, 0)
        grid_layout_1.addWidget(CaruselOption(self, self.pixmap_dict, self.menu_info, ['large', 'set']), 0, 1)
        blank_label = QtWidgets.QLabel(self)
        blank_label.setMaximumSize(110, 160)
        blank_label.setMinimumSize(110, 160)
        blank_label.setStyleSheet('background:transparent;')
        grid_layout_1.addWidget(blank_label, 0, 2)

        grid_layout_2 = QtWidgets.QGridLayout(self.widget_select_area_2)
        grid_layout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_select_area_2.setLayout(grid_layout_2)
        side_menu_info_list = [x for x in self.total_menu_list if x.is_asked_additional_side == 1]
        side_page_row = 0
        side_page_col = 0

        for side_menu_info in side_menu_info_list:
            grid_layout_2.addWidget(CaruselOption(self, self.pixmap_dict, side_menu_info, f'{side_menu_info.menu_id}')
                                    , side_page_row, side_page_col)
            side_page_col += 1
            if side_page_col == 3:
                side_page_row += 1
                side_page_col = 0

        grid_layout_3 = QtWidgets.QGridLayout(self.widget_select_area_3)
        grid_layout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_select_area_3.setLayout(grid_layout_3)
        beverage_menu_info_list = [x for x in self.total_menu_list if x.is_asked_additional_beverage == 1]
        beverage_page_row = 0
        beverage_page_col = 0
        beverage_total_row = len(beverage_menu_info_list) // 3
        self.widget_select_area_3.setMinimumHeight(170 * beverage_total_row)
        self.widget_select_area_3.setMaximumHeight(170 * beverage_total_row)

        for beverage_menu_info in beverage_menu_info_list:
            grid_layout_3.addWidget(
                CaruselOption(self, self.pixmap_dict, beverage_menu_info, f'{beverage_menu_info.menu_id}')
                , beverage_page_row, beverage_page_col)
            beverage_page_col += 1
            if beverage_page_col == 3:
                beverage_page_row += 1
                beverage_page_col = 0

    def _set_banner_groups(self):
        result_list = list()
        result_list.append(self.banner_1)
        result_list.append(self.banner_2)
        result_list.append(self.banner_3)
        result_list.append(self.banner_4)
        return result_list

    def _hide_banners(self):
        for banner in self.banner_list:
            banner.hide()

    def _showing_banners(self, step_index):
        for i in range(step_index + 1):
            self.banner_list[i].show()

    def _refresh_title_name_label(self):
        # 세부 상단 메뉴 이름
        option = None
        if self._option_list is not None:
            option = self._option_list
        quantity = int(self.label_item_count_2.text())
        title_info = f'''{self.menu_info.name}\n￦{self.menu_info.now_price(option) * quantity:,d} {common.calories_handler(self.menu_info.get_calories()) * quantity:,}kcal'''
        self.label_menu_name_header_name_1.setText(title_info)
        self.label_menu_name_header_name_2.setText(title_info)
        self.label_menu_name_header_name_3.setText(title_info)
        self.label_menu_name_header_name_4.setText(title_info)
        self.label_menu_title.setText(title_info)
        # self.label_menu_title_2.setText(title_info)

        if self.now_index == 0:
            self.label_banner_1.setText('세트 크기 선택')

        elif self.now_index == 1:
            if 'large' in self._option_list:
                self.label_banner_1.setText(f'{self.menu_info.name}-라지')
            else:
                self.label_banner_1.setText(f'{self.menu_info.name}')
            self.label_banner_2.setText('사이드 선택')

        elif self.now_index == 2:
            self.label_banner_2.setText(f'{self.total_menu_list[int(self._option_list[-1]) - 1].name}')
            self.label_banner_3.setText(f'음료 선택')
        elif self.now_index == 3:
            self.label_banner_3.setText(f'{self.total_menu_list[int(self._option_list[-1]) - 1].name}')

    def _config_labels(self):
        self.label_menu_name.setText(self.menu_info.name)
        self._refresh_title_name_label()

        # 이미지 넣기
        self.label_info.hide()
        if self.menu_info.is_new_menu:
            self.label_info.show()
        elif self.menu_info.is_happy_snack:
            self.label_info.setText("해피스낵")
            self.label_info.show()
        self.label_item_img.setPixmap(self.pixmap_dict[f'{self.menu_info.basic_img_path:03d}'])

        self.label_selected_burger.setPixmap(self.pixmap_dict[f'{self.menu_info.basic_img_path:03d}'])

        # 세트 or 단품
        self.label_info_set.setText('세트 선택')
        self.label_info_single.setText(f'단품 선택\n{self.menu_info.now_price(None):,d}원 {self.menu_info.get_calories()}')
        self.label_set_image.setPixmap(self.pixmap_dict[self.menu_info.get_set_img_path()])
        self.label_single_image.setPixmap(self.pixmap_dict[self.menu_info.get_basic_img_path()])

        # 메뉴 조합 배경 설정
        self.widget_combination_image.setStyleSheet(f"""
            #widget_combination_image {{
               background-image: url(src/background_logo.png);   
            }}""")

        # 배너 글씨는 O으로 초기화
        self.label_banner_1.setText('○')
        self.label_banner_2.setText('○')
        self.label_banner_3.setText('○')
        self.label_banner_4.setText('○')
        self.label_banner_1.setText('○')

    def _set_carusel_into_option_set(self):
        grid_layout_1 = QtWidgets.QGridLayout(self.widget_select_area_1)
        self.widget_select_area_1.setLayout(grid_layout_1)

    def _set_btn_triggered(self):
        self.btn_cancel_1.clicked.connect(lambda state: self.close())
        self.btn_cancel_2.clicked.connect(lambda state: self.close())
        self.btn_plus_1.clicked.connect(lambda state: self._stepper_add(self.label_item_count_1, 1))
        self.btn_plus_2.clicked.connect(lambda state: self._stepper_add(self.label_item_count_2, 1))
        self.btn_minus_1.clicked.connect(lambda state: self._stepper_add(self.label_item_count_1, -1))
        self.btn_minus_2.clicked.connect(lambda state: self._stepper_add(self.label_item_count_2, -1))
        self.btn_go_standby_1.clicked.connect(lambda state: self._go_to_standby())
        self.btn_go_standby_2.clicked.connect(lambda state: self._go_to_standby())
        self.btn_go_standby_3.clicked.connect(lambda state: self._go_to_standby())

        self.widget_left.mousePressEvent = self.left_widget_click_event
        self.widget_left.mouseReleaseEvent = self.left_widget_release_event
        self.widget_right.mousePressEvent = self.right_widget_click_event
        self.widget_right.mouseReleaseEvent = self.right_widget_release_event
        self.btn_add_basket_option.clicked.connect(lambda state: self._apply_quantity_and_add_item_on_basket('set'))
        self.btn_add_basket_count.clicked.connect(lambda state: self._apply_quantity_and_add_item_on_basket('single'))
        self.btn_nutrition_set.clicked.connect(lambda state: self.make_nutrition_info_modal())
        self.btn_nutrition_count.clicked.connect(lambda state: self.make_nutrition_info_modal())

    def make_nutrition_info_modal(self):
        if self.nutrition_modal is None:
            self.nutrition_modal = ModalNutrition(self.parent, self, self.menu_info, self.pixmap_dict,
                                                  self.total_menu_list)
            self.parent.add_opened_modal(self.nutrition_modal)
        else:
            self.nutrition_modal.menu_info = self.menu_info
        self.nutrition_modal.show()

    def _apply_quantity_and_add_item_on_basket(self, from_page):
        quantity = 0
        menu_id = self.menu_info.menu_id
        if from_page == 'set':
            quantity = int(self.label_item_count_2.text())
        elif from_page == 'single':
            quantity = int(self.label_item_count_1.text())

        self._option_list[0] = quantity

        # parent의 basket 리스트에 추가하는 로직
        self.parent.add_basket_menu(menu_id, self._option_list)
        # 모달을 닫는 화면
        self._go_to_select_menu_page()

    def add_option(self, option_info):
        if isinstance(option_info, str):
            self._option_list.append(option_info)
        elif isinstance(option_info, list):
            self._option_list.extend(option_info)
        self.next_step()

    def next_step(self):
        self.now_index = self.body_stacked_widget.currentIndex()

        self._showing_banners(self.now_index)

        self.now_index += 1
        self._refresh_title_name_label()
        if self.now_index == 3:
            self._refresh_combination_page()
            self.stackedWidget.setCurrentIndex(2)
            self._hide_banners()
            self.now_index = 0
        self.body_stacked_widget.setCurrentIndex(self.now_index)

    def _refresh_combination_page(self):
        side_menu_img_path = None
        beverage_menu_img_path = None
        if 'set' in self._option_list:
            side_menu_id = int(self._option_list[-2])
            beverage_menu_id = int(self._option_list[-1])
            side_menu_img_path = self.total_menu_list[side_menu_id - 1].get_basic_img_path()
            beverage_menu_img_path = self.total_menu_list[beverage_menu_id - 1].get_basic_img_path()
        elif 'combo' in self._option_list:
            beverage_menu_id = int(self._option_list[-1])
            beverage_menu_img_path = self.total_menu_list[beverage_menu_id - 1].get_basic_img_path()

        if side_menu_img_path is not None:
            self.label_selected_side.setPixmap(self.pixmap_dict[side_menu_img_path])
        if beverage_menu_img_path is not None:
            self.label_selected_beverage.setPixmap(self.pixmap_dict[beverage_menu_img_path])

    def show(self):
        self._reset_option_list()
        # 단품 vs 세트
        if self.menu_info.is_asked_set_service:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(3)
        super().show()

    def _go_to_standby(self):
        self.parent._go_to_standby_main()
        self.close()

    def _go_to_select_menu_page(self):
        self.parent._ask_recommend_page()
        self.close()

    def _stepper_add(self, label_counter, value):
        if self.parent.is_refractory_period is True:
            return
        int_value = int(label_counter.text())
        int_value += value
        # 1과 같아지면 버튼 비활성화
        if self.label_item_count_1 == label_counter and int_value == 1:
            self.btn_minus_1.setEnabled(False)
            self.btn_minus_1.setStyleSheet('background-color:#e3e3e3')
        elif self.label_item_count_2 == label_counter and int_value == 1:
            self.btn_minus_2.setEnabled(False)
            self.btn_minus_2.setStyleSheet('background-color:#e3e3e3')
        # 2, 9부터는 둘다 활성화
        if self.label_item_count_1 == label_counter and int_value == 2 or int_value == 9:
            self.btn_minus_1.setEnabled(True)
            self.btn_minus_1.setStyleSheet('background-color:white')
            self.btn_plus_1.setEnabled(True)
            self.btn_plus_1.setStyleSheet('background-color:white')
        elif self.label_item_count_2 == label_counter and int_value == 2 or int_value == 9:
            self.btn_minus_2.setEnabled(True)
            self.btn_minus_2.setStyleSheet('background-color:white')
            self.btn_plus_2.setEnabled(True)
            self.btn_plus_2.setStyleSheet('background-color:white')
        # 10과 같아지면 버튼 비활성화
        if self.label_item_count_1 == label_counter and int_value == 10:
            self.btn_plus_1.setEnabled(False)
            self.btn_plus_1.setStyleSheet('background-color:#e3e3e3')
        elif self.label_item_count_2 == label_counter and int_value == 10:
            self.btn_plus_2.setEnabled(False)
            self.btn_plus_2.setStyleSheet('background-color:#e3e3e3')

        label_counter.setText(str(int_value))
        self._refresh_label_on_count_page(label_counter)
        self._refresh_title_name_label()
        self.parent.set_refractory_period()

    def _refresh_label_on_count_page(self, label_counter):
        quantity = int(label_counter.text())
        name = self.menu_info.name
        price = self.menu_info.now_price(self._option_list) * quantity
        calories = common.calories_handler(self.menu_info.get_calories()) * quantity
        self.label_menu_title_2.setText(f"""{name}\n￦{price:,d} {calories:,d}kcal""")

    def left_widget_click_event(self, event):
        self.label_set_image.setMaximumSize(180, 180)
        self.label_set_image.setMinimumSize(180, 180)

    def left_widget_release_event(self, event):
        self.label_set_image.setMaximumSize(150, 150)
        self.label_set_image.setMinimumSize(150, 150)
        self._go_to_set_option()

    def right_widget_click_event(self, event):
        self.label_single_image.setMaximumSize(180, 180)
        self.label_single_image.setMinimumSize(180, 180)

    def right_widget_release_event(self, event):
        self.label_single_image.setMaximumSize(150, 150)
        self.label_single_image.setMinimumSize(150, 150)
        self._go_to_single_option()

    def _go_to_set_option(self):
        # 옵션을 추가할 수 있게 하는 로직
        self.body_stacked_widget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        if common.is_morning():
            self.add_option(['set'])

    def _go_to_single_option(self):
        # 카운트 페이지로 넘어가는 로직
        self.stackedWidget.setCurrentIndex(3)
