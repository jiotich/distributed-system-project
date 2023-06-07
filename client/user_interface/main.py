import sys
sys.dont_write_bytecode = True
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui
from login_window import *
from main_window import *
import event_handlers.login_handler as lh
from frame_loaders.main_window_loader import change_to_main_window

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
        self.feed_posts = []
        self.self_posts = []
        self.user_posts = []
        self.search_results = []
        self.post_number = 0
        self.self_post_number = 0
        self.user_post_number = 0
        self.search_result_number = 0
        self.is_maximized = False
        self.username = ""
        self.description = ""
        self.is_followed = False
        self.image_path = ""
        self.other_user = ""
        self.feed_likes = []
        self.self_profile_likes = []
        self.user_profile_likes = []

    def login(self):
        username = self.ui.login_username.text()
        password = self.ui.login_password.text()
        if (username == "" or password == ""):
            self.pop_up("All fields must be filled.             ")
            self.ui.login_username.setText("")
            self.ui.login_password.setText("")
            return
        is_logged_in = lh.login_clicked(username, password)
        if (is_logged_in):
            self.username = username
            change_to_main_window(self)
        else:
            self.pop_up("Login error: Invalid credentials.")
            self.ui.login_username.setText("")
            self.ui.login_password.setText("")

    def signin(self):
        username = self.ui.signin_username.text()
        password = self.ui.signin_password.text()
        password_confirmation = self.ui.signin_confirm_password.text()
        if (username == "" or password == "" or password_confirmation == ""):
            self.pop_up("All fields must be filled.             ")
            return
        if (password != password_confirmation):
            self.pop_up("Password confirmation error.        ")
            return
        lh.signin_clicked(username, password)

    def pop_up(self, message):
        msg = QMessageBox(parent=self)
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("background-color: rgb(21, 21, 21);")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
