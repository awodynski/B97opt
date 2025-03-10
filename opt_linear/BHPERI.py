from testsetclass import TestsetClass


class BHPERI(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['13ts_6a', '06ts', 'TS3', '1,3-Cyclohexadiene', '09r', '01r', '05r', '13r_1', '13ts_5a', '13ts_2a', 'Cis-triscyclopropacyclohexane', '1,3-Pentadiene', '13r_7', '02ts', '09ts', '1,3-Butadiene', 'Cyclobutene', 'Ethylene', '1,3-Cyclopentadiene', '13ts_8a', '13r_3', '13r_6', '02r', '01ts', 'TS9', '13ts_4a', '08ts', '13_c2h4', '04r', '13ts_3a', '1,5-Hexadiene', 'TS8', '05ts', 'Cyclonona-1,4,7-triene', 'TS10', '03r', 'TS1', 'TS5', 'ortho-xylylene', 'Benzocyclobutane', '07ts', '07r', '13ts_1a', '13ts_7a', 'cis-1,3,5-Hexatriene', 'Cyclohexene', '13r_4', 'TS7', 'TS2', '13r_2', 'TS6', '13r_5', 'Norbornene', '13ts_9a', '04ts', '03ts', '00r', '13r_8', 'TS4', '13r_9', 'TS11']
        self.exp_values = {'0': 35.3, '1': 30.8, '2': 28.1, '3': 39.7, '4': 28.3, '5': 35.8, '6': 22.3, '7': 18.0, '8': 14.5, '9': 26.4, '10': 27.6, '11': 20.0, '12': 13.8, '13': 11.8, '14': 6.5, '15': 4.7, '16': 13.1, '17': 5.9, '18': 0.5, '19': 18.1, '20': 16.6, '21': 22.9, '22': 27.8, '23': 21.3, '24': 21.6, '25': 31.3}
        self.testset_calculations = {'0': "-1 * ['Cyclobutene'] +1 * ['TS1']",
              '1': "-1 * ['cis-1,3,5-Hexatriene'] +1 * ['TS2']",
              '2': "-1 * ['ortho-xylylene'] +1 * ['TS3']",
              '3': "-1 * ['1,3-Pentadiene'] +1 * ['TS4']",
              '4': "-1 * ['1,3-Cyclopentadiene'] +1 * ['TS5']",
              '5': "-1 * ['1,5-Hexadiene'] +1 * ['TS6']",
              '6': "-1 * ['1,3-Butadiene'] -1 * ['Ethylene'] +1 * ['TS7']",
              '7': "-1 * ['1,3-Cyclopentadiene'] -1 * ['Ethylene'] +1 * ['TS8']",
              '8': "-2 * ['1,3-Cyclopentadiene'] +1 * ['TS11']",
              '9': "-1 * ['Cis-triscyclopropacyclohexane'] +1 * ['TS9']",
              '10': "-1 * ['13r_1'] -1 * ['13_c2h4'] +1 * ['13ts_1a']",
              '11': "-1 * ['13r_2'] -1 * ['13_c2h4'] +1 * ['13ts_2a']",
              '12': "-1 * ['13r_3'] -1 * ['13_c2h4'] +1 * ['13ts_3a']",
              '13': "-1 * ['13r_4'] -1 * ['13_c2h4'] +1 * ['13ts_4a']",
              '14': "-1 * ['13r_5'] -1 * ['13_c2h4'] +1 * ['13ts_5a']",
              '15': "-1 * ['13r_6'] -1 * ['13_c2h4'] +1 * ['13ts_6a']",
              '16': "-1 * ['13r_7'] -1 * ['13_c2h4'] +1 * ['13ts_7a']",
              '17': "-1 * ['13r_8'] -1 * ['13_c2h4'] +1 * ['13ts_8a']",
              '18': "-1 * ['13r_9'] -1 * ['13_c2h4'] +1 * ['13ts_9a']",
              '19': "-1 * ['02r'] -1 * ['00r'] +1 * ['02ts']",
              '20': "-1 * ['03r'] -1 * ['00r'] +1 * ['03ts']",
              '21': "-1 * ['04r'] -1 * ['00r'] +1 * ['04ts']",
              '22': "-1 * ['05r'] -1 * ['00r'] +1 * ['06ts']",
              '23': "-1 * ['07r'] -1 * ['00r'] +1 * ['07ts']",
              '24': "-1 * ['07r'] -1 * ['00r'] +1 * ['08ts']",
              '25': "-1 * ['09r'] -1 * ['00r'] +1 * ['09ts']"}
        self.charges = {'13ts_6a': -0.0, '06ts': -0.0, 'TS3': 0.0, '1,3-Cyclohexadiene': 0.0, '09r': 0.0, '01r': 0.0, '05r': 0.0, '13r_1': -0.0, '13ts_5a': 0.0, '13ts_2a': -0.0, 'Cis-triscyclopropacyclohexane': 0.0, '1,3-Pentadiene': 0.0, '13r_7': 0.0, '02ts': 0.0, '09ts': 0.0, '1,3-Butadiene': 0.0, 'Cyclobutene': 0.0, 'Ethylene': 0.0, '1,3-Cyclopentadiene': -0.0, '13ts_8a': 0.0, '13r_3': -0.0, '13r_6': -0.0, '02r': -0.0, '01ts': 0.0, 'TS9': 0.0, '13ts_4a': 0.0, '08ts': 0.0, '13_c2h4': 0.0, '04r': 0.0, '13ts_3a': -0.0, '1,5-Hexadiene': 0.0, 'TS8': -0.0, '05ts': -0.0, 'Cyclonona-1,4,7-triene': 0.0, 'TS10': -0.0, '03r': -0.0, 'TS1': 0.0, 'TS5': -0.0, 'ortho-xylylene': 0.0, 'Benzocyclobutane': 0.0, '07ts': 0.0, '07r': -0.0, '13ts_1a': 0.0, '13ts_7a': -0.0, 'cis-1,3,5-Hexatriene': 0.0, 'Cyclohexene': 0.0, '13r_4': -0.0, 'TS7': 0.0, 'TS2': -0.0, '13r_2': -0.0, 'TS6': 0.0, '13r_5': -0.0, 'Norbornene': -0.0, '13ts_9a': 0.0, '04ts': 0.0, '03ts': 0.0, '00r': 0.0, '13r_8': 0.0, 'TS4': -0.0, '13r_9': -0.0, 'TS11': 0.0}
    