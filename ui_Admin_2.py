# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_1niYxoU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 533)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"color:#fff;\n"
"}\n"
"#centralwidget{\n"
"background-color:#040f13;\n"
"border-color:5px;\n"
"}\n"
"#main_body_frame{\n"
"background-color:#040f13;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"#body_left_frame{\n"
"background-color:#040f13;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"#body_right_frame{\n"
"background-color:#040f13;\n"
"border-radius:20px;\n"
"}\n"
"QPushbutton{\n"
"padding:10px;\n"
"background-color:#040f13;\n"
"border-radius:5px;\n"
"}\n"
"#close_window_button:pressed,#minimize_window_button:pressed,#restore_window_bottom:pressed,#menu_open_close_btn:pressed,#info_btn:pressed,#notification_closed_btn_1:pressed{\n"
"padding-left:3px;\n"
"padding-bottom:3px;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"#add_new_base_btn:hover, #base_statistic_btn:hover, #exists_bases_btn:hover{\n"
"padding-right:2px;\n"
"border-radius:5px;\n"
"background-color:#071e26;\n"
"}\n"
"\n"
"#add_new_base_btn:pressed, #base_statistic_btn:pressed, #exists_bases_btn:pres"
                        "sed{\n"
"padding-left:3px;\n"
"padding-bottom:3px;\n"
"}\n"
"\n"
"#new_base_save_btn:hover{\n"
"padding-right:2px;\n"
"border-radius:5px;\n"
"border:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.926, stop:0 rgba(83, 235, 0, 150), stop:1 rgba(80, 85, 255, 150));\n"
"}\n"
"\n"
"#new_base_save_btn:pressed{\n"
"padding-left:3px;\n"
"padding-bottom:3px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        self.header_frame.setFont(font)
        self.header_frame.setStyleSheet(u"")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.header_left_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.menu_open_close_btn = QPushButton(self.header_left_frame)
        self.menu_open_close_btn.setObjectName(u"menu_open_close_btn")
        self.menu_open_close_btn.setMaximumSize(QSize(15154, 11155))
        font1 = QFont()
        font1.setFamily(u"Narkisim")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.menu_open_close_btn.setFont(font1)
        self.menu_open_close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_open_close_btn.setIcon(icon)
        self.menu_open_close_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.menu_open_close_btn, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.header_center_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 0)
        self.label_5 = QLabel(self.header_center_frame)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamily(u"Narkisim")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignTop)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setStyleSheet(u"")
        self.main_body_frame.setFrameShape(QFrame.Box)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 5, 0)
        self.body_left_frame = QCustomSlideMenu(self.main_body_frame)
        self.body_left_frame.setObjectName(u"body_left_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body_left_frame.sizePolicy().hasHeightForWidth())
        self.body_left_frame.setSizePolicy(sizePolicy1)
        self.body_left_frame.setMinimumSize(QSize(50, 0))
        self.body_left_frame.setMaximumSize(QSize(50, 16777215))
        self.body_left_frame.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout_4 = QVBoxLayout(self.body_left_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.body_left_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setMaximumSize(QSize(200, 16777215))
        self.menu_frame.setStyleSheet(u"border-radius:10px;")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 10, 0, 0)
        self.add_new_base_btn = QPushButton(self.menu_frame)
        self.add_new_base_btn.setObjectName(u"add_new_base_btn")
        self.add_new_base_btn.setMinimumSize(QSize(175, 30))
        font3 = QFont()
        font3.setFamily(u"Narkisim")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.add_new_base_btn.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_new_base_btn.setIcon(icon4)
        self.add_new_base_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.add_new_base_btn)

        self.exists_bases_btn = QPushButton(self.menu_frame)
        self.exists_bases_btn.setObjectName(u"exists_bases_btn")
        self.exists_bases_btn.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.exists_bases_btn.sizePolicy().hasHeightForWidth())
        self.exists_bases_btn.setSizePolicy(sizePolicy2)
        self.exists_bases_btn.setMinimumSize(QSize(175, 30))
        self.exists_bases_btn.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Narkisim")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.exists_bases_btn.setFont(font4)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exists_bases_btn.setIcon(icon5)
        self.exists_bases_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.exists_bases_btn)

        self.base_statistic_btn = QPushButton(self.menu_frame)
        self.base_statistic_btn.setObjectName(u"base_statistic_btn")
        self.base_statistic_btn.setMinimumSize(QSize(175, 30))
        self.base_statistic_btn.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.base_statistic_btn.setIcon(icon6)
        self.base_statistic_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.base_statistic_btn)


        self.verticalLayout_4.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame = QFrame(self.body_left_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_5.addWidget(self.body_left_frame)

        self.body_right_frame = QFrame(self.main_body_frame)
        self.body_right_frame.setObjectName(u"body_right_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.body_right_frame.sizePolicy().hasHeightForWidth())
        self.body_right_frame.setSizePolicy(sizePolicy3)
        self.body_right_frame.setStyleSheet(u"background-color:#071e26;\n"
"border-radius:10px;\n"
"")
        self.body_right_frame.setFrameShape(QFrame.StyledPanel)
        self.body_right_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.body_right_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.body_right_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setStyleSheet(u"border-radius:10px;")
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.main_null_widget = QWidget()
        self.main_null_widget.setObjectName(u"main_null_widget")
        sizePolicy.setHeightForWidth(self.main_null_widget.sizePolicy().hasHeightForWidth())
        self.main_null_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.main_null_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_7 = QFrame(self.main_null_widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)
        self.label_21.setMinimumSize(QSize(200, 80))
        font5 = QFont()
        font5.setFamily(u"Vani")
        font5.setPointSize(15)
        self.label_21.setFont(font5)

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1, Qt.AlignRight)

        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        sizePolicy5.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy5)
        self.label_22.setMinimumSize(QSize(30, 30))
        self.label_22.setMaximumSize(QSize(30, 30))
        self.label_22.setPixmap(QPixmap(u":/icons/icons/arrow-down-circle.svg"))

        self.gridLayout_3.addWidget(self.label_22, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        font6 = QFont()
        font6.setFamily(u"Modern No. 20")
        font6.setPointSize(34)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_20.setFont(font6)
        self.label_20.setStyleSheet(u"color: rgba(60, 255, 16, 155);")

        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 2)


        self.verticalLayout_10.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.main_null_widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.frame_6.setStyleSheet(u"QPushButton:hover{\n"
"	color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.926, stop:0 rgba(0, 241, 0, 18), stop:1 rgba(0, 255, 255, 21));\n"
"\n"
"padding-right:4px;\n"
"padding-bottom:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"	color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"/*	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.926, stop:0 rgba(0, 241, 0, 38), stop:1 rgba(0, 255, 255, 41));\n"
"*/\n"
"padding-left:3px;\n"
"padding-top:2px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.add_new_base_btn_2 = QPushButton(self.frame_6)
        self.add_new_base_btn_2.setObjectName(u"add_new_base_btn_2")
        self.add_new_base_btn_2.setMinimumSize(QSize(175, 30))
        self.add_new_base_btn_2.setFont(font3)
        self.add_new_base_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_new_base_btn_2.setIcon(icon4)
        self.add_new_base_btn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.add_new_base_btn_2)

        self.exists_bases_btn_2 = QPushButton(self.frame_6)
        self.exists_bases_btn_2.setObjectName(u"exists_bases_btn_2")
        self.exists_bases_btn_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.exists_bases_btn_2.sizePolicy().hasHeightForWidth())
        self.exists_bases_btn_2.setSizePolicy(sizePolicy2)
        self.exists_bases_btn_2.setMinimumSize(QSize(175, 30))
        self.exists_bases_btn_2.setSizeIncrement(QSize(0, 0))
        self.exists_bases_btn_2.setFont(font4)
        self.exists_bases_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.exists_bases_btn_2.setIcon(icon5)
        self.exists_bases_btn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.exists_bases_btn_2)

        self.base_statistic_btn_2 = QPushButton(self.frame_6)
        self.base_statistic_btn_2.setObjectName(u"base_statistic_btn_2")
        self.base_statistic_btn_2.setMinimumSize(QSize(175, 30))
        self.base_statistic_btn_2.setFont(font3)
        self.base_statistic_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.base_statistic_btn_2.setIcon(icon6)
        self.base_statistic_btn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.base_statistic_btn_2)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_8 = QFrame(self.main_null_widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.main_null_widget)
        self.create_new_base_widget = QWidget()
        self.create_new_base_widget.setObjectName(u"create_new_base_widget")
        self.verticalLayout_5 = QVBoxLayout(self.create_new_base_widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.notification_widget = QWidget(self.create_new_base_widget)
        self.notification_widget.setObjectName(u"notification_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.notification_widget.sizePolicy().hasHeightForWidth())
        self.notification_widget.setSizePolicy(sizePolicy7)
        self.notification_widget.setMinimumSize(QSize(0, 0))
        self.notification_widget.setMaximumSize(QSize(16777215, 0))
        self.notification_widget.setStyleSheet(u"#notification_widget{\n"
"\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(0, 255, 0);}\n"
"\n"
"*{	background-color: rgb(1, 154, 136);}")
        self.horizontalLayout_6 = QHBoxLayout(self.notification_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_19 = QLabel(self.notification_widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_6.addWidget(self.label_19)

        self.label_18 = QLabel(self.notification_widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(30, 30))
        self.label_18.setPixmap(QPixmap(u":/icons/icons/check-circle (3).svg"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_18, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_17 = QLabel(self.notification_widget)
        self.label_17.setObjectName(u"label_17")
        font7 = QFont()
        font7.setPointSize(17)
        self.label_17.setFont(font7)

        self.horizontalLayout_6.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.notification_closed_btn_1 = QPushButton(self.notification_widget)
        self.notification_closed_btn_1.setObjectName(u"notification_closed_btn_1")
        self.notification_closed_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.notification_closed_btn_1.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-up-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notification_closed_btn_1.setIcon(icon7)

        self.horizontalLayout_6.addWidget(self.notification_closed_btn_1, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.notification_widget)

        self.create_new_base_frame = QFrame(self.create_new_base_widget)
        self.create_new_base_frame.setObjectName(u"create_new_base_frame")
        self.create_new_base_frame.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.create_new_base_frame.sizePolicy().hasHeightForWidth())
        self.create_new_base_frame.setSizePolicy(sizePolicy3)
        self.create_new_base_frame.setFrameShape(QFrame.StyledPanel)
        self.create_new_base_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.create_new_base_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, -1, -1, 15)
        self.label_12 = QLabel(self.create_new_base_frame)
        self.label_12.setObjectName(u"label_12")
        font8 = QFont()
        font8.setFamily(u"Palatino Linotype")
        font8.setPointSize(12)
        self.label_12.setFont(font8)

        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(180, 0))
        self.lineEdit_11.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_11.setFont(font8)
        self.lineEdit_11.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_11.setMaxLength(35)
        self.lineEdit_11.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_11, 2, 4, 1, 1)

        self.label_7 = QLabel(self.create_new_base_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font8)

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.new_base_save_btn = QPushButton(self.create_new_base_frame)
        self.new_base_save_btn.setObjectName(u"new_base_save_btn")
        self.new_base_save_btn.setMinimumSize(QSize(0, 30))
        self.new_base_save_btn.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setFamily(u"Lucida Fax")
        font9.setPointSize(15)
        font9.setBold(True)
        font9.setWeight(75)
        self.new_base_save_btn.setFont(font9)
        self.new_base_save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_base_save_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.new_base_save_btn.setIcon(icon8)
        self.new_base_save_btn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.new_base_save_btn, 9, 4, 1, 1)

        self.label_9 = QLabel(self.create_new_base_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font8)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.user_login = QLineEdit(self.create_new_base_frame)
        self.user_login.setObjectName(u"user_login")
        self.user_login.setMinimumSize(QSize(180, 0))
        self.user_login.setMaximumSize(QSize(300, 16777215))
        self.user_login.setFont(font8)
        self.user_login.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.user_login.setMaxLength(35)
        self.user_login.setCursorPosition(0)

        self.gridLayout.addWidget(self.user_login, 6, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(180, 0))
        self.lineEdit_7.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_7.setFont(font8)
        self.lineEdit_7.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_7.setMaxLength(35)
        self.lineEdit_7.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_7, 5, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(180, 0))
        self.lineEdit_5.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_5.setFont(font8)
        self.lineEdit_5.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_5.setMaxLength(35)
        self.lineEdit_5.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_5, 4, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(180, 0))
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_2.setFont(font8)
        self.lineEdit_2.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_2.setMaxLength(35)
        self.lineEdit_2.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.label_6 = QLabel(self.create_new_base_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_13 = QLabel(self.create_new_base_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)

        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)

        self.label_8 = QLabel(self.create_new_base_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font8)

        self.gridLayout.addWidget(self.label_8, 4, 3, 1, 1)

        self.label_15 = QLabel(self.create_new_base_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_15, 5, 2, 1, 1)

        self.label_2 = QLabel(self.create_new_base_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(180, 0))
        self.lineEdit_6.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_6.setFont(font8)
        self.lineEdit_6.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_6.setMaxLength(35)
        self.lineEdit_6.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(180, 0))
        self.lineEdit_3.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3.setFont(font8)
        self.lineEdit_3.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_3.setMaxLength(35)
        self.lineEdit_3.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_3, 3, 4, 1, 1)

        self.label_14 = QLabel(self.create_new_base_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font8)

        self.gridLayout.addWidget(self.label_14, 8, 0, 1, 1)

        self.pass_test_lb2 = QLabel(self.create_new_base_frame)
        self.pass_test_lb2.setObjectName(u"pass_test_lb2")
        self.pass_test_lb2.setMinimumSize(QSize(25, 25))
        self.pass_test_lb2.setMaximumSize(QSize(25, 25))
        self.pass_test_lb2.setTextFormat(Qt.AutoText)
        self.pass_test_lb2.setPixmap(QPixmap(u":/icons/icons/null.svg"))
        self.pass_test_lb2.setScaledContents(True)

        self.gridLayout.addWidget(self.pass_test_lb2, 8, 2, 1, 1)

        self.label_10 = QLabel(self.create_new_base_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font8)

        self.gridLayout.addWidget(self.label_10, 5, 3, 1, 1)

        self.user_password2 = QLineEdit(self.create_new_base_frame)
        self.user_password2.setObjectName(u"user_password2")
        self.user_password2.setMinimumSize(QSize(180, 0))
        self.user_password2.setMaximumSize(QSize(300, 16777215))
        self.user_password2.setFont(font8)
        self.user_password2.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.user_password2.setMaxLength(35)
        self.user_password2.setEchoMode(QLineEdit.Password)
        self.user_password2.setCursorPosition(0)

        self.gridLayout.addWidget(self.user_password2, 8, 1, 1, 1)

        self.lineEdit = QLineEdit(self.create_new_base_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(180, 0))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setFont(font8)
        self.lineEdit.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit.setMaxLength(35)
        self.lineEdit.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_16 = QLabel(self.create_new_base_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font8)

        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)

        self.user_password1 = QLineEdit(self.create_new_base_frame)
        self.user_password1.setObjectName(u"user_password1")
        self.user_password1.setMinimumSize(QSize(180, 0))
        self.user_password1.setMaximumSize(QSize(300, 16777215))
        self.user_password1.setFont(font8)
        self.user_password1.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.user_password1.setMaxLength(35)
        self.user_password1.setEchoMode(QLineEdit.Password)
        self.user_password1.setCursorPosition(0)

        self.gridLayout.addWidget(self.user_password1, 7, 1, 1, 1)

        self.pass_test_lb1 = QLabel(self.create_new_base_frame)
        self.pass_test_lb1.setObjectName(u"pass_test_lb1")
        self.pass_test_lb1.setMinimumSize(QSize(25, 25))
        self.pass_test_lb1.setMaximumSize(QSize(25, 25))
        self.pass_test_lb1.setTextFormat(Qt.AutoText)
        self.pass_test_lb1.setPixmap(QPixmap(u":/icons/icons/null.svg"))
        self.pass_test_lb1.setScaledContents(True)

        self.gridLayout.addWidget(self.pass_test_lb1, 7, 2, 1, 1)

        self.label_11 = QLabel(self.create_new_base_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font8)

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.create_new_base_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(180, 0))
        self.lineEdit_4.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_4.setFont(font8)
        self.lineEdit_4.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(164, 255, 232, 10);\n"
