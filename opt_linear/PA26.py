from testsetclass import TestsetClass


class PA26(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['cysp', 'si2h6p', 'p4', 'h2p', 'phenolp', 'p6p', 'c2h2', 'T', 'Cp', 'ch2sp', 'C', 'ethanol', 'ass', 'ph3', 'assp', 'p8p', 'ch3coohp', 'A', 'hcl', 'ch3cooh', 'p2', 'phenol', 'phosphapyrrol', 'ethanolp', 'glyp', 'Tp', 'p4p', 'ph3p', 'sih4p', 'h2o', 'h2', 'hclp', 'p2p', 'phosphapyrrolp', 'h2op', 'G', 'h2s', 'ch2s', 'nh3', 'nh3p', 'c2h2p', 'sih4', 'c2f6', 'h2sp', 'si2h6', 'Ap', 'Gp', 'p6', 'cys', 'c2f6p', 'gly', 'p8']
        self.exp_values = {'0': 167.2, '1': 192.9, '2': 209.2, '3': 219.2, '4': 211.9, '5': 171.4, '6': 157.4, '7': 156.9, '8': 192.8, '9': 174.3, '10': 137.8, '11': 106.2, '12': 120.8, '13': 191.9, '14': 190.9, '15': 218.2, '16': 200.4, '17': 210.2, '18': 188.3, '19': 181.9, '20': 221.3, '21': 219.6, '22': 192.9, '23': 210.7, '24': 236.0, '25': 235.1}
        self.testset_calculations = {'0': "+1 * ['p2'] -1 * ['p2p']",
              '1': "+1 * ['p4'] -1 * ['p4p']",
              '2': "+1 * ['p6'] -1 * ['p6p']",
              '3': "+1 * ['p8'] -1 * ['p8p']",
              '4': "+1 * ['nh3'] -1 * ['nh3p']",
              '5': "+1 * ['h2o'] -1 * ['h2op']",
              '6': "+1 * ['c2h2'] -1 * ['c2h2p']",
              '7': "+1 * ['sih4'] -1 * ['sih4p']",
              '8': "+1 * ['ph3'] -1 * ['ph3p']",
              '9': "+1 * ['h2s'] -1 * ['h2sp']",
              '10': "+1 * ['hcl'] -1 * ['hclp']",
              '11': "+1 * ['h2'] -1 * ['h2p']",
              '12': "+1 * ['c2f6'] -1 * ['c2f6p']",
              '13': "+1 * ['ethanol'] -1 * ['ethanolp']",
              '14': "+1 * ['ch3cooh'] -1 * ['ch3coohp']",
              '15': "+1 * ['gly'] -1 * ['glyp']",
              '16': "+1 * ['phenol'] -1 * ['phenolp']",
              '17': "+1 * ['ass'] -1 * ['assp']",
              '18': "+1 * ['ch2s'] -1 * ['ch2sp']",
              '19': "+1 * ['si2h6'] -1 * ['si2h6p']",
              '20': "+1 * ['cys'] -1 * ['cysp']",
              '21': "+1 * ['phosphapyrrol'] -1 * ['phosphapyrrolp']",
              '22': "+1 * ['A'] -1 * ['Ap']",
              '23': "+1 * ['T'] -1 * ['Tp']",
              '24': "+1 * ['G'] -1 * ['Gp']",
              '25': "+1 * ['C'] -1 * ['Cp']"}
        self.charges = {'cysp': 1.0, 'si2h6p': 1.0, 'p4': 0.0, 'h2p': 1.0, 'phenolp': 1.0, 'p6p': 1.0, 'c2h2': 0.0, 'T': -0.0, 'Cp': 1.0, 'ch2sp': 1.0, 'C': -0.0, 'ethanol': -0.0, 'ass': 0.0, 'ph3': -0.0, 'assp': 1.0, 'p8p': 1.0, 'ch3coohp': 1.0, 'A': 0.0, 'hcl': -0.0, 'ch3cooh': -0.0, 'p2': 0.0, 'phenol': -0.0, 'phosphapyrrol': -0.0, 'ethanolp': 1.0, 'glyp': 1.0, 'Tp': 1.0, 'p4p': 1.0, 'ph3p': 1.0, 'sih4p': 1.0, 'h2o': -0.0, 'h2': -0.0, 'hclp': 1.0, 'p2p': 1.0, 'phosphapyrrolp': 1.0, 'h2op': 1.0, 'G': 0.0, 'h2s': -0.0, 'ch2s': -0.0, 'nh3': 0.0, 'nh3p': 1.0, 'c2h2p': 1.0, 'sih4': -0.0, 'c2f6': 0.0, 'h2sp': 1.0, 'si2h6': 0.0, 'Ap': 1.0, 'Gp': 1.0, 'p6': 0.0, 'cys': 0.0, 'c2f6p': 1.0, 'gly': -0.0, 'p8': 0.0}
    