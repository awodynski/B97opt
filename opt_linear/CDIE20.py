from testsetclass import TestsetClass


class CDIE20(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['R25', 'R51', 'R47', 'R20', 'R22', 'R43', 'P26', 'P46', 'P51', 'R21', 'P40', 'R49', 'P48', 'P56', 'P49', 'R60', 'R29', 'R56', 'P44', 'P52', 'R46', 'R48', 'R57', 'R28', 'P43', 'R40', 'P45', 'P47', 'P60', 'P25', 'R44', 'R26', 'P22', 'P20', 'R52', 'R45']
        self.exp_values = {'0': -3.3, '1': 4.4, '2': -5.9, '3': -4.8, '4': -2.5, '5': 4.0, '6': 4.5, '7': 1.7, '8': 2.9, '9': 3.7, '10': 1.2, '11': 3.7, '12': 3.8, '13': 4.4, '14': 4.2, '15': 1.6, '16': 4.2, '17': 5.9, '18': 5.8, '19': 8.6}
        self.testset_calculations = {'0': "-1 * ['R20'] +1 * ['P20']",
              '1': "-1 * ['R21'] +1 * ['P20']",
              '2': "-1 * ['R22'] +1 * ['P22']",
              '3': "-1 * ['R25'] +1 * ['P25']",
              '4': "-1 * ['R26'] +1 * ['P26']",
              '5': "-1 * ['R28'] +1 * ['P26']",
              '6': "-1 * ['R29'] +1 * ['P25']",
              '7': "-1 * ['R40'] +1 * ['P40']",
              '8': "-1 * ['R43'] +1 * ['P43']",
              '9': "-1 * ['R44'] +1 * ['P44']",
              '10': "-1 * ['R45'] +1 * ['P45']",
              '11': "-1 * ['R46'] +1 * ['P46']",
              '12': "-1 * ['R47'] +1 * ['P47']",
              '13': "-1 * ['R48'] +1 * ['P48']",
              '14': "-1 * ['R49'] +1 * ['P49']",
              '15': "-1 * ['R51'] +1 * ['P51']",
              '16': "-1 * ['R52'] +1 * ['P52']",
              '17': "-1 * ['R56'] +1 * ['P56']",
              '18': "-1 * ['R57'] +1 * ['P51']",
              '19': "-1 * ['R60'] +1 * ['P60']"}
        self.charges = {'R25': 0.0, 'R51': 0.0, 'R47': 0.0, 'R20': 0.0, 'R22': 0.0, 'R43': -0.0, 'P26': -0.0, 'P46': 0.0, 'P51': 0.0, 'R21': 0.0, 'P40': -0.0, 'R49': 0.0, 'P48': -0.0, 'P56': 0.0, 'P49': -0.0, 'R60': 0.0, 'R29': 0.0, 'R56': 0.0, 'P44': 0.0, 'P52': 0.0, 'R46': 0.0, 'R48': 0.0, 'R57': -0.0, 'R28': 0.0, 'P43': -0.0, 'R40': 0.0, 'P45': 0.0, 'P47': 0.0, 'P60': -0.0, 'P25': 0.0, 'R44': 0.0, 'R26': 0.0, 'P22': 0.0, 'P20': 0.0, 'R52': 0.0, 'R45': 0.0}
    