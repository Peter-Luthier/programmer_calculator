from PyQt6.QtGui import QShortcut, QKeySequence

# @TODO - Handle value overflow
# @TODO - Themes


class CalculatorController:
    def __init__(self, calculator_model, calculator_view):
        self.mode_list = ['Binary', 'Decimal', 'Hex']
        self.bit_depth_list = ['64 bit', '32 bit', '16 bit', '8 bit', '+ bit', '- bit']
        self.base_value_list = [2, 10, 16]
        self.model = calculator_model
        self.view = calculator_view
        self.view.handle_button_press = self.handle_button_press
        self.view.set_base(self.model.base)
        self.view.bit_depth = self.model.bit_depth
        self.setup_actions()
        self.view.update_output(self.model.working_value)

        # --- Key shortcuts --- #

        self.enter_shortcut = QShortcut(QKeySequence("Enter"), self.view)
        self.enter_shortcut.activated.connect(lambda: self.handle_button_press('='))
        self.return_shortcut = QShortcut(QKeySequence("Return"), self.view)
        self.return_shortcut.activated.connect(lambda: self.handle_button_press('='))

        self.multiply_shortcut = QShortcut(QKeySequence("*"), self.view)
        self.multiply_shortcut.activated.connect(lambda: self.handle_button_press('x'))

        self.divide_shortcut = QShortcut(QKeySequence("/"), self.view)
        self.divide_shortcut.activated.connect(lambda: self.handle_button_press('÷'))

        self.tab_shortcut = QShortcut(QKeySequence("Tab"), self.view)
        self.tab_shortcut.activated.connect(lambda: self.toggle_mode())

        self.escape_shortcut = QShortcut(QKeySequence("Escape"), self.view)
        self.escape_shortcut.activated.connect(lambda: self.all_clear())


    def setup_actions(self):
        for button in self.view.operand_buttons + self.view.operator_buttons + self.view.function_buttons:
            self.view.update_button_action(button, self.handle_button_press)

    def handle_button_press(self, button_text):
        operands = '0123456789ABCDEF'
        operator_dict = {
            'AND': '&',
            'OR': '|',
            'XOR': '^',
            'NOR': 'NOR',
            'XNOR': 'XNOR',
            '÷': '//',
            'x': '*',
            '-': '-',
            '+': '+',
            }
        function_dict = {'CL': self.clear,
                         'AC': self.all_clear,
                        '=': self.evaluate_expression,
                        'NOT': self.handle_not_operator_input,
                         '<<': self.handle_left_bit_shift,
                         '>>': self.handle_right_bit_shift
                         }
        if button_text in function_dict:
            handler_function = function_dict.get(button_text, lambda: print('Invalid input'))
            handler_function()
        elif button_text in self.mode_list:
            self.set_base_mode(button_text)
        elif button_text in self.bit_depth_list:
            self.set_bit_depth(button_text)
        elif button_text in operands:
            self.model.handle_numeric_input(operands.index(button_text))
            self.view.update_output(self.model.working_value)
        elif button_text in operator_dict:
            self.handle_operator_input(operator_dict[button_text])
        self.print_model_state()

    def evaluate_expression(self):
        self.model.evaluate()
        self.view.update_output(self.model.result)

    def handle_operator_input(self, input_value):
        self.model.handle_operator(input_value)

    def handle_not_operator_input(self):
        self.model.handle_not_operator()
        self.view.update_output(self.model.working_value)

    def handle_left_bit_shift(self):
        self.model.handle_bitshift_left()
        self.view.update_output(self.model.working_value)

    def handle_right_bit_shift(self):
        self.model.handle_bitshift_right()
        self.view.update_output(self.model.working_value)

    def set_base_mode(self, mode):
        mode_index = None
        try:
            mode_index = self.mode_list.index(mode)
        except ValueError:
            print("Invalid mode")
        self.model.base = self.base_value_list[mode_index]
        self.view.set_base(self.model.base)

    def set_bit_depth(self, value):
        change_value = value.split(' ')[0]
        if change_value == '+':
            self.model.increase_bit_depth()
            self.view.bit_depth = self.model.bit_depth
        elif change_value == '-':
            self.model.decrease_bit_depth()
            self.view.bit_depth = self.model.bit_depth
        else:
            self.model.set_bit_depth(int(change_value))
        self.view.bit_depth = self.model.bit_depth
        self.view.update_output(self.model.working_value)

    def toggle_mode(self):
        current_index = self.base_value_list.index(self.model.base)
        new_index = current_index + 1
        if new_index == len(self.mode_list):
            new_index = 0
        print(self.mode_list[new_index])
        self.model.base = self.base_value_list[new_index]
        self.view.set_base(self.model.base)

    def clear(self):
        self.model.clear_working_value()
        self.view.update_output(self.model.working_value)

    def all_clear(self):
        self.model.clear_state()
        self.view.update_output(self.model.working_value)

    def print_model_state(self):
        print(f"{self.model.operand1} {self.model.operator} {self.model.operand2}, "
              f"Result: {self.model.result}, WorkingVal: {self.model.working_value}")