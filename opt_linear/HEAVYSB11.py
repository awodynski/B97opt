from testsetclass import TestsetClass


class HEAVYSB11(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['asme2', 'snme3', 'teme', 'h2se2', 'p2me4', 'pme2', 'ge2h6', 'br2', 'sh', 'as2me4', 'sbme2', 'pbme3', 'te2me2', 'sn2me6', 'pb2me6', 'br', 'sb2me4', 'h2s2', 'seh', 'cl', 'cl2', 'geh3']
        self.exp_values = {'0': 73.82, '1': 61.74, '2': 52.92, '3': 67.85, '4': 58.37, '5': 52.91, '6': 61.85, '7': 52.18, '8': 43.79, '9': 59.65, '10': 53.17}
        self.testset_calculations = {'0': "+2 * ['geh3'] -1 * ['ge2h6']",
              '1': "+2 * ['snme3'] -1 * ['sn2me6']",
              '2': "+2 * ['pbme3'] -1 * ['pb2me6']",
              '3': "+2 * ['sh'] -1 * ['h2s2']",
              '4': "+2 * ['seh'] -1 * ['h2se2']",
              '5': "+2 * ['teme'] -1 * ['te2me2']",
              '6': "+2 * ['pme2'] -1 * ['p2me4']",
              '7': "+2 * ['asme2'] -1 * ['as2me4']",
              '8': "+2 * ['sbme2'] -1 * ['sb2me4']",
              '9': "+2 * ['cl'] -1 * ['cl2']",
              '10': "+2 * ['br'] -1 * ['br2']"}
        self.charges = {'asme2': -0.0, 'snme3': -0.0, 'teme': 0.0, 'h2se2': -0.0, 'p2me4': 0.0, 'pme2': 0.0, 'ge2h6': 0.0, 'br2': 0.0, 'sh': -0.0, 'as2me4': -0.0, 'sbme2': -0.0, 'pbme3': -0.0, 'te2me2': 0.0, 'sn2me6': -0.0, 'pb2me6': -0.0, 'br': 0.0, 'sb2me4': -0.0, 'h2s2': 0.0, 'seh': 0.0, 'cl': 0.0, 'cl2': -0.0, 'geh3': 0.0}
    