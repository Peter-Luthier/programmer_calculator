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
        self.display_num_bits = 8
        self.working_value = 0
        self.base = 10
        self.style_path = styles['Light']

        self.setWindowTitle('Binary Calculator')

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

        # -- Operator Keys -- #

        self.operator_values = ['AND', 'OR', 'NOT', 'NOR', 'XOR', 'XNOR', '÷', 'x', '<<', '-', '+', '>>', 'AC', 'CL', '=']
        self.operator_buttons = []

        for operator in self.operator_values:
            self.operator_buttons.append(
                CustomRoundButton(
                    operator, self.handle_button_press, self.style_path, operator))

        # -- Operator Keys Layout -- #

        self.layout_operator = QGridLayout()

        column_num = 0
        row_num = 0
        for button in self.operator_buttons:
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
        self.layout_container.addWidget(self.operand_widget, 2, 0)
        self.layout_container.addWidget(self.operator_widget, 2, 1)

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
        max_binary_value = 2 ** self.display_num_bits - 1
        if self.working_value > max_binary_value:
            return '** Overflow **'
        binary_length = (self.display_num_bits - 1) + self.display_num_bits // 4
        binary_string = format(self.working_value, f'0{binary_length}_b').replace('_', ' ')
        return binary_string

    def update_button_action(self, button, click_action):
        button.clicked.disconnect()
        button.clicked.connect(lambda: click_action(button.text()))

    def create_shortcut(self, button, key):
        shortcut = QShortcut(QKeySequence(key), button)
        shortcut.activated.connect(button.click)
        self.shortcuts.append(shortcut)
