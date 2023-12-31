# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_qr_keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QRCodeKeyBoard(object):
    def setupUi(self, QRCodeKeyBoard):
        QRCodeKeyBoard.setObjectName("QRCodeKeyBoard")
        QRCodeKeyBoard.resize(540, 960)
        QRCodeKeyBoard.setMinimumSize(QtCore.QSize(540, 960))
        QRCodeKeyBoard.setMaximumSize(QtCore.QSize(540, 960))
        QRCodeKeyBoard.setStyleSheet("#QRCodeKeyBoard{\n"
"    background-color: white;\n"
"}\n"
"#widget_label_background{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #a3a3a3;\n"
"    background-color : #ffffff;\n"
"}\n"
"#title_upper{\n"
"    font: 22pt;\n"
"}\n"
"\n"
"#title_lower, #label_code_text{\n"
"    font: 14pt;\n"
"}\n"
"#label_footer{\n"
"    font: 24pt;\n"
"}    \n"
"\n"
"#widget_footer_scan{\n"
"    background-color: #ffbc0d;\n"
"}\n"
"\n"
"#widget_footer_scan{\n"
"    background-img\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(QRCodeKeyBoard)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_qr_code = QtWidgets.QWidget(QRCodeKeyBoard)
        self.widget_qr_code.setObjectName("widget_qr_code")
        self.verticalLayout_93 = QtWidgets.QVBoxLayout(self.widget_qr_code)
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName("verticalLayout_93")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_93.addItem(spacerItem)
        self.widget_80 = QtWidgets.QWidget(self.widget_qr_code)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_80.sizePolicy().hasHeightForWidth())
        self.widget_80.setSizePolicy(sizePolicy)
        self.widget_80.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_80.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_80.setObjectName("widget_80")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.widget_80)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_14 = QtWidgets.QLabel(self.widget_80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(40, 40))
        self.label_14.setMaximumSize(QtCore.QSize(40, 40))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("ui\\../src/logo.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_47.addWidget(self.label_14)
        self.verticalLayout_93.addWidget(self.widget_80)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_93.addItem(spacerItem1)
        self.widget_2 = QtWidgets.QWidget(self.widget_qr_code)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_81 = QtWidgets.QWidget(self.widget_2)
        self.widget_81.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_81.setMaximumSize(QtCore.QSize(400, 150))
        self.widget_81.setObjectName("widget_81")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_81)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_upper = QtWidgets.QLabel(self.widget_81)
        self.title_upper.setScaledContents(True)
        self.title_upper.setAlignment(QtCore.Qt.AlignCenter)
        self.title_upper.setWordWrap(True)
        self.title_upper.setObjectName("title_upper")
        self.verticalLayout_2.addWidget(self.title_upper)
        self.title_lower = QtWidgets.QLabel(self.widget_81)
        self.title_lower.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lower.setWordWrap(True)
        self.title_lower.setObjectName("title_lower")
        self.verticalLayout_2.addWidget(self.title_lower)
        self.horizontalLayout_2.addWidget(self.widget_81)
        self.verticalLayout_93.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.widget_qr_code)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_82 = QtWidgets.QWidget(self.widget)
        self.widget_82.setMinimumSize(QtCore.QSize(0, 440))
        self.widget_82.setMaximumSize(QtCore.QSize(440, 440))
        self.widget_82.setObjectName("widget_82")
        self.verticalLayout_96 = QtWidgets.QVBoxLayout(self.widget_82)
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName("verticalLayout_96")
        self.widget_label_background = QtWidgets.QWidget(self.widget_82)
        self.widget_label_background.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_label_background.setObjectName("widget_label_background")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_label_background)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_code_text = QtWidgets.QLabel(self.widget_label_background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_code_text.sizePolicy().hasHeightForWidth())
        self.label_code_text.setSizePolicy(sizePolicy)
        self.label_code_text.setMinimumSize(QtCore.QSize(0, 40))
        self.label_code_text.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_code_text.setText("")
        self.label_code_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_code_text.setObjectName("label_code_text")
        self.verticalLayout_3.addWidget(self.label_code_text)
        self.verticalLayout_96.addWidget(self.widget_label_background)
        self.widget_lower_recommend = QtWidgets.QWidget(self.widget_82)
        self.widget_lower_recommend.setObjectName("widget_lower_recommend")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_lower_recommend)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.widget_lower_recommend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_2 = QtWidgets.QPushButton(self.widget_3)
        self.btn_2.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_2.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.widget_3)
        self.btn_3.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_3.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_3.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(self.widget_3)
        self.btn_4.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_4.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_3.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.widget_3)
        self.btn_5.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_5.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_5.setObjectName("btn_5")
        self.horizontalLayout_3.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.widget_3)
        self.btn_6.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_6.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_3.addWidget(self.btn_6)
        self.btn_7 = QtWidgets.QPushButton(self.widget_3)
        self.btn_7.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_7.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout_3.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.widget_3)
        self.btn_8.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_8.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout_3.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.widget_3)
        self.btn_9.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_9.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_9.setObjectName("btn_9")
        self.horizontalLayout_3.addWidget(self.btn_9)
        self.btn_10 = QtWidgets.QPushButton(self.widget_3)
        self.btn_10.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_10.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_10.setObjectName("btn_10")
        self.horizontalLayout_3.addWidget(self.btn_10)
        self.btn_1 = QtWidgets.QPushButton(self.widget_3)
        self.btn_1.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_1.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_3.addWidget(self.btn_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_lower_recommend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btn_11 = QtWidgets.QPushButton(self.widget_4)
        self.btn_11.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_11.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_11.setObjectName("btn_11")
        self.horizontalLayout_4.addWidget(self.btn_11)
        self.btn_12 = QtWidgets.QPushButton(self.widget_4)
        self.btn_12.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_12.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_12.setObjectName("btn_12")
        self.horizontalLayout_4.addWidget(self.btn_12)
        self.btn_13 = QtWidgets.QPushButton(self.widget_4)
        self.btn_13.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_13.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_13.setObjectName("btn_13")
        self.horizontalLayout_4.addWidget(self.btn_13)
        self.btn_14 = QtWidgets.QPushButton(self.widget_4)
        self.btn_14.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_14.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_14.setObjectName("btn_14")
        self.horizontalLayout_4.addWidget(self.btn_14)
        self.btn_15 = QtWidgets.QPushButton(self.widget_4)
        self.btn_15.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_15.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_15.setObjectName("btn_15")
        self.horizontalLayout_4.addWidget(self.btn_15)
        self.btn_16 = QtWidgets.QPushButton(self.widget_4)
        self.btn_16.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_16.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_16.setObjectName("btn_16")
        self.horizontalLayout_4.addWidget(self.btn_16)
        self.btn_17 = QtWidgets.QPushButton(self.widget_4)
        self.btn_17.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_17.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_17.setObjectName("btn_17")
        self.horizontalLayout_4.addWidget(self.btn_17)
        self.btn_18 = QtWidgets.QPushButton(self.widget_4)
        self.btn_18.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_18.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_18.setObjectName("btn_18")
        self.horizontalLayout_4.addWidget(self.btn_18)
        self.btn_19 = QtWidgets.QPushButton(self.widget_4)
        self.btn_19.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_19.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_19.setObjectName("btn_19")
        self.horizontalLayout_4.addWidget(self.btn_19)
        self.btn_20 = QtWidgets.QPushButton(self.widget_4)
        self.btn_20.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_20.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_20.setObjectName("btn_20")
        self.horizontalLayout_4.addWidget(self.btn_20)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.widget_lower_recommend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.btn_31 = QtWidgets.QPushButton(self.widget_6)
        self.btn_31.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_31.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_31.setObjectName("btn_31")
        self.horizontalLayout_6.addWidget(self.btn_31)
        self.btn_32 = QtWidgets.QPushButton(self.widget_6)
        self.btn_32.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_32.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_32.setObjectName("btn_32")
        self.horizontalLayout_6.addWidget(self.btn_32)
        self.btn_33 = QtWidgets.QPushButton(self.widget_6)
        self.btn_33.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_33.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_33.setObjectName("btn_33")
        self.horizontalLayout_6.addWidget(self.btn_33)
        self.btn_34 = QtWidgets.QPushButton(self.widget_6)
        self.btn_34.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_34.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_34.setObjectName("btn_34")
        self.horizontalLayout_6.addWidget(self.btn_34)
        self.btn_35 = QtWidgets.QPushButton(self.widget_6)
        self.btn_35.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_35.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_35.setObjectName("btn_35")
        self.horizontalLayout_6.addWidget(self.btn_35)
        self.btn_36 = QtWidgets.QPushButton(self.widget_6)
        self.btn_36.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_36.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_36.setObjectName("btn_36")
        self.horizontalLayout_6.addWidget(self.btn_36)
        self.btn_37 = QtWidgets.QPushButton(self.widget_6)
        self.btn_37.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_37.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_37.setObjectName("btn_37")
        self.horizontalLayout_6.addWidget(self.btn_37)
        self.btn_38 = QtWidgets.QPushButton(self.widget_6)
        self.btn_38.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_38.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_38.setObjectName("btn_38")
        self.horizontalLayout_6.addWidget(self.btn_38)
        self.btn_39 = QtWidgets.QPushButton(self.widget_6)
        self.btn_39.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_39.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_39.setObjectName("btn_39")
        self.horizontalLayout_6.addWidget(self.btn_39)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(self.widget_lower_recommend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.btn_28 = QtWidgets.QPushButton(self.widget_5)
        self.btn_28.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_28.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_28.setStyleSheet("font:20pt;")
        self.btn_28.setObjectName("btn_28")
        self.horizontalLayout_5.addWidget(self.btn_28)
        self.btn_21 = QtWidgets.QPushButton(self.widget_5)
        self.btn_21.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_21.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_21.setObjectName("btn_21")
        self.horizontalLayout_5.addWidget(self.btn_21)
        self.btn_22 = QtWidgets.QPushButton(self.widget_5)
        self.btn_22.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_22.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_22.setObjectName("btn_22")
        self.horizontalLayout_5.addWidget(self.btn_22)
        self.btn_23 = QtWidgets.QPushButton(self.widget_5)
        self.btn_23.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_23.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_23.setObjectName("btn_23")
        self.horizontalLayout_5.addWidget(self.btn_23)
        self.btn_24 = QtWidgets.QPushButton(self.widget_5)
        self.btn_24.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_24.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_24.setObjectName("btn_24")
        self.horizontalLayout_5.addWidget(self.btn_24)
        self.btn_25 = QtWidgets.QPushButton(self.widget_5)
        self.btn_25.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_25.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_25.setObjectName("btn_25")
        self.horizontalLayout_5.addWidget(self.btn_25)
        self.btn_26 = QtWidgets.QPushButton(self.widget_5)
        self.btn_26.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_26.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_26.setObjectName("btn_26")
        self.horizontalLayout_5.addWidget(self.btn_26)
        self.btn_27 = QtWidgets.QPushButton(self.widget_5)
        self.btn_27.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_27.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_27.setObjectName("btn_27")
        self.horizontalLayout_5.addWidget(self.btn_27)
        self.btn_29 = QtWidgets.QPushButton(self.widget_5)
        self.btn_29.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_29.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_29.setObjectName("btn_29")
        self.horizontalLayout_5.addWidget(self.btn_29)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_7 = QtWidgets.QWidget(self.widget_lower_recommend)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.btn_space = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_space.sizePolicy().hasHeightForWidth())
        self.btn_space.setSizePolicy(sizePolicy)
        self.btn_space.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_space.setMaximumSize(QtCore.QSize(120, 50))
        self.btn_space.setObjectName("btn_space")
        self.horizontalLayout_7.addWidget(self.btn_space)
        self.btn_back = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_back.setMaximumSize(QtCore.QSize(120, 50))
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_7.addWidget(self.btn_back)
        spacerItem11 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_lower_recommend)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_close = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_8.addWidget(self.btn_close)
        self.btn_confirm = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_confirm.sizePolicy().hasHeightForWidth())
        self.btn_confirm.setSizePolicy(sizePolicy)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout_8.addWidget(self.btn_confirm)
        self.verticalLayout_4.addWidget(self.widget_8)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.widget_9 = QtWidgets.QWidget(self.widget_lower_recommend)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.label_2 = QtWidgets.QLabel(self.widget_9)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.verticalLayout_4.addWidget(self.widget_9)
        self.verticalLayout_96.addWidget(self.widget_lower_recommend)
        self.horizontalLayout.addWidget(self.widget_82)
        self.verticalLayout_93.addWidget(self.widget)
        self.widget_footer_scan = QtWidgets.QWidget(self.widget_qr_code)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_footer_scan.sizePolicy().hasHeightForWidth())
        self.widget_footer_scan.setSizePolicy(sizePolicy)
        self.widget_footer_scan.setStyleSheet("")
        self.widget_footer_scan.setObjectName("widget_footer_scan")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_footer_scan)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem15)
        self.widget_10 = QtWidgets.QWidget(self.widget_footer_scan)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_footer = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_footer.sizePolicy().hasHeightForWidth())
        self.label_footer.setSizePolicy(sizePolicy)
        self.label_footer.setMinimumSize(QtCore.QSize(0, 80))
        self.label_footer.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label_footer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_footer.setWordWrap(True)
        self.label_footer.setObjectName("label_footer")
        self.horizontalLayout_10.addWidget(self.label_footer)
        self.label = QtWidgets.QLabel(self.widget_10)
        self.label.setMinimumSize(QtCore.QSize(160, 160))
        self.label.setMaximumSize(QtCore.QSize(160, 160))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui\\../src/qr_sample.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.verticalLayout_5.addWidget(self.widget_10)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.verticalLayout_93.addWidget(self.widget_footer_scan)
        self.verticalLayout.addWidget(self.widget_qr_code)

        self.retranslateUi(QRCodeKeyBoard)
        QtCore.QMetaObject.connectSlotsByName(QRCodeKeyBoard)

    def retranslateUi(self, QRCodeKeyBoard):
        _translate = QtCore.QCoreApplication.translate
        QRCodeKeyBoard.setWindowTitle(_translate("QRCodeKeyBoard", "Form"))
        self.title_upper.setText(_translate("QRCodeKeyBoard", "코드를 입력하세요"))
        self.title_lower.setText(_translate("QRCodeKeyBoard", "스캔 코드 옆에 있는 텍스트 코드를 입력하세요"))
        self.btn_2.setText(_translate("QRCodeKeyBoard", "1"))
        self.btn_3.setText(_translate("QRCodeKeyBoard", "2"))
        self.btn_4.setText(_translate("QRCodeKeyBoard", "3"))
        self.btn_5.setText(_translate("QRCodeKeyBoard", "4"))
        self.btn_6.setText(_translate("QRCodeKeyBoard", "5"))
        self.btn_7.setText(_translate("QRCodeKeyBoard", "6"))
        self.btn_8.setText(_translate("QRCodeKeyBoard", "7"))
        self.btn_9.setText(_translate("QRCodeKeyBoard", "8"))
        self.btn_10.setText(_translate("QRCodeKeyBoard", "9"))
        self.btn_1.setText(_translate("QRCodeKeyBoard", "0"))
        self.btn_11.setText(_translate("QRCodeKeyBoard", "Q"))
        self.btn_12.setText(_translate("QRCodeKeyBoard", "W"))
        self.btn_13.setText(_translate("QRCodeKeyBoard", "E"))
        self.btn_14.setText(_translate("QRCodeKeyBoard", "R"))
        self.btn_15.setText(_translate("QRCodeKeyBoard", "T"))
        self.btn_16.setText(_translate("QRCodeKeyBoard", "Y"))
        self.btn_17.setText(_translate("QRCodeKeyBoard", "U"))
        self.btn_18.setText(_translate("QRCodeKeyBoard", "I"))
        self.btn_19.setText(_translate("QRCodeKeyBoard", "O"))
        self.btn_20.setText(_translate("QRCodeKeyBoard", "P"))
        self.btn_31.setText(_translate("QRCodeKeyBoard", "A"))
        self.btn_32.setText(_translate("QRCodeKeyBoard", "S"))
        self.btn_33.setText(_translate("QRCodeKeyBoard", "D"))
        self.btn_34.setText(_translate("QRCodeKeyBoard", "F"))
        self.btn_35.setText(_translate("QRCodeKeyBoard", "G"))
        self.btn_36.setText(_translate("QRCodeKeyBoard", "H"))
        self.btn_37.setText(_translate("QRCodeKeyBoard", "J"))
        self.btn_38.setText(_translate("QRCodeKeyBoard", "K"))
        self.btn_39.setText(_translate("QRCodeKeyBoard", "L"))
        self.btn_28.setText(_translate("QRCodeKeyBoard", "⇧"))
        self.btn_21.setText(_translate("QRCodeKeyBoard", "Z"))
        self.btn_22.setText(_translate("QRCodeKeyBoard", "X"))
        self.btn_23.setText(_translate("QRCodeKeyBoard", "C"))
        self.btn_24.setText(_translate("QRCodeKeyBoard", "V"))
        self.btn_25.setText(_translate("QRCodeKeyBoard", "B"))
        self.btn_26.setText(_translate("QRCodeKeyBoard", "N"))
        self.btn_27.setText(_translate("QRCodeKeyBoard", "M"))
        self.btn_29.setText(_translate("QRCodeKeyBoard", "⌫"))
        self.btn_space.setText(_translate("QRCodeKeyBoard", "띄어쓰기"))
        self.btn_back.setText(_translate("QRCodeKeyBoard", "지우기"))
        self.btn_close.setText(_translate("QRCodeKeyBoard", "뒤로"))
        self.btn_confirm.setText(_translate("QRCodeKeyBoard", "계속"))
        self.label_2.setText(_translate("QRCodeKeyBoard", "또는"))
        self.label_footer.setText(_translate("QRCodeKeyBoard", "QR코드를스캔"))
