# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Raw/interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_left_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_left_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_main.setObjectName("frame_left_main")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_left_main)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_leftdown = QtWidgets.QFrame(self.frame_left_main)
        self.frame_leftdown.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_leftdown.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_leftdown.setObjectName("frame_leftdown")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_leftdown)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_leftdown)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 552, 271))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_leftdown, 1, 0, 1, 1)
        self.frame_left_top = QtWidgets.QFrame(self.frame_left_main)
        self.frame_left_top.setMaximumSize(QtCore.QSize(16777215, 450))
        self.frame_left_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_top.setObjectName("frame_left_top")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_left_top)
        self.gridLayout_7.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_7.setVerticalSpacing(9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_left_top)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(450, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 570, 193))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.pushButton_start_process = QtWidgets.QPushButton(self.frame_left_top)
        self.pushButton_start_process.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_start_process.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_start_process.setStyleSheet("QPushButton{\n"
"    border: 1px solid grey;\n"
"    background-color: white;\n"
"    border-radius: 35;\n"
"}\n"
"QPushButton::hover:!pressed{\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton::pressed{\n"
"    border: 2px solid black;\n"
"    padding: 5px;\n"
"}")
        self.pushButton_start_process.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start_process.setIcon(icon)
        self.pushButton_start_process.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_start_process.setObjectName("pushButton_start_process")
        self.gridLayout_7.addWidget(self.pushButton_start_process, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_left_top, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_left_main, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_new_regex_row = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_new_regex_row.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_new_regex_row.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_new_regex_row.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_regex_row.setIcon(icon1)
        self.pushButton_new_regex_row.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_new_regex_row.setObjectName("pushButton_new_regex_row")
        self.gridLayout_8.addWidget(self.pushButton_new_regex_row, 1, 1, 1, 1)
        self.pushButton_export = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_export.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_export.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_export.setIcon(icon2)
        self.pushButton_export.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_export.setObjectName("pushButton_export")
        self.gridLayout_8.addWidget(self.pushButton_export, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_new_rows = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_new_rows.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_new_rows.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_new_rows.setText("")
        self.pushButton_new_rows.setIcon(icon1)
        self.pushButton_new_rows.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_new_rows.setObjectName("pushButton_new_rows")
        self.gridLayout_5.addWidget(self.pushButton_new_rows, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(320, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_status = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_status.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget_status.setObjectName("listWidget_status")
        self.gridLayout.addWidget(self.listWidget_status, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea_2, self.pushButton_start_process)
        MainWindow.setTabOrder(self.pushButton_start_process, self.pushButton_new_rows)
        MainWindow.setTabOrder(self.pushButton_new_rows, self.listWidget_status)
        MainWindow.setTabOrder(self.listWidget_status, self.pushButton_new_regex_row)
        MainWindow.setTabOrder(self.pushButton_new_regex_row, self.scrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader"))
        self.pushButton_start_process.setToolTip(_translate("MainWindow", "start executing added jobs"))
from . import icons_qrc_rc
