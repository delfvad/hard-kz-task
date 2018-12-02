# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
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

class EMainWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_6 = QtWidgets.QMenu(self.menu_3)
        self.menu_6.setObjectName(_fromUtf8("menu_6"))
        self.menu_7 = QtWidgets.QMenu(self.menu_3)
        self.menu_7.setObjectName(_fromUtf8("menu_7"))
        self.menu_8 = QtWidgets.QMenu(self.menu_3)
        self.menu_8.setObjectName(_fromUtf8("menu_8"))
        self.menu_9 = QtWidgets.QMenu(self.menu_3)
        self.menu_9.setObjectName(_fromUtf8("menu_9"))
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName(_fromUtf8("menu_4"))
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName(_fromUtf8("menu_5"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.open_goverment_coeffitients = QtWidgets.QAction(MainWindow)
        self.open_goverment_coeffitients.setObjectName(_fromUtf8("open_goverment_coeffitients"))
        self.open_goverment_initial_conditions1 = QtWidgets.QAction(MainWindow)
        self.open_goverment_initial_conditions1.setObjectName(_fromUtf8("open_goverment_initial_conditions1"))
        self.open_goverment_initial_conditions2 = QtWidgets.QAction(MainWindow)
        self.open_goverment_initial_conditions2.setObjectName(_fromUtf8("open_goverment_initial_conditions2"))
        self.open_population_coefficients = QtWidgets.QAction(MainWindow)
        self.open_population_coefficients.setObjectName(_fromUtf8("open_population_coefficients"))
        self.open_population_initial_conditions = QtWidgets.QAction(MainWindow)
        self.open_population_initial_conditions.setObjectName(_fromUtf8("open_population_initial_conditions"))
        self.open_production_setup = QtWidgets.QAction(MainWindow)
        self.open_production_setup.setObjectName(_fromUtf8("open_production_setup"))
        self.open_bank_coeffitients = QtWidgets.QAction(MainWindow)
        self.open_bank_coeffitients.setObjectName(_fromUtf8("open_bank_coeffitients"))
        self.setup_application = QtWidgets.QAction(MainWindow)
        self.setup_application.setObjectName(_fromUtf8("setup_application"))
        self.login = QtWidgets.QAction(MainWindow)
        self.login.setObjectName(_fromUtf8("login"))
        self.open_output_data = QtWidgets.QAction(MainWindow)
        self.open_output_data.setObjectName(_fromUtf8("open_output_data"))
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.menu.addAction(self.setup_application)
        self.menu_2.addAction(self.login)
        self.menu_6.addAction(self.open_goverment_coeffitients)
        self.menu_6.addAction(self.open_goverment_initial_conditions1)
        self.menu_6.addAction(self.open_goverment_initial_conditions2)
        self.menu_7.addAction(self.open_population_initial_conditions)
        self.menu_7.addAction(self.open_population_coefficients)
        self.menu_8.addAction(self.open_production_setup)
        self.menu_9.addAction(self.open_bank_coeffitients)
        self.menu_3.addAction(self.menu_8.menuAction())
        self.menu_3.addAction(self.menu_7.menuAction())
        self.menu_3.addAction(self.menu_6.menuAction())
        self.menu_3.addAction(self.menu_9.menuAction())
        self.menu_4.addAction(self.open_output_data)
        self.menu_5.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu.setTitle(_translate("MainWindow", "Настройка", None))
        self.menu_2.setTitle(_translate("MainWindow", "Диспетчеризация", None))
        self.menu_3.setTitle(_translate("MainWindow", "Корректировка данных", None))
        self.menu_6.setTitle(_translate("MainWindow", "Государство", None))
        self.menu_7.setTitle(_translate("MainWindow", "Население", None))
        self.menu_8.setTitle(_translate("MainWindow", "Производство", None))
        self.menu_9.setTitle(_translate("MainWindow", "Банк", None))
        self.menu_4.setTitle(_translate("MainWindow", "Просмотр входных данных", None))
        self.menu_5.setTitle(_translate("MainWindow", "Выход", None))
        self.open_goverment_coeffitients.setText(_translate("MainWindow", "Корректировка коэффициентов", None))
        self.open_goverment_initial_conditions1.setText(_translate("MainWindow", "Корректировка начальных условий 1", None))
        self.open_goverment_initial_conditions2.setText(_translate("MainWindow", "Корректировка начальных условий 2", None))
        self.open_population_coefficients.setText(_translate("MainWindow", "Начальные условия и коэффициенты", None))
        self.open_population_initial_conditions.setText(_translate("MainWindow", "Начальные условия", None))
        self.open_production_setup.setText(_translate("MainWindow", "Коэффициенты и начальные условия", None))
        self.open_bank_coeffitients.setText(_translate("MainWindow", "Коэффициенты и начальные условия", None))
        self.setup_application.setText(_translate("MainWindow", "Настройка", None))
        self.login.setText(_translate("MainWindow", "Диспетчеризация", None))
        self.open_output_data.setText(_translate("MainWindow", "Просмотр выходные данных", None))
        self.exit.setText(_translate("MainWindow", "Выход", None))

