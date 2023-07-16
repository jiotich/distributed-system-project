from PyQt5.QtWidgets import QFileDialog
from user_interface.main_window import *
import user_interface.event_handlers.main_handler as mh

def load_publish_page(window):
    window.image_path = ""
    window.ui.image_url_browser.setPlainText("")

def open_browser(window):
    info = QFileDialog.getOpenFileName(filter="Images (*.jpg *.jpeg)")
    window.image_path = info[0]
    window.ui.image_url_browser.setPlainText(window.image_path)

def post_button(window):
    if(window.ui.image_url_browser.toPlainText() == "" or window.ui.publish_description_browser.toPlainText() == ""):
        window.pop_up("All fields must be filled.             ")
    else:
        response = mh.publish_click(window, window.image_path, window.ui.publish_description_browser.toPlainText())
        if response:
            window.pop_up("Published!                                    ")
        else:
            window.pop_up("Something went wrong                          ")