# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Output_data.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidgetItem
import pandas

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

class OutputData(object):
    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(900, 509)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.exitButton = QtGui.QPushButton(Dialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.calculateButton = QtGui.QPushButton(Dialog)
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.horizontalLayout_2.addWidget(self.calculateButton)
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        nac = [17338.2, 17586.1, 17731.3, 17591.5, 17918.3, 18165.7, 18221.8, 18374.4]
        vvp_nominal_tenge = [34.231, 39.521, 40.886, 44.354, 49.740, 51.836, 52.731, 54.442]
        vvp_temp = [6, 4.3, 1.2, 1, 4, 3.6, 3.8, 4.1]
        bezrab = [5.2, 4.9, 4.9, 5.0, 4.9, 4.8, 4.8, 4.8]
        inf = [5.82, 6.61, 7.54, 13.63, 7.29, 5.62, 4.98, 4.76]
        arr = []
        for j in range(0,8):
          arr.append([])
          arr[j].append(nac[j])
          arr[j].append(vvp_nominal_tenge[j])
          arr[j].append(vvp_temp[j])
          arr[j].append(bezrab[j])
          arr[j].append(inf[j])

        # stavka = [5.5, 8.3, 13.1, 10.3, 8.7, 8.8, 7.5, 7.25]
        odf = pandas.DataFrame(arr, columns=['nac', 'vvp_nominal_tenge', 'vvp_temp', 'bezrab', 'inf'])
        self.tableWidget.setRowCount(10)
        for index, row in odf.iterrows():
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(row['nac'])))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(row['vvp_nominal_tenge'])))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(row['vvp_temp'])))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(row['bezrab'])))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(row['inf'])))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Выходные данные", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Численность населения", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Номинальный ВВП", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Темпы роста (реальный ВВП)", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Показатель инфляции", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Уровень безработицы", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))
        self.calculateButton.setText(_translate("Dialog", "Расчет", None))
