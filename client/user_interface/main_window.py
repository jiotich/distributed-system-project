# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(746, 595)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMinimumSize(QtCore.QSize(0, 50))
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_header.setFrameShape(QtWidgets.QFrame.Panel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.main_header)
        self.frame_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.search_text = QtWidgets.QLineEdit(self.frame_3)
        self.search_text.setStyleSheet("color: rgb(0, 173, 103);\n"
"border-bottom-color: rgb(0, 173, 103);")
        self.search_text.setFrame(True)
        self.search_text.setObjectName("search_text")
        self.horizontalLayout_5.addWidget(self.search_text)
        self.search_button = QtWidgets.QPushButton(self.frame_3)
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_5.addWidget(self.search_button)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.main_header)
        self.frame.setStyleSheet("image: url(:/images/images/imago.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.main_header)
        self.frame_4.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimize_button = QtWidgets.QPushButton(self.frame_4)
        self.minimize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_4.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(self.frame_4)
        self.maximize_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_4.addWidget(self.maximize_button)
        self.close_button = QtWidgets.QPushButton(self.frame_4)
        self.close_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_4.addWidget(self.close_button)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.main_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QFrame(self.main_body)
        self.side_menu.setMinimumSize(QtCore.QSize(60, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(60, 16777215))
        self.side_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.side_menu)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.feed_button = QtWidgets.QPushButton(self.frame_5)
        self.feed_button.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.feed_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.feed_button.setIcon(icon4)
        self.feed_button.setIconSize(QtCore.QSize(32, 32))
        self.feed_button.setObjectName("feed_button")
        self.profile_button = QtWidgets.QPushButton(self.frame_5)
        self.profile_button.setGeometry(QtCore.QRect(10, 100, 41, 41))
        self.profile_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_button.setIcon(icon5)
        self.profile_button.setIconSize(QtCore.QSize(32, 32))
        self.profile_button.setObjectName("profile_button")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.side_menu)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.side_menu)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.publish_page_button = QtWidgets.QPushButton(self.frame_2)
        self.publish_page_button.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.publish_page_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.publish_page_button.setIcon(icon6)
        self.publish_page_button.setIconSize(QtCore.QSize(32, 32))
        self.publish_page_button.setObjectName("publish_page_button")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_frame = QtWidgets.QFrame(self.main_body)
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.feed_page = QtWidgets.QWidget()
        self.feed_page.setObjectName("feed_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.feed_page)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.feed_page)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 674, 501))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(6, 6, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.feed_page)
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")
        self.stackedWidget.addWidget(self.profile_page)
        self.publish_page = QtWidgets.QWidget()
        self.publish_page.setObjectName("publish_page")
        self.stackedWidget.addWidget(self.publish_page)
        self.search_page = QtWidgets.QWidget()
        self.search_page.setObjectName("search_page")
        self.stackedWidget.addWidget(self.search_page)
        self.post_page = QtWidgets.QWidget()
        self.post_page.setObjectName("post_page")
        self.stackedWidget.addWidget(self.post_page)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.main_frame)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMinimumSize(QtCore.QSize(0, 30))
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        
        self.search_text.setPlaceholderText(_translate("main_window", "Search"))
        
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
