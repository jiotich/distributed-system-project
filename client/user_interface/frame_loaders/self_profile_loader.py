from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import *
import event_handlers.main_handler as mh

def clear_self_profile(window):
    for frame in window.self_posts:
        frame.deleteLater()
        window.self_posts = window.self_posts[:-1]
    window.self_post_number = 0
    window.self_profile_likes = []

def load_self_profile(window, description, likes, post_id, is_liked, img_path):
    current_index = window.self_post_number
    window.self_profile_likes.append([is_liked, likes])
    window.post_frame = QtWidgets.QFrame(window.ui.scrollAreaWidgetContents_3)
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
    window.feed_username_button.setText(window.username)
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
    if(window.self_profile_likes[current_index][0]):
        window.like_button.setIcon(icon2)
    else:
        window.like_button.setIcon(icon1)
    window.like_button.setFlat(True)
    window.like_button.setObjectName("like_button")
    window.like_button.setText(str(window.self_profile_likes[current_index][1]))
    window.self_profile_likes[current_index].append(window.like_button)
    window.like_button.clicked.connect(lambda: self_profile_like_button(window, current_index, window.self_profile_likes[current_index][2], post_id))
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
    window.ui.gridLayout_self_profile.addWidget(window.post_frame, window.self_post_number, 0, 1, 1)
    window.self_post_number += 1
    window.self_posts.append(window.post_frame)
    
def edit_description(window):
    window.ui.edit_button.setEnabled(False)
    window.ui.confirm_edit_button.setEnabled(True)
    window.ui.cancel_edit_button.setEnabled(True)
    window.ui.textEdit.setReadOnly(False)

def confirm_edit(window):
    window.ui.edit_button.setEnabled(True)
    window.ui.confirm_edit_button.setEnabled(False)
    window.ui.cancel_edit_button.setEnabled(False)
    window.ui.textEdit.setReadOnly(True)
    window.description = window.ui.textEdit.toPlainText()
    mh.change_user_description(window.username, window.description)
    window.ui.textEdit.setPlainText(window.description)

def cancel_edit(window):
    window.ui.edit_button.setEnabled(True)
    window.ui.confirm_edit_button.setEnabled(False)
    window.ui.cancel_edit_button.setEnabled(False)
    window.ui.textEdit.setReadOnly(True)
    window.ui.textEdit.setPlainText(window.description)

def self_profile_like_button(window, index, current_like_button, post_id):
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/images/images/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(":/images/images/filled-heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    if(window.self_profile_likes[index][0]):
        mh.unliked_post(window.username, post_id)
        window.self_profile_likes[index][0] = False
        current_like_button.setIcon(icon1)
        window.self_profile_likes[index][1] -= 1
        current_like_button.setText(str(window.self_profile_likes[index][1]))
    else:
        mh.liked_post(window.username, post_id)
        window.self_profile_likes[index][0] = True
        current_like_button.setIcon(icon2)
        window.self_profile_likes[index][1] += 1
        current_like_button.setText(str(window.self_profile_likes[index][1]))