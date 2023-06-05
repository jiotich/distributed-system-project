from PyQt5.QtWidgets import QFileDialog
from main_window import *
import event_handlers.main_handler as mh

def load_publish_page(window):
    window.image_path = ""
    window.ui.image_url_browser.setPlainText("")
    window.ui.select_image_button.clicked.connect(lambda: open_browser(window))
    window.ui.publish_button.clicked.connect(lambda: post_button(window))

def open_browser(window):
    info = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")
    window.image_path = info[0]
    window.ui.image_url_browser.setPlainText(window.image_path)

def post_button(window):
    if(window.ui.image_url_browser.toPlainText() == "" or window.ui.publish_description_browser.toPlainText() == ""):
        print("Everything must be filled")
    else:
        print("Published!")
        mh.publish_click(window.username, window.image_path, window.ui.publish_description_browser.toPlainText())