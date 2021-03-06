# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Login(object):
    def __init__(self, setFieldsStateFunc):
      self.setFieldsState = setFieldsStateFunc

    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(606, 377)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.LineEdit = QtWidgets.QLineEdit(Dialog)
        self.LineEdit.setObjectName(_fromUtf8("LineEdit"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.horizontalLayout.addWidget(self.login_button)
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.horizontalLayout.addWidget(self.exit_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.login_button.clicked.connect(self.handleLoginButtonPress)
        self.exit_button.clicked.connect(self.window.hide)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Диспетчеризация", None))
        self.Label.setText(_translate("Dialog", "Введите пароль:", None))
        self.login_button.setText(_translate("Dialog", "Авторизоваться", None))
        self.exit_button.setText(_translate("Dialog", "Выход", None))
        self.label_2.setText(_translate("Dialog", "Исследование и управление детерминированными хаотическими процессами\n"
"в развитии экономической системы", None))

    def handleLoginButtonPress(self):
      print(self.LineEdit.text())
      if (self.LineEdit.text() == 'Gulnur'):
        self.label.setText(_translate("Dialog", "Пароль введен верно\nДоступ разрешен", None))
        self.setFieldsState(False)
      else:
        self.label.setText(_translate("Dialog", "Неверный пароль", None))

        
