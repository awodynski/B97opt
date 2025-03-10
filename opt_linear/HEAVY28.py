from testsetclass import TestsetClass


class HEAVY28(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['pbh4_2', 'bih3_hcl', 'pbh4_hbr', 'hi', 'teh2_2', 'sbh3', 'bih3_nh3', 'hcl', 'teh2', 'pbh4_teh2', 'sbh3_nh3', 'sbh3_hi', 'bih3_hbr', 'pbh4_h2o', 'bih3_h2s', 'h2o', 'teh2_nh3', 'pbh4', 'sbh3_hcl', 'bih3_2', 'teh2_hcl', 'teh2_hbr', 'sbh3_h2o', 'pbh4_hi', 'sbh3_hbr', 'pbh4_bih3', 'h2s', 'bih3_h2o', 'nh3', 'sbh3_h2s', 'teh2_hi', 'bih3_hi', 'hbr', 'teh2_h2o', 'sbh3_2', 'bih3', 'pbh4_hcl', 'teh2_h2s']
        self.exp_values = {'0': 1.16, '1': 2.49, '2': 1.36, '3': 0.77, '4': 0.98, '5': 1.30, '6': 0.60, '7': 1.25, '8': 0.55, '9': 0.36, '10': 0.75, '11': 0.93, '12': 1.18, '13': 0.65, '14': 1.28, '15': 1.57, '16': 1.06, '17': 2.02, '18': 1.89, '19': 1.49, '20': 2.84, '21': 0.52, '22': 0.68, '23': 0.48, '24': 1.23, '25': 1.22, '26': 0.80, '27': 3.35}
        self.testset_calculations = {'0': "-1 * ['bih3_2'] +2 * ['bih3']",
              '1': "-1 * ['bih3_h2o'] +1 * ['bih3'] +1 * ['h2o']",
              '2': "-1 * ['bih3_h2s'] +1 * ['bih3'] +1 * ['h2s']",
              '3': "-1 * ['bih3_hcl'] +1 * ['bih3'] +1 * ['hcl']",
              '4': "-1 * ['bih3_hbr'] +1 * ['bih3'] +1 * ['hbr']",
              '5': "-1 * ['bih3_hi'] +1 * ['bih3'] +1 * ['hi']",
              '6': "-1 * ['bih3_nh3'] +1 * ['bih3'] +1 * ['nh3']",
              '7': "-1 * ['pbh4_2'] +2 * ['pbh4']",
              '8': "-1 * ['pbh4_bih3'] +1 * ['pbh4'] +1 * ['bih3']",
              '9': "-1 * ['pbh4_h2o'] +1 * ['pbh4'] +1 * ['h2o']",
              '10': "-1 * ['pbh4_hcl'] +1 * ['pbh4'] +1 * ['hcl']",
              '11': "-1 * ['pbh4_hbr'] +1 * ['pbh4'] +1 * ['hbr']",
              '12': "-1 * ['pbh4_hi'] +1 * ['pbh4'] +1 * ['hi']",
              '13': "-1 * ['pbh4_teh2'] +1 * ['pbh4'] +1 * ['teh2']",
              '14': "-1 * ['sbh3_2'] +2 * ['sbh3']",
              '15': "-1 * ['sbh3_h2o'] +1 * ['sbh3'] +1 * ['h2o']",
              '16': "-1 * ['sbh3_h2s'] +1 * ['sbh3'] +1 * ['h2s']",
              '17': "-1 * ['sbh3_hcl'] +1 * ['sbh3'] +1 * ['hcl']",
              '18': "-1 * ['sbh3_hbr'] +1 * ['sbh3'] +1 * ['hbr']",
              '19': "-1 * ['sbh3_hi'] +1 * ['sbh3'] +1 * ['hi']",
              '20': "-1 * ['sbh3_nh3'] +1 * ['sbh3'] +1 * ['nh3']",
              '21': "-1 * ['teh2_2'] +2 * ['teh2']",
              '22': "-1 * ['teh2_h2o'] +1 * ['teh2'] +1 * ['h2o']",
              '23': "-1 * ['teh2_h2s'] +1 * ['teh2'] +1 * ['h2s']",
              '24': "-1 * ['teh2_hcl'] +1 * ['teh2'] +1 * ['hcl']",
              '25': "-1 * ['teh2_hbr'] +1 * ['teh2'] +1 * ['hbr']",
              '26': "-1 * ['teh2_hi'] +1 * ['teh2'] +1 * ['hi']",
              '27': "-1 * ['teh2_nh3'] +1 * ['teh2'] +1 * ['nh3']"}
        self.charges = {'pbh4_2': -0.0, 'bih3_hcl': -0.0, 'pbh4_hbr': -0.0, 'hi': 0.0, 'teh2_2': -0.0, 'sbh3': 0.0, 'bih3_nh3': 0.0, 'hcl': -0.0, 'teh2': 0.0, 'pbh4_teh2': -0.0, 'sbh3_nh3': 0.0, 'sbh3_hi': -0.0, 'bih3_hbr': 0.0, 'pbh4_h2o': -0.0, 'bih3_h2s': 0.0, 'h2o': 0.0, 'teh2_nh3': -0.0, 'pbh4': 0.0, 'sbh3_hcl': 0.0, 'bih3_2': -0.0, 'teh2_hcl': -0.0, 'teh2_hbr': -0.0, 'sbh3_h2o': 0.0, 'pbh4_hi': -0.0, 'sbh3_hbr': -0.0, 'pbh4_bih3': -0.0, 'h2s': -0.0, 'bih3_h2o': 0.0, 'nh3': -0.0, 'sbh3_h2s': -0.0, 'teh2_hi': -0.0, 'bih3_hi': 0.0, 'hbr': -0.0, 'teh2_h2o': 0.0, 'sbh3_2': -0.0, 'bih3': 0.0, 'pbh4_hcl': 0.0, 'teh2_h2s': 0.0}
    