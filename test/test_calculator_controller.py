from unittest import TestCase
from calculator_controller import *
from calculator_model import *
from calculator_view import *


class TestCalcController(TestCase):
    def test_handle_numeric_input(self):
        self.fail()

    def test_handle_decimal_numeric_input(self):
        self.fail()

    def test_handle_hex_numeric_input(self):
        self.fail()

    def test_handle_binary_numeric_input(self):
        self.fail()

    def test_set_base_mode(self):
        controller = CalculatorController(CalculatorModel(), CalculatorView())
        mode_list = ['Hexadecimal', 'Binary', 'Decimal']
        base_list = [16, 2, 10]
        for i in range(0, len(mode_list)):
            new_mode = mode_list[i]
            new_base = base_list[i]
            with self.subTest(new_mode=new_mode):
                controller.set_base_mode(new_mode)
                self.assertEqual(controller.model.base, new_base)

