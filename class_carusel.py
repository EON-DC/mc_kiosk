from PyQt5.QtCore import Qt

from class_menu import Menu
from ui_carusel import Ui_Carusel
from PyQt5 import QtCore, QtGui, QtWidgets
from class_ui_modal import ModalOption


class Carusel(QtWidgets.QWidget, Ui_Carusel):
    def __init__(self, parent, pixmap_dict, menu_info, total_menu_list):
        assert isinstance(menu_info, Menu)
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.label_info.hide()
        self.pixmap_dict = pixmap_dict
        self.menu_info = menu_info
        self.total_menu_list = total_menu_list
        self.img = self.pixmap_dict[f'{self.menu_info.basic_img_path:03d}']
        self.item_img.setPixmap(self.img)
        self.menu_name.setText(self.menu_info.name)
        self._set_menu_price_and_calories()
        self._set_clicked_event()
        self.option_modal = self._initialize_modal_window()
        self._set_title()

    def _set_title(self):
        self.label_info.hide()
        if self.menu_info.is_new_menu:
            self.label_info.show()
            self.label_info.setText('신메뉴')
        elif self.menu_info.is_happy_snack:
            self.label_info.show()
            self.label_info.setText('해피메뉴')

    def _initialize_modal_window(self):
        modal = ModalOption(self.parent, self.menu_info, self.pixmap_dict, self.total_menu_list)
        return modal

    def _set_clicked_event(self):
        self.frame_4.mousePressEvent = self.widget_click_event
        self.frame_4.mouseReleaseEvent = self.widget_release_event

    def widget_click_event(self, event):
        self.item_img.setMinimumSize(100, 100)
        self.item_img.setMaximumSize(100, 100)

    def widget_release_event(self, event):
        self.item_img.setMinimumSize(80, 80)
        self.item_img.setMaximumSize(80, 80)
        if self.option_modal is not None:
            self.option_modal.show()
        else:  # 다음페이지로 넘기고 부모한테 옵션을 추가해줘야함
            self.parent.add_option(self.option_info)

    def _set_menu_price_and_calories(self):
        price = self.menu_info.now_price(None)
        if price is None:
            price = self.menu_info.additional_price
        self.menu_price_cal.setText(f'{price:,d}원 {self.menu_info.get_calories()}')
