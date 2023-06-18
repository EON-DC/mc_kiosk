import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from class_controller import KioskController
from class_ui_main import MainWindow
from class_db_connect import KioskDBConnector


def main():
    connector = KioskDBConnector()
    controller = KioskController(connector)
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainWindow(controller)
    myWindow.show()

    def show_error_message(message, traceback):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
        traceback.print_exc()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    app.exec_()


if __name__ == '__main__':
    main()
