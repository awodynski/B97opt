from testsetclass import TestsetClass


class ALK8(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['li3_me', 'na2', 'na+', 'li_h', 'li_me', 'li4_me4', 'na8', 'na2_h2', 'li4_c', 'li8', 'li2', 'li5_ch', 'li_ch2n', 'li_na_h2', 'li2_ch2n_2', 'li2_ch4', 'li+']
        self.exp_values = {'0': 86.47, '1': 53.15, '2': 131.13, '3': 34.51, '4': 47.42, '5': 66.28, '6': 56.55, '7': 25.30}
        self.testset_calculations = {'0': "-1 * ['li8'] +4 * ['li2']",
              '1': "-1 * ['na8'] +4 * ['na2']",
              '2': "-1 * ['li4_me4'] +4 * ['li_me']",
              '3': "-1 * ['li3_me'] +1 * ['li_me'] +1 * ['li2']",
              '4': "-1 * ['li2_ch4'] +1 * ['li_me'] +1 * ['li_h']",
              '5': "-1 * ['li5_ch'] +1 * ['li4_c'] +1 * ['li_h']",
              '6': "-1 * ['li2_ch2n_2'] +2 * ['li_ch2n']",
              '7': "-1 * ['na+'] -1 * ['li_na_h2'] +1 * ['li+'] +1 * ['na2_h2']"}
        self.charges = {'li3_me': 0.0, 'na2': -0.0, 'na+': 1.0, 'li_h': 0.0, 'li_me': 0.0, 'li4_me4': -0.0, 'na8': -0.0, 'na2_h2': 0.0, 'li4_c': 0.0, 'li8': 0.0, 'li2': 0.0, 'li5_ch': 0.0, 'li_ch2n': 0.0, 'li_na_h2': -0.0, 'li2_ch2n_2': 0.0, 'li2_ch4': 0.0, 'li+': 1.0}
    