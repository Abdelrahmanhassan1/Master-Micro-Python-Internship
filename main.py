import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Adding the matplotlib figure to the application
        self.function_plotter_figure = Figure()
        self.function_plotter_figure_canvas = FigureCanvas(
            self.function_plotter_figure)
        self.ui.Plotting_Layout.addWidget(self.function_plotter_figure_canvas)

        # handling max and min value inputs to accept just numbers
        validator = QDoubleValidator()
        self.ui.min_value_input.setValidator(validator)
        self.ui.max_value_input.setValidator(validator)

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
