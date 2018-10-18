# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Goverment_start_conditions2.ui'
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

class GovermentStartConditions2(object):
    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(869, 490)
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
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
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

        self.lineEdit.setText('1000000')
        self.lineEdit_2.setText('44350125')
        self.lineEdit_3.setText('207400')
        self.lineEdit_4.setText('29451122')
        self.lineEdit_5.setText('0')
        self.lineEdit_9.setText('0')
        self.lineEdit_10.setText('63050000')
        self.lineEdit_11.setText('30485000')

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

