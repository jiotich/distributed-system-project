import sys
sys.dont_write_bytecode = True
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from login_window import *
from main_window import *
import event_handlers.login_handler as lh
import event_handlers.main_handler as mh

class Window(QMainWindow):
    
#Starts the login window
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        #Removing the standard OS frame
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #Adding an icon
        self.setWindowIcon(QtGui.QIcon("images/imago.png"))
        #Setting window title
        self.setWindowTitle("Imago")
        #Minimize window button
        self.ui.login_minimize_button.clicked.connect(lambda: self.showMinimized())
        #Close window button
        self.ui.login_close_button.clicked.connect(lambda: self.close())
        #LogIn button
        self.ui.login_button.clicked.connect(self.login)
        #SignIn button
        self.ui.signin_button.clicked.connect(self.signin)
        self.show()

    def login(self):
        username = self.ui.login_username.text()
        password = self.ui.login_password.text()
        if (username == "" or password == ""):
            print("All fields must be filled")
            return
        is_logged_in = lh.login_clicked(username, password)
        if (is_logged_in):
            self.username = username
            self.change_to_main_window()
        else:
            print("Login error: invalid credentials")

    def signin(self):
        username = self.ui.signin_username.text()
        password = self.ui.signin_password.text()
        password_confirmation = self.ui.signin_confirm_password.text()
        if (username == "" or password == "" or password_confirmation == ""):
            print("All fields must be filled")
            return
        if (password != password_confirmation):
            print("Password confirmation error")
            return
        lh.signin_clicked(username, password)

#From here, the ui changes to the main window, so the functions above are not used anymore

    def change_to_main_window(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_main_window()
        self.ui.setupUi(self.main_window)
        self.hide()
        #Removing the standard OS frame
        self.main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #Adding an icon
        self.main_window.setWindowIcon(QtGui.QIcon("images/imago.png"))
        #Setting window title
        self.main_window.setWindowTitle("Imago")
        #Minimize window button
        self.ui.minimize_button.clicked.connect(lambda: self.main_window.showMinimized())
        self.is_maximized = False
        #Maximize window button
        self.ui.maximize_button.clicked.connect(self.maximize)
        #Close window button
        self.ui.close_button.clicked.connect(lambda: self.main_window.close())
        #Search button
        self.ui.search_button.clicked.connect(self.search)
        #Home button
        self.ui.feed_button.clicked.connect(self.home)
        #Profile button
        self.ui.profile_button.clicked.connect(self.profile)
        #Publish page button
        self.ui.publish_page_button.clicked.connect(self.publish_page)
        self.post_number = 0
        self.feed_posts = []
        self.main_window.show()

    def maximize(self):
        if (self.is_maximized):
            self.main_window.showNormal()
            self.is_maximized = False
        else:
            self.main_window.showMaximized()
            self.is_maximized = True

    def search(self):
        search = self.ui.search_text.text()
        if (search == ""):
            return
        mh.search_click(search)

    def home(self):
        mh.home_click()
        self.create_feed_post()

    def profile(self):
        mh.profile_click()
        self.clear_feed()

    def publish_page(self):
        mh.publish_click()

    def create_feed_post(self):
        self.post_frame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
        self.post_frame.setMaximumSize(QtCore.QSize(16777215, 700))
        self.post_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.post_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.post_frame.setObjectName("post_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.post_frame)
        self.horizontalLayout_6.setContentsMargins(6, 6, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.post_frame)
        self.frame_7.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.post_main_frame = QtWidgets.QFrame(self.post_frame)
        self.post_main_frame.setMaximumSize(QtCore.QSize(700, 16777215))
        self.post_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.post_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.post_main_frame.setObjectName("post_main_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.post_main_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.post_user_frame = QtWidgets.QFrame(self.post_main_frame)
        self.post_user_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.post_user_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.post_user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.post_user_frame.setObjectName("post_user_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.post_user_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.post_user_frame)
        self.pushButton.setStyleSheet("background-color: rgb(21, 21, 21);\ncolor: rgb(255, 255, 255);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_4.addWidget(self.post_user_frame)
        self.post_image_frame = QtWidgets.QFrame(self.post_main_frame)
        self.post_image_frame.setMinimumSize(QtCore.QSize(0, 300))
        self.post_image_frame.setMaximumSize(QtCore.QSize(16777215, 800))
        self.post_image_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_image_frame.setStyleSheet("image: url(:/images/images/picture.png);")
        self.post_image_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.post_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.post_image_frame.setObjectName("post_image_frame")
        self.verticalLayout_4.addWidget(self.post_image_frame)
        self.post_description_frame = QtWidgets.QFrame(self.post_main_frame)
        self.post_description_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.post_description_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.post_description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.post_description_frame.setObjectName("post_description_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.post_description_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.post_description_frame)
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.verticalLayout_4.addWidget(self.post_description_frame)
        self.horizontalLayout_6.addWidget(self.post_main_frame)
        self.frame_9 = QtWidgets.QFrame(self.post_frame)
        self.frame_9.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.ui.gridLayout.addWidget(self.post_frame, self.post_number, 0, 1, 1)
        self.post_number += 1
        self.retranslate()
        self.feed_posts.append(self.post_frame)
        
    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("main_window", "Username"))
        self.textBrowser.setHtml(_translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description</p></body></html>"))

    def clear_feed(self):
        for frame in self.feed_posts:
            frame.deleteLater()
            self.feed_posts = self.feed_posts[:-1]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())