from testsetclass import TestsetClass


class ICONF(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['SI5H12_2', 'N4H6_1', 'S8_2', 'P7H7_2', 'SI6H12_1', 'N4H6_3', 'H4P2O7_4', 'N3P3H12_1', 'S4O4_1', 'H2S2O7_2', 'SI5H12_1', 'H4P2O7_2', 'N4H6_2', 'N3P3H12_2', 'S4O4_2', 'N3H5_3', 'H2S2O7_1', 'N3H5_1', 'H2S2O7_3', 'N3H5_2', 'P7H7_1', 'SI5H12_3', 'SI6H12_2', 'S8_1', 'SI5H12_4', 'H4P2O7_1', 'H4P2O7_3']
        self.exp_values = {'0': 0.90, '1': 5.29, '2': 0.13, '3': 2.33, '4': 12.16, '5': 0.10, '6': 1.03, '7': 3.51, '8': 1.69, '9': 1.40, '10': 4.39, '11': 9.16, '12': 0.55, '13': 3.55, '14': 1.33, '15': 3.66, '16': 4.35}
        self.testset_calculations = {'0': "-1 * ['N3H5_1'] +1 * ['N3H5_2']",
              '1': "-1 * ['N3H5_1'] +1 * ['N3H5_3']",
              '2': "-1 * ['N4H6_1'] +1 * ['N4H6_2']",
              '3': "-1 * ['N4H6_1'] +1 * ['N4H6_3']",
              '4': "-1 * ['N3P3H12_1'] +1 * ['N3P3H12_2']",
              '5': "-1 * ['SI5H12_1'] +1 * ['SI5H12_2']",
              '6': "-1 * ['SI5H12_1'] +1 * ['SI5H12_3']",
              '7': "-1 * ['SI5H12_1'] +1 * ['SI5H12_4']",
              '8': "-1 * ['SI6H12_1'] +1 * ['SI6H12_2']",
              '9': "-1 * ['P7H7_1'] +1 * ['P7H7_2']",
              '10': "-1 * ['S4O4_1'] +1 * ['S4O4_2']",
              '11': "-1 * ['S8_1'] +1 * ['S8_2']",
              '12': "-1 * ['H2S2O7_1'] +1 * ['H2S2O7_2']",
              '13': "-1 * ['H2S2O7_1'] +1 * ['H2S2O7_3']",
              '14': "-1 * ['H4P2O7_1'] +1 * ['H4P2O7_2']",
              '15': "-1 * ['H4P2O7_1'] +1 * ['H4P2O7_3']",
              '16': "-1 * ['H4P2O7_1'] +1 * ['H4P2O7_4']"}
        self.charges = {'SI5H12_2': -0.0, 'N4H6_1': 0.0, 'S8_2': 0.0, 'P7H7_2': -0.0, 'SI6H12_1': -0.0, 'N4H6_3': 0.0, 'H4P2O7_4': -0.0, 'N3P3H12_1': -0.0, 'S4O4_1': -0.0, 'H2S2O7_2': -0.0, 'SI5H12_1': -0.0, 'H4P2O7_2': -0.0, 'N4H6_2': 0.0, 'N3P3H12_2': -0.0, 'S4O4_2': -0.0, 'N3H5_3': 0.0, 'H2S2O7_1': -0.0, 'N3H5_1': -0.0, 'H2S2O7_3': -0.0, 'N3H5_2': 0.0, 'P7H7_1': -0.0, 'SI5H12_3': -0.0, 'SI6H12_2': -0.0, 'S8_1': 0.0, 'SI5H12_4': -0.0, 'H4P2O7_1': -0.0, 'H4P2O7_3': -0.0}
    