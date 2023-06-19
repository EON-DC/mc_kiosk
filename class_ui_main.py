import datetime

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

import common
from class_basket import Basket
from class_controller import KioskController
from class_ui_modal import ModalFinish, ListConfirmItem
from ui_kiosk import Ui_MainWidget
from class_carusel import Carusel
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class MainWindow(QtWidgets.QWidget, Ui_MainWidget):
    def __init__(self, controller):
        assert isinstance(controller, KioskController)
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.ad_pixmap_list = self._get_pixmap_ad_list()
        self.ad_index = 0
        self.menu_list = self._set_menu_list()
        self._set_standby_initial()
        self.ad_timer = self._init_timer()
        self.banners = self._get_banners()
        self.qmovie_card_insert_gif = None
        self._adjustment_style_detail()
        self.menu_img_dict = self._set_pixmap_list()
        # self.menu_carusel_dict = self._set_carusel_dict()
        self._set_btn_triggered()
        self.yellow_under_lines = self._get_yellow_underlines()
        self._banner_click_event(0)  # 주문하기 버튼이 눌렸을 때 홈화면으로 셋팅되게함
        self.now_basket = None
        self.now_option_list = None
        self.widget_carusel_menu_list = self._grouping_carusel_widget()
        self._initialize_select_menu_page_carusel()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # self.burger_carusel_list, self.coffee_carusel_list = self._set_burger_and_coffee_carusel_list()
        self._reset_gui_and_attributes_before_get_orders()

    def _reset_gui_and_attributes_before_get_orders(self):
        self.btn_confirm_order.setStyleSheet(f"background-color:white")

        self.stackedWidget_carusel_menu_burger.setCurrentIndex(0)
        self.stackedWidget_carusel_menu_coffee.setCurrentIndex(0)

        self._refresh_cart_count_and_total_price()

    # def _set_burger_and_coffee_carusel_list(self):
    #     burger_list = list()
    #     coffee_list = list()
    #
    #     for carusel in self.menu_carusel_dict.values():
    #         carusel: Carusel
    #         if carusel.menu_info.classification_id == 1:
    #             burger_list.append(carusel)
    #         elif carusel.menu_info.classification_id == 5:
    #             coffee_list.append(carusel)
    #
    #     return burger_list, coffee_list

    # 배너 그룹핑
    def _get_banners(self):
        result_list = list()
        result_list.append(self.widget_banner_1_home)
        result_list.append(self.widget_banner_2_recommend)
        result_list.append(self.widget_banner_3_burger)
        result_list.append(self.widget_banner_4_happy_snack)
        result_list.append(self.widget_banner_5_side)
        result_list.append(self.widget_banner_6_coffee)
        result_list.append(self.widget_banner_7_dessert)
        result_list.append(self.widget_banner_8_beverage)
        result_list.append(self.widget_banner_9_happymeal)
        return result_list

    # todo: 배너가 클릭되었을 때, 노랑색 밑줄이 그어지게 만드는 것
    def _get_yellow_underlines(self):
        result_list = list()
        result_list.append(self.frame_line_1)
        result_list.append(self.frame_line_2)
        result_list.append(self.frame_line_3)
        result_list.append(self.frame_line_4)
        result_list.append(self.frame_line_5)
        result_list.append(self.frame_line_6)
        result_list.append(self.frame_line_7)
        result_list.append(self.frame_line_8)
        result_list.append(self.frame_line_9)
        return result_list

    def _set_turn_off_banner_yellow_underline(self):
        for line in self.yellow_under_lines:
            line.hide()

    def _set_turn_on_banner_yellow_underline(self, index):
        self._set_turn_off_banner_yellow_underline()
        self.yellow_under_lines[index].show()

    def _set_pixmap_list(self):
        file_name_list = os.listdir('src/')
        menu_png_dict = dict()
        for file_name in file_name_list:
            if file_name.startswith('0') or file_name.startswith('1'):
                menu_png_dict.update({f'{file_name[:3]}': QPixmap(f'src/{file_name}')})
        return menu_png_dict

    def _set_menu_list(self):
        return self.controller.get_menu_data()

    # def _set_carusel_dict(self):
    #     carusel_dict = dict()
    #     # carusel 만들기
    #     for menu in self.menu_list:
    #         if menu.basic_img_path is not None:
    #             carusel_dict.update(
    #                 {f'{menu.menu_id:03d}': Carusel(self, self.menu_img_dict, menu)})
    #
    #     return carusel_dict

    def add_basket_menu(self, menu_id, option_list):
        self.now_basket: Basket
        self.btn_confirm_order.setStyleSheet(f"background-color:{common.yellow}")
        self.now_basket.add_item(menu_id, option_list)
        self._refresh_cart_count_and_total_price()
        print(self.now_basket)

    def _refresh_cart_count_and_total_price(self):
        self.now_basket: Basket
        if self.now_basket is None:
            self.label_item_count_footer.setText('0')
            self.label_total_price_footer.setText('￦0')
        else:
            self.label_item_count_footer.setText(f'{len(self.now_basket.menu_id_list)}')
            self.label_total_price_footer.setText(f'￦{sum(self.now_basket.price_list):,d}')

    def _refresh_confirm_page(self):
        self.label_small_price.setText(f'{self.now_basket.get_total_price()}')
        self.label_total_price.setText(f'{self.now_basket.get_total_price()}')
        # 아이템 리스트 추가하는 로직
        v_layout = QtWidgets.QVBoxLayout(self.widget_confrim_item_area)
        self.widget_confrim_item_area.setLayout(v_layout)
        idx = 0
        menu_id_list, option_list, price_list = self.now_basket.get_basket_as_zip()
        for menu_id, option, price in zip(menu_id_list, option_list, price_list):
            v_layout.addWidget(
                ListConfirmItem(self, self.menu_list[menu_id - 1], self.menu_img_dict, self.menu_list, option, price,
                                idx))
            idx += 1

    def _grouping_carusel_widget(self):
        widget_list = list()
        widget_list.append(self.widget_carusel_menu_1)
        widget_list.append(self.widget_carusel_menu_2)
        widget_list.append(self.widget_carusel_menu_3)
        widget_list.append(self.widget_carusel_menu_4)
        widget_list.append(self.widget_carusel_menu_5)
        widget_list.append(self.widget_carusel_menu_6)
        widget_list.append(self.widget_carusel_menu_7)
        widget_list.append(self.widget_carusel_menu_8)
        widget_list.append(self.widget_carusel_menu_9)
        for i in widget_list:
            grid_layout = QtWidgets.QGridLayout(i)
            grid_layout.setContentsMargins(0, 0, 0, 0)
            i.setLayout(grid_layout)

        # 카테고리 선택버튼내 스택위젯도 grid_layout 추가
        sub_widget_list = list()
        sub_widget_list.append(self.page_beef)
        sub_widget_list.append(self.page_chicken)
        sub_widget_list.append(self.page_seafood)
        sub_widget_list.append(self.page_pork)
        sub_widget_list.append(self.page_icecream)
        sub_widget_list.append(self.page_mccafe)
        sub_widget_list.append(self.page_others)
        for i in sub_widget_list:
            grid_layout = QtWidgets.QGridLayout(i)
            grid_layout.setContentsMargins(0, 0, 0, 0)
            i.setLayout(grid_layout)

        return widget_list

    def _initialize_select_menu_page_carusel(self):
        # 추천 메뉴
        if common.is_morning():
            page_1_menu_id_list = [21, 24, 26, 40, 52, 69]
        else:
            page_1_menu_id_list = [5, 6, 3, 40, 52, 69]
        self._set_menu_carusel_on_select_page(1, page_1_menu_id_list)
        # 추천 메뉴 더 다양
        if common.is_morning():
            page_2_menu_id_list = [x.menu_id for x in self.menu_list if
                                   x.marketing_priority == 1 and x.is_mcmorning_service == 1]
        else:
            page_2_menu_id_list = [x.menu_id for x in self.menu_list if
                                   x.marketing_priority == 1 and x.is_mcmorning_service != 1]

        self._set_menu_carusel_on_select_page(2, page_2_menu_id_list)
        # 버거 메뉴
        page_3_menu_id_list = [x.menu_id for x in self.menu_list if x.classification_id == 1]
        if common.is_morning():
            self.label_home_1_title_3.hide()
            self.btn_group_body.hide()
            page_3_menu_id_list = [x.menu_id for x in self.menu_list if x.classification_id == 2]
        self._set_menu_carusel_on_select_page(3, page_3_menu_id_list)
        # 해피스낵 메뉴
        if common.is_morning():
            page_4_menu_id_list = [x.menu_id for x in self.menu_list if x.is_happy_snack == 1
                                   and x.is_mcmorning_service == 1]
        else:
            page_4_menu_id_list = [x.menu_id for x in self.menu_list if x.is_happy_snack == 1
                                   and x.is_mcmorning_service != 1]
        self._set_menu_carusel_on_select_page(4, page_4_menu_id_list)
        # 사이드 메뉴
        page_5_menu_id_list = [x.menu_id for x in self.menu_list if x.classification_id == 3]
        self._set_menu_carusel_on_select_page(5, page_5_menu_id_list)
        # 커피 메뉴
        page_6_menu_id_list = [x.menu_id for x in self.menu_list if x.classification_id == 5]
        self._set_menu_carusel_on_select_page(6, page_6_menu_id_list)
        # 디저트
        page_7_menu_id_list = [x.menu_id for x in self.menu_list if x.classification_id == 4]
        self._set_menu_carusel_on_select_page(7, page_7_menu_id_list)
        # 음료
        page_8_menu_id_list = [x.menu_id for x in self.menu_list if x.classification_id == 6]
        page_8_menu_id_list.remove(72)  # 오렌지주스는 개별 구매 불가
        self._set_menu_carusel_on_select_page(8, page_8_menu_id_list)
        # 해피밀
        if common.is_morning():
            page_9_menu_id_list = [21, 24]
        else:
            page_9_menu_id_list = [x.menu_id for x in self.menu_list if
                                   x.is_asked_happy_meal == 1 and x.classification_id == 1]
        self._set_menu_carusel_on_select_page(9, page_9_menu_id_list)

        # 버거 - 비프
        page_beef_id_list = [3, 4, 5, 9, 16, 17, 18, 19, 20]
        self._set_menu_carusel_on_selected_origin_page(self.page_beef, page_beef_id_list)

        # 버거 - 치킨
        page_chicken_id_list = [1, 2, 6, 7, 8, 10, 11]
        self._set_menu_carusel_on_selected_origin_page(self.page_chicken, page_chicken_id_list)
        self.page_chicken.setMinimumHeight(480)
        self.page_chicken.setMaximumHeight(480)

        # 버거 - 씨푸드
        page_seafood_id_list = [15, 16]
        self._set_menu_carusel_on_selected_origin_page(self.page_seafood, page_seafood_id_list)

        # 버거 - 불고기
        page_pork_id_list = [12, 13, 14]
        self._set_menu_carusel_on_selected_origin_page(self.page_pork, page_pork_id_list)

        # 맥카페 - 아이스크림
        page_icecream_id_list = list(range(43, 49))
        self._set_menu_carusel_on_selected_origin_page(self.page_icecream, page_icecream_id_list)

        # 맥카페 - 맥카페
        page_mccafe_id_list = list(range(51, 65))
        self._set_menu_carusel_on_selected_origin_page(self.page_mccafe, page_mccafe_id_list)

        # 맥카페 - 그 외
        page_others_id_list = [49, 50]
        self._set_menu_carusel_on_selected_origin_page(self.page_others, page_others_id_list)

    def _set_menu_carusel_on_selected_origin_page(self, page_widget, menu_id_list):
        recommend_menu_list = menu_id_list
        while len(recommend_menu_list) < 3:
            recommend_menu_list.append(999)

        total_row = len(recommend_menu_list) // 3
        row_index = 0
        col_index = 0

        add_height = total_row * 165
        selected_widget = page_widget
        selected_widget.setMinimumHeight(add_height)
        selected_widget.setMaximumHeight(add_height)

        for idx in recommend_menu_list:
            if idx == 999:
                blank_label = QtWidgets.QLabel(self)
                blank_label.setMaximumSize(110, 160)
                blank_label.setMinimumSize(110, 160)
                blank_label.setStyleSheet('background:transparent;')
                page_widget.layout().addWidget(blank_label, row_index, col_index)
            else:
                page_widget.layout().addWidget(
                    Carusel(self, self.menu_img_dict, self.menu_list[idx - 1], self.menu_list),
                    row_index, col_index)
            col_index += 1
            if col_index % 3 == 0:
                col_index = 0
                row_index += 1

    def _set_menu_carusel_on_select_page(self, page_number, menu_id_list):
        recommend_menu_list = menu_id_list
        while len(recommend_menu_list) < 3:
            recommend_menu_list.append(999)

        total_row = len(recommend_menu_list) // 3
        row_index = 0
        col_index = 0

        add_height = total_row * 165
        selected_widget = self.widget_carusel_menu_list[page_number - 1]
        selected_widget.setMinimumHeight(add_height)
        selected_widget.setMaximumHeight(add_height)

        if page_number in [6, 8]:
            selected_widget.setMinimumHeight(add_height + 200)
            selected_widget.setMaximumHeight(add_height + 200)
        if page_number == 3 and common.is_morning():
            selected_widget.setMinimumHeight(add_height + 200)
            selected_widget.setMaximumHeight(add_height + 200)

        for idx in recommend_menu_list:
            if idx == 999:
                blank_label = QtWidgets.QLabel(self)
                blank_label.setMaximumSize(110, 160)
                blank_label.setMinimumSize(110, 160)
                blank_label.setStyleSheet('background:transparent;')
                self.widget_carusel_menu_list[page_number - 1].layout().addWidget(
                    blank_label, row_index, col_index)
            else:
                self.widget_carusel_menu_list[page_number - 1].layout().addWidget(
                    Carusel(self, self.menu_img_dict, self.menu_list[idx - 1], self.menu_list),
                    row_index, col_index)
            col_index += 1
            if col_index % 3 == 0:
                col_index = 0
                row_index += 1

    def _showing_selected_menu(self, category_str):
        result_list = list()
        if category_str == '전체':
            self.stackedWidget_carusel_menu_burger.setCurrentIndex(0)
            self.stackedWidget_carusel_menu_coffee.setCurrentIndex(0)
        elif category_str == '비프':
            self.stackedWidget_carusel_menu_burger.setCurrentIndex(1)
        elif category_str == '치킨':
            self.stackedWidget_carusel_menu_burger.setCurrentIndex(2)
        elif category_str == '씨푸드':
            self.stackedWidget_carusel_menu_burger.setCurrentIndex(3)
        elif category_str == '불고기':
            self.stackedWidget_carusel_menu_burger.setCurrentIndex(4)
        elif category_str == '아이스크림':
            self.stackedWidget_carusel_menu_coffee.setCurrentIndex(1)
        elif category_str == '커피':
            self.stackedWidget_carusel_menu_coffee.setCurrentIndex(2)
        elif category_str == '그 외':
            self.stackedWidget_carusel_menu_coffee.setCurrentIndex(3)

    def _adjustment_style_detail(self):
        # 메뉴 선택 화면
        self.label_logo.setMargin(20)
        now_time = datetime.datetime.now()
        if not common.is_morning(now_time):
            self.btn_season_ad_1.setStyleSheet(f'QPushButton {{ background-image: url(src/season_ad_1.png); }}')
            self.btn_season_ad_2.setStyleSheet(f'QPushButton {{ background-image: url(src/season_ad_2.png); }}')
        else:
            self.btn_season_ad_1.setStyleSheet(f'QPushButton {{ background-image: url(src/season_ad_3.png); }}')
            self.btn_season_ad_2.setStyleSheet(f'QPushButton {{ background-image: url(src/season_ad_4.png); }}')

        # 식사방법 버튼 이미지
        self.btn_restaurant.setStyleSheet(f'''
            QPushButton {{ 
                background-image: url(src/background_restaurant.png);
                font: 12pt;}}
            QPushButton:Pressed{{
                font: 16pt;
            }}''')
        self.btn_take_out.setStyleSheet(f'''
            QPushButton {{ 
                background-image: url(src/background_bag.png);
                font: 12pt;}}
            QPushButton:Pressed{{
                font: 16pt;
            }}''')

        # gif 설정
        self.qmovie_card_insert_gif = QtGui.QMovie('src/insert_card.gif')
        self.label_card_insert_gif.setMovie(self.qmovie_card_insert_gif)

    def _init_timer(self):
        ad_timer = QtCore.QTimer()
        ad_timer.setInterval(3000)
        ad_timer.timeout.connect(self._change_ad_page)
        ad_timer.start()
        return ad_timer

    def _selected_eat_way(self, way_str):
        # 장바구니 객체 만들기
        self.now_basket = Basket(self.controller.connector, self.menu_list)
        self.now_basket.set_eat_way(way_str)
        # 메뉴 선택화면으로 전환
        self.main_stacked_widget.setCurrentIndex(2)

    def _go_to_extra_order(self):
        self.main_stacked_widget.setCurrentIndex(2)

    def _go_to_standby_main(self):
        self.now_basket = None
        self.main_stacked_widget.setCurrentIndex(0)

    def _go_select_eat_way(self):
        self._reset_gui_and_attributes_before_get_orders()
        self.main_stacked_widget.setCurrentIndex(1)

    def _go_to_confirm_order(self):
        self.main_stacked_widget.setCurrentIndex(3)
        self._refresh_confirm_page()

    def _go_to_ask_pay_way(self):
        self.main_stacked_widget.setCurrentIndex(4)

    def _pay_way_1_click_and_released_event(self, event):
        self.main_stacked_widget.setCurrentIndex(5)
        self.qmovie_card_insert_gif.start()
        tempTimer = QtCore.QTimer(self)
        tempTimer.singleShot(5000, lambda: self._update_order_on_db())

    def _pay_way_2_click_and_released_event(self, event):
        pass

    def play_video(self, video_path):
        video_url = QtCore.QUrl.fromLocalFile(video_path)
        media_content = QMediaContent(video_url)
        self.media_player.setMedia(media_content)
        self.media_player.play()

    def _update_order_on_db(self):
        self.controller.add_order(self.now_basket)
        end_page = ModalFinish()
        end_page.show()
        self._go_to_standby_main()

    def _set_btn_triggered(self):
        self.btn_take_out.clicked.connect(lambda state: self._selected_eat_way('take_out'))
        self.btn_restaurant.clicked.connect(lambda state: self._selected_eat_way('restaurant'))
        self.btn_order_start.clicked.connect(lambda state: self._go_select_eat_way())
        self.btn_home_burger.clicked.connect(lambda state: self._banner_click_event(2))
        self.btn_home_coffee.clicked.connect(lambda state: self._banner_click_event(5))
        self.btn_home_recommend.clicked.connect(lambda state: self._banner_click_event(1))
        self.btn_home_happy_snack.clicked.connect(lambda state: self._banner_click_event(3))
        self.btn_season_ad_1.clicked.connect(lambda state: self._banner_click_event(2))
        self.btn_season_ad_2.clicked.connect(lambda state: self._banner_click_event(3))
        self.btn_go_standby.clicked.connect(lambda state: self._go_to_standby_main())
        self.btn_go_standby_2.clicked.connect(lambda state: self._go_to_standby_main())
        self.btn_go_standby_3.clicked.connect(lambda state: self._go_to_standby_main())
        self.btn_go_standby_4.clicked.connect(lambda state: self._go_to_standby_main())
        self.btn_confirm_order.clicked.connect(lambda state: self._go_to_confirm_order())
        self.btn_extra_order.clicked.connect(lambda state: self._go_to_extra_order())
        self.pay_way_1.mouseReleaseEvent = self._pay_way_1_click_and_released_event
        self.pay_way_2.mouseReleaseEvent = self._pay_way_2_click_and_released_event
        self.btn_confirm_complete.clicked.connect(lambda state: self._go_to_ask_pay_way())

        self.btn_whole_burger.clicked.connect(lambda state: self._showing_selected_menu('전체'))
        self.btn_beef_burger.clicked.connect(lambda state: self._showing_selected_menu('비프'))
        self.btn_pig_burger.clicked.connect(lambda state: self._showing_selected_menu('불고기'))
        self.btn_chicken_burger.clicked.connect(lambda state: self._showing_selected_menu('치킨'))
        self.btn_seafood_burger.clicked.connect(lambda state: self._showing_selected_menu('씨푸드'))
        self.btn_whole_coffee.clicked.connect(lambda state: self._showing_selected_menu('전체'))
        self.btn_icecream.clicked.connect(lambda state: self._showing_selected_menu('아이스크림'))
        self.btn_mccafe.clicked.connect(lambda state: self._showing_selected_menu('커피'))
        self.btn_others.clicked.connect(lambda state: self._showing_selected_menu('그 외'))
        for idx, banner in enumerate(self.banners):
            banner.mousePressEvent = lambda e, y=idx: self._banner_click_event(y)

    # 배너가 클릭되었을 떄, body_stacked_widget 인덱스가 바뀌는 것
    def _banner_click_event(self, index):
        self.body_stacked_widget.setCurrentIndex(index)
        self._set_turn_on_banner_yellow_underline(index)

    def _change_ad_page(self):
        ad_length = len(self.ad_pixmap_list)
        self.ad_index = (self.ad_index + 1) % ad_length
        self.season_ad.setPixmap(self.ad_pixmap_list[self.ad_index])

    def _set_standby_initial(self):
        self.main_stacked_widget.setCurrentIndex(0)
        self._change_ad_page()

    def _get_pixmap_ad_list(self):
        result_list = list()
        src_file_list = os.listdir('src/')
        for file_name in src_file_list:
            if file_name.startswith('ad'):
                result_list.append(QtGui.QPixmap(f'src/{file_name}'))
        return result_list
