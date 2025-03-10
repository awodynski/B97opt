from testsetclass import TestsetClass


class PArel(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['h2s2o71', 's4o42', 'c2h2f41', 'his3', 'sugar2', 'A2', 'his2', 'sugar3', 'sugar4', 'h4p2o71', 'aminocoohbz2', 'aminocoohbz3', 'arg2', 'c2cl43', 'T2', 'c2cl42', 'T3', 'h2s2o72', 's4o41', 'A0', 'c2h2f42', 'his0', 'sugar0', 'his1', 'A1', 'arg0', 'h4p2o72', 'aminocoohbz1', 'T1', 'T0', 'c2cl41']
        self.exp_values = {'0': 1.61, '1': 8.50, '2': 2.94, '3': 6.22, '4': 7.19, '5': 2.38, '6': 1.19, '7': 0.79, '8': 7.05, '9': 2.98, '10': 3.41, '11': 3.21, '12': 0.60, '13': 7.21, '14': 2.36, '15': 17.88, '16': 11.20, '17': 1.27, '18': 2.47, '19': 2.15}
        self.testset_calculations = {'0': "-1 * ['A0'] +1 * ['A1']",
              '1': "-1 * ['A0'] +1 * ['A2']",
              '2': "-1 * ['T1'] +1 * ['T0']",
              '3': "-1 * ['T1'] +1 * ['T2']",
              '4': "-1 * ['T1'] +1 * ['T3']",
              '5': "-1 * ['arg2'] +1 * ['arg0']",
              '6': "-1 * ['his1'] +1 * ['his2']",
              '7': "-1 * ['his1'] +1 * ['his0']",
              '8': "-1 * ['his1'] +1 * ['his3']",
              '9': "-1 * ['sugar0'] +1 * ['sugar2']",
              '10': "-1 * ['sugar0'] +1 * ['sugar4']",
              '11': "-1 * ['sugar0'] +1 * ['sugar3']",
              '12': "-1 * ['aminocoohbz2'] +1 * ['aminocoohbz1']",
              '13': "-1 * ['aminocoohbz2'] +1 * ['aminocoohbz3']",
              '14': "-1 * ['h4p2o71'] +1 * ['h4p2o72']",
              '15': "-1 * ['h2s2o71'] +1 * ['h2s2o72']",
              '16': "-1 * ['s4o42'] +1 * ['s4o41']",
              '17': "-1 * ['c2h2f41'] +1 * ['c2h2f42']",
              '18': "-1 * ['c2cl43'] +1 * ['c2cl42']",
              '19': "-1 * ['c2cl43'] +1 * ['c2cl41']"}
        self.charges = {'h2s2o71': 1.0, 's4o42': 1.0, 'c2h2f41': 1.0, 'his3': 1.0, 'sugar2': 1.0, 'A2': 1.0, 'his2': 1.0, 'sugar3': 1.0, 'sugar4': 1.0, 'h4p2o71': 1.0, 'aminocoohbz2': 1.0, 'aminocoohbz3': 1.0, 'arg2': 1.0, 'c2cl43': 1.0, 'T2': 1.0, 'c2cl42': 1.0, 'T3': 1.0, 'h2s2o72': 1.0, 's4o41': 1.0, 'A0': 1.0, 'c2h2f42': 1.0, 'his0': 1.0, 'sugar0': 1.0, 'his1': 1.0, 'A1': 1.0, 'arg0': 1.0, 'h4p2o72': 1.0, 'aminocoohbz1': 1.0, 'T1': 1.0, 'T0': 1.0, 'c2cl41': 1.0}
    