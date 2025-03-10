from testsetclass import TestsetClass


class DARC(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['P6', 'P3', 'P10X', 'P4', 'P5', 'butadiene', 'P8X', 'P8', 'chdiene', 'ethine', 'P2', 'P7', 'maleinNH', 'cpdiene', 'malein', 'P9', 'P1', 'P7X', 'P9X', 'furane', 'ethene', 'P10']
        self.exp_values = {'0': -45.4, '1': -60.8, '2': -29.9, '3': -33.6, '4': -37.6, '5': -49.0, '6': -14.0, '7': -15.9, '8': -16.8, '9': -18.9, '10': -31.7, '11': -32.2, '12': -34.2, '13': -34.6}
        self.testset_calculations = {'0': "-1 * ['ethene'] -1 * ['butadiene'] +1 * ['P1']",
              '1': "-1 * ['ethine'] -1 * ['butadiene'] +1 * ['P2']",
              '2': "-1 * ['ethene'] -1 * ['cpdiene'] +1 * ['P3']",
              '3': "-1 * ['ethine'] -1 * ['cpdiene'] +1 * ['P4']",
              '4': "-1 * ['ethene'] -1 * ['chdiene'] +1 * ['P5']",
              '5': "-1 * ['ethine'] -1 * ['chdiene'] +1 * ['P6']",
              '6': "-1 * ['furane'] -1 * ['malein'] +1 * ['P7']",
              '7': "-1 * ['furane'] -1 * ['malein'] +1 * ['P7X']",
              '8': "-1 * ['furane'] -1 * ['maleinNH'] +1 * ['P8']",
              '9': "-1 * ['furane'] -1 * ['maleinNH'] +1 * ['P8X']",
              '10': "-1 * ['cpdiene'] -1 * ['malein'] +1 * ['P9']",
              '11': "-1 * ['cpdiene'] -1 * ['malein'] +1 * ['P9X']",
              '12': "-1 * ['cpdiene'] -1 * ['maleinNH'] +1 * ['P10']",
              '13': "-1 * ['cpdiene'] -1 * ['maleinNH'] +1 * ['P10X']"}
        self.charges = {'P6': 0.0, 'P3': -0.0, 'P10X': -0.0, 'P4': -0.0, 'P5': 0.0, 'butadiene': 0.0, 'P8X': -0.0, 'P8': -0.0, 'chdiene': 0.0, 'ethine': 0.0, 'P2': -0.0, 'P7': -0.0, 'maleinNH': -0.0, 'cpdiene': -0.0, 'malein': -0.0, 'P9': -0.0, 'P1': 0.0, 'P7X': -0.0, 'P9X': -0.0, 'furane': 0.0, 'ethene': 0.0, 'P10': -0.0}
    