from testsetclass import TestsetClass


class NBPRC(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['K_H', 'BH3PH3', 'K_F', 'H2', 'BCl3', 'BF3', 'BH3', 'ch', 'PH3', 'nh2-bh2', 'nh-bh', 'nh3-bh3', 'K_Cl', 'PMe3', 'cbut', 'bz', 'BF3PMe3', 'nh3', 'BCl3PMe3']
        self.exp_values = {'0': -32.1, '1': -0.2, '2': 37.6, '3': -19.5, '4': -48.9, '5': -46.1, '6': -25.2, '7': 40.4,
                           '8': -15.2, '9': 18.5, '10': -31.2, '11': 17.6}
        self.testset_calculations = {'0': "-1 * ['nh3'] -1 * ['BH3'] +1 * ['nh3-bh3']",
            '1': "-1 * ['nh3-bh3'] +1 * ['nh2-bh2'] +1 * ['H2']",
            '2': "-1 * ['nh2-bh2'] +1 * ['nh-bh'] +1 * ['H2']",
            '3': "-2 * ['nh2-bh2'] +1 * ['cbut']",
            '4': "-3 * ['nh2-bh2'] +1 * ['bz'] +3 * ['H2']",
            '5': "-3 * ['nh2-bh2'] +1 * ['ch']",
            '6': "+1 * ['BH3PH3'] -1 * ['BH3'] -1 * ['PH3']",
            '7': "+1 * ['K_H'] -1 * ['BH3PH3'] -1 * ['H2']",
            '8': "+1 * ['BF3PMe3'] -1 * ['BF3'] -1 * ['PMe3']",
            '9': "+1 * ['K_F'] -1 * ['BF3PMe3'] -1 * ['H2']",
            '10': "+1 * ['BCl3PMe3'] -1 * ['BCl3'] -1 * ['PMe3']",
            '11': "+1 * ['K_Cl'] -1 * ['BCl3PMe3'] -1 * ['H2']"}
        self.charges = {'K_H': -0.0, 'BH3PH3': -0.0, 'K_F': -0.0, 'H2': -0.0, 'BCl3': -0.0, 'BF3': 0.0, 'BH3': -0.0, 'ch': -0.0, 'PH3': -0.0, 'nh2-bh2': 0.0, 'nh-bh': -0.0, 'nh3-bh3': -0.0, 'K_Cl': -0.0, 'PMe3': 0.0, 'cbut': 0.0, 'bz': -0.0, 'BF3PMe3': -0.0, 'nh3': 0.0, 'BCl3PMe3': -0.0}
    