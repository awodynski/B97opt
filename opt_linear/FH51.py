from testsetclass import TestsetClass


class FH51(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['CO2', 'methanol', 'C2H5CO2CH3', 'NH3', 'C4H9ONO', 'butanediol', 'C3H7CO2H', 'HCl', 'HCON_C2H5_2', 'propylfuran', 'C2H5CCNCHCH3', 'diethylamine', 'propylthiophene', 'OS_C2H5_2', 'H2O2', 'methyl-d-valerolactone', 'Cl2', 'pentadiene', 'COCl2', 'cis-2-pentene', 'C4H9CHO', 'C2H5CClCHCH3', 'dimethylpyrrole', '1-pentene', 'tetramethylpentane', 'C2H5CONH2', 'methylpyrrole', 'HCO2C5H11', 'methylcyclohexa-1,4-diene', '3-methylpentane', 'methylcyclohexane', 'H2', 'methylimidazole', 'C3H7SH', 'pentanediol', 'C3H7CONH2', 'CO', 'dimethyloxirane', 'methylpyridine', 'toluene', '1-pentyne', 'methylpyrazole', 'methylcyclohexa-1,3-diene', 'C4H9NO2', 'H2O', 'diethyloxirane', 'C4H9CO2H', 'eq-methylcyclohexene', 'hexandione', 'C4H9NH2', 'H2S', 'heptatriyne', 'C2H5CO2H', 'dimethylbutane', 'C6H12O', 'C3H7NH2', 'ax-methylcyclohexene', '3-hexene', 'Heptene', 'S_C2H5_2', 'HCN', 'C3H7NCO', 'hexyne', 'CO_2NHC3H7_2', '1-hexene', 'C2H5O_2', 'C4H9NCO', 'ethyl-g-butyrolactone', 'C3H7CO2C2H3', 'C4H9SO3H', 'C4H9NHCONH2', 'methylfuran', '2-pentyne', 'pentanol', 'n-nonane', 'H2C-C5-CH2', 'C3H7S_2', 'C2H4OH_2', 'trans-2-pentene', 'C3H7CN', 'ethene', 'H2CO', 'propyloxirane', 'C3H7CHCO', 'C4H9SO2H', 'neo-hexane', 'n-hexane']
        self.exp_values = {'0': -150.81, '1': -144.38, '2': -89.35, '3': -82.55, '4': -78.51, '5': -66.96, '6': -63.89, '7': -58.53, '8': -56.64, '9': -52.85, '10': -52.60, '11': -46.72, '12': -44.82, '13': -43.67, '14': -42.89, '15': -37.08, '16': -34.93, '17': -32.47, '18': -32.10, '19': -31.22, '20': -29.98, '21': -25.84, '22': -23.47, '23': -22.45, '24': -20.27, '25': -19.72, '26': -19.34, '27': -19.45, '28': -17.39, '29': -16.98, '30': -16.14, '31': -14.30, '32': -13.14, '33': -11.68, '34': -10.70, '35': -9.39, '36': -8.53, '37': -6.63, '38': -6.65, '39': -6.45, '40': -5.11, '41': -3.25, '42': -2.64, '43': -2.48, '44': -2.11, '45': -1.47, '46': -1.15, '47': -0.86, '48': -0.43, '49': -0.41, '50': -0.18}
        self.testset_calculations = {'0': "-1 * ['C6H12O'] -2 * ['H2O2'] +1 * ['ethyl-g-butyrolactone'] +3 * ['H2O']",
              '1': "-1 * ['C4H9NH2'] -3 * ['H2O2'] +1 * ['C4H9NO2'] +4 * ['H2O']",
              '2': "-1 * ['C4H9CHO'] -1 * ['H2O2'] +1 * ['C4H9CO2H'] +1 * ['H2O']",
              '3': "-1 * ['C4H9SO2H'] -1 * ['H2O2'] +1 * ['C4H9SO3H'] +1 * ['H2O']",
              '4': "-1 * ['trans-2-pentene'] -1 * ['H2O2'] +1 * ['pentanediol']",
              '5': "-1 * ['toluene'] -3 * ['H2'] +1 * ['methylcyclohexane']",
              '6': "-1 * ['pentanol'] -1 * ['H2O2'] +1 * ['C4H9CHO'] +2 * ['H2O']",
              '7': "-1 * ['C2H5O_2'] +1 * ['C2H4OH_2']",
              '8': "-1 * ['3-hexene'] -1 * ['H2O2'] +1 * ['diethyloxirane'] +1 * ['H2O']",
              '9': "-1 * ['S_C2H5_2'] -1 * ['H2O2'] +1 * ['OS_C2H5_2'] +1 * ['H2O']",
              '10': "-1 * ['ax-methylcyclohexene'] +1 * ['eq-methylcyclohexene']",
              '11': "-1 * ['hexyne'] -1 * ['H2'] +1 * ['1-hexene']",
              '12': "-1 * ['2-pentyne'] -1 * ['H2'] +1 * ['trans-2-pentene']",
              '13': "-1 * ['2-pentyne'] -1 * ['H2'] +1 * ['cis-2-pentene']",
              '14': "-1 * ['2-pentyne'] -1 * ['HCN'] +1 * ['C2H5CCNCHCH3']",
              '15': "-1 * ['1-hexene'] -1 * ['H2'] +1 * ['n-hexane']",
              '16': "-1 * ['1-pentyne'] -1 * ['H2O'] +1 * ['C4H9CHO']",
              '17': "-2 * ['C3H7NH2'] -1 * ['COCl2'] +1 * ['CO_2NHC3H7_2'] +2 * ['HCl']",
              '18': "-1 * ['eq-methylcyclohexene'] -1 * ['H2'] +1 * ['methylcyclohexane']",
              '19': "-1 * ['trans-2-pentene'] -1 * ['Cl2'] +1 * ['C2H5CClCHCH3'] +1 * ['HCl']",
              '20': "-1 * ['2-pentyne'] -1 * ['HCl'] +1 * ['C2H5CClCHCH3']",
              '21': "-1 * ['1-pentene'] -1 * ['ethene'] +1 * ['Heptene']",
              '22': "-1 * ['C4H9CHO'] -1 * ['H2'] +1 * ['pentanol']",
              '23': "-1 * ['dimethyloxirane'] -1 * ['H2O'] +1 * ['butanediol']",
              '24': "-1 * ['methylpyridine'] -1 * ['H2'] +1 * ['dimethylpyrrole']",
              '25': "-1 * ['C4H9NCO'] -1 * ['NH3'] +1 * ['C4H9NHCONH2']",
              '26': "-1 * ['C3H7CN'] -1 * ['H2O'] +1 * ['C3H7CONH2']",
              '27': "-1 * ['propylfuran'] -1 * ['H2S'] +1 * ['propylthiophene'] +1 * ['H2O']",
              '28': "-1 * ['diethylamine'] -1 * ['CO'] +1 * ['HCON_C2H5_2']",
              '29': "-1 * ['C3H7NCO'] -1 * ['H2O'] +1 * ['C3H7NH2'] +1 * ['CO2']",
              '30': "-1 * ['C3H7CO2C2H3'] +1 * ['ethyl-g-butyrolactone']",
              '31': "-1 * ['H2C-C5-CH2'] +1 * ['heptatriyne']",
              '32': "-1 * ['methylpyrazole'] +1 * ['methylimidazole']",
              '33': "-1 * ['1-pentene'] -1 * ['H2O'] +1 * ['pentanol']",
              '34': "-1 * ['methylfuran'] -1 * ['NH3'] +1 * ['methylpyrrole'] +1 * ['H2O']",
              '35': "-1 * ['C3H7CHCO'] -1 * ['H2CO'] +1 * ['propyloxirane'] +1 * ['CO']",
              '36': "-1 * ['pentanol'] -1 * ['CO'] +1 * ['HCO2C5H11']",
              '37': "-1 * ['C3H7S_2'] -1 * ['H2'] +2 * ['C3H7SH']",
              '38': "+1 * ['pentadiene'] +1 * ['ethene'] -1 * ['ax-methylcyclohexene']",
              '39': "-1 * ['hexandione'] +1 * ['methyl-d-valerolactone']",
              '40': "-1 * ['C2H5CO2H'] -1 * ['methanol'] +1 * ['C2H5CO2CH3'] +1 * ['H2O']",
              '41': "-1 * ['C4H9ONO'] +1 * ['C4H9NO2']",
              '42': "-1 * ['n-hexane'] +1 * ['neo-hexane']",
              '43': "-1 * ['methylcyclohexa-1,4-diene'] +1 * ['methylcyclohexa-1,3-diene']",
              '44': "-1 * ['1-pentene'] +1 * ['trans-2-pentene']",
              '45': "-1 * ['toluene'] -1 * ['H2'] +1 * ['methylcyclohexa-1,3-diene']",
              '46': "-1 * ['cis-2-pentene'] +1 * ['trans-2-pentene']",
              '47': "-1 * ['3-methylpentane'] +1 * ['dimethylbutane']",
              '48': "-1 * ['C2H5CO2H'] -1 * ['NH3'] +1 * ['C2H5CONH2'] +1 * ['H2O']",
              '49': "-1 * ['n-nonane'] +1 * ['tetramethylpentane']",
              '50': "-1 * ['C3H7CO2H'] -1 * ['NH3'] +1 * ['C3H7CONH2'] +1 * ['H2O']"}
        self.charges = {'CO2': -0.0, 'methanol': 0.0, 'C2H5CO2CH3': -0.0, 'NH3': 0.0, 'C4H9ONO': 0.0, 'butanediol': -0.0, 'C3H7CO2H': -0.0, 'HCl': 0.0, 'HCON_C2H5_2': -0.0, 'propylfuran': 0.0, 'C2H5CCNCHCH3': 0.0, 'diethylamine': -0.0, 'propylthiophene': 0.0, 'OS_C2H5_2': 0.0, 'H2O2': -0.0, 'methyl-d-valerolactone': -0.0, 'Cl2': -0.0, 'pentadiene': 0.0, 'COCl2': 0.0, 'cis-2-pentene': 0.0, 'C4H9CHO': 0.0, 'C2H5CClCHCH3': 0.0, 'dimethylpyrrole': -0.0, '1-pentene': 0.0, 'tetramethylpentane': 0.0, 'C2H5CONH2': -0.0, 'methylpyrrole': -0.0, 'HCO2C5H11': -0.0, 'methylcyclohexa-1,4-diene': 0.0, '3-methylpentane': 0.0, 'methylcyclohexane': -0.0, 'H2': 0.0, 'methylimidazole': 0.0, 'C3H7SH': -0.0, 'pentanediol': 0.0, 'C3H7CONH2': -0.0, 'CO': -0.0, 'dimethyloxirane': 0.0, 'methylpyridine': 0.0, 'toluene': 0.0, '1-pentyne': -0.0, 'methylpyrazole': -0.0, 'methylcyclohexa-1,3-diene': 0.0, 'C4H9NO2': -0.0, 'H2O': 0.0, 'diethyloxirane': 0.0, 'C4H9CO2H': -0.0, 'eq-methylcyclohexene': 0.0, 'hexandione': -0.0, 'C4H9NH2': -0.0, 'H2S': -0.0, 'heptatriyne': -0.0, 'C2H5CO2H': -0.0, 'dimethylbutane': 0.0, 'C6H12O': 0.0, 'C3H7NH2': 0.0, 'ax-methylcyclohexene': -0.0, '3-hexene': 0.0, 'Heptene': 0.0, 'S_C2H5_2': -0.0, 'HCN': 0.0, 'C3H7NCO': -0.0, 'hexyne': 0.0, 'CO_2NHC3H7_2': -0.0, '1-hexene': 0.0, 'C2H5O_2': 0.0, 'C4H9NCO': -0.0, 'ethyl-g-butyrolactone': 0.0, 'C3H7CO2C2H3': -0.0, 'C4H9SO3H': -0.0, 'C4H9NHCONH2': 0.0, 'methylfuran': 0.0, '2-pentyne': 0.0, 'pentanol': 0.0, 'n-nonane': 0.0, 'H2C-C5-CH2': 0.0, 'C3H7S_2': 0.0, 'C2H4OH_2': -0.0, 'trans-2-pentene': 0.0, 'C3H7CN': -0.0, 'ethene': 0.0, 'H2CO': 0.0, 'propyloxirane': 0.0, 'C3H7CHCO': 0.0, 'C4H9SO2H': -0.0, 'neo-hexane': 0.0, 'n-hexane': 0.0}
    