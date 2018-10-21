# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import settings

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Login(object):
    def __init__(self, setFieldsStateFunc):
      self.setFieldsState = setFieldsStateFunc

    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(606, 377)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.Label = QtGui.QLabel(Dialog)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.Label)
        self.LineEdit = QtGui.QLineEdit(Dialog)
        self.LineEdit.setObjectName(_fromUtf8("LineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.LineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_button = QtGui.QPushButton(Dialog)
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.horizontalLayout.addWidget(self.login_button)
        self.exit_button = QtGui.QPushButton(Dialog)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.horizontalLayout.addWidget(self.exit_button)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.login_button.clicked.connect(self.handleLoginButtonPress)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Диспетчеризация", None))
        self.Label.setText(_translate("Dialog", "Введите пароль:", None))
        self.login_button.setText(_translate("Dialog", "Авторизоваться", None))
        self.exit_button.setText(_translate("Dialog", "Выход", None))

    def handleLoginButtonPress(self):
      print(self.LineEdit.text())
      if (self.LineEdit.text() == 'mypass'):
        self.label.setText(_translate("Dialog", "Пароль введен верно\nДоступ разрешен", None))
        self.setFieldsState(False)
      else:
        self.label.setText(_translate("Dialog", "Неверный пароль", None))
