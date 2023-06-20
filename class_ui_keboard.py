from ui_qr_keyboard import Ui_QRCodeKeyBoard
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import common


class QRcodeInsertModal(QtWidgets.QWidget, Ui_QRCodeKeyBoard):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self._set_btn_triggered()
    def _set_btn_triggered(self):
        self.pushButton_3.clicked.connect(lambda state: self.close())
