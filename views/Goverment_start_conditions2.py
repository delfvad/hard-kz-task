# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Goverment_start_conditions2.ui'
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

class GovermentStartConditions2(object):
    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(869, 490)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEdit.setText('1000000')
        self.lineEdit_2.setText('44350125')
        self.lineEdit_3.setText('207400')
        self.lineEdit_4.setText('29451122')
        self.lineEdit_5.setText('0')
        self.lineEdit_9.setText('0')
        self.lineEdit_10.setText('63050000')
        self.lineEdit_11.setText('30485000')

        self.exitButton.clicked.connect(self.window.hide)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Государство начальные условия и коэффициенты 2", None))
        self.label.setText(_translate("Dialog", "Государство ( начальные условия )", None))
        self.label_2.setText(_translate("Dialog", "расходы бюджета на обслуживание\n"
"внешнего гос долга", None))
        self.label_3.setText(_translate("Dialog", "начальные значения внутреннего\n"
"гос долга", None))
        self.label_4.setText(_translate("Dialog", "внутренние займы гос-ва для погашения \n"
"дефицита бюджета", None))
        self.label_9.setText(_translate("Dialog", "начальное значение сумма \n"
"внешнего гос долга", None))
        self.label_5.setText(_translate("Dialog", "общая сумма кредита, получаемая гос-вом\n"
"извне страны", None))
        self.label_10.setText(_translate("Dialog", "начальное значение накопления\n"
"иностранной валюты в стране", None))
        self.label_11.setText(_translate("Dialog", "общая сумма инвестиций в производство\n"
"внешними инвесторами", None))
        self.label_12.setText(_translate("Dialog", "чачальное значение долга произв. сферы\n"
" экономики внешним инвесторам", None))
        self.saveButton.setText(_translate("Dialog", "Запись", None))
        self.cancelButton.setText(_translate("Dialog", "Отмена", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))

