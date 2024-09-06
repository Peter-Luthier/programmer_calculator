class CalculatorModel:
    def __init__(self):
        self.working_operand = 0
        self.accumulator_operand = None
        self.operator = None
        self.base_mode = 'Decimal'
        self.base = 10
        self.signed = False
        self.eval_flag = False
        self.operator_flag = False
        self.display_value = 0
        self.display_num_bits = 8

    def clear_working_operand(self):
        self.working_operand = 0

    def clear_accumulator_operand(self):
        self.accumulator_operand = 0

    def clear_operator(self):
        self.operator = None

    def handle_operator(self, operator_value):
        if self.operator:
            self.accumulator_operand = self.evaluate()
        self.operator = operator_value
        self.operator_flag = True

    def evaluate(self):
        special_operators = {
            '~': self.evaluate_not_operation,
            'NOR': self.evaluate_nor_operation,
            'XNOR': self.evaluate_xnor_operation,
        }
        if self.operator in special_operators:
            result =  special_operators[self.operator]()
        else:
            result =  eval(str(self.accumulator_operand) + self.operator + str(self.working_operand))
        return result

    def evaluate_not_operation(self):
        if self.signed:
            return ~ self.working_operand
        else:
            mask = 2 ** self.display_num_bits - 1
            return self.working_operand ^ mask

    def evaluate_nor_operation(self):
        pass

    def evaluate_xnor_operation(self):
        pass

    def check_value(self):
        pass
