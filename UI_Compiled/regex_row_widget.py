# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Raw/regex_row_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 547)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_replace_text = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(15)
        self.lineEdit_replace_text.setFont(font)
        self.lineEdit_replace_text.setText("")
        self.lineEdit_replace_text.setObjectName("lineEdit_replace_text")
        self.gridLayout_5.addWidget(self.lineEdit_replace_text, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 2)
        self.lineEdit_global_manipulator = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit_global_manipulator.setFont(font)
        self.lineEdit_global_manipulator.setText("")
        self.lineEdit_global_manipulator.setObjectName("lineEdit_global_manipulator")
        self.gridLayout_5.addWidget(self.lineEdit_global_manipulator, 1, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_sequence = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_sequence.setFont(font)
        self.label_sequence.setObjectName("label_sequence")
        self.gridLayout.addWidget(self.label_sequence, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 3)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Replace with"))
        self.label_2.setText(_translate("Form", "Link Manipulator"))
        self.label_sequence.setText(_translate("Form", "00"))
