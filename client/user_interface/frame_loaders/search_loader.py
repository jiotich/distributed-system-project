from PyQt5 import QtCore, QtWidgets
from user_interface.main_window import *
import user_interface.event_handlers.main_handler as mh
from user_interface.frame_loaders.profile_loader import *

def clear_search_page(window):
    for result in window.search_results:
        result.deleteLater()
        window.search_results = window.search_results[:-1]
    window.search_result_number = 0

def load_search_page(window, search):
    clear_search_page(window)
    window.ui.label_2.setText("Searching for '"+search+"'")
    window.ui.search_text.setText("")
    user = mh.search_click(window, search)
    #for user in users:
    print(user)
    if (user != None):
        load_search_results(window=window, username=user[0], description=user[1])

def load_search_results(window, username, description=""):
    window.search_user_frame = QtWidgets.QFrame(window.ui.scrollAreaWidgetContents_search)
    window.search_user_frame.setMinimumSize(QtCore.QSize(0, 100))
    window.search_user_frame.setMaximumSize(QtCore.QSize(16777215, 100))
    window.search_user_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.search_user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    window.search_user_frame.setObjectName("search_user_frame")
    window.search_user_frame.setStyleSheet("background-color: rgb(34, 34, 34); border-radius: 8px;")
    window.verticalLayout_18 = QtWidgets.QVBoxLayout(window.search_user_frame)
    window.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
    window.verticalLayout_18.setSpacing(0)
    window.verticalLayout_18.setObjectName("verticalLayout_18")
    window.search_username = QtWidgets.QFrame(window.search_user_frame)
    window.search_username.setMaximumSize(QtCore.QSize(16777215, 30))
    window.search_username.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.search_username.setFrameShadow(QtWidgets.QFrame.Raised)
    window.search_username.setObjectName("search_username")
    window.verticalLayout_19 = QtWidgets.QVBoxLayout(window.search_username)
    window.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
    window.verticalLayout_19.setSpacing(0)
    window.verticalLayout_19.setObjectName("verticalLayout_19")
    window.search_user_button = QtWidgets.QPushButton(window.search_username)
    window.search_user_button.setStyleSheet("color: rgb(255, 255, 255);")
    window.search_user_button.setFlat(True)
    window.search_user_button.setObjectName("search_user_button")
    window.search_user_button.setText(username)
    window.search_user_button.clicked.connect(lambda: load_profile(window, username))
    window.verticalLayout_19.addWidget(window.search_user_button)
    window.verticalLayout_18.addWidget(window.search_username)
    window.search_info = QtWidgets.QFrame(window.search_user_frame)
    window.search_info.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.search_info.setFrameShadow(QtWidgets.QFrame.Raised)
    window.search_info.setObjectName("search_info")
    window.horizontalLayout_9 = QtWidgets.QHBoxLayout(window.search_info)
    window.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
    window.horizontalLayout_9.setSpacing(0)
    window.horizontalLayout_9.setObjectName("horizontalLayout_9")
    window.search_picture = QtWidgets.QFrame(window.search_info)
    window.search_picture.setMinimumSize(QtCore.QSize(70, 0))
    window.search_picture.setMaximumSize(QtCore.QSize(16777215, 70))
    window.search_picture.setStyleSheet("image: url(:/images/images/user.png);")
    window.search_picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
    window.search_picture.setFrameShadow(QtWidgets.QFrame.Raised)
    window.search_picture.setObjectName("search_picture")
    window.horizontalLayout_9.addWidget(window.search_picture)
    window.search_description = QtWidgets.QFrame(window.search_info)
    window.search_description.setMinimumSize(QtCore.QSize(200, 0))
    window.search_description.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.search_description.setFrameShadow(QtWidgets.QFrame.Raised)
    window.search_description.setObjectName("search_description")
    window.verticalLayout_20 = QtWidgets.QVBoxLayout(window.search_description)
    window.verticalLayout_20.setObjectName("verticalLayout_20")
    window.textBrowser_4 = QtWidgets.QTextBrowser(window.search_description)
    window.textBrowser_4.setStyleSheet("color: rgb(255, 255, 255);")
    window.textBrowser_4.setObjectName("textBrowser_4")
    window.textBrowser_4.setPlainText(description)
    window.verticalLayout_20.addWidget(window.textBrowser_4)
    window.horizontalLayout_9.addWidget(window.search_description)
    window.verticalLayout_18.addWidget(window.search_info, 0, QtCore.Qt.AlignHCenter)
    window.ui.gridLayout_search.addWidget(window.search_user_frame, window.search_result_number, 0, 1, 1)
    window.search_result_number += 1
    window.search_results.append(window.search_user_frame)
