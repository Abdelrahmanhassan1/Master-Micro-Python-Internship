import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sympy
import numpy as np
from main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # global variables
        self.number_of_points = 100
        self.max_range_value = 0
        self.min_range_value = 0
        self.valid_chars = ["x", "1", "2", "3", "4", "5", "6",
                            "7", "8", "9", "0", "*", "/", "-", "^", "+", ".", " "]
        self.operators = ["*", "/", "^"]
        self.x_symbol = sympy.symbols("x")

        # Adding the matplotlib figure to the application
        self.function_plotter_figure = Figure()
        self.function_plotter_figure_canvas = FigureCanvas(
            self.function_plotter_figure)
        self.ui.Plotting_Layout.addWidget(self.function_plotter_figure_canvas)

        # handling max and min value inputs to accept just numbers
        validator = QDoubleValidator()
        self.ui.min_value_input.setValidator(validator)
        self.ui.max_value_input.setValidator(validator)

        # connecting the buttons to their functions
        self.ui.pushButton.clicked.connect(self.get_user_function)
        self.ui.pushButton_2.clicked.connect(self.save_figure_from_gui)

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

    def get_user_function(self):
        try:
            self.user_function = self.ui.function_input.text().strip()
            self.max_range_value = self.ui.max_value_input.text()
            self.min_range_value = self.ui.min_value_input.text()

            # check for input validation
            if self.check_entered_input_values(
                    self.user_function, self.min_range_value, self.max_range_value):

                self.min_range_value = float(self.min_range_value)
                self.max_range_value = float(self.max_range_value)

                equation_expressions = self.calculate_function_expression(
                    self.user_function)

                if not equation_expressions:
                    return

                range_values = np.linspace(
                    self.min_range_value, self.max_range_value, self.number_of_points)

                full_equation = 0
                x_axis = []
                y_axis = []

                for expression in equation_expressions:
                    full_equation += expression

                # check if the expression is a single number
                if not (isinstance(full_equation, float)):
                    for i in range_values:
                        new_y = full_equation.subs(self.x_symbol, i)
                        if new_y == sympy.zoo:
                            self.raise_error(
                                f"The value x={i} after substitution cause infinity!!")
                            x_axis = []
                            y_axis = []
                            break
                        x_axis.append(i)
                        y_axis.append(new_y)

                else:
                    x_axis = range_values
                    y_axis = np.repeat(full_equation, len(range_values))

                if (len(x_axis) > 0 or len(y_axis) > 0):
                    figure_axes = self.function_plotter_figure.gca()
                    figure_axes.cla()
                    figure_axes.grid(True)
                    figure_axes.set_facecolor((1, 1, 1))
                    figure_axes.set_title("Equation: " + str(full_equation))
                    figure_axes.set_xlabel("x axis")
                    figure_axes.set_ylabel("y axis")
                    figure_axes.plot(x_axis, y_axis)

                self.function_plotter_figure_canvas.draw()
                self.function_plotter_figure_canvas.flush_events()
        except Exception as e:
            print(e)

    def calculate_function_expression(self, function):
        try:
            added_expressions = []
            new_expression = 1

            index = 0
            while True:
                if index == len(function):
                    added_expressions.append(new_expression)
                    break

                char = function[index]
                if char == "x":
                    new_expression *= self.x_symbol
                # if having a power character
                elif char == "^":
                    index += 1
                    power = np.double(function[index])

                    while (power > 1):
                        if function[index-2] == "x":
                            new_expression *= self.x_symbol
                        elif function[index-2].isdigit():
                            new_expression *= np.double(function[index-2])
                        power -= 1

                elif char == "*":
                    index += 1
                    if (function[index] == "x"):
                        new_expression *= self.x_symbol
                    elif (function[index].isdigit()):
                        new_expression *= np.double(function[index])

                elif char == "/":
                    index += 1
                    if (function[index] == "x"):
                        new_expression /= self.x_symbol
                    elif (function[index].isdigit()):
                        new_expression /= np.double(function[index])

                elif char.isdigit():
                    first_index = index
                    while True:
                        index += 1
                        if index == len(function):
                            break
                        next_char = function[index]
                        if next_char.isdigit() or next_char == ".":
                            continue
                        else:
                            break

                    last_index = index
                    index -= 1
                    if first_index == last_index:
                        new_expression *= np.double(function[first_index])
                    else:
                        new_expression *= np.double(
                            function[first_index:last_index])

                elif char == "+":
                    if index != 0:
                        added_expressions.append(new_expression)
                    new_expression = 1

                elif char == "-":
                    if index != 0:
                        added_expressions.append(new_expression)
                    new_expression = -1

                elif char == ".":
                    self.raise_error(
                        "Floating Numbers must start with Digit. (i.e 0.21)")
                    added_expressions = []
                    new_expression = 1
                    return False

                index += 1
            return added_expressions
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
