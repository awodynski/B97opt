from testsetclass import TestsetClass


class ADIM6(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['AM5', 'AD3', 'AM2', 'AD4', 'AM7', 'AD6', 'AM3', 'AD5', 'AD2', 'AD7', 'AM6', 'AM4']
        self.exp_values = {'0': 1.34, '1': 1.99, '2': 2.89, '3': 3.78, '4': 4.60, '5': 5.55}
        self.testset_calculations = {'0': "+2 * ['AM2'] -1 * ['AD2']",
              '1': "+2 * ['AM3'] -1 * ['AD3']",
              '2': "+2 * ['AM4'] -1 * ['AD4']",
              '3': "+2 * ['AM5'] -1 * ['AD5']",
              '4': "+2 * ['AM6'] -1 * ['AD6']",
              '5': "+2 * ['AM7'] -1 * ['AD7']"}
        self.charges = {'AM5': 0.0, 'AD3': 0.0, 'AM2': 0.0, 'AD4': 0.0, 'AM7': 0.0, 'AD6': 0.0, 'AM3': 0.0, 'AD5': 0.0, 'AD2': 0.0, 'AD7': 0.0, 'AM6': 0.0, 'AM4': 0.0}
    