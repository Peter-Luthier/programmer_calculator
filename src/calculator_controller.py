
class CalcController:
    def __init__(self, calculator_model):
        self.model = calculator_model

    def handle_numeric_input(self, input_value):
        modes = {
            'decimal': self.handle_decimal_numeric_input,
            'hex': self.handle_hex_numeric_input,
            'binary': self.handle_binary_numeric_input
        }
        modes[self.model.base_mode](input_value)
        print("key pressed")

    def handle_decimal_numeric_input(self, input_value):
        self.model.working_value = (self.model.working_value * 10) + int(input_value)

    def handle_hex_numeric_input(self, input_value):
        hex_letters = ['A', 'B', 'C', 'D', 'E', 'F']
        if input_value in hex_letters:
            input_int = hex_letters.index(input_value) + 10
        else:
            input_int = int(input_value)
        self.model.working_value = self.model.working_value << 4 | input_int
        print(self.model.working_value)
        print(format(self.model.working_value, 'X'))

    def handle_binary_numeric_input(self, input_value):
        self.model.working_value = int(input_value) | self.model.working_value << 1
        print(self.model.working_value)
        print(hex(self.model.working_value))

    def set_base_mode(self, mode):
        self.model.base_mode = mode
