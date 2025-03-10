from testsetclass import TestsetClass


class G2RC(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['56', '60', '18', '73', '45', '126', '68', '22', '51', '52', '59', '40', '121', '33', '23', '32', '14', '82', '21', '94', '100', '24', '39', '47', '113', '58', '34', '57', '61', '25', '6', '117', '11', '104', '26', '97', '62', '106', '128', '118', '8', '1', '13', '67', '88', '66', '30']
        self.exp_values = {'0': -2.23, '1': -2.26, '2': -2.18, '3': -4.10, '4': -7.10, '5': -10.70, '6': -19.47, '7': -26.97, '8': -27.30, '9': -27.15, '10': -24.89, '11': -29.46, '12': -32.71, '13': -36.32, '14': -39.43, '15': -48.52, '16': -49.20, '17': -61.67, '18': -65.15, '19': -68.90, '20': -81.21, '21': -109.11, '22': -135.40, '23': -154.04, '24': -216.11}
        self.testset_calculations = {'0': "-1 * ['118'] +1 * ['117'] +1 * ['13']",
              '1': "-1 * ['40'] -1 * ['1'] +1 * ['104']",
              '2': "-1 * ['113'] +1 * ['30'] +1 * ['8']",
              '3': "-1 * ['52'] -1 * ['1'] +2 * ['18']",
              '4': "-1 * ['30'] -1 * ['13'] +1 * ['40'] +1 * ['1']",
              '5': "-1 * ['128'] -1 * ['13'] +1 * ['126'] +1 * ['22']",
              '6': "-1 * ['100'] -1 * ['13'] +1 * ['106']",
              '7': "-1 * ['25'] -1 * ['14'] +1 * ['121']",
              '8': "-1 * ['39'] -1 * ['45'] +2 * ['51']",
              '9': "-1 * ['58'] -1 * ['59'] +1 * ['57'] +1 * ['60']",
              '10': "-1 * ['67'] -1 * ['61'] +1 * ['66'] +1 * ['62']",
              '11': "-1 * ['32'] -1 * ['1'] +1 * ['33']",
              '12': "-1 * ['25'] -1 * ['26'] +1 * ['88']",
              '13': "-1 * ['47'] -3 * ['1'] +1 * ['18'] +1 * ['13']",
              '14': "-1 * ['34'] -3 * ['1'] +2 * ['11']",
              '15': "-1 * ['8'] -2 * ['45'] +1 * ['97'] +2 * ['22']",
              '16': "-1 * ['25'] -1 * ['1'] +1 * ['26']",
              '17': "-1 * ['56'] -3 * ['1'] +1 * ['21'] +2 * ['13']",
              '18': "-1 * ['30'] -3 * ['1'] +1 * ['13'] +1 * ['8']",
              '19': "-1 * ['73'] -1 * ['1'] +1 * ['39'] +1 * ['13']",
              '20': "-1 * ['68'] -1 * ['1'] +1 * ['34'] +1 * ['13']",
              '21': "-1 * ['26'] -1 * ['6'] +1 * ['82']",
              '22': "-1 * ['1'] -1 * ['39'] +2 * ['14']",
              '23': "-3 * ['25'] +1 * ['94']",
              '24': "-1 * ['23'] -1 * ['39'] +2 * ['24']"}
        self.charges = {'56': -0.0, '60': 0.0, '18': -0.0, '73': -0.0, '45': -0.0, '126': -0.0, '68': -0.0, '22': -0.0, '51': 0.0, '52': -0.0, '59': -0.0, '40': -0.0, '121': 0.0, '33': 0.0, '23': 0.0, '32': 0.0, '14': 0.0, '82': 0.0, '21': -0.0, '94': -0.0, '100': -0.0, '24': 0.0, '39': 0.0, '47': -0.0, '113': 0.0, '58': -0.0, '34': 0.0, '57': 0.0, '61': -0.0, '25': 0.0, '6': -0.0, '117': -0.0, '11': 0.0, '104': 0.0, '26': 0.0, '97': -0.0, '62': 0.0, '106': -0.0, '128': 0.0, '118': 0.0, '8': -0.0, '1': 0.0, '13': 0.0, '67': 0.0, '88': 0.0, '66': 0.0, '30': 0.0}
    