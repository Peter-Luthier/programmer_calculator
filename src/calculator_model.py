class CalcModel:
    def __init__(self):
        self.working_value = 0
        self.accumulator_value = []
        self.base_mode = 'Decimal'
        self.base = 10
        self.display_value = 0
        self.display_num_bits = 8
        self.max_binary_value = 2 ** self.display_num_bits - 1

    def clear(self):
        self.working_value = 0
