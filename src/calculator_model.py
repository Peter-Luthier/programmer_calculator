from unittest import result


class CalculatorModel:
    def __init__(self):
        self.working_value = None
        self.operand1 = None
        self.operand2 = None
        self.operator = None
        self.result = None
        self.base_value = 10
        self.signed = False
        self.display_value = 0
        self.display_num_bits = 8

    def clear_working_value(self):
        self.working_value = 0

    def clear_operand1(self):
        self.operand1 = None

    def clear_operator(self):
        self.operator = None

    def clear_state(self):
        self.operand1 = None
        self.operand2 = None
        self.operator = None
        self.result = None
        print('Clear All')


    def handle_operator(self, operator_value):
        if self.result is not None:
            self.operand1 = self.result
        elif self.operand2:
            self.operand1 = self.evaluate()
        else:
            self.operand1 = self.working_value
        self.operator = operator_value
        self.result = None
        self.working_value = None

    def evaluate(self):
        special_operators = {
            '~': self.evaluate_not_operation,
            'NOR': self.evaluate_nor_operation,
            'XNOR': self.evaluate_xnor_operation,
        }

        if not self.operand2:
            if self.operand1 is None and self.operator is None:
                if self.result is None:
                    self.result = self.working_value
                    self.working_value = None
                return result
        if self.result:
            self.operand1 = self.result
        else:
            self.operand2 = self.working_value if self.working_value else self.operand1
        if self.operator in special_operators:
            self.result =  special_operators[self.operator]()
        else:
            self.result =  eval(str(self.operand1) + self.operator + str(self.operand2))
        self.working_value = None
        return self.result

    def evaluate_not_operation(self):
        if self.signed:
            self.working_value =  ~ self.working_value
        else:
            mask = 2 ** self.display_num_bits - 1
            self.working_value =  self.working_value ^ mask

    def evaluate_nor_operation(self):
        pass

    def evaluate_xnor_operation(self):
        pass

    def check_value(self):
        pass
