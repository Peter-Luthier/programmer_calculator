
class CalculatorController:
    def __init__(self, calculator_model, calculator_view):
        self.model = calculator_model
        self.view = calculator_view
        self.view.handle_button_press = self.handle_button_press
        self.view.set_base(self.model.base)
        self.setup_actions()

    def setup_actions(self):
        for button in self.view.operand_buttons:
            self.view.update_button_action(button, self.handle_button_press)

    def handle_button_press(self, button_text):
        mode_list = ['Decimal', 'Hex', 'Binary']
        operands = '0123456789ABCDEF'
        operator_dict = {
            'AND': '&',
            'OR': '|',
            'NOT': '~',
            'NOR': 'NOR',
            'XOR': '^',
            'XNOR': 'XNOR',
            '÷': '/',
            'x': '*',
            '<<': '<<',
            '-': '-',
            '+': '+',
            '>>': '>>',
            }
        function_list = ['CL', 'AC', '=']
        if button_text in mode_list:
            self.set_base_mode(button_text)
        elif button_text in function_list:
            self.handle_function_input(button_text)
        elif button_text in operands:
            self.handle_numeric_input(operands.index(button_text))
        elif button_text in operator_dict:
            self.handle_operator_input(operator_dict[button_text])

    def handle_numeric_input(self, input_value):
        self.model.working_operand = self.model.working_operand * self.model.base + input_value
        self.view.update_output(self.model.working_operand)

    def handle_function_input(self, input_value):
        pass

    def handle_operator_input(self, input_value):
        print(input_value)
        if self.model.operator:
            self.model.accumulator_operand = self.model.evaluate()

        self.model.handle_operator(input_value)
        self.view.update_output(self.model.working_operand)
        print(self.model.accumulator_operand + self.model.operator + self.model.working_operand)

    def set_base_mode(self, mode):
        modes = {
            'Decimal': 10,
            'Hex': 16,
            'Binary': 2
        }
        self.model.base = modes[mode]
        self.view.set_base(modes[mode])
