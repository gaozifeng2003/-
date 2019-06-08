# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_testmake.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1048, 713)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 10, 841, 141))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 160, 841, 171))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 540, 121, 31))
        self.pushButton.setMinimumSize(QtCore.QSize(121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 600, 121, 31))
        self.pushButton_2.setMinimumSize(QtCore.QSize(121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 650, 121, 31))
        self.pushButton_3.setMinimumSize(QtCore.QSize(121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 550, 121, 31))
        self.pushButton_4.setMinimumSize(QtCore.QSize(121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 540, 121, 31))
        self.pushButton_5.setMinimumSize(QtCore.QSize(121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 340, 841, 171))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 41, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.slot_testsave)
        self.pushButton_2.clicked.connect(Form.slot_testderive)
        self.pushButton_3.clicked.connect(Form.slot_testclear)
        self.pushButton_4.clicked.connect(Form.slot_testexit)
        self.pushButton_5.clicked.connect(Form.slot_testnext)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "试题制作"))
        self.label.setText(_translate("Form", "题目"))
        self.label_2.setText(_translate("Form", "答案"))
        self.pushButton.setText(_translate("Form", "保存试题"))
        self.pushButton_2.setText(_translate("Form", "试题库导出"))
        self.pushButton_3.setText(_translate("Form", "清除试题库并退出"))
        self.pushButton_4.setText(_translate("Form", "保存题库退出"))
        self.pushButton_5.setText(_translate("Form", "下一题"))
        self.label_3.setText(_translate("Form", "讲解"))


