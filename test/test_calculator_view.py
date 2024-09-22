from unittest import TestCase
from calculator_view import CalculatorView


class TestCalculatorView(TestCase):
    def test_format_binary_string(self):
        value_inputs = [0, 0, 0, 0, 0, 0, 0, 200, 200, 95023, 95023]
        length_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 32, 33]
        expected_outputs = ['0', '00', '000', '0000', '0 0000', '00 0000', '000 0000', '1100 1000',
                            '0 1100 1000', '0000 0000 0000 0001 0111 0011 0010 1111', '0\n0000 0000 0000 0001 0111 0011 0010 1111']
        for i in range(0, len(expected_outputs)):
            with self.subTest(i = f'Bit length: {length_inputs[i]}'):
                test_output = CalculatorView.format_binary_string(value_inputs[i], length_inputs[i], 32)
                self.assertEqual(expected_outputs[i], test_output)
