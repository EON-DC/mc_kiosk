from PyQt5.QtCore import Qt

from class_menu import Menu
from ui_carusel import Ui_Carusel
from PyQt5 import QtCore, QtGui, QtWidgets
from class_ui_modal import ModalOption


class Carusel(QtWidgets.QWidget, Ui_Carusel):
    def __init__(self, parent, pixmap_dict, menu_info, option_=None):
        assert isinstance(menu_info, Menu)
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.label_info.hide()
        self.pixmap_dict = pixmap_dict
        self.menu_info = menu_info
        self.img = self.pixmap_dict[f'{self.menu_info.basic_img_path:03d}']
        self.item_img.setPixmap(self.img)
        self.menu_name.setText(self.menu_info.name)
        self._set_menu_price_and_calories()
        self._set_clicked_event()
        self._set_title()
        if option_ is None:
            self.option_modal = self._initialize_modal_window()
        else:
            self.option_info = option_

    def _set_title(self):
        self.label_info.hide()
        if self.menu_info.is_new_menu:
            self.label_info.show()
            self.label_info.setText('신메뉴')
        elif self.menu_info.is_happy_snack:
            self.label_info.show()
            self.label_info.setText('해피메뉴')



    def _initialize_modal_window(self):
        modal = ModalOption(self.parent, self.menu_info, self.pixmap_dict)
        return modal

    def _reset_option_modal(self):
        # 단품 vs 세트
        if self.menu_info.is_asked_set_service:
            self.option_modal.stackedWidget.setCurrentIndex(0)
        else:
            self.option_modal.stackedWidget.setCurrentIndex(3)

    def _set_clicked_event(self):
        self.frame_4.mousePressEvent = self.widget_click_event
        self.frame_4.mouseReleaseEvent = self.widget_release_event

    def widget_click_event(self, event):
        self.item_img.setMinimumSize(100, 100)
        self.item_img.setMaximumSize(100, 100)

    def widget_release_event(self, event):
        self.item_img.setMinimumSize(80, 80)
        self.item_img.setMaximumSize(80, 80)
        self._reset_option_modal()
        self.option_modal.show()

    def _set_menu_price_and_calories(self):
        price = self.menu_info.ordinary_price
        if price is None:
            price = self.menu_info.additional_price
        calories = self.menu_info.calory
        if self.menu_info.calory is None:
            calories = '0kcal'
        self.menu_price_cal.setText(f'{price}원 {calories}')
