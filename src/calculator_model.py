

class CalculatorModel:
    def __init__(self):
        self.working_value = None
        self.operand1 = None
        self.operand2 = None
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
        self.operand1 = None

    def clear_operator(self):
        self.operator = None

    def clear_state(self):
        self.working_value = None
        self.operand1 = None
        self.operand2 = None
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
            self.operand1 = self.result
        else:
            if self.operator:
                self.operand1 = self.evaluate()
        if self.result is not None:
            self.operand1 = self.result
        elif self.operand2:
            self.operand1 = self.evaluate()
        else:
            self.operand1 = self.working_value
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
        if not self.operand2:
            if self.operand1 is None and self.operator is None:
                if self.result is None:
                    self.result = self.working_value
                    self.working_value = None
                return self.result
        if self.result:
            self.operand1 = self.result
        else:
            self.operand2 = self.working_value if self.working_value is not None else self.operand1
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
            eval_result =  eval(str(self.operand1) + self.operator + str(self.operand2))
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
        or_result = self.operand1 | self.operand2
        return self.evaluate_not_operation(or_result)

    def evaluate_xnor_operation(self):
        xor_result = self.operand1 ^ self.operand2
        return self.evaluate_not_operation(xor_result)

    def check_value_range(self, value):
        max_value = 2 ** self.bit_depth - 1
        min_value = -max_value if self.signed else 0
        return min_value <= value <= max_value
