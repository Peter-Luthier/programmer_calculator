from pathlib import Path

from PyQt6.QtWidgets import *
from button_widget import CustomRoundButton

light_style_path = Path(__file__).parent.absolute() / 'resources' / 'light_style.qss'
dark_style_path = Path(__file__).parent.absolute() / 'resources' / 'dark_style.qss'


class CalculatorView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons = None
        self.display_num_bits = 8
        self.working_value = 0
        self.base = 10

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

        self.button0 = CustomRoundButton('0', self.handle_button_press, light_style_path, 0)
        self.button1 = CustomRoundButton('1', self.handle_button_press, light_style_path, 1)
        self.button2 = CustomRoundButton('2', self.handle_button_press, light_style_path, 2)
        self.button3 = CustomRoundButton('3', self.handle_button_press, light_style_path, 3)
        self.button4 = CustomRoundButton('4', self.handle_button_press, light_style_path, 4)
        self.button5 = CustomRoundButton('5', self.handle_button_press, light_style_path, 5)
        self.button6 = CustomRoundButton('6', self.handle_button_press, light_style_path, 6)
        self.button7 = CustomRoundButton('7', self.handle_button_press, light_style_path, 7)
        self.button8 = CustomRoundButton('8', self.handle_button_press, light_style_path, 8)
        self.button9 = CustomRoundButton('9', self.handle_button_press, light_style_path, 9)
        self.button_a = CustomRoundButton('A', self.handle_button_press, light_style_path, 10)
        self.button_b = CustomRoundButton('B', self.handle_button_press, light_style_path, 11)
        self.button_c = CustomRoundButton('C', self.handle_button_press, light_style_path, 12)
        self.button_d = CustomRoundButton('D', self.handle_button_press, light_style_path, 13)
        self.button_e = CustomRoundButton('E', self.handle_button_press, light_style_path, 14)
        self.button_f = CustomRoundButton('F', self.handle_button_press, light_style_path, 15)

        self.buttons = [
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

        self.layout_input.addWidget(self.button_d, 0, 0)
        self.layout_input.addWidget(self.button_e, 0, 1)
        self.layout_input.addWidget(self.button_f, 0, 2)
        self.layout_input.addWidget(self.button_a, 1, 0)
        self.layout_input.addWidget(self.button_b, 1, 1)
        self.layout_input.addWidget(self.button_c, 1, 2)
        self.layout_input.addWidget(self.button7, 2, 0)
        self.layout_input.addWidget(self.button8, 2, 1)
        self.layout_input.addWidget(self.button9, 2, 2)
        self.layout_input.addWidget(self.button4, 3, 0)
        self.layout_input.addWidget(self.button5, 3, 1)
        self.layout_input.addWidget(self.button6, 3, 2)
        self.layout_input.addWidget(self.button1, 4, 0)
        self.layout_input.addWidget(self.button2, 4, 1)
        self.layout_input.addWidget(self.button3, 4, 2)
        self.layout_input.addWidget(self.button0, 5, 0, 1, 3)

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
        base_dict = {
            2: self.set_input_mode_binary,
            10: self.set_input_mode_decimal,
            16: self.set_input_mode_hex,
        }
        if base in base_dict:
            base_dict[base]()

    def set_input_mode_decimal(self):
        self.set_disabled_a_f_keys(True)
        self.set_disabled_2_9_keys(False)
        print('Decimal Mode')

    def set_input_mode_hex(self):
        self.set_disabled_a_f_keys(False)
        self.set_disabled_2_9_keys(False)
        print('Hexadecimal Mode')

    def set_input_mode_binary(self):
        self.set_disabled_a_f_keys(True)
        self.set_disabled_2_9_keys(True)
        print('Binary Mode')

    def set_disabled_a_f_keys(self, state: bool):
        self.button_a.setDisabled(state)
        self.button_b.setDisabled(state)
        self.button_c.setDisabled(state)
        self.button_d.setDisabled(state)
        self.button_e.setDisabled(state)
        self.button_f.setDisabled(state)

    def set_disabled_2_9_keys(self, state: bool):
        self.button2.setDisabled(state)
        self.button3.setDisabled(state)
        self.button4.setDisabled(state)
        self.button5.setDisabled(state)
        self.button6.setDisabled(state)
        self.button7.setDisabled(state)
        self.button8.setDisabled(state)
        self.button9.setDisabled(state)

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


class CalcButton(QPushButton):
    def __init__(self, label, handle_button_press, num_value=None):
        super().__init__(label)
        self.setMinimumHeight(35)
        self.clicked.connect(handle_button_press(label))
