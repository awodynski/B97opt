from testsetclass import TestsetClass


class INV24(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['H2O', 'PCl3_TS', 'H2S', 'Thioether', 'PMe3_TS', 'Tetrabenzopyracylene', 'Sumanene', 'BN_Corannulene_TS', 'BN_Corannulene', 'Pentahelicene', 'Corannulene', 'BN_Sumanene', 'Triindenotriphenylene', 'Hexahelicene_TS', 'Tetrahelicene', 'SO2', 'Dibenzocycloheptene_TS', 'Tetrahelicene_TS', 'PH2Ph_TS', 'NCl3_TS', 'PPh3_TS', 'Dibenzocarbazole', 'NMe3_TS', 'PCl3', 'Ether_TS', 'PMe3', 'Pentahelicene_TS', 'Ether', 'H2O_TS', 'Dibenzocycloheptene', 'NMe3', 'NCl3', 'H2S_TS', 'Hexahelicene', 'Tetrabenzopyracylene_TS', 'Thioether_TS', 'PPh3', 'SO2_TS', 'Triazasumanene', 'Dibenzocarbazole_TS', 'Methinecyanine', 'Corannulene_TS', 'Sumanene_TS', 'PH2Ph', 'Triazasumanene_TS', 'Methinecyanine_TS', 'Triindenotriphenylene_TS', 'BN_Sumanene_TS']
        self.exp_values = {'0': 31.7, '1': 69.3, '2': 60.6, '3': 37.0, '4': 74.2, '5': 9.7, '6': 18.9, '7': 43.2,
                           '8': 79.7, '9': 31.2, '10': 29.3, '11': 10.3, '12': 4.5, '13': 24.7, '14': 37.6, '15': 4.1,
                           '16': 13.1, '17': 11.2, '18': 6.2, '19': 21.3, '20': 42.3, '21': 27.2, '22': 8.4, '23': 68.6}
        self.testset_calculations = {'0': "-1 * ['H2O'] +1 * ['H2O_TS']",
            '1': "-1 * ['H2S'] +1 * ['H2S_TS']",
            '2': "-1 * ['SO2'] +1 * ['SO2_TS']",
            '3': "-1 * ['Ether'] +1 * ['Ether_TS']",
            '4': "-1 * ['Thioether'] +1 * ['Thioether_TS']",
            '5': "-1 * ['NMe3'] +1 * ['NMe3_TS']",
            '6': "-1 * ['NCl3'] +1 * ['NCl3_TS']",
            '7': "-1 * ['PMe3'] +1 * ['PMe3_TS']",
            '8': "-1 * ['PCl3'] +1 * ['PCl3_TS']",
            '9': "-1 * ['PH2Ph'] +1 * ['PH2Ph_TS']",
            '10': "-1 * ['PPh3'] +1 * ['PPh3_TS']",
            '11': "-1 * ['Dibenzocycloheptene'] +1 * ['Dibenzocycloheptene_TS']",
            '12': "-1 * ['Tetrahelicene'] +1 * ['Tetrahelicene_TS']",
            '13': "-1 * ['Pentahelicene'] +1 * ['Pentahelicene_TS']",
            '14': "-1 * ['Hexahelicene'] +1 * ['Hexahelicene_TS']",
            '15': "-1 * ['Dibenzocarbazole'] +1 * ['Dibenzocarbazole_TS']",
            '16': "-1 * ['Methinecyanine'] +1 * ['Methinecyanine_TS']",
            '17': "-1 * ['Corannulene'] +1 * ['Corannulene_TS']",
            '18': "-1 * ['BN_Corannulene'] +1 * ['BN_Corannulene_TS']",
            '19': "-1 * ['Sumanene'] +1 * ['Sumanene_TS']",
            '20': "-1 * ['Triazasumanene'] +1 * ['Triazasumanene_TS']",
            '21': "-1 * ['BN_Sumanene'] +1 * ['BN_Sumanene_TS']",
            '22': "-1 * ['Tetrabenzopyracylene'] +1 * ['Tetrabenzopyracylene_TS']",
            '23': "-1 * ['Triindenotriphenylene'] +1 * ['Triindenotriphenylene_TS']"}
        self.charges = {'H2O': 0.0, 'PCl3_TS': 0.0, 'H2S': -0.0, 'Thioether': -0.0, 'PMe3_TS': -0.0, 'Tetrabenzopyracylene': 0.0, 'Sumanene': 0.0, 'BN_Corannulene_TS': -0.0, 'BN_Corannulene': 0.0, 'Pentahelicene': 0.0, 'Corannulene': 0.0, 'BN_Sumanene': -0.0, 'Triindenotriphenylene': 0.0, 'Hexahelicene_TS': 0.0, 'Tetrahelicene': 0.0, 'SO2': -0.0, 'Dibenzocycloheptene_TS': 0.0, 'Tetrahelicene_TS': 0.0, 'PH2Ph_TS': 0.0, 'NCl3_TS': -0.0, 'PPh3_TS': 0.0, 'Dibenzocarbazole': 0.0, 'NMe3_TS': 0.0, 'PCl3': 0.0, 'Ether_TS': -0.0, 'PMe3': 0.0, 'Pentahelicene_TS': 0.0, 'Ether': -0.0, 'H2O_TS': 0.0, 'Dibenzocycloheptene': 0.0, 'NMe3': -0.0, 'NCl3': 0.0, 'H2S_TS': -0.0, 'Hexahelicene': 0.0, 'Tetrabenzopyracylene_TS': 0.0, 'Thioether_TS': -0.0, 'PPh3': 0.0, 'SO2_TS': -0.0, 'Triazasumanene': 0.0, 'Dibenzocarbazole_TS': 0.0, 'Methinecyanine': 1.0, 'Corannulene_TS': 0.0, 'Sumanene_TS': 0.0, 'PH2Ph': 0.0, 'Triazasumanene_TS': 0.0, 'Methinecyanine_TS': 1.0, 'Triindenotriphenylene_TS': 0.0, 'BN_Sumanene_TS': 0.0}
    