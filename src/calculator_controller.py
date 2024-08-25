
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
        mode_list = ['Decimal', 'Hexadecimal', 'Binary']
        operand_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if button_text in mode_list:
            self.set_base_mode(button_text)
        elif button_text in operand_list:
            self.handle_numeric_input(operand_list.index(button_text))

    def handle_numeric_input(self, input_value):
        self.model.working_value = self.model.working_value * self.model.base + input_value
        self.view.update_output(self.model.working_value)

    def set_base_mode(self, mode):
        modes = {
            'Decimal': 10,
            'Hexadecimal': 16,
            'Binary': 2
        }
        self.model.base = modes[mode]
        self.view.set_base(modes[mode])
