from testsetclass import TestsetClass


class DC13(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['ISO_E36', 'ch2n2', 'c2h2', 'c20bowl', 'ISO_C8H8_1', 'c2h4', 'CL2', 's2', 'C6Cl6', 'c20cage', 'carbooxo2', 'o3', 'o3_c2h4_add', '13dip', 'be4', 'ISO_E35', 'heptatriyne', 'ISO_P36', 's8', 'heptahexaene', 'o3_c2h2_add', 'C6H6', 'carbooxo1', 'HCL', 'tmethen', 'omcb', 'ethen', 'ISO_P35', 'be', 'ISO_C8H8_41']
        self.exp_values = {'0': -1.0, '1': -7.7, '2': -15.2, '3': -18.8, '4': -22.9, '5': -25.7, '6': -38.9, '7': -92.0, '8': -106.0, '9': 109.92, '10': -65.3, '11': -58.7, '12': 152.6}
        self.testset_calculations = {'0': "+1 * ['ISO_E36'] -1 * ['ISO_P36']",
              '1': "-1 * ['c20cage'] +1 * ['c20bowl']",
              '2': "+1 * ['heptatriyne'] -1 * ['heptahexaene']",
              '3': "-2 * ['tmethen'] +1 * ['omcb']",
              '4': "+1 * ['ISO_E35'] -1 * ['ISO_P35']",
              '5': "-1 * ['carbooxo2'] +1 * ['carbooxo1']",
              '6': "-1 * ['ethen'] -1 * ['ch2n2'] +1 * ['13dip']",
              '7': "+1 * ['be4'] -4 * ['be']",
              '8': "-4 * ['s2'] +1 * ['s8']",
              '9': "-1 * ['ISO_C8H8_1'] +1 * ['ISO_C8H8_41']",
              '10': "-1 * ['o3'] -1 * ['c2h2'] +1 * ['o3_c2h2_add']",
              '11': "-1 * ['o3'] -1 * ['c2h4'] +1 * ['o3_c2h4_add']",
              '12': "-1 * ['C6Cl6'] -6 * ['HCL'] +1 * ['C6H6'] +6 * ['CL2']"}
        self.charges = {'ISO_E36': -0.0, 'ch2n2': -0.0, 'c2h2': 0.0, 'c20bowl': -0.0, 'ISO_C8H8_1': 0.0, 'c2h4': 0.0, 'CL2': -0.0, 's2': -0.0, 'C6Cl6': 0.0, 'c20cage': 0.0, 'carbooxo2': 0.0, 'o3': 0.0, 'o3_c2h4_add': -0.0, '13dip': 0.0, 'be4': 0.0, 'ISO_E35': -0.0, 'heptatriyne': -0.0, 'ISO_P36': -0.0, 's8': 0.0, 'heptahexaene': 0.0, 'o3_c2h2_add': 0.0, 'C6H6': -0.0, 'carbooxo1': 0.0, 'HCL': 0.0, 'tmethen': 0.0, 'omcb': 0.0, 'ethen': 0.0, 'ISO_P35': -0.0, 'be': -0.0, 'ISO_C8H8_41': 0.0}
    