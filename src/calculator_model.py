

class CalculatorModel:
    def __init__(self):
        self.working_value = None
        self.x_register = None
        self.y_register = None
        self.operator = None
        self.result = None
        self.base = 10
        self.signed = False
        self.bit_depth = 16
        self.overflow = False

    def set_bit_depth(self, value):
        self.bit_depth = value
        if self.working_value:
            self.overflow = self.check_value_range(self.working_value)

    def increase_bit_depth(self):
        if self.bit_depth <= 64:
            self.bit_depth += 1

    def decrease_bit_depth(self):
        if self.bit_depth > 1:
            self.bit_depth -= 1

    def clear_working_value(self):
        self.working_value = None

    def clear_operand1(self):
        self.x_register = None

    def clear_operator(self):
        self.operator = None

    def clear_state(self):
        self.working_value = None
        self.x_register = None
        self.y_register = None
        self.operator = None
        self.result = None
        print('Clear All')

    def handle_numeric_input(self, value):
        if self.result:
            self.clear_state()
        if not self.working_value:
            self.working_value = 0
        self.working_value = self.working_value * self.base + value

    def handle_operator(self, operator_value):
        if self.result:
            self.x_register = self.result
        else:
            if self.operator:
                self.x_register = self.evaluate()
        if self.result is not None:
            self.x_register = self.result
        elif self.y_register:
            self.x_register = self.evaluate()
        else:
            self.x_register = self.working_value
        self.operator = operator_value
        self.result = None
        self.working_value = None

    def handle_not_operator(self):
        if not self.working_value:
            self.working_value = self.result if self.result else 0
        self.working_value = self.evaluate_not_operation(self.working_value)

    def handle_bitshift_left(self):
        if not self.working_value:
            self.working_value = self.result if self.result else 0
            self.result = None
        self.working_value = (self.working_value * 2) % (2 ** self.bit_depth)

    def handle_bitshift_right(self):
        if not self.working_value:
            self.working_value = self.result if self.result else 0
            self.result = None
        self.working_value = self.working_value >> 1

    def evaluate(self):
        if not self.y_register:
            if self.x_register is None and self.operator is None:
                if self.result is None:
                    self.result = self.working_value
                    self.working_value = None
                return self.result
        if self.result:
            self.x_register = self.result
        else:
            self.y_register = self.working_value if self.working_value is not None else self.x_register
        eval_result = self.evaluate_current_state()
        if not self.signed and eval_result < 0:
            raise ValueError('Overflow')
        self.result = eval_result
        self.working_value = None
        return self.result

    def evaluate_current_state(self):
        special_operations = {
            'NOR': self.evaluate_nor_operation,
            'XNOR': self.evaluate_xnor_operation,
        }
        if self.operator in special_operations:
            function = special_operations[self.operator]
            return function()
        try:
            eval_result =  eval(str(self.x_register) + self.operator + str(self.y_register))
        except ZeroDivisionError:
            print('Cannot divide by zero')
            return None
        return eval_result

    def evaluate_not_operation(self, value):
        if self.signed:
            return  ~ value
        else:
            mask = 2 ** self.bit_depth - 1
            return value ^ mask

    def evaluate_nor_operation(self):
        or_result = self.x_register | self.y_register
        return self.evaluate_not_operation(or_result)

    def evaluate_xnor_operation(self):
        xor_result = self.x_register ^ self.y_register
        return self.evaluate_not_operation(xor_result)

    def check_value_range(self, value):
        if self.signed is True:
            max_value = 2 ** (self.bit_depth - 1) -1
            min_value = -max_value
        else:
            max_value = 2 ** self.bit_depth - 1
            min_value = 0
        return min_value <= value <= max_value