"")
        self.lineEdit_4.setMaxLength(35)
        self.lineEdit_4.setCursorPosition(0)

        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.frame_2 = QFrame(self.create_new_base_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 15, -1, 40)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font10 = QFont()
        font10.setFamily(u"MS Mincho")
        font10.setPointSize(19)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_3.setFont(font10)
        self.label_3.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_9.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 2, 5)


        self.verticalLayout_5.addWidget(self.create_new_base_frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.create_new_base_widget)
        self.exists_bases_widget = QWidget()
        self.exists_bases_widget.setObjectName(u"exists_bases_widget")
        self.gridLayout_4 = QGridLayout(self.exists_bases_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.exsist_base_left_frame = QFrame(self.exists_bases_widget)
        self.exsist_base_left_frame.setObjectName(u"exsist_base_left_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.exsist_base_left_frame.sizePolicy().hasHeightForWidth())
        self.exsist_base_left_frame.setSizePolicy(sizePolicy8)
        self.exsist_base_left_frame.setMaximumSize(QSize(250, 16777215))
        self.exsist_base_left_frame.setStyleSheet(u"")
        self.exsist_base_left_frame.setFrameShape(QFrame.StyledPanel)
        self.exsist_base_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.exsist_base_left_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_23 = QLabel(self.exsist_base_left_frame)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_23.setFont(font11)

        self.verticalLayout_13.addWidget(self.label_23)

        self.scrollArea = QScrollArea(self.exsist_base_left_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy9)
        self.scrollArea.setMinimumSize(QSize(230, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setStyleSheet(u"*{\n"
"border: 2px solid rgb(48, 72, 93);}\n"
"QPushButton:hover{\n"
"padding-right:2px;\n"
"padding-bottom:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:2px;\n"
"padding-top:3px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 209, 588))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.first_base_btn_13 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_13.setObjectName(u"first_base_btn_13")
        self.first_base_btn_13.setMinimumSize(QSize(175, 30))
        self.first_base_btn_13.setFont(font3)
        self.first_base_btn_13.setIcon(icon5)
        self.first_base_btn_13.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_13)

        self.first_base_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn.setObjectName(u"first_base_btn")
        self.first_base_btn.setMinimumSize(QSize(175, 30))
        self.first_base_btn.setFont(font3)
        self.first_base_btn.setIcon(icon5)
        self.first_base_btn.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn)

        self.first_base_btn_12 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_12.setObjectName(u"first_base_btn_12")
        self.first_base_btn_12.setMinimumSize(QSize(175, 30))
        self.first_base_btn_12.setFont(font3)
        self.first_base_btn_12.setIcon(icon5)
        self.first_base_btn_12.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_12)

        self.first_base_btn_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_2.setObjectName(u"first_base_btn_2")
        self.first_base_btn_2.setMinimumSize(QSize(175, 30))
        self.first_base_btn_2.setFont(font3)
        self.first_base_btn_2.setIcon(icon5)
        self.first_base_btn_2.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_2)

        self.first_base_btn_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_3.setObjectName(u"first_base_btn_3")
        self.first_base_btn_3.setMinimumSize(QSize(175, 30))
        self.first_base_btn_3.setFont(font3)
        self.first_base_btn_3.setIcon(icon5)
        self.first_base_btn_3.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_3)

        self.first_base_btn_4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_4.setObjectName(u"first_base_btn_4")
        self.first_base_btn_4.setMinimumSize(QSize(175, 30))
        self.first_base_btn_4.setFont(font3)
        self.first_base_btn_4.setIcon(icon5)
        self.first_base_btn_4.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_4)

        self.first_base_btn_15 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_15.setObjectName(u"first_base_btn_15")
        self.first_base_btn_15.setMinimumSize(QSize(175, 30))
        self.first_base_btn_15.setFont(font3)
        self.first_base_btn_15.setIcon(icon5)
        self.first_base_btn_15.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_15)

        self.first_base_btn_16 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_16.setObjectName(u"first_base_btn_16")
        self.first_base_btn_16.setMinimumSize(QSize(175, 30))
        self.first_base_btn_16.setFont(font3)
        self.first_base_btn_16.setIcon(icon5)
        self.first_base_btn_16.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_16)

        self.first_base_btn_14 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_14.setObjectName(u"first_base_btn_14")
        self.first_base_btn_14.setMinimumSize(QSize(175, 30))
        self.first_base_btn_14.setFont(font3)
        self.first_base_btn_14.setIcon(icon5)
        self.first_base_btn_14.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_14)

        self.first_base_btn_5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_5.setObjectName(u"first_base_btn_5")
        self.first_base_btn_5.setMinimumSize(QSize(175, 30))
        self.first_base_btn_5.setFont(font3)
        self.first_base_btn_5.setIcon(icon5)
        self.first_base_btn_5.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_5)

        self.first_base_btn_6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_6.setObjectName(u"first_base_btn_6")
        self.first_base_btn_6.setMinimumSize(QSize(175, 30))
        self.first_base_btn_6.setFont(font3)
        self.first_base_btn_6.setIcon(icon5)
        self.first_base_btn_6.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_6)

        self.first_base_btn_7 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_7.setObjectName(u"first_base_btn_7")
        self.first_base_btn_7.setMinimumSize(QSize(175, 30))
        self.first_base_btn_7.setFont(font3)
        self.first_base_btn_7.setIcon(icon5)
        self.first_base_btn_7.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_7)

        self.first_base_btn_11 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_11.setObjectName(u"first_base_btn_11")
        self.first_base_btn_11.setMinimumSize(QSize(175, 30))
        self.first_base_btn_11.setFont(font3)
        self.first_base_btn_11.setIcon(icon5)
        self.first_base_btn_11.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_11)

        self.first_base_btn_8 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_8.setObjectName(u"first_base_btn_8")
        self.first_base_btn_8.setMinimumSize(QSize(175, 30))
        self.first_base_btn_8.setFont(font3)
        self.first_base_btn_8.setIcon(icon5)
        self.first_base_btn_8.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_8)

        self.first_base_btn_10 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_10.setObjectName(u"first_base_btn_10")
        self.first_base_btn_10.setMinimumSize(QSize(175, 30))
        self.first_base_btn_10.setFont(font3)
        self.first_base_btn_10.setIcon(icon5)
        self.first_base_btn_10.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_10)

        self.first_base_btn_9 = QPushButton(self.scrollAreaWidgetContents_2)
        self.first_base_btn_9.setObjectName(u"first_base_btn_9")
        self.first_base_btn_9.setMinimumSize(QSize(175, 30))
        self.first_base_btn_9.setFont(font3)
        self.first_base_btn_9.setIcon(icon5)
        self.first_base_btn_9.setIconSize(QSize(20, 24))

        self.verticalLayout_11.addWidget(self.first_base_btn_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.exsist_base_left_frame, 0, 0, 1, 1, Qt.AlignLeft)

        self.frame_3 = QFrame(self.exists_bases_widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.exists_bases_widget)
        self.statistic_widget = QWidget()
        self.statistic_widget.setObjectName(u"statistic_widget")
        self.label_4 = QLabel(self.statistic_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 40, 131, 31))
        self.stackedWidget.addWidget(self.statistic_widget)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.body_right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 2)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.footer_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(15, 10))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.info_btn = QPushButton(self.frame_5)
        self.info_btn.setObjectName(u"info_btn")
        self.info_btn.setMaximumSize(QSize(20, 20))
        self.info_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.info_btn)


        self.horizontalLayout_2.addWidget(self.frame_5, 0, Qt.AlignRight|Qt.AlignBottom)

        self.grid_frame = QFrame(self.footer_frame)
        self.grid_frame.setObjectName(u"grid_frame")
        self.grid_frame.setMinimumSize(QSize(10, 10))
        self.grid_frame.setMaximumSize(QSize(10, 10))
        self.grid_frame.setFrameShape(QFrame.StyledPanel)
        self.grid_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.grid_frame, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_open_close_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Admin Pages", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.add_new_base_btn.setText(QCoreApplication.translate("MainWindow", u"    ADD NEW BASE ", None))
        self.exists_bases_btn.setText(QCoreApplication.translate("MainWindow", u"     EXISTS BASES   ", None))
        self.base_statistic_btn.setText(QCoreApplication.translate("MainWindow", u"      STATISTIC        ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Choose the menu", None))
        self.label_22.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Hi, Jaloliddin", None))
        self.add_new_base_btn_2.setText(QCoreApplication.translate("MainWindow", u"    ADD NEW BASE ", None))
        self.exists_bases_btn_2.setText(QCoreApplication.translate("MainWindow", u"     EXISTS BASES   ", None))
        self.base_statistic_btn_2.setText(QCoreApplication.translate("MainWindow", u"      STATISTIC        ", None))
        self.label_19.setText("")
        self.label_18.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Saved Succesfully", None))
        self.notification_closed_btn_1.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Number Of Stores", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.new_base_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Passport (S/N)", None))
        self.user_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's Login", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's Email Adress", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's  Adress", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's First Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.label_15.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name Base", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's Telephone Number", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's Last Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Coniform Password", None))
        self.pass_test_lb2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.user_password2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coniform Password", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Base Name", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Number Stores", None))
        self.user_password1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's Password", None))
        self.pass_test_lb1.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Telephone", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User's Passport (S/N)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Adding New Base", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Exists Bases", None))
        self.first_base_btn_13.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_12.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_2.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_3.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_4.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_15.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_16.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_14.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_5.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_6.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_7.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_11.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_8.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_10.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.first_base_btn_9.setText(QCoreApplication.translate("MainWindow", u"First Base", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"statistic_widget", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  Version 1.0 | @CopyRight", None))
        self.info_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

