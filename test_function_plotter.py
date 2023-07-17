from PySide2.QtCore import Qt
from pytestqt import qtbot
from main import MainWindow


def test_empty_input_values(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "")
    qtbot.keyClicks(window.ui.min_value_input, "")
    qtbot.keyClicks(window.ui.max_value_input, "")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert error_message == "Function, min, and max value must be entered."


def test_wrong_min_max_values(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^2")
    qtbot.keyClicks(window.ui.min_value_input, "5")
    qtbot.keyClicks(window.ui.max_value_input, "0")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert error_message == "Maximum value must be greater than Minimum value."


def test_right_input_values(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^2")
    qtbot.keyClicks(window.ui.min_value_input, "0")
    qtbot.keyClicks(window.ui.max_value_input, "5")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert window.function_plotter_figure.gca().get_title() == "Equation: x**2"
    assert window.function_plotter_figure.gca().get_xlabel() == "x axis"
    assert window.function_plotter_figure.gca().get_ylabel() == "y axis"
    assert len(window.function_plotter_figure.gca().lines) == 1


def test_invalid_float_number(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^2 + 3.3.3")
    qtbot.keyClicks(window.ui.min_value_input, "3")
    qtbot.keyClicks(window.ui.max_value_input, "5")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert error_message == "Floating Numbers must have one dot. (i.e 0.21)"


def test_invalid_float_number_2(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^2 + .3")
    qtbot.keyClicks(window.ui.min_value_input, "3")
    qtbot.keyClicks(window.ui.max_value_input, "5")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert error_message == "Floating Numbers must start with Digit. (i.e 0.21)"


def test_valid_float_number(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^2 + 3")
    qtbot.keyClicks(window.ui.min_value_input, "3.3")
    qtbot.keyClicks(window.ui.max_value_input, "5.5")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert window.function_plotter_figure.gca().get_title() == "Equation: x**2 + 3.0"
    assert window.function_plotter_figure.gca().get_xlabel() == "x axis"
    assert window.function_plotter_figure.gca().get_ylabel() == "y axis"
    assert len(window.function_plotter_figure.gca().lines) == 1


def test_invalid_char_in_function(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^@ + 3")
    qtbot.keyClicks(window.ui.min_value_input, "3")
    qtbot.keyClicks(window.ui.max_value_input, "5")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert error_message == "Char ( @ ) is not valid!"


def test_invalid_function_format(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    error_message = ""

    def mock_raise_error(message):
        nonlocal error_message
        error_message = message

    window.raise_error = mock_raise_error

    qtbot.keyClicks(window.ui.function_input, "x^2 + 3 -")
    qtbot.keyClicks(window.ui.min_value_input, "3")
    qtbot.keyClicks(window.ui.max_value_input, "5")

    qtbot.mouseClick(window.ui.pushButton, Qt.LeftButton)

    assert error_message == "The function can't start or end with operator."
