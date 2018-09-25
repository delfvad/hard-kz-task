from PyQt4 import QtCore, QtGui
from views.Main_window import EMainWindow
from views.Bank_input_data import BankInputData
from views.Goverment_input_data import GovermentInputData
from views.Goverment_start_conditions1 import GovermentStartConditions1
from views.Goverment_start_conditions2 import GovermentStartConditions2
from views.Output_data import OutputData
from views.Population_Input_data import PopulationInputData
from views.Population_start_conditions import PopulationStartConditions
from views.Production_input_data import ProductionInputData




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    main_window = EMainWindow()
    main_window.setupUi(QtGui.QMainWindow())
    main_window.window.show()

    bank_input_data = BankInputData()
    bank_input_data.setupUi(QtGui.QDialog())

    goverment_input_data = GovermentInputData()
    goverment_input_data.setupUi(QtGui.QDialog())

    goverment_start_conditions_1 = GovermentStartConditions1()
    goverment_start_conditions_1.setupUi(QtGui.QDialog())

    goverment_start_conditions_2 = GovermentStartConditions2()
    goverment_start_conditions_2.setupUi(QtGui.QDialog())

    # output_data = OutputData()
    # output_data.setupUi(QtGui.QDialog())

    # population_input_data = PopulationInputData()
    # population_input_data.setupUi(QtGui.QDialog)

    # population_start_conditions = PopulationStartConditions()
    # population_start_conditions.setupUi(QtGui.QDialog)

    # production_input_data = ProductionInputData()
    # production_input_data.setupUi(QtGui.QDialog)

    main_window.open_bank_coeffitients.triggered.connect(
        bank_input_data.window.show)
    main_window.open_goverment_coeffitients.triggered.connect(
        goverment_input_data.window.show)
    main_window.open_goverment_initial_conditions1.triggered.connect(
        goverment_start_conditions_1.window.show)
    main_window.open_goverment_initial_conditions2.triggered.connect(
        goverment_start_conditions_2.window.show)
    # main_window.open_output_data.triggered.connect(output_data.window.show)
    # main_window.open_population_coefficients.connect(population_input_data.window.show)
    # main_window.open_population_initial_conditions.connect(population_start_conditions.window.show)
    # main_window.open_production_setup.triggered.connect(production_input_data.window.show)

    sys.exit(app.exec_())
