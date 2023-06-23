
import os

if __name__ == '__main__':
    os.system('pyuic5 ui/ui_kiosk.ui -o ui_kiosk.py')
    os.system('pyuic5 ui/ui_set_option_modal.ui -o ui_set_option_modal.py')
    os.system('pyuic5 ui/ui_carusel.ui -o ui_carusel.py')
    os.system('pyuic5 ui/ui_pay_finish_modal.ui -o ui_pay_finish.py')
    os.system('pyuic5 ui/widget_list_item.ui -o ui_widget_list_item.py')
    os.system('pyuic5 ui/ui_qr_keyboard.ui -o ui_qr_keyboard.py')
    os.system('pyuic5 ui/ui_nutrition_form.ui -o ui_nutrition_form.py')
