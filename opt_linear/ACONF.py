from testsetclass import TestsetClass


class ACONF(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['H_t+g+x-', 'B_T', 'P_GX', 'H_x+g-x+', 'P_GG', 'P_TG', 'H_tgt', 'P_TT', 'H_ttt', 'H_tgg', 'H_gtt', 'H_g+x-g-', 'H_x+g-g-', 'B_G', 'H_ggg', 'H_gtg', 'H_g+t+g-', 'H_g+x-t+']
        self.exp_values = {'0': 0.598, '1': 0.614, '2': 0.961, '3': 2.813, '4': 0.595, '5': 0.604, '6': 0.934, '7': 1.178, '8': 1.302, '9': 1.250, '10': 2.632, '11': 2.740, '12': 3.283, '13': 3.083, '14': 4.925}
        self.testset_calculations = {'0': "-1 * ['B_T'] +1 * ['B_G']",
              '1': "-1 * ['P_TT'] +1 * ['P_TG']",
              '2': "-1 * ['P_TT'] +1 * ['P_GG']",
              '3': "-1 * ['P_TT'] +1 * ['P_GX']",
              '4': "-1 * ['H_ttt'] +1 * ['H_gtt']",
              '5': "-1 * ['H_ttt'] +1 * ['H_tgt']",
              '6': "-1 * ['H_ttt'] +1 * ['H_tgg']",
              '7': "-1 * ['H_ttt'] +1 * ['H_gtg']",
              '8': "-1 * ['H_ttt'] +1 * ['H_g+t+g-']",
              '9': "-1 * ['H_ttt'] +1 * ['H_ggg']",
              '10': "-1 * ['H_ttt'] +1 * ['H_g+x-t+']",
              '11': "-1 * ['H_ttt'] +1 * ['H_t+g+x-']",
              '12': "-1 * ['H_ttt'] +1 * ['H_g+x-g-']",
              '13': "-1 * ['H_ttt'] +1 * ['H_x+g-g-']",
              '14': "-1 * ['H_ttt'] +1 * ['H_x+g-x+']"}
        self.charges = {'H_t+g+x-': 0.0, 'B_T': 0.0, 'P_GX': 0.0, 'H_x+g-x+': 0.0, 'P_GG': 0.0, 'P_TG': 0.0, 'H_tgt': 0.0, 'P_TT': 0.0, 'H_ttt': 0.0, 'H_tgg': 0.0, 'H_gtt': 0.0, 'H_g+x-g-': 0.0, 'H_x+g-g-': -0.0, 'B_G': 0.0, 'H_ggg': 0.0, 'H_gtg': 0.0, 'H_g+t+g-': 0.0, 'H_g+x-t+': -0.0}
    