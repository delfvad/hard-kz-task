# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Population_Input_data.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem
from IPython import embed

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

class PopulationInputData(object):

    def handleTable(self, df):
      self.tableWidget.setRowCount(70)
      for index, row in df.iterrows():
          print index
          self.tableWidget.setItem(index, 0, QTableWidgetItem(str(row['age'])))
          self.tableWidget.setItem(index, 1, QTableWidgetItem(str(row['count'])))
          self.tableWidget.setItem(index, 2, QTableWidgetItem(str(row['birth'])))
          self.tableWidget.setItem(index, 3, QTableWidgetItem(str(row['immigration'])))
          self.tableWidget.setItem(index, 4, QTableWidgetItem(str(row['emigration'])))
          self.tableWidget.setItem(index, 5, QTableWidgetItem(str(row['mortality'])))
          self.tableWidget.setItem(index, 6, QTableWidgetItem(str(row['employment'])))


    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1061, 548)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(102)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_15 = QtGui.QLineEdit(Dialog)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.horizontalLayout_4.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtGui.QLineEdit(Dialog)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.horizontalLayout_4.addWidget(self.lineEdit_16)
        self.lineEdit_17 = QtGui.QLineEdit(Dialog)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.horizontalLayout_4.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtGui.QLineEdit(Dialog)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.horizontalLayout_4.addWidget(self.lineEdit_18)
        self.lineEdit_19 = QtGui.QLineEdit(Dialog)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.horizontalLayout_4.addWidget(self.lineEdit_19)
        self.lineEdit_20 = QtGui.QLineEdit(Dialog)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.horizontalLayout_4.addWidget(self.lineEdit_20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.valueButton = QtGui.QPushButton(Dialog)
        self.valueButton.setObjectName(_fromUtf8("valueButton"))
        self.horizontalLayout_2.addWidget(self.valueButton)
        self.adjustmentButton = QtGui.QPushButton(Dialog)
        self.adjustmentButton.setObjectName(_fromUtf8("adjustmentButton"))
        self.horizontalLayout_2.addWidget(self.adjustmentButton)
        self.plotButton = QtGui.QPushButton(Dialog)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_2.addWidget(self.plotButton)
        self.exitButton = QtGui.QPushButton(Dialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Возраст", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Численность", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Рождаемость", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Иммиграция", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Эммиграция", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Смертность", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Трудоспособность", None))
        self.label.setText(_translate("Dialog", "min трудосп. возр.", None))
        self.label_2.setText(_translate("Dialog", "max трудосп. возр.", None))
        self.label_3.setText(_translate("Dialog", "Доля обуч. в ВУЗ и СУЗ", None))
        self.label_4.setText(_translate("Dialog", "Норма % по банк. вкладам", None))
        self.label_5.setText(_translate("Dialog", "к-т склонности населения\n"
" к потреблению", None))
        self.label_6.setText(_translate("Dialog", "Норма под. налога с физ.\n"
" лиц в банковской сфере", None))
        self.label_7.setText(_translate("Dialog", "Норма под. налога с физ.\n"
" лиц в производст. сфере", None))
        self.label_8.setText(_translate("Dialog", "Норма под. налога с физ.\n"
" лиц в бюджет. сфере", None))
        self.valueButton.setText(_translate("Dialog", "Числ. знач.", None))
        self.adjustmentButton.setText(_translate("Dialog", "Коррект. к-тов", None))
        self.plotButton.setText(_translate("Dialog", "График", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))

