import sys

from PyQt6.QtWidgets import QApplication

from calculator_view import CalculatorWindow
from calculator_controller import CalcController
from calculator_model import CalcModel

controller = CalcController(CalcModel())

app = QApplication(sys.argv)

window = CalculatorWindow(controller)
window.show()

app.exec()