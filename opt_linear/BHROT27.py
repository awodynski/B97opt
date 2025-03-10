from testsetclass import TestsetClass


class BHROT27(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['butadiene_strans', 'bifuran_syn', 'tmethane_120', 'tmethane_60', 'ethylthiourea_0', 'butadiene_TS', 'tmethane_180', 'bithiophene_anti', 'acetamide_TS1', 'bifuran_anti', 'butadiene_scis', 'methanol_st', 'ethylthiourea_TS2', 'biphenyl_TS', 'n2h4_ecl1', 'nh2oh_ecl', 'nh2oh_st1', 'methanol_ecl', 'ethylthiourea_180', 'h2s2_cis', 'bithiophene_TS', 'h2o2_trans', 'methylamine_st', 'h2o2', 'bifuran_TS', 'ethane_ecl', 'acetamide_TS2', 'ethane_st', 'ethylthiourea_TS1', 'h2s2', 'h2o2_cis', 'bithiophene_syn', 'n2h4_st1', 'n2h4_ecl2', 'h2s2_trans', 'nh2oh_st2', 'biphenyl', 'tmethane_0', 'acetamide_RC', 'methylamine_ecl']
        self.exp_values = {'0': 2.73, '1': 7.01, '2': 3.46, '3': 3.72, '4': 1.01, '5': 2.28, '6': 1.01, '7': 7.17, '8': 5.79, '9': 8.03, '10': 1.62, '11': 8.41, '12': 6.91, '13': 2.68, '14': 17.24, '15': 14.52, '16': 2.10, '17': 3.89, '18': 2.09, '19': 1.78, '20': 1.39, '21': 6.30, '22': 3.35, '23': 10.36, '24': 10.24, '25': 17.20, '26': 17.08}
        self.testset_calculations = {'0': "-1 * ['ethane_st'] +1 * ['ethane_ecl']",
              '1': "-1 * ['tmethane_60'] +1 * ['tmethane_0']",
              '2': "-1 * ['tmethane_60'] +1 * ['tmethane_120']",
              '3': "-1 * ['tmethane_180'] +1 * ['tmethane_120']",
              '4': "-1 * ['methanol_st'] +1 * ['methanol_ecl']",
              '5': "-1 * ['methylamine_st'] +1 * ['methylamine_ecl']",
              '6': "-1 * ['h2o2'] +1 * ['h2o2_trans']",
              '7': "-1 * ['h2o2'] +1 * ['h2o2_cis']",
              '8': "-1 * ['h2s2'] +1 * ['h2s2_trans']",
              '9': "-1 * ['h2s2'] +1 * ['h2s2_cis']",
              '10': "-1 * ['n2h4_st1'] +1 * ['n2h4_ecl1']",
              '11': "-1 * ['n2h4_st1'] +1 * ['n2h4_ecl2']",
              '12': "-1 * ['nh2oh_st1'] +1 * ['nh2oh_ecl']",
              '13': "-1 * ['nh2oh_st2'] +1 * ['nh2oh_ecl']",
              '14': "-1 * ['acetamide_RC'] +1 * ['acetamide_TS1']",
              '15': "-1 * ['acetamide_RC'] +1 * ['acetamide_TS2']",
              '16': "-1 * ['biphenyl'] +1 * ['biphenyl_TS']",
              '17': "-1 * ['bifuran_anti'] +1 * ['bifuran_TS']",
              '18': "-1 * ['bifuran_syn'] +1 * ['bifuran_TS']",
              '19': "-1 * ['bithiophene_anti'] +1 * ['bithiophene_TS']",
              '20': "-1 * ['bithiophene_syn'] +1 * ['bithiophene_TS']",
              '21': "-1 * ['butadiene_strans'] +1 * ['butadiene_TS']",
              '22': "-1 * ['butadiene_scis'] +1 * ['butadiene_TS']",
              '23': "-1 * ['ethylthiourea_180'] +1 * ['ethylthiourea_TS1']",
              '24': "-1 * ['ethylthiourea_0'] +1 * ['ethylthiourea_TS1']",
              '25': "-1 * ['ethylthiourea_180'] +1 * ['ethylthiourea_TS2']",
              '26': "-1 * ['ethylthiourea_0'] +1 * ['ethylthiourea_TS2']"}
        self.charges = {'butadiene_strans': 0.0, 'bifuran_syn': 0.0, 'tmethane_120': 0.0, 'tmethane_60': 0.0, 'ethylthiourea_0': 0.0, 'butadiene_TS': 0.0, 'tmethane_180': 0.0, 'bithiophene_anti': 0.0, 'acetamide_TS1': -0.0, 'bifuran_anti': 0.0, 'butadiene_scis': 0.0, 'methanol_st': 0.0, 'ethylthiourea_TS2': 0.0, 'biphenyl_TS': 0.0, 'n2h4_ecl1': 0.0, 'nh2oh_ecl': 0.0, 'nh2oh_st1': 0.0, 'methanol_ecl': 0.0, 'ethylthiourea_180': 0.0, 'h2s2_cis': -0.0, 'bithiophene_TS': 0.0, 'h2o2_trans': 0.0, 'methylamine_st': 0.0, 'h2o2': -0.0, 'bifuran_TS': -0.0, 'ethane_ecl': 0.0, 'acetamide_TS2': -0.0, 'ethane_st': 0.0, 'ethylthiourea_TS1': 0.0, 'h2s2': 0.0, 'h2o2_cis': 0.0, 'bithiophene_syn': 0.0, 'n2h4_st1': 0.0, 'n2h4_ecl2': 0.0, 'h2s2_trans': 0.0, 'nh2oh_st2': 0.0, 'biphenyl': 0.0, 'tmethane_0': 0.0, 'acetamide_RC': 0.0, 'methylamine_ecl': 0.0}
    