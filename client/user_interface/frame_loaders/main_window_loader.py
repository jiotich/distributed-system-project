from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import *
import event_handlers.main_handler as mh
from frame_loaders.feed_loader import *
from frame_loaders.self_profile_loader import *

def change_to_main_window(window):
    window.main_window = QtWidgets.QMainWindow()
    window.ui = Ui_main_window()
    window.ui.setupUi(window.main_window)
    window.hide()
    #Removing the standard OS frame
    window.main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #Adding an icon
    window.main_window.setWindowIcon(QtGui.QIcon("images/imago.png"))
    #Setting window title
    window.main_window.setWindowTitle("Imago")
    #Minimize window button
    window.ui.minimize_button.clicked.connect(lambda: window.main_window.showMinimized())
    #Maximize window button
    window.ui.maximize_button.clicked.connect(lambda: maximize(window))
    #Close window button
    window.ui.close_button.clicked.connect(lambda: window.main_window.close())
    #Search button
    window.ui.search_button.clicked.connect(lambda: search(window))
    #Home button
    window.ui.feed_button.clicked.connect(lambda: home(window))
    #Self Profile button
    window.ui.profile_button.clicked.connect(lambda: self_profile(window))
    #Publish page button
    window.ui.publish_page_button.clicked.connect(lambda: publish_page(window))
    #Self profile name
    window.ui.label.setText(window.username)
    #Edit profile button
    window.ui.edit_button.clicked.connect(lambda: edit_description(window))
    #Confirm edit button
    window.ui.confirm_edit_button.clicked.connect(lambda: confirm_edit(window))
    #Cancel edit button
    window.ui.cancel_edit_button.clicked.connect(lambda: cancel_edit(window))
    window.ui.textEdit.setReadOnly(True)
    window.main_window.show()
    home(window)
        
def maximize(window):
    if (window.is_maximized):
        window.main_window.showNormal()
        window.is_maximized = False
    else:
        window.main_window.showMaximized()
        window.is_maximized = True
        
def home(window):
    clear_feed(window)
    window.ui.stackedWidget.setCurrentIndex(0)
    posts = mh.home_click(window)
    for post in posts:
        create_feed_post(window, post[0], post[1], post[2], 0)

def self_profile(window):
    clear_self_profile(window)
    window.ui.stackedWidget.setCurrentIndex(1)
    info = mh.self_profile_click(window.username)
    window.description = info[0]
    window.ui.textEdit.setText(window.description)
    posts = info[1]
    for post in posts:
        load_self_profile(window, post[0], post[1], 0)

def publish_page(window):
    window.ui.stackedWidget.setCurrentIndex(3)
    mh.publish_click()
    
    
def search(window):
    search = window.ui.search_text.text()
    if (search == ""):
        return
    window.ui.stackedWidget.setCurrentIndex(4)
    mh.search_click(search)