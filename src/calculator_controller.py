from PyQt6.QtGui import QShortcut, QKeySequence


class CalculatorController:
    def __init__(self, calculator_model, calculator_view):
        self.mode_list = ['Binary', 'Decimal', 'Hex']
        self.base_value_list = [2, 10, 16]
        self.model = calculator_model
        self.view = calculator_view
        self.view.handle_button_press = self.handle_button_press
        self.view.set_base(self.model.base_value)
        self.setup_actions()

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
            'NOT': '~',
            'NOR': 'NOR',
            'XOR': '^',
            'XNOR': 'XNOR',
            '÷': '//',
            'x': '*',
            '<<': '<<',
            '-': '-',
            '+': '+',
            '>>': '>>',
            }
        function_list = ['CL', 'AC', '=']
        if button_text in self.mode_list:
            self.set_base_mode(button_text)
        elif button_text in function_list:
            self.handle_function_input(button_text)
        elif button_text in operands:
            self.handle_numeric_input(operands.index(button_text))
        elif button_text in operator_dict:
            self.handle_operator_input(operator_dict[button_text])
        self.print_model_state()

    def handle_numeric_input(self, input_value):
        if self.model.result:
            self.model.clear_state()
        if not self.model.working_value:
            self.model.working_value = 0
        self.model.working_value = self.model.working_value * self.model.base_value + input_value
        self.view.update_output(self.model.working_value)

    def handle_function_input(self, input_value):
        if input_value == '=':
            self.evaluate_expression()

    def evaluate_expression(self):
        self.model.evaluate()
        self.view.update_output(self.model.result)

    def handle_operator_input(self, input_value):
        if self.model.operator:
            self.model.operand1 = self.model.evaluate()

        self.model.handle_operator(input_value)

    def set_base_mode(self, mode):
        mode_index = None
        try:
            mode_index = self.mode_list.index(mode)
        except ValueError:
            print("Invalid mode")
        self.model.base_value = self.base_value_list[mode_index]
        self.view.set_base(self.model.base_value)

    def toggle_mode(self):
        current_index = self.base_value_list.index(self.model.base_value)
        new_index = current_index + 1
        if new_index == len(self.mode_list):
            new_index = 0
        print(self.mode_list[new_index])
        self.model.base_value = self.base_value_list[new_index]
        self.view.set_base(self.model.base_value)

    def all_clear(self):
        self.model.clear_state()
        self.view.update_output(self.model.working_value)

    def print_model_state(self):
        print(f"{self.model.operand1} {self.model.operator} {self.model.operand2}, "
              f"Result: {self.model.result}, WorkingVal: {self.model.working_value}")