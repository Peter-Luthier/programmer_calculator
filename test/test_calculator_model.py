from unittest import TestCase
from calculator_model import CalculatorModel


class TestCalculatorModel(TestCase):
    def test_clear_working_value(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.clear_working_value()
        self.assertEqual(calculator.working_value, None)

    def test_clear_state(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('+')
        calculator.handle_numeric_input(4)
        calculator.handle_numeric_input(2)
        calculator.evaluate()
        calculator = CalculatorModel()
        calculator.handle_numeric_input(4)
        calculator.handle_numeric_input(8)
        calculator.handle_operator('-')
        calculator.handle_numeric_input(1)
        calculator.handle_numeric_input(0)
        calculator.clear_state()
        self.assertEqual(calculator.working_value, None)
        self.assertEqual(calculator.operand1, None)
        self.assertEqual(calculator.operand2, None)
        self.assertEqual(calculator.operator, None)
        self.assertEqual(calculator.result, None)

    def test_add(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('+')
        calculator.handle_numeric_input(4)

        expected_result = 31
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_subsequent_addition_with_equals(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('+')
        calculator.handle_numeric_input(4)
        calculator.evaluate()
        calculator.handle_operator('+')
        calculator.handle_numeric_input(9)

        expected_result = 40
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_subsequent_addition_without_equals(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('+')
        calculator.handle_numeric_input(4)
        calculator.handle_operator('+')
        calculator.handle_numeric_input(9)

        expected_result = 40
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_subtract(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('-')
        calculator.handle_numeric_input(4)

        expected_result = 23
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_multiply(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('*')
        calculator.handle_numeric_input(4)

        expected_result = 108
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_divide(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('//')
        calculator.handle_numeric_input(4)

        expected_result = 6
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_and(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('&')
        calculator.handle_numeric_input(7)

        expected_result = 3
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_or(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('|')
        calculator.handle_numeric_input(5)

        expected_result = 31
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_xor(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('^')
        calculator.handle_numeric_input(5)

        expected_result = 30
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_not(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_not_operator()

        expected_result = 228
        self.assertEqual(calculator.working_value, expected_result)

    def test_bitwise_shift_left(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_bitshift_left()
        expected_result = 54
        self.assertEqual(calculator.working_value, expected_result)

    def test_bitwise_shift_left_drop_highest(self):
        calculator = CalculatorModel()
        calculator.bit_depth = 8
        calculator.handle_numeric_input(1)
        calculator.handle_numeric_input(6)
        calculator.handle_numeric_input(1)
        calculator.handle_bitshift_left()
        expected_result = 66
        self.assertEqual(calculator.working_value, expected_result)

    def test_bitwise_shift_right(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_bitshift_right()
        expected_result = 13
        self.assertEqual(calculator.working_value, expected_result)

    def test_bitwise_nor(self):
        calculator = CalculatorModel()
        calculator.bit_depth = 8
        calculator.handle_numeric_input(2)
        calculator.handle_numeric_input(7)
        calculator.handle_operator('NOR')
        calculator.handle_numeric_input(1)
        calculator.handle_numeric_input(5)

        expected_result = 224
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_evaluate_number_plus_equals(self):
        calculator = CalculatorModel()
        calculator.handle_numeric_input(1)
        calculator.handle_numeric_input(2)
        calculator.handle_operator('+')

        expected_result = 24
        self.assertEqual(calculator.evaluate(), expected_result)