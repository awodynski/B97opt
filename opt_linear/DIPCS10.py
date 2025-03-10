from testsetclass import TestsetClass


class DIPCS10(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['h2s_2+', 'c2h4', 'nh3_2+', 'ch2o_2+', 'ph3', 'mg_2+', 'mg', 'ph3_2+', 'ch2o', 'c4h4', 'c2h6_2+', 'n2h2', 'h2s', 'be_2+', 'nh3', 'n2h2_2+', 'c4h4_2+', 'c2h4_2+', 'be', 'c2h6']
        self.exp_values = {'0': 529.2, '1': 667.1, '2': 655.8, '3': 626.9, '4': 776.5, '5': 747.6, '6': 733.0, '7': 649.6, '8': 522.1, '9': 634.8}
        self.testset_calculations = {'0': "-1 * ['c4h4'] +1 * ['c4h4_2+']",
              '1': "-1 * ['c2h6'] +1 * ['c2h6_2+']",
              '2': "-1 * ['c2h4'] +1 * ['c2h4_2+']",
              '3': "-1 * ['n2h2'] +1 * ['n2h2_2+']",
              '4': "-1 * ['nh3'] +1 * ['nh3_2+']",
              '5': "-1 * ['ch2o'] +1 * ['ch2o_2+']",
              '6': "-1 * ['h2s'] +1 * ['h2s_2+']",
              '7': "-1 * ['ph3'] +1 * ['ph3_2+']",
              '8': "-1 * ['mg'] +1 * ['mg_2+']",
              '9': "-1 * ['be'] +1 * ['be_2+']"}
        self.charges = {'h2s_2+': 2.0, 'c2h4': 0.0, 'nh3_2+': 2.0, 'ch2o_2+': 2.0, 'ph3': -0.0, 'mg_2+': 2.0, 'mg': -0.0, 'ph3_2+': 2.0, 'ch2o': 0.0, 'c4h4': 0.0, 'c2h6_2+': 2.0, 'n2h2': 0.0, 'h2s': -0.0, 'be_2+': 2.0, 'nh3': 0.0, 'n2h2_2+': 2.0, 'c4h4_2+': 2.0, 'c2h4_2+': 2.0, 'be': 0.0, 'c2h6': -0.0}
    