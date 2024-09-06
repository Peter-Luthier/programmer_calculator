from unittest import TestCase
from calculator_model import CalculatorModel


class TestCalculatorModel(TestCase):
    def test_clear(self):
        calculator = CalculatorModel()
        calculator.working_operand = 27
        calculator.clear()
        self.assertEqual(calculator.working_operand, 0)

    def test_add(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 4
        calculator.operator = '+'
        expected_result = 27 + 4
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_subtract(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 4
        calculator.operator = '-'
        expected_result = 23
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_multiply(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 4
        calculator.operator = '*'
        expected_result = 27 * 4
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_divide(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 4
        calculator.operator = '//'
        expected_result = 6
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_and(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 7
        calculator.operator = '&'
        expected_result = 3
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_or(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 5
        calculator.operator = '|'
        expected_result = 31
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_xor(self):
        calculator = CalculatorModel()
        calculator.accumulator_operand = 27
        calculator.working_operand = 5
        calculator.operator = '^'
        expected_result = 30
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_not(self):
        calculator = CalculatorModel()
        calculator.working_operand = 27
        calculator.operator = '~'
        expected_result = 228
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_shift_left(self):
        calculator = CalculatorModel()
        calculator.working_operand = 27
        calculator.operator = '<<'
        expected_result = 54
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_shift_right(self):
        calculator = CalculatorModel()
        calculator.working_operand = 27
        calculator.operator = '>>'
        expected_result = 13
        self.assertEqual(calculator.evaluate(), expected_result)

    def test_bitwise_nor(self):
        calculator = CalculatorModel()
        calculator.display_num_bits = 8
        calculator.accumulator_operand = 27
        calculator.working_operand = 15
        calculator.operator = 'NOR'
        expected_result = 224
        self.assertEqual(calculator.evaluate_nor_operation(), expected_result)