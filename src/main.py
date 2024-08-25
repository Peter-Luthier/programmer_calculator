import sys

from PyQt6.QtWidgets import QApplication

from calculator_view import CalculatorView
from calculator_controller import CalculatorController
from calculator_model import CalculatorModel

app = QApplication(sys.argv)

model = CalculatorModel()
view = CalculatorView()
controller = CalculatorController(model, view)

view.show()

app.exec()