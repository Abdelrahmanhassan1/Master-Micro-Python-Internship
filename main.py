import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # global variables
        self.number_of_points = 100

        # Connecting the buttons to their functions
        self.ui.pushButton_2.clicked.connect(self.save_figure_from_gui)

        # Adding the matplotlib figure to the application
        self.function_plotter_figure = Figure()
        self.function_plotter_figure_canvas = FigureCanvas(
            self.function_plotter_figure)
        self.ui.Plotting_Layout.addWidget(self.function_plotter_figure_canvas)

        # handling max and min value inputs to accept just numbers
        validator = QDoubleValidator()
        self.ui.min_value_input.setValidator(validator)
        self.ui.max_value_input.setValidator(validator)

    def check_entered_input_values(self, function, min, max):
        ###
        # function used to check the validity of the entered values
        ###
        try:
            if function == "" or min == "" or max == "":
                self.raise_error(
                    "Function, min, and max value must be entered.")
                return False

            if float(max) <= float(min):
                self.raise_error(
                    "Maximum value must be greater than Minimum value.")
                return False

            return True
        except Exception as e:
            print(e)

    def save_figure_from_gui(self):
        ###
        # function used to save the plotted equation figure from the gui
        ###
        figname, ok = QInputDialog.getText(
            self, 'input dialog', 'Name of Figure:')
        if ok:
            try:
                self.function_plotter_figure.savefig(
                    f"figures_plotted/{figname}.png")
                self.raise_success("Figure Saved Successfully")
            except Exception as e:
                self.raise_error("Error Figure Not Saved")

    def raise_error(self, error_message):
        ###
        # function used to raise a given error message
        ###
        QMessageBox.about(self, "Error", error_message)

    def raise_success(self, success_message):
        ###
        # function used to raise a given success message
        ###
        QMessageBox.about(self, "Success", success_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
