# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Goverment_start_conditions.ui'
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

class GovermentStartConditions1(object):
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
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.Label = QtGui.QLabel(Dialog)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.Label)
        self.lineEdit_16 = QtGui.QLineEdit(Dialog)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEdit_16)
        self.Label_2 = QtGui.QLabel(Dialog)
        self.Label_2.setObjectName(_fromUtf8("Label_2"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.Label_2)
        self.lineEdit_17 = QtGui.QLineEdit(Dialog)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEdit_17)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
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
        self.lineEdit_15 = QtGui.QLineEdit(Dialog)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_15)
        self.Label_3 = QtGui.QLabel(Dialog)
        self.Label_3.setObjectName(_fromUtf8("Label_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.Label_3)
        self.LineEdit_3 = QtGui.QLineEdit(Dialog)
        self.LineEdit_3.setObjectName(_fromUtf8("LineEdit_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.LineEdit_3)
        self.Label_4 = QtGui.QLabel(Dialog)
        self.Label_4.setObjectName(_fromUtf8("Label_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.Label_4)
        self.LineEdit_4 = QtGui.QLineEdit(Dialog)
        self.LineEdit_4.setObjectName(_fromUtf8("LineEdit_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.LineEdit_4)
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

        self.lineEdit.setText('43000')
        self.lineEdit_2.setText('6300000')
        self.lineEdit_3.setText('7100000')
        self.lineEdit_4.setText('9755000')
        self.lineEdit_5.setText('15000000')
        self.lineEdit_6.setText('922000')
        self.lineEdit_7.setText('1605100')
        self.lineEdit_8.setText('304969000')
        self.lineEdit_9.setText('534262281')
        self.lineEdit_10.setText('18858100')
        self.lineEdit_11.setText('8333208')
        self.lineEdit_12.setText('17515770')
        self.lineEdit_13.setText('22427620')
        self.lineEdit_14.setText('3050000')
        self.lineEdit_15.setText('43568230')
        self.lineEdit_16.setText('39250000')
        self.lineEdit_17.setText('12854964')
        self.LineEdit_3.setText('3087822')
        self.LineEdit_4.setText('8064750')

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Государство начальные условия и коэффициенты 1", None))
        self.label.setText(_translate("Dialog", "Государство ( начальные условия )", None))
        self.label_2.setText(_translate("Dialog", "Площадь земли сданной на пользование", None))
        self.label_3.setText(_translate("Dialog", "объем экспорта", None))
        self.label_4.setText(_translate("Dialog", "объем импорта", None))
        self.label_9.setText(_translate("Dialog", "сумма выплат за аренду байконура", None))
        self.label_5.setText(_translate("Dialog", "доходы от продажи акций и осн капитал", None))
        self.label_6.setText(_translate("Dialog", "получ. официальные трансфеты гос-ва", None))
        self.label_7.setText(_translate("Dialog", "административные сборы и платежи", None))
        self.label_8.setText(_translate("Dialog", "объем других неналоговых доходов", None))
        self.Label.setText(_translate("Dialog", "общ. расхода гос-ва на произв сферы", None))
        self.Label_2.setText(_translate("Dialog", "гос расходы общего характера", None))
        self.label_10.setText(_translate("Dialog", "расходы гос-ва на научно-культ мероприятия", None))
        self.label_11.setText(_translate("Dialog", "расходы гос-ва на оборону", None))
        self.label_12.setText(_translate("Dialog", "расходы гос-ва на правоохранительную\n"
"деятельность и безопастность", None))
        self.label_13.setText(_translate("Dialog", "расходы гос-ва на науку", None))
        self.label_14.setText(_translate("Dialog", "расходы гос-ва на образование", None))
        self.label_15.setText(_translate("Dialog", "расходы гос-ва на здравоохранение", None))
        self.label_16.setText(_translate("Dialog", "расходы гос-ва на соц страхование", None))
        self.Label_3.setText(_translate("Dialog", "прочие расходы гос-ва", None))
        self.Label_4.setText(_translate("Dialog", "расходы гос-ва по внутр. гос долгу", None))
        self.saveButton.setText(_translate("Dialog", "Запись", None))
        self.cancelButton.setText(_translate("Dialog", "Отмена", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

