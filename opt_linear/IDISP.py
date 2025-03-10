from testsetclass import TestsetClass


class IDISP(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['pxylene', 'F22f', 'undecan1', 'octane1', 'pc22', 'ant', 'F22l', 'undecan2', 'h2', 'octane2', 'F14l', 'antdimer', 'F14f']
        self.exp_values = {'0': -9.15, '1': -60.28, '2': -1.21, '3': 9.10, '4': -3.64, '5': -1.96}
        self.testset_calculations = {'0': "+1 * ['antdimer'] -2 * ['ant']",
              '1': "+2 * ['pxylene'] -1 * ['pc22'] -2 * ['h2']",
              '2': "+1 * ['octane1'] -1 * ['octane2']",
              '3': "+1 * ['undecan1'] -1 * ['undecan2']",
              '4': "-1 * ['F14f'] +1 * ['F14l']",
              '5': "-1 * ['F22f'] +1 * ['F22l']"}
        self.charges = {'pxylene': 0.0, 'F22f': 0.0, 'undecan1': 0.0, 'octane1': 0.0, 'pc22': 0.0, 'ant': -0.0, 'F22l': 0.0, 'undecan2': -0.0, 'h2': 0.0, 'octane2': 0.0, 'F14l': -0.0, 'antdimer': 0.0, 'F14f': 0.0}
    