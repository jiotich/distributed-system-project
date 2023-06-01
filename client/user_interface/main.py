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
        #Maximize window button
        self.ui.maximize_button.clicked.connect(lambda: self.main_window.showMaximized())
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
        self.main_window.show()

    def search(self):
        search = self.ui.search_text.text()
        if (search == ""):
            return
        mh.search_click(search)

    def home(self):
        mh.home_click()

    def profile(self):
        mh.profile_click()

    def publish_page(self):
        mh.publish_click()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())