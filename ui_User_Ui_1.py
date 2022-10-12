# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Ui_1iRvFNN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 544)
        icon = QIcon()
        icon.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"color:#fff;\n"
"}\n"
"#centralwidget{\n"
"background-color:#040f13;\n"
"border-color:5px;\n"
"}\n"
"\n"
"#close_window_btn:hover, #minimize_window_btn:hover, #resize_window_btn:hover,#info_btn:hover{\n"
"padding-right:3px;\n"
"padding-top:2px;\n"
"} \n"
"\n"
"#close_window_btn:pressed, #minimize_window_btn:pressed, #resize_window_btn:pressed,#info_btn:pressed{\n"
"padding-left:3px;\n"
"padding-bottom:2px;\n"
"} ")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgba(175, 251, 255, 55);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_open_close_frame = QFrame(self.header_frame)
        self.menu_open_close_frame.setObjectName(u"menu_open_close_frame")
        self.menu_open_close_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_open_close_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_open_close_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_open_close_btn = QPushButton(self.menu_open_close_frame)
        self.menu_open_close_btn.setObjectName(u"menu_open_close_btn")
        font = QFont()
        font.setFamily(u"MS PMincho")
        font.setPointSize(14)
        self.menu_open_close_btn.setFont(font)
        self.menu_open_close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_open_close_btn.setIcon(icon1)
        self.menu_open_close_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.menu_open_close_btn, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.menu_open_close_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.name_frame = QFrame(self.header_frame)
        self.name_frame.setObjectName(u"name_frame")
        font1 = QFont()
        font1.setPointSize(12)
        self.name_frame.setFont(font1)
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.name_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.name_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"MS PMincho")
        font2.setPointSize(19)
        self.label.setFont(font2)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.name_frame, 0, Qt.AlignVCenter)

        self.components_frame = QFrame(self.header_frame)
        self.components_frame.setObjectName(u"components_frame")
        self.components_frame.setFrameShape(QFrame.StyledPanel)
        self.components_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.components_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.minimize_window_btn = QPushButton(self.components_frame)
        self.minimize_window_btn.setObjectName(u"minimize_window_btn")
        self.minimize_window_btn.setMaximumSize(QSize(28, 24))
        font3 = QFont()
        font3.setFamily(u"Music")
        self.minimize_window_btn.setFont(font3)
        self.minimize_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_btn.setIcon(icon2)
        self.minimize_window_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimize_window_btn)

        self.resize_window_btn = QPushButton(self.components_frame)
        self.resize_window_btn.setObjectName(u"resize_window_btn")
        self.resize_window_btn.setMaximumSize(QSize(24, 20))
        self.resize_window_btn.setFont(font3)
        self.resize_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_window_btn.setIcon(icon3)
        self.resize_window_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.resize_window_btn)

        self.close_window_btn = QPushButton(self.components_frame)
        self.close_window_btn.setObjectName(u"close_window_btn")
        self.close_window_btn.setMaximumSize(QSize(28, 24))
        self.close_window_btn.setFont(font3)
        self.close_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon4)
        self.close_window_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_window_btn)


        self.horizontalLayout.addWidget(self.components_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setStyleSheet(u"background-color: rgba(100, 15, 28, 155);\n"
"border-radius:20px ;")
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.main_body_left_frame = QFrame(self.main_body_frame)
        self.main_body_left_frame.setObjectName(u"main_body_left_frame")
        self.main_body_left_frame.setMinimumSize(QSize(200, 0))
        self.main_body_left_frame.setMaximumSize(QSize(200, 16777215))
        self.main_body_left_frame.setStyleSheet(u"background-color: rgb(152, 255, 164);")
        self.main_body_left_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_body_left_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.info_top_frame = QFrame(self.main_body_left_frame)
        self.info_top_frame.setObjectName(u"info_top_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_top_frame.sizePolicy().hasHeightForWidth())
        self.info_top_frame.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Narkisim")
        font4.setPointSize(15)
        self.info_top_frame.setFont(font4)
        self.info_top_frame.setStyleSheet(u"background-color: rgba(167, 144, 133, 155);")
        self.info_top_frame.setFrameShape(QFrame.StyledPanel)
        self.info_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.info_top_frame)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.info_top_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setMaximumSize(QSize(150, 50))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/airplay.svg"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.info_top_frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setPointSize(15)
        self.label_4.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.info_top_frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.info_top_frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.info_top_frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.info_top_frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.info_top_frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.info_top_frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_10)


        self.verticalLayout_5.addWidget(self.info_top_frame, 0, Qt.AlignTop)

        self.pushButton_7 = QPushButton(self.main_body_left_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)


        self.horizontalLayout_5.addWidget(self.main_body_left_frame, 0, Qt.AlignLeft)

        self.main_body_right_frame = QFrame(self.main_body_frame)
        self.main_body_right_frame.setObjectName(u"main_body_right_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body_right_frame.sizePolicy().hasHeightForWidth())
        self.main_body_right_frame.setSizePolicy(sizePolicy3)
        self.main_body_right_frame.setStyleSheet(u"background-color: rgba(149, 155, 103, 155);")
        self.main_body_right_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.main_body_right_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.main_body_menu_frame = QFrame(self.main_body_right_frame)
        self.main_body_menu_frame.setObjectName(u"main_body_menu_frame")
        sizePolicy1.setHeightForWidth(self.main_body_menu_frame.sizePolicy().hasHeightForWidth())
        self.main_body_menu_frame.setSizePolicy(sizePolicy1)
        self.main_body_menu_frame.setMinimumSize(QSize(180, 0))
        self.main_body_menu_frame.setMaximumSize(QSize(200, 16777215))
        font6 = QFont()
        font6.setPointSize(13)
        self.main_body_menu_frame.setFont(font6)
        self.main_body_menu_frame.setStyleSheet(u"QPushButton:hover{\n"
"padding-right:5px;\n"
"padding-top:3px;\n"
"	color: rgba(105, 211, 188, 155);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-bottom:3px;\n"
"	color: rgba(255, 181, 238, 255);\n"
"}\n"
"\n"
"*{\n"
"background-color: rgba(158, 253, 155, 155);\n"
"}")
        self.main_body_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_body_menu_frame)
        self.verticalLayout_8.setSpacing(17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 11, 0, 7)
        self.pushButton_6 = QPushButton(self.main_body_menu_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font7 = QFont()
        font7.setFamily(u"Narkisim")
        font7.setPointSize(16)
        self.pushButton_6.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.main_body_menu_frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.main_body_menu_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.main_body_menu_frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.main_body_menu_frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_12)

        self.pushButton_14 = QPushButton(self.main_body_menu_frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.main_body_menu_frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_13)

        self.pushButton_11 = QPushButton(self.main_body_menu_frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_11)

        self.pushButton_15 = QPushButton(self.main_body_menu_frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font7)

        self.verticalLayout_8.addWidget(self.pushButton_15)


        self.horizontalLayout_6.addWidget(self.main_body_menu_frame, 0, Qt.AlignTop)

        self.main_body_right_frame_2 = QFrame(self.main_body_right_frame)
        self.main_body_right_frame_2.setObjectName(u"main_body_right_frame_2")
        sizePolicy3.setHeightForWidth(self.main_body_right_frame_2.sizePolicy().hasHeightForWidth())
        self.main_body_right_frame_2.setSizePolicy(sizePolicy3)
        self.main_body_right_frame_2.setStyleSheet(u"background-color: rgba(148, 255, 140, 55);")
        self.main_body_right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.main_body_right_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_body_right_frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.main_body_right_frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        font8 = QFont()
        font8.setPointSize(14)
        self.stackedWidget.setFont(font8)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_48 = QLabel(self.page)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(60, 50, 279, 37))
        font9 = QFont()
        font9.setPointSize(23)
        self.label_48.setFont(font9)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(110, 60, 121, 51))
        self.label_13.setFont(font9)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_10 = QVBoxLayout(self.page_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QStackedWidget(self.frame_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_15 = QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea = QScrollArea(self.page_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 327, 657))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_16)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_17)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_18)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_19)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_20)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_21)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_22)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_29)

        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_23)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_24)

        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_25)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_28)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_27)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font9)

        self.verticalLayout_12.addWidget(self.label_26)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_14 = QVBoxLayout(self.page_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea_2 = QScrollArea(self.page_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        font10 = QFont()
        font10.setPointSize(7)
        self.scrollArea_2.setFont(font10)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -265, 326, 967))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font9)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_15)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font9)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label_35)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font9)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_34)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font9)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.label_33)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font9)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.label_32)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font9)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.label_43)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font9)

        self.formLayout.setWidget(20, QFormLayout.SpanningRole, self.label_42)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font9)

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.label_41)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font9)

        self.formLayout.setWidget(25, QFormLayout.SpanningRole, self.label_40)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font9)

        self.formLayout.setWidget(27, QFormLayout.FieldRole, self.label_39)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font9)

        self.formLayout.setWidget(30, QFormLayout.LabelRole, self.label_38)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font9)

        self.formLayout.setWidget(32, QFormLayout.FieldRole, self.label_36)

        self.label_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font9)

        self.formLayout.setWidget(36, QFormLayout.FieldRole, self.label_47)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font9)

        self.formLayout.setWidget(41, QFormLayout.SpanningRole, self.label_37)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font9)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_30)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font9)

        self.formLayout.setWidget(35, QFormLayout.LabelRole, self.label_45)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font9)

        self.formLayout.setWidget(39, QFormLayout.LabelRole, self.label_44)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font9)

        self.formLayout.setWidget(40, QFormLayout.FieldRole, self.label_46)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font9)

        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self.label_31)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollArea_2)

        self.stackedWidget_2.addWidget(self.page_6)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(120, 40, 121, 51))
        self.label_12.setFont(font9)
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.main_body_right_frame_2)


        self.horizontalLayout_5.addWidget(self.main_body_right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgba(167, 255, 249, 55);")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.version_frame = QFrame(self.footer_frame)
        self.version_frame.setObjectName(u"version_frame")
        self.version_frame.setFrameShape(QFrame.StyledPanel)
        self.version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.version_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.version_frame)
        self.label_2.setObjectName(u"label_2")
        font11 = QFont()
        font11.setPointSize(9)
        self.label_2.setFont(font11)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.version_frame, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.footer_center_frame = QFrame(self.footer_frame)
        self.footer_center_frame.setObjectName(u"footer_center_frame")
        self.footer_center_frame.setMinimumSize(QSize(0, 15))
        self.footer_center_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_center_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.footer_center_frame, 0, Qt.AlignBottom)

        self.info_btn_frame = QFrame(self.footer_frame)
        self.info_btn_frame.setObjectName(u"info_btn_frame")
        self.info_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.info_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.info_btn_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.info_btn = QPushButton(self.info_btn_frame)
        self.info_btn.setObjectName(u"info_btn")
        sizePolicy1.setHeightForWidth(self.info_btn.sizePolicy().hasHeightForWidth())
        self.info_btn.setSizePolicy(sizePolicy1)
        self.info_btn.setMinimumSize(QSize(15, 15))
        self.info_btn.setFont(font6)
        self.info_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.info_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.info_btn, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.info_btn_frame, 0, Qt.AlignRight)

        self.grip_frame = QFrame(self.footer_frame)
        self.grip_frame.setObjectName(u"grip_frame")
        self.grip_frame.setMinimumSize(QSize(10, 10))
        self.grip_frame.setMaximumSize(QSize(10, 10))
        self.grip_frame.setFrameShape(QFrame.StyledPanel)
        self.grip_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.grip_frame, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User's Page", None))
        self.menu_open_close_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User's Pages", None))
        self.minimize_window_btn.setText("")
#if QT_CONFIG(shortcut)
        self.minimize_window_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.resize_window_btn.setText("")
#if QT_CONFIG(shortcut)
        self.resize_window_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.close_window_btn.setText("")
#if QT_CONFIG(shortcut)
        self.close_window_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Bazadagi Mahsulotlar", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"menu 2", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"menu 3", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"menu 4", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"menu 5", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"menu 6", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"menu 7", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"menu 8", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"menu 9", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Widget 3", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Widget 1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"list", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"diagramma", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Bazadagi mahsulotlar", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Widget 4", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Bazadagi mahsulotlar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Widget 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | CopyRight", None))
        self.info_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

