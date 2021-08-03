# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceMrlaUu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 629)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_left_main = QFrame(self.centralwidget)
        self.frame_left_main.setObjectName(u"frame_left_main")
        self.frame_left_main.setFrameShape(QFrame.NoFrame)
        self.frame_left_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_left_main)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_leftdown = QFrame(self.frame_left_main)
        self.frame_leftdown.setObjectName(u"frame_leftdown")
        self.frame_leftdown.setFrameShape(QFrame.StyledPanel)
        self.frame_leftdown.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_leftdown)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.frame_leftdown)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 506, 385))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_leftdown, 1, 0, 1, 1)

        self.frame_left_top = QFrame(self.frame_left_main)
        self.frame_left_top.setObjectName(u"frame_left_top")
        self.frame_left_top.setMaximumSize(QSize(16777215, 256))
        self.frame_left_top.setFrameShape(QFrame.NoFrame)
        self.frame_left_top.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_left_top)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_start_process = QPushButton(self.frame_left_top)
        self.pushButton_start_process.setObjectName(u"pushButton_start_process")

        self.gridLayout_2.addWidget(self.pushButton_start_process, 7, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_left_top)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_global_manipulator = QLineEdit(self.frame_3)
        self.lineEdit_global_manipulator.setObjectName(u"lineEdit_global_manipulator")
        font = QFont()
        font.setFamily(u"Tlwg Mono")
        font.setPointSize(15)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.lineEdit_global_manipulator.setFont(font)

        self.gridLayout_3.addWidget(self.lineEdit_global_manipulator, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 2)

        self.frame_4 = QFrame(self.frame_left_top)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_replace_text = QLineEdit(self.frame_4)
        self.lineEdit_replace_text.setObjectName(u"lineEdit_replace_text")
        font1 = QFont()
        font1.setFamily(u"URW Gothic [urw]")
        font1.setPointSize(15)
        self.lineEdit_replace_text.setFont(font1)

        self.gridLayout_7.addWidget(self.lineEdit_replace_text, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_left_top, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_left_main)

        self.pushButton_new_rows = QPushButton(self.centralwidget)
        self.pushButton_new_rows.setObjectName(u"pushButton_new_rows")

        self.horizontalLayout.addWidget(self.pushButton_new_rows)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget_status = QListWidget(self.frame_2)
        self.listWidget_status.setObjectName(u"listWidget_status")
        self.listWidget_status.setSpacing(5)

        self.gridLayout.addWidget(self.listWidget_status, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 910, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader", None))
        self.pushButton_start_process.setText(QCoreApplication.translate("MainWindow", u"Start process", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Link Manipulator", None))
        self.lineEdit_global_manipulator.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Replace with", None))
        self.lineEdit_replace_text.setText("")
        self.pushButton_new_rows.setText(QCoreApplication.translate("MainWindow", u"Add\n"
"New Rows", None))
    # retranslateUi

