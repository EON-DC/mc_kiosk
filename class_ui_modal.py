from PyQt5.QtCore import Qt

from class_menu import Menu
from ui_set_option_modal import Ui_Modal_set_option
from ui_pay_finish import Ui_Modal_finish
from PyQt5 import QtCore, QtGui, QtWidgets


class ModalFinish(QtWidgets.QWidget, Ui_Modal_finish):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.timer = QtCore.QTimer(self)
        self.timer.singleShot(2000, lambda: self.close())


class ModalOption(QtWidgets.QWidget, Ui_Modal_set_option):
    def __init__(self, parent, menu_info, pixmap_dict):
        assert isinstance(menu_info, Menu)
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.parent = parent
        self.menu_info = menu_info
        self.pixmap_dict = pixmap_dict
        self._config_labels()
        self._set_click_event()

    def _config_labels(self):
        self.label_menu_name.setText(self.menu_info.name)
        # self.label_info_set.setText('세트 선택')
        # self.label_info_single.setText(f'단품 선택\n{self.menu_info.now_price()}원 {self.menu_info.get_calories()}')



        # 세부 상단 메뉴 이름
        title_info = f'{self.menu_info.name}\n￦{self.menu_info.now_price()} {self.menu_info.get_calories()}'
        self.label_menu_name_header_name_1.setText(title_info)
        self.label_menu_name_header_name_2.setText(title_info)
        self.label_menu_name_header_name_3.setText(title_info)
        self.label_menu_name_header_name_4.setText(title_info)
        self.label_menu_title.setText(title_info)
        self.label_menu_title_2.setText(title_info)

        # stepper 초기화
        self.btn_minus_1.setStyleSheet('background-color:#e3e3e3')
        self.btn_minus_2.setStyleSheet('background-color:#e3e3e3')
        self.label_item_count_1.setText('1')
        self.label_item_count_2.setText('1')
        
        # 이미지 넣기
        self.label_info.hide()
        if self.menu_info.is_new_menu:
            self.label_info.show()
        elif self.menu_info.is_happy_snack:
            self.label_info.setText("해피스낵")
            self.label_info.show()
        self.label_item_img.setPixmap(self.pixmap_dict[f'{self.menu_info.basic_img_path:03d}'])



        # 세트 or 단품
        self.label_info_set.setText('세트 선택')
        self.label_info_single.setText(f'단품 선택\n{self.menu_info.now_price()} {self.menu_info.get_calories()}')
        self.label_set_image.setPixmap(self.pixmap_dict[self.menu_info.get_set_img_path()])
        self.label_single_image.setPixmap(self.pixmap_dict[self.menu_info.get_basic_img_path()])



    def _set_carusel_into_option_set(self):
        grid_layout_1 = QtWidgets.QGridLayout(self.widget_select_area_1)
        self.widget_select_area_1.setLayout(grid_layout_1)

    def _set_click_event(self):
        self.btn_cancel_1.clicked.connect(lambda state: self.close())
        self.btn_cancel_2.clicked.connect(lambda state: self.close())
        self.btn_plus_1.clicked.connect(lambda state: self._stepper_add(self.label_item_count_1, 1))
        self.btn_plus_2.clicked.connect(lambda state: self._stepper_add(self.label_item_count_2, 1))
        self.btn_minus_1.clicked.connect(lambda state: self._stepper_add(self.label_item_count_1, -1))
        self.btn_minus_2.clicked.connect(lambda state: self._stepper_add(self.label_item_count_2, -1))
        self.btn_go_standby_1.clicked.connect(lambda state: self._go_to_standby())
        self.btn_go_standby_2.clicked.connect(lambda state: self._go_to_standby())
        self.btn_go_standby_3.clicked.connect(lambda state: self._go_to_standby())
        self.btn_go_standby_4.clicked.connect(lambda state: self._go_to_standby())

        self.widget_left.mousePressEvent = self.left_widget_click_event
        self.widget_left.mouseReleaseEvent = self.left_widget_release_event
        self.widget_right.mousePressEvent = self.right_widget_click_event
        self.widget_right.mouseReleaseEvent = self.right_widget_release_event

    def _go_to_standby(self):
        self.parent._go_standby()
        self.close()

    def _stepper_add(self, label_counter, value):
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
        elif self.label_item_count_2 == label_counter and  int_value == 2 or int_value == 9:
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

    def left_widget_click_event(self, event):
        self.label_set_image.setMaximumSize(180, 180)
        self.label_set_image.setMinimumSize(180, 180)

    def left_widget_release_event(self, event):
        self.label_set_image.setMaximumSize(150, 150)
        self.label_set_image.setMinimumSize(150, 150)

    def right_widget_click_event(self, event):
        self.label_single_image.setMaximumSize(180, 180)
        self.label_single_image.setMinimumSize(180, 180)

    def right_widget_release_event(self, event):
        self.label_single_image.setMaximumSize(150, 150)
        self.label_single_image.setMinimumSize(150, 150)
