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

        button_hex = QPushButton('Hexadecimal')
        button_hex.clicked.connect(lambda: self.handle_button_press('Hexadecimal'))

        button_binary = QPushButton('Binary')
        button_binary.clicked.connect(lambda: self.handle_button_press('Binary'))

        layout_input_mode = QHBoxLayout()

        layout_input_mode.addWidget(button_decimal)
        layout_input_mode.addWidget(button_hex)
        layout_input_mode.addWidget(button_binary)

        self.input_mode = QWidget()
        self.input_mode.setLayout(layout_input_mode)

        # -- Input Keys -- #

        self.button0 = CustomRoundButton('0', self.handle_button_press, self.style_path, 0)
        self.button1 = CustomRoundButton('1', self.handle_button_press, self.style_path, 1)
        self.button2 = CustomRoundButton('2', self.handle_button_press, self.style_path, 2)
        self.button3 = CustomRoundButton('3', self.handle_button_press, self.style_path, 3)
        self.button4 = CustomRoundButton('4', self.handle_button_press, self.style_path, 4)
        self.button5 = CustomRoundButton('5', self.handle_button_press, self.style_path, 5)
        self.button6 = CustomRoundButton('6', self.handle_button_press, self.style_path, 6)
        self.button7 = CustomRoundButton('7', self.handle_button_press, self.style_path, 7)
        self.button8 = CustomRoundButton('8', self.handle_button_press, self.style_path, 8)
        self.button9 = CustomRoundButton('9', self.handle_button_press, self.style_path, 9)
        self.button_a = CustomRoundButton('A', self.handle_button_press, self.style_path, 10)
        self.button_b = CustomRoundButton('B', self.handle_button_press, self.style_path, 11)
        self.button_c = CustomRoundButton('C', self.handle_button_press, self.style_path, 12)
        self.button_d = CustomRoundButton('D', self.handle_button_press, self.style_path, 13)
        self.button_e = CustomRoundButton('E', self.handle_button_press, self.style_path, 14)
        self.button_f = CustomRoundButton('F', self.handle_button_press, self.style_path, 15)

        self.operand_buttons = [
            self.button0,
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
            self.button_a,
            self.button_b,
            self.button_c,
            self.button_d,
            self.button_e,
            self.button_f
        ]

        # -- Input Keys Layout -- #

        self.layout_input = QGridLayout()

        column_num = 2
        row_num = 5
        for button in self.operand_buttons:
            self.layout_input.addWidget(button, row_num, column_num)
            column_num += 1
            if column_num > 2:
                row_num -= 1
                column_num = 0
            self.create_shortcut(button, button.text())

        self.input_keys = QWidget()
        self.input_keys.setLayout(self.layout_input)

        # -- Output Displays -- #

        decimal_label = QLabel('Decimal')
        self.decimal_output = QLabel()
        hex_label = QLabel('Hexadecimal')
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

        self.output = QWidget()
        self.output.setLayout(layout_output)

        self.layout_container = QGridLayout()
        self.layout_container.addWidget(self.output, 0, 0)
        self.layout_container.addWidget(self.input_mode, 1, 0)
        self.layout_container.addWidget(self.input_keys, 2, 0)

        self.container = QWidget()
        self.container.setLayout(self.layout_container)

        self.setCentralWidget(self.container)

    def set_base(self, base):
        self.base = base
        self.set_disabled_buttons()

    def set_disabled_buttons(self):
        for button in self.operand_buttons:
            if button.value >= self.base:
                button.setDisabled(True)
            else:
                button.setDisabled(False)

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
        # Create a shortcut and connect it to the button's click action
        shortcut = QShortcut(QKeySequence(key), button)
        shortcut.activated.connect(button.click)
        self.shortcuts.append(shortcut)
