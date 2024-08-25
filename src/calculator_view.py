import sys
from PyQt6.QtWidgets import *

# from .calculator_controller import CalcController


class CalcButton(QPushButton):
    def __init__(self, label, controller_obj):
        super().__init__(label)


class CalculatorWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.ctrl = controller
        self.model = controller.model

        self.setWindowTitle('Binary Calculator')
        self.calc_mode = self.model.base_mode



        # -- Input Mode Keys -- #

        button_decimal = QPushButton('DEC')
        button_decimal.clicked.connect(self.set_input_mode_decimal)

        button_hex = QPushButton('HEX')
        button_hex.clicked.connect(self.set_input_mode_hex)

        button_binary = QPushButton('BIN')
        button_binary.clicked.connect(self.set_input_mode_binary)

        layout_input_mode = QHBoxLayout()

        layout_input_mode.addWidget(button_decimal)
        layout_input_mode.addWidget(button_hex)
        layout_input_mode.addWidget(button_binary)

        self.input_mode = QWidget()
        self.input_mode.setLayout(layout_input_mode)

        # -- Input Keys -- #

        self.button_a = QPushButton('A')
        self.button_a.clicked.connect(lambda: self.handle_key_press('A'))
        self.button_b = QPushButton('B')
        self.button_b.clicked.connect(lambda: self.handle_key_press('B'))
        self.button_c = QPushButton('C')
        self.button_c.clicked.connect(lambda: self.handle_key_press('C'))
        self.button_d = QPushButton('D')
        self.button_d.clicked.connect(lambda: self.handle_key_press('D'))
        self.button_e = QPushButton('E')
        self.button_e.clicked.connect(lambda: self.handle_key_press('E'))
        self.button_f = QPushButton('F')
        self.button_f.clicked.connect(lambda: self.handle_key_press('F'))

        self.button1 = QPushButton('1')
        self.button1.clicked.connect(lambda: self.handle_key_press('1'))
        self.button2 = QPushButton('2')
        self.button2.clicked.connect(lambda: self.handle_key_press('2'))
        self.button3 = QPushButton('3')
        self.button3.clicked.connect(lambda: self.handle_key_press('3'))
        self.button4 = QPushButton('4')
        self.button4.clicked.connect(lambda: self.handle_key_press('4'))
        self.button5 = QPushButton('5')
        self.button5.clicked.connect(lambda: self.handle_key_press('5'))
        self.button6 = QPushButton('6')
        self.button6.clicked.connect(lambda: self.handle_key_press('6'))
        self.button7 = QPushButton('7')
        self.button7.clicked.connect(lambda: self.handle_key_press('7'))
        self.button8 = QPushButton('8')
        self.button8.clicked.connect(lambda: self.handle_key_press('8'))
        self.button9 = QPushButton('9')
        self.button9.clicked.connect(lambda: self.handle_key_press('9'))
        self.button0 = QPushButton('0')
        self.button0.clicked.connect(lambda: self.handle_key_press('0'))

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

        decimal_label = QLabel('DEC')
        self.decimal_output = QLabel()
        hex_label = QLabel('HEX')
        self.hex_output = QLabel()
        binary_label = QLabel('BIN')
        self.binary_output = QLabel()

        self.update_outputs()

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

        self.set_input_mode_decimal()

        print(self.model.max_binary_value)

    def set_input_mode_decimal(self):
        self.set_disabled_a_f_keys(True)
        self.set_disabled_2_9_keys(False)
        self.ctrl.set_base_mode('decimal')
        print('Decimal Mode')

    def set_input_mode_hex(self):
        self.set_disabled_a_f_keys(False)
        self.set_disabled_2_9_keys(False)
        self.ctrl.set_base_mode('hex')
        print('HEX Mode')

    def set_input_mode_binary(self):
        self.set_disabled_a_f_keys(True)
        self.set_disabled_2_9_keys(True)
        self.ctrl.set_base_mode('binary')
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

    """
    def key_press_event(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            self.ctrl.handle_numeric_input(key_text.upper())
            self.update_outputs()
            """

    def handle_key_press(self, input_value):
        self.ctrl.handle_numeric_input(input_value)
        self.update_outputs()

    def update_outputs(self):
        self.decimal_output.setText(str(format(self.model.working_value, ',')))
        self.hex_output.setText(self.format_hex_output())
        self.binary_output.setText(self.format_binary_output())

    def format_hex_output(self):
        hex_string = format(self.model.working_value, 'X')
        reversed_hex_string = hex_string[::-1]
        hex_string = ' '.join(reversed_hex_string[i:i+2] for i in range(0, len(hex_string), 2))
        return hex_string[::-1]

    def format_binary_output(self):
        if self.model.working_value > self.model.max_binary_value:
            return '** Overflow **'
        binary_length = (self.model.display_num_bits - 1) + self.model.display_num_bits // 4
        binary_string = format(self.model.working_value, f'0{binary_length}_b').replace('_', ' ')
        return binary_string


if __name__ == '__main__':
    from calculator_model import CalcModel
    from calculator_controller import CalcController
    app = QApplication(sys.argv)

    window = CalculatorWindow(CalcController(CalcModel()))
    window.show()

    app.exec()
