from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.main_window import *
import user_interface.event_handlers.main_handler as mh

def clear_profile(window):
    for frame in window.user_posts:
        frame.deleteLater()
        window.user_posts = window.user_posts[:-1]
    window.user_post_number = 0
    window.user_profile_likes = []

def load_profile(window, username):
    clear_profile(window)
    window.ui.profile_username.setText(username)
    window.other_user = username
    window.ui.stackedWidget.setCurrentIndex(2)
    info = mh.profile_click(window, username)
    description = info[0]
    window.is_followed = info[1]
    posts = info[2]
    window.ui.textBrowser_2.setText(description)
    if(window.is_followed):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.ui.add_button.setIcon(icon)
        window.ui.add_button.setText("Unfollow")
    else:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/user-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.ui.add_button.setIcon(icon)
        window.ui.add_button.setText("Follow")
    for post in posts:
        load_profile_post(window, window.other_user, post[1], post[2], "1", False, post[3])
        
def load_profile_post(window, username, description, likes, post_id, is_liked, img_path):
    current_index = window.user_post_number
    window.user_profile_likes.append([is_liked, likes])
    window.post_frame = QtWidgets.QFrame(window.ui.scrollAreaWidgetContents_profile)
    window.post_frame.setMaximumSize(QtCore.QSize(16777215, 700))
    window.post_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.post_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    window.post_frame.setObjectName("post_frame")
    window.horizontalLayout_6 = QtWidgets.QHBoxLayout(window.post_frame)
    window.horizontalLayout_6.setContentsMargins(6, 6, -1, -1)
    window.horizontalLayout_6.setObjectName("horizontalLayout_6")
    window.frame_7 = QtWidgets.QFrame(window.post_frame)
    window.frame_7.setMinimumSize(QtCore.QSize(150, 0))
    window.frame_7.setMaximumSize(QtCore.QSize(150, 16777215))
    window.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
    window.frame_7.setObjectName("frame_7")
    window.horizontalLayout_6.addWidget(window.frame_7)
    window.post_main_frame = QtWidgets.QFrame(window.post_frame)
    window.post_main_frame.setMaximumSize(QtCore.QSize(700, 16777215))
    window.post_main_frame.setStyleSheet("background-color: rgb(34, 34, 34); border-radius: 5px;")
    window.post_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    window.post_main_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
    window.post_main_frame.setObjectName("post_main_frame")
    window.verticalLayout_4 = QtWidgets.QVBoxLayout(window.post_main_frame)
    window.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
    window.verticalLayout_4.setSpacing(0)
    window.verticalLayout_4.setObjectName("verticalLayout_4")
    window.post_user_frame = QtWidgets.QFrame(window.post_main_frame)
    window.post_user_frame.setMaximumSize(QtCore.QSize(16777215, 50))
    window.post_user_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.post_user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    window.post_user_frame.setObjectName("post_user_frame")
    window.verticalLayout_6 = QtWidgets.QVBoxLayout(window.post_user_frame)
    window.verticalLayout_6.setObjectName("verticalLayout_6")
    window.feed_username_button = QtWidgets.QPushButton(window.post_user_frame)
    window.feed_username_button.setStyleSheet("background-color: rgb(34, 34, 34); color: rgb(255, 255, 255)")
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(":/images/images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    window.feed_username_button.setIcon(icon5)
    window.feed_username_button.setFlat(True)
    window.feed_username_button.setObjectName("feed_username_button")
    window.feed_username_button.setText(username)
    window.verticalLayout_6.addWidget(window.feed_username_button)
    window.verticalLayout_4.addWidget(window.post_user_frame)
    window.post_image_frame = QtWidgets.QFrame(window.post_main_frame)
    window.post_image_frame.setMinimumSize(QtCore.QSize(0, 300))
    window.post_image_frame.setMaximumSize(QtCore.QSize(16777215, 800))
    window.post_image_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
    window.post_image_frame.setStyleSheet("image: url("+img_path+");")
    window.post_image_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.post_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    window.post_image_frame.setObjectName("post_image_frame")
    window.verticalLayout_4.addWidget(window.post_image_frame)
    window.post_description_frame = QtWidgets.QFrame(window.post_main_frame)
    window.post_description_frame.setMaximumSize(QtCore.QSize(16777215, 80))
    window.post_description_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.post_description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    window.post_description_frame.setObjectName("post_description_frame")
    window.verticalLayout_5 = QtWidgets.QVBoxLayout(window.post_description_frame)
    window.verticalLayout_5.setObjectName("verticalLayout_5")
    window.textBrowser = QtWidgets.QTextBrowser(window.post_description_frame)
    window.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
    window.textBrowser.setObjectName("textBrowser")
    window.textBrowser.setText(description)
    window.verticalLayout_5.addWidget(window.textBrowser)
    window.verticalLayout_4.addWidget(window.post_description_frame)
    window.frame_16 = QtWidgets.QFrame(window.post_main_frame)
    window.frame_16.setMinimumSize(QtCore.QSize(0, 30))
    window.frame_16.setMaximumSize(QtCore.QSize(16777215, 30))
    window.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
    window.frame_16.setObjectName("frame_16")
    window.horizontalLayout_10 = QtWidgets.QHBoxLayout(window.frame_16)
    window.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
    window.horizontalLayout_10.setSpacing(0)
    window.horizontalLayout_10.setObjectName("horizontalLayout_10")
    window.frame_17 = QtWidgets.QFrame(window.frame_16)
    window.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
    window.frame_17.setObjectName("frame_17")
    window.verticalLayout_21 = QtWidgets.QVBoxLayout(window.frame_17)
    window.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
    window.verticalLayout_21.setSpacing(0)
    window.verticalLayout_21.setObjectName("verticalLayout_21")
    window.comments_button = QtWidgets.QPushButton(window.frame_17)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    window.comments_button.setFont(font)
    window.comments_button.setStyleSheet("color: rgb(255, 255, 255);")
    window.comments_button.setFlat(True)
    window.comments_button.setObjectName("comments_button")
    window.comments_button.setText("See Comments")
    window.verticalLayout_21.addWidget(window.comments_button)
    window.horizontalLayout_10.addWidget(window.frame_17, 0, QtCore.Qt.AlignLeft)
    window.frame_18 = QtWidgets.QFrame(window.frame_16)
    window.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
    window.frame_18.setObjectName("frame_18")
    window.verticalLayout_22 = QtWidgets.QVBoxLayout(window.frame_18)
    window.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
    window.verticalLayout_22.setSpacing(0)
    window.verticalLayout_22.setObjectName("verticalLayout_22")
    window.like_button = QtWidgets.QPushButton(window.frame_18)
    window.like_button.setStyleSheet("color: rgb(255, 255, 255);")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/images/images/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(":/images/images/filled-heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    if(window.user_profile_likes[current_index][0]):
        window.like_button.setIcon(icon2)
    else:
        window.like_button.setIcon(icon1)
    window.like_button.setFlat(True)
    window.like_button.setObjectName("like_button")
    window.like_button.setText(str(window.user_profile_likes[current_index][1]))
    window.user_profile_likes[current_index].append(window.like_button)
    window.like_button.clicked.connect(lambda: user_profile_like_button(window, current_index, window.user_profile_likes[current_index][2], post_id))
    window.verticalLayout_22.addWidget(window.like_button)
    window.horizontalLayout_10.addWidget(window.frame_18, 0, QtCore.Qt.AlignRight)
    window.verticalLayout_4.addWidget(window.frame_16)
    window.horizontalLayout_6.addWidget(window.post_main_frame)
    window.frame_9 = QtWidgets.QFrame(window.post_frame)
    window.frame_9.setMinimumSize(QtCore.QSize(150, 0))
    window.frame_9.setMaximumSize(QtCore.QSize(150, 16777215))
    window.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
    window.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
    window.frame_9.setObjectName("frame_9")
    window.horizontalLayout_6.addWidget(window.frame_9)
    window.ui.gridLayout_user.addWidget(window.post_frame, window.user_post_number, 0, 1, 1)
    window.user_post_number += 1
    window.user_posts.append(window.post_frame)

def follow(window, username):
    if(window.is_followed):
        #mh.unfollow_user(window.username, username)
        #window.is_followed = False
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(":/images/images/user-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #window.ui.add_button.setIcon(icon)
        #window.ui.add_button.setText("Follow")
        pass
    else:
        mh.follow_user(window, username)
        window.is_followed = True
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.ui.add_button.setIcon(icon)
        window.ui.add_button.setText("Unfollow")

def user_profile_like_button(window, index, current_like_button, post_id):
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/images/images/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(":/images/images/filled-heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    if(window.user_profile_likes[index][0]):
        mh.unliked_post(window.username, post_id)
        window.user_profile_likes[index][0] = False
        current_like_button.setIcon(icon1)
        window.user_profile_likes[index][1] -= 1
        current_like_button.setText(str(window.user_profile_likes[index][1]))
    else:
        mh.liked_post(window.username, post_id)
        window.user_profile_likes[index][0] = True
        current_like_button.setIcon(icon2)
        window.user_profile_likes[index][1] += 1
        current_like_button.setText(str(window.user_profile_likes[index][1]))