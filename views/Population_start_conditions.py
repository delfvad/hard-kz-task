# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Population_start_conditions.ui'
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

class PopulationStartConditions(object):
    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(842, 295)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEdit.setText('2000000')
        self.lineEdit_2.setText('1500000')
        self.lineEdit_3.setText('15')
        self.lineEdit_4.setText('1.60')
        self.lineEdit_5.setText('1.900')
        self.lineEdit_6.setText('18200000')
        self.lineEdit_7.setText('19')

        self.exitButton.clicked.connect(self.window.hide)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Население начальные условия", None))
        self.label_8.setText(_translate("Dialog", "Население ( начальные условия )", None))
        self.label.setText(_translate("Dialog", "Численность работающих в бюджетных организациях", None))
        self.label_2.setText(_translate("Dialog", "Численность работающих в банковской сфере", None))
        self.label_3.setText(_translate("Dialog", "зар. плата бюджетников", None))
        self.label_4.setText(_translate("Dialog", "Средний уровень стипендий", None))
        self.label_5.setText(_translate("Dialog", "Средний уровень пенсий", None))
        self.label_6.setText(_translate("Dialog", "Вклады населения", None))
        self.label_7.setText(_translate("Dialog", "зар. плата банк работников", None))
        self.saveButton.setText(_translate("Dialog", "Запись", None))
        self.cancelButton.setText(_translate("Dialog", "Отмена", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))


