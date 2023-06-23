from PyQt5 import QtWidgets

from class_menu import Menu
from ui_carusel import Ui_Carusel


class CaruselOption(QtWidgets.QWidget, Ui_Carusel):
    def __init__(self, parent, pixmap_dict, menu_info, option_=None):
        assert isinstance(menu_info, Menu)
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.label_info.hide()
        self.pixmap_dict = pixmap_dict
        self.menu_info = menu_info
        self.option_info = option_
        self.img = self.pixmap_dict[f'{self.menu_info.basic_img_path:03d}']
        self.item_img.setPixmap(self.img)
        self.menu_name.setText(self.menu_info.name)
        self._set_menu_price_and_calories()
        self._set_clicked_event()
        self._set_title()

    def _set_title(self):
        self.label_info.hide()
        if self.menu_info.is_new_menu:
            self.label_info.show()
            self.label_info.setText('신메뉴')
        elif self.menu_info.is_happy_snack:
            self.label_info.show()
            self.label_info.setText('해피메뉴')

    def _set_clicked_event(self):
        self.frame_4.mousePressEvent = self.widget_click_event
        self.frame_4.mouseReleaseEvent = self.widget_release_event

    def widget_click_event(self, event):
        self.item_img.setMinimumSize(100, 100)
        self.item_img.setMaximumSize(100, 100)

    def widget_release_event(self, event):
        self.item_img.setMinimumSize(80, 80)
        self.item_img.setMaximumSize(80, 80)
        self.parent.add_option(self.option_info)

    def _set_menu_price_and_calories(self):
        if 'large' in self.option_info:
            carusel_name = self.menu_name.text() + '-라지세트'
            self.menu_name.setText(carusel_name)
            self.menu_price_cal.setText(f"+{self.menu_info.additional_price}원")
        elif 'medium' in self.option_info:
            self.menu_price_cal.setText(f"")
        else:
            self.menu_price_cal.setText(f'+{self.menu_info.additional_price}원 {self.menu_info.get_calories()}')

