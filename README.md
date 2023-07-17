# Master-Micro-Python-Internship

## Install required packages

```
pip install -r requirements.txt
```

## Run the code

```
python main.py

# or

python3 main.py
```

## How it works

<p>

The application takes the user function from input field with the minimum and maximum value.<br />

The user function consists of x variable either in capital or small letter, and other numbers.<br />

The function <em>"check_entered_input_values"</em> checks the user input values that they are not empty values, and the maximum value is greater than the minimum value.<br />

In case of invalid input values, the application shows the error message using <em>QMessageBox</em> from <em>PySide2.QtWidgets</em>.<br />

The function <em>"calculate_function_expression"</em> takes the user function from input field and divide it into expressions.<br />

These expressions are then added together into a single equation variable. According to the minimum and maximum value, the equation variable is calculated and the result is displayed in the <em>matplotlib figure</em>.<br />

The figure title has the user function written in a right format. Like if the user typed <Strong>(x + 4.3 + x + 2 + 3*x + x^2)</Strong> <br /> it will be modified into <strong>(x^2 + 5*x + 6.3 )</strong>. <br />

</p>

## Demo

![Demo]()

## Screenshots

### Valid Examples

![Working Examples]()

### Invalid Examples

![Invalid Examples]()

## Testing the application
