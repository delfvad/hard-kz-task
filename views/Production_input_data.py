# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Production_input_data.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class ProductionInputData(object):
    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(865, 490)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_18 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_2.addWidget(self.label_18)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_17 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout.addWidget(self.label_17)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_10 = QtGui.QLineEdit(Dialog)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_11 = QtGui.QLineEdit(Dialog)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_12 = QtGui.QLineEdit(Dialog)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_13 = QtGui.QLineEdit(Dialog)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_14 = QtGui.QLineEdit(Dialog)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_17 = QtGui.QLineEdit(Dialog)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.horizontalLayout_3.addWidget(self.lineEdit_17)
        self.lineEdit_16 = QtGui.QLineEdit(Dialog)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.horizontalLayout_3.addWidget(self.lineEdit_16)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(Dialog)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.exitButton = QtGui.QPushButton(Dialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEdit.setText('0.10')
        self.lineEdit_2.setText('0.20')
        self.lineEdit_3.setText('0.10')
        self.lineEdit_4.setText('0.20')
        self.lineEdit_5.setText('0.30')
        self.lineEdit_6.setText('0.20')
        self.lineEdit_7.setText('0.33')
        self.lineEdit_8.setText('0.15')
        self.lineEdit_9.setText('827000000')
        self.lineEdit_10.setText('3000000')
        self.lineEdit_11.setText('15')
        self.lineEdit_12.setText('0.32')
        self.lineEdit_13.setText('0')
        self.lineEdit_14.setText('92500000')
        self.lineEdit_16.setText('0.90')
        self.lineEdit_17.setText('3.00')

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Производство", None))
        self.label_18.setText(_translate("Dialog", "коэффициенты", None))
        self.label_2.setText(_translate("Dialog", "к-т износа основных фондов", None))
        self.label_3.setText(_translate("Dialog", "доля материалоемк. в вал. прод.", None))
        self.label_4.setText(_translate("Dialog", "доля трудоемк в вал. прод.", None))
        self.label_9.setText(_translate("Dialog", "норма фондоемк. в вал. прод.", None))
        self.label_5.setText(_translate("Dialog", "норма соц. стархования", None))
        self.label_6.setText(_translate("Dialog", "норма налога на доб. с-ть", None))
        self.label_7.setText(_translate("Dialog", "норма налога на доход", None))
        self.label_8.setText(_translate("Dialog", "норма амортизации отчислений", None))
        self.label_17.setText(_translate("Dialog", "начальные условия", None))
        self.label_10.setText(_translate("Dialog", "объема основных фондов", None))
        self.label_11.setText(_translate("Dialog", "числ. раб. в произв. сфере", None))
        self.label_12.setText(_translate("Dialog", "уровня заралат в произв. сфере", None))
        self.label_13.setText(_translate("Dialog", "кредитных ставок", None))
        self.label_14.setText(_translate("Dialog", "суммы кредита в производство", None))
        self.label_15.setText(_translate("Dialog", "сумма кред., выд на n периодов", None))
        self.label_16.setText(_translate("Dialog", "Параметры произв. функции", None))
        self.saveButton.setText(_translate("Dialog", "Запись", None))
        self.cancelButton.setText(_translate("Dialog", "Отмена", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))
