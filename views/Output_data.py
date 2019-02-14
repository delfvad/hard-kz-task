# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Output_data.ui'
#
# Created by: PyQt5 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pandas
from numpy.random import normal, uniform, choice
import matplotlib.pyplot as plt

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

class OutputData(object):

    START_YEAR = 2012
    def __init__(self):
        self.nac = [17338.2, 17586.1, 17731.3, 17591.5, 17918.3, 18165.7, 18221.8, 18374.4]
        self.vvp_nominal_tenge = [34.231, 39.521, 40.886, 44.354, 49.740, 51.836, 52.731, 54.442]
        self.vvp_temp = [6.0, 4.3, 1.2, 1, 4, 3.6, 3.8, 4.1]
        self.bezrab = [5.2, 4.9, 4.9, 5.0, 4.9, 4.8, 4.8, 4.8]
        self.inf = [5.82, 6.61, 7.54, 13.63, 7.29, 5.62, 4.98, 4.76]
        self.data = [self.nac, self.vvp_nominal_tenge, self.vvp_temp, self.bezrab, self.inf]

    def setupUi(self, Dialog):
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(900, 509)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.plotButton = QtWidgets.QPushButton(Dialog)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_2.addWidget(self.plotButton)
        self.horizontalLayout_2.addWidget(self.calculateButton)
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.plotButton.clicked.connect(self.handlePlotButtonPress)
        self.calculateButton.clicked.connect(self.handleCalculateButtonPress)
        self.exitButton.clicked.connect(self.window.hide)

        # nac = [17338.2, 17586.1, 17731.3, 17591.5, 17918.3, 18165.7, 18221.8, 18374.4]
        # vvp_nominal_tenge = [34.231, 39.521, 40.886, 44.354, 49.740, 51.836, 52.731, 54.442]
        # vvp_temp = [6, 4.3, 1.2, 1, 4, 3.6, 3.8, 4.1]
        # bezrab = [5.2, 4.9, 4.9, 5.0, 4.9, 4.8, 4.8, 4.8]
        # inf = [5.82, 6.61, 7.54, 13.63, 7.29, 5.62, 4.98, 4.76]
        # stavka = [5.5, 8.3, 13.1, 10.3, 8.7, 8.8, 7.5, 7.25]
        arr = []
        for j in range(0,8):
          arr.append([])
          arr[j].append(self.nac[j])
          arr[j].append(self.vvp_nominal_tenge[j])
          arr[j].append(self.vvp_temp[j])
          arr[j].append(self.bezrab[j])
          arr[j].append(self.inf[j])
        self.updateTableWidget(arr)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Выходные данные", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Численность населения, тыс. чел.", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Номинальный ВВП, трлн. тенге", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Темпы роста (реальный ВВП), тенге %", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Показатель инфляции, %", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Уровень безработицы, %", None))
        self.exitButton.setText(_translate("Dialog", "Выход", None))
        self.calculateButton.setText(_translate("Dialog", "Расчет", None))
        self.plotButton.setText(_translate("Dialog", "График", None))


    def updateTableWidget(self, arr):
        odf = pandas.DataFrame(arr, columns=['nac', 'vvp_nominal_tenge', 'vvp_temp', 'bezrab', 'inf'])
        self.tableWidget.setRowCount(10)
        for index, row in odf.iterrows():
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(round(row['nac'],1))))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(round(row['vvp_nominal_tenge'],1))))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(round(row['vvp_temp'],1))))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(round(row['bezrab'],1))))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(round(row['inf'],1))))

    def handleCalculateButtonPress(self):
        nac = self.doDataModellingImitation(self.nac)
        vvp_nominal_tenge = self.doDataModellingImitation(self.vvp_nominal_tenge)
        vvp_temp = self.doDataModellingImitation(self.vvp_temp)
        bezrab = self.doDataModellingImitation(self.bezrab)
        inf = self.doDataModellingImitation(self.inf)
        self.data = [nac, vvp_nominal_tenge, vvp_temp, bezrab, inf]
        arr = []
        for j in range(0,8):
          arr.append([])
          arr[j].append(nac[j])
          arr[j].append(vvp_nominal_tenge[j])
          arr[j].append(vvp_temp[j])
          arr[j].append(bezrab[j])
          arr[j].append(inf[j])
        self.updateTableWidget(arr)

    def doDataModellingImitation(self, data):
        d_min = min(data)
        d_max = max(data)
        G = (d_max - d_min)/ float(3.0)
        G_coeffs = uniform(0.1, 0.5, len(data))
        data_new = [ normal(x, G * choice(G_coeffs)) for x in data ]
        return data_new

    def handlePlotButtonPress(self):
        selectedIndexes = self.tableWidget.selectedIndexes()
        if (len(selectedIndexes) > 0):
          column = selectedIndexes[0].column()
          header = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentItem().column()).text();
          y = self.data[column]
          x = range(self.START_YEAR, self.START_YEAR + len(y))
          plt.figure(num=header)
          plt.xlabel('Год')
          plt.ylabel(header)
          plt.plot(x,y)
          plt.show()
