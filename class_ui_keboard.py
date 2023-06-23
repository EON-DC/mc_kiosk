from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui_qr_keyboard import Ui_QRCodeKeyBoard


class QRcodeInsertModal(QtWidgets.QWidget, Ui_QRCodeKeyBoard):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(30, 30, 540, 960)
        self.parent = parent
        self.setStyleSheet(self.styleSheet() + self.parent.styleSheet())
        self.code_text = ''
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.btn_group = self._set_btn_group()
        self.btn_char_group = self._set_btn_char_group()
        self._set_btn_triggered()

    def _set_btn_group(self):
        self.btn_28.setStyleSheet('font: 20pt Arial')
        result_list = list()
        for btn in self.widget_3.findChildren(QtWidgets.QPushButton):
            result_list.append(btn)
        for btn in self.widget_4.findChildren(QtWidgets.QPushButton):
            result_list.append(btn)
        for btn in self.widget_5.findChildren(QtWidgets.QPushButton):
            result_list.append(btn)
        for btn in self.widget_6.findChildren(QtWidgets.QPushButton):
            result_list.append(btn)
        return result_list

    def _set_btn_char_group(self):
        result_list = list()
        for btn in self.btn_group:
            btn: QtWidgets.QPushButton
            text = btn.text()
            if not text.isdigit() and not (text == '⇧' or text == '⌫'):
                result_list.append(btn)
        return result_list

    def _set_btn_triggered(self):
        self.btn_close.clicked.connect(lambda state: self.close())
        self.btn_confirm.clicked.connect(lambda state: self.confirm_code())
        self.btn_space.clicked.connect(lambda state: self._keyboard_action(' '))
        self.btn_back.clicked.connect(lambda state: self._keyboard_action('back'))
        for btn in self.btn_group:
            btn: QtWidgets.QPushButton
            btn.clicked.connect(lambda state, key=btn.text(): self._keyboard_action(key))

    def _keyboard_action(self, key):
        if key == '⇧':
            self.toggle_char_btns()
        elif key == '⌫':
            if len(self.code_text) != 0:
                self.code_text = self.code_text[:len(self.code_text) - 1]
        elif key == 'back':
            self.code_text = ''
        else:
            self.code_text = self.code_text + key
        self.label_code_text.setText(self.code_text)

    def toggle_char_btns(self):
        if self.btn_char_group[0].text().isupper():
            for btn in self.btn_char_group:
                btn.setText(btn.text().lower())
        else:
            for btn in self.btn_char_group:
                btn.setText(btn.text().upper())

    def confirm_code(self):
        self.parent.set_qr_code(self.label_code_text.text())

    def show(self):
        self.code_text = ''
        super().show()
