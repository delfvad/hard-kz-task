import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from views.Main_window import EMainWindow
from views.Bank_input_data import BankInputData
from views.Goverment_input_data import GovermentInputData
from views.Goverment_start_conditions1 import GovermentStartConditions1
from views.Goverment_start_conditions2 import GovermentStartConditions2
from views.Output_data import OutputData
from views.Population_Input_data import PopulationInputData
from views.Population_start_conditions import PopulationStartConditions
from views.Production_input_data import ProductionInputData
from views.Login import Login
import pandas
from IPython import embed

def setFieldsState(state):
    pass

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

df = pandas.read_csv(resource_path('intens.csv'))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    main_window = EMainWindow()
    main_window.setupUi(QtWidgets.QMainWindow())
    main_window.window.show()

    bank_input_data = BankInputData()
    bank_input_data.setupUi(QtWidgets.QDialog())

    goverment_input_data = GovermentInputData()
    goverment_input_data.setupUi(QtWidgets.QDialog())

    goverment_start_conditions_1 = GovermentStartConditions1()
    goverment_start_conditions_1.setupUi(QtWidgets.QDialog())

    goverment_start_conditions_2 = GovermentStartConditions2()
    goverment_start_conditions_2.setupUi(QtWidgets.QDialog())

    output_data = OutputData()
    output_data.setupUi(QtWidgets.QDialog())

    population_input_data = PopulationInputData()
    population_input_data.setupUi(QtWidgets.QDialog())
    population_input_data.handleTable(df)

    global population_start_conditions
    population_start_conditions = PopulationStartConditions()
    population_start_conditions.setupUi(QtWidgets.QDialog())

    production_input_data = ProductionInputData()
    production_input_data.setupUi(QtWidgets.QDialog())

    login_window = Login(setFieldsState)
    login_window.setupUi(QtWidgets.QDialog())

    main_window.open_bank_coeffitients.triggered.connect(
        bank_input_data.window.show)
    main_window.open_goverment_coeffitients.triggered.connect(
        goverment_input_data.window.show)
    main_window.open_goverment_initial_conditions1.triggered.connect(
        goverment_start_conditions_1.window.show)
    main_window.open_goverment_initial_conditions2.triggered.connect(
        goverment_start_conditions_2.window.show)
    main_window.open_output_data.triggered.connect(output_data.window.show)
    main_window.open_population_coefficients.triggered.connect(population_input_data.window.show)
    main_window.open_population_initial_conditions.triggered.connect(population_start_conditions.window.show)
    main_window.open_production_setup.triggered.connect(production_input_data.window.show)
    main_window.login.triggered.connect(login_window.window.show)
    main_window.exit.triggered.connect(app.quit)

    sys.exit(app.exec_())

