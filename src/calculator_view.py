from pathlib import Path
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import *
from button_widget import CustomRoundButton

styles = {
    'Light': Path(__file__).parent.absolute() / 'resources' / 'light_style.qss',
    'Dark': Path(__file__).parent.absolute() / 'resources' / 'dark_style.qss',
}

class CalculatorView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.shortcuts = []
        self.operand_buttons = None
        self.bit_depth = 16
        self.max_bits_per_line = 32
        self.working_value = 0
        self.base = 10
        self.style_path = styles['Light']

        self.setWindowTitle('Programmer Calculator')

        # -- Input Mode Keys -- #

        button_decimal = QPushButton('Decimal')
        button_decimal.clicked.connect(lambda: self.handle_button_press('Decimal'))

        button_hex = QPushButton('Hex')
        button_hex.clicked.connect(lambda: self.handle_button_press('Hex'))

        button_binary = QPushButton('Binary')
        button_binary.clicked.connect(lambda: self.handle_button_press('Binary'))

        layout_input_mode = QHBoxLayout()

        layout_input_mode.addWidget(button_decimal)
        layout_input_mode.addWidget(button_hex)
        layout_input_mode.addWidget(button_binary)

        self.input_mode_widget = QWidget()
        self.input_mode_widget.setLayout(layout_input_mode)

        # -- Bit Depth Keys -- #

        button_64_bit = QPushButton('64 bit')
        button_64_bit.clicked.connect(lambda: self.handle_button_press('64 bit'))

        button_32_bit = QPushButton('32 bit')
        button_32_bit.clicked.connect(lambda: self.handle_button_press('32 bit'))

        button_16_bit = QPushButton('16 bit')
        button_16_bit.clicked.connect(lambda: self.handle_button_press('16 bit'))

        button_8_bit = QPushButton('8 bit')
        button_8_bit.clicked.connect(lambda: self.handle_button_press('8 bit'))

        button_minus_bit = QPushButton('-bit')
        button_minus_bit.clicked.connect(lambda: self.handle_button_press('- bit'))

        button_plus_bit = QPushButton('+bit')
        button_plus_bit.clicked.connect(lambda: self.handle_button_press('+ bit'))

        layout_bit_depth = QHBoxLayout()

        layout_bit_depth.addWidget(button_64_bit)
        layout_bit_depth.addWidget(button_32_bit)
        layout_bit_depth.addWidget(button_16_bit)
        layout_bit_depth.addWidget(button_8_bit)
        layout_bit_depth.addWidget(button_minus_bit)
        layout_bit_depth.addWidget(button_plus_bit)

        self.input_bit_depth_widget = QWidget()
        self.input_bit_depth_widget.setLayout(layout_bit_depth)

        # -- Operand Keys -- #

        self.operand_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        self.operand_buttons = []

        for operand in self.operand_values:
            self.operand_buttons.append(
                CustomRoundButton(
                    operand, self.handle_button_press, self.style_path, self.operand_values.index(operand)))

        # -- Operand Keys Layout -- #

        self.layout_operand = QGridLayout()

        column_num = 2
        row_num = 5
        for button in self.operand_buttons:
            self.layout_operand.addWidget(button, row_num, column_num)
            column_num += 1
            if column_num > 2:
                row_num -= 1
                column_num = 0
            self.create_shortcut(button, button.text())

        self.operand_widget = QWidget()
        self.operand_widget.setLayout(self.layout_operand)

        # -- Operator Buttons -- #

        button_plus = CustomRoundButton('+', self.handle_button_press, self.style_path, '+')
        button_minus = CustomRoundButton('-', self.handle_button_press, self.style_path, '-')
        button_multiply = CustomRoundButton('x', self.handle_button_press, self.style_path, '*')
        button_divide = CustomRoundButton('÷', self.handle_button_press, self.style_path, '//')
        button_shift_left = CustomRoundButton('<<', self.handle_button_press, self.style_path, '<<')
        button_shift_right = CustomRoundButton('>>', self.handle_button_press, self.style_path, '>>')
        button_binary_and = CustomRoundButton('AND', self.handle_button_press, self.style_path, '&')
        button_binary_or = CustomRoundButton('OR', self.handle_button_press, self.style_path, '|')
        button_binary_not = CustomRoundButton('NOT', self.handle_button_press, self.style_path, '~')
        button_binary_xor = CustomRoundButton('XOR', self.handle_button_press, self.style_path, '^')
        button_binary_nor = CustomRoundButton('NOR', self.handle_button_press, self.style_path, 'NOR')

        # self.operator_values = ['AND', 'OR', 'NOT', 'NOR', 'XOR', 'XNOR', '÷', 'x', '<<', '-', '+', '>>', 'AC', 'CL', '=']



        self.operator_buttons = [button_plus,
                                 button_minus,
                                 button_multiply,
                                 button_divide,
                                 button_shift_left,
                                 button_shift_right,
                                 button_binary_and,
                                 button_binary_or,
                                 button_binary_not,
                                 button_binary_xor,
                                 button_binary_nor]

        # -- Function Buttons -- #

        button_equals = CustomRoundButton('=', self.handle_button_press, self.style_path, '=')
        button_clear = CustomRoundButton('CL', self.handle_button_press, self.style_path, 'CL')
        button_all_clear = CustomRoundButton('AC', self.handle_button_press, self.style_path, 'AC')

        self.function_buttons = [button_equals,
                                 button_clear,
                                 button_all_clear]

        # -- Operator Keys Layout -- #

        self.layout_operator = QGridLayout()

        column_num = 0
        row_num = 0
        for button in self.operator_buttons + self.function_buttons:
            self.layout_operator.addWidget(button, row_num, column_num)
            column_num += 1
            if column_num > 2:
                row_num += 1
                column_num = 0
            self.create_shortcut(button, button.text())

        self.operator_widget = QWidget()
        self.operator_widget.setLayout(self.layout_operator)

        # -- Output Displays -- #

        decimal_label = QLabel('Decimal')
        self.decimal_output = QLabel()
        hex_label = QLabel('Hex')
        self.hex_output = QLabel()
        binary_label = QLabel('Binary')
        self.binary_output = QLabel()

        self.update_output(self.working_value)

        layout_output = QGridLayout()
        layout_output.addWidget(decimal_label, 0, 0, 1, 1)
        layout_output.addWidget(self.decimal_output, 0, 1, 1, 4)
        layout_output.addWidget(hex_label, 1, 0, 1, 1)
        layout_output.addWidget(self.hex_output, 1, 1, 1, 4)
        layout_output.addWidget(binary_label, 2, 0, 1, 1)
        layout_output.addWidget(self.binary_output, 2, 1, 1, 4)

        self.output_widget = QWidget()
        self.output_widget.setLayout(layout_output)

        self.layout_container = QGridLayout()
        self.layout_container.addWidget(self.output_widget, 0, 0, 1, 2)
        self.layout_container.addWidget(self.input_mode_widget, 1, 0, 1, 2)
        self.layout_container.addWidget(self.input_bit_depth_widget, 2, 0, 1, 2)
        self.layout_container.addWidget(self.operand_widget, 3, 0)
        self.layout_container.addWidget(self.operator_widget, 3, 1)

        self.container = QWidget()
        self.container.setLayout(self.layout_container)

        self.setCentralWidget(self.container)

    def set_base(self, base):
        self.base = base
        self.set_disabled_buttons()

    def set_disabled_buttons(self):
        for button in self.operand_buttons:
            button.set_disabled(self.base)

    def handle_button_press(self, input_value):
        pass

    def update_output(self, value):
        if not value:
            value = 0
        self.working_value = value
        self.decimal_output.setText(str(format(self.working_value, ',')))
        self.hex_output.setText(self.format_hex_output())
        self.binary_output.setText(self.format_binary_output())

    def format_hex_output(self):
        hex_string = format(self.working_value, 'X')
        reversed_hex_string = hex_string[::-1]
        hex_string = ' '.join(reversed_hex_string[i:i + 2] for i in range(0, len(hex_string), 2))
        return hex_string[::-1]

    def format_binary_output(self):
        max_binary_value = 2 ** self.bit_depth - 1
        if self.working_value > max_binary_value:
            return '** Overflow **'
        binary_string = self.format_binary_string(self.working_value, self.bit_depth, self.max_bits_per_line)
        return binary_string

    @staticmethod
    def format_binary_string(num, bit_length, max_bits_per_line):
        binary_string = f"{num:0{bit_length}b}"
        rev_bin_str = binary_string[::-1]
        binary_lines = [rev_bin_str[i:i+max_bits_per_line] for i in range(0, len(rev_bin_str), max_bits_per_line)]
        line_list = []
        for line in binary_lines:
            grouped_bits = ' '.join([line[i:i+4] for i in range(0, len(line), 4)])
            line_list.insert(0, grouped_bits[::-1])
        formatted_string =  '\n'.join(line_list)

        return formatted_string

    @staticmethod
    def update_button_action(button, click_action):
        button.clicked.disconnect()
        button.clicked.connect(lambda: click_action(button.text()))

    def create_shortcut(self, button, key):
        shortcut = QShortcut(QKeySequence(key), button)
        shortcut.activated.connect(button.click)
        self.shortcuts.append(shortcut)
