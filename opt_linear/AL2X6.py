from testsetclass import TestsetClass


class AL2X6(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['alf3', 'al2me4', 'al2me5', 'alh3', 'al2f6', 'al2me6', 'al2cl6', 'alme3', 'alcl3', 'al2h6', 'alme2']
        self.exp_values = {'0': 38.5, '1': 51.6, '2': 32.5, '3': 38.4, '4': 31.2, '5': 23.1}
        self.testset_calculations = {'0': "-1 * ['al2h6'] +2 * ['alh3']",
              '1': "-1 * ['al2f6'] +2 * ['alf3']",
              '2': "-1 * ['al2cl6'] +2 * ['alcl3']",
              '3': "-1 * ['al2me4'] +2 * ['alme2']",
              '4': "-1 * ['al2me5'] +1 * ['alme2'] +1 * ['alme3']",
              '5': "-1 * ['al2me6'] +2 * ['alme3']"}
        self.charges = {'alf3': -0.0, 'al2me4': 0.0, 'al2me5': 0.0, 'alh3': -0.0, 'al2f6': -0.0, 'al2me6': -0.0, 'al2cl6': -0.0, 'alme3': -0.0, 'alcl3': -0.0, 'al2h6': -0.0, 'alme2': -0.0}
    