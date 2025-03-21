from testsetclass import TestsetClass


class BH76(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['hcn', 'n2', 'N2H2', 'hfch3ts', 'NH3', 'hclhts', 'fch3clcomp2', 'hf2ts', 'RKT09', 'f', 'ch3cl', 'fch3fcomp', 'RKT06', 'c2h4', 'RKT04', 'RKT21', 'RKT05', 'hn2ts', 'RKT17', 'RKT03', 'n2o', 'c2h5', 'oh-', 'HS', 'O', 'RKT18', 'cl', 'f2', 'cl-', 'c2h5ts', 'H2', 'f-', 'CH4', 'fch3clcomp1', 'NH', 'hcots', 'RKT22', 'PH2', 'hcnts', 'hcl', 'ch3', 'RKT16', 'hnc', 'H2O', 'C5H8', 'hoch3fcomp2', 'H2S', 'hoch3fts', 'ch3f', 'hfhts', 'c3h7', 'RKT15', 'fch3clts', 'clch3clts', 'c3h7ts', 'ch3fclts', 'hch3clts', 'RKT20', 'N2H', 'RKT11', 'RKT19', 'C2H6', 'RKT02', 'RKT14', 'hoch3fcomp1', 'RKT10', 'n2ohts', 'PH3', 'NH2', 'ch3oh', 'clf', 'RKT07', 'C2H5', 'oh', 'co', 'fch3fts', 'hf', 'h', 'RKT13', 'clch3clcomp', 'CH2OH', 'hn2', 'RKT01', 'RKT12', 'hco', 'RKT08']
        self.exp_values = {'0': 17.7, '1': 82.6, '2': 42.1, '3': 42.1, '4': 17.8, '5': 17.8, '6': 30.5, '7': 56.9, '8': 1.5, '9': 104.8, '10': 7.1, '11': 59.8, '12': -0.6, '13': -0.6, '14': 13.4, '15': 13.4, '16': 2.5, '17': 2.5, '18': 13.5, '19': 13.5, '20': -12.3, '21': 19.8, '22': 3.5, '23': 29.6, '24': -2.7, '25': 17.6, '26': 11.0, '27': 47.7, '28': 14.6, '29': 10.9, '30': 3.2, '31': 22.8, '32': 2.0, '33': 42.0, '34': 6.4, '35': 33.0, '36': 48.1, '37': 33.0, '38': 6.1, '39': 8.0, '40': 5.2, '41': 21.6, '42': 11.9, '43': 15.0, '44': 6.3, '45': 19.5, '46': 9.7, '47': 9.7, '48': 3.4, '49': 13.7, '50': 1.8, '51': 6.8, '52': 3.5, '53': 20.4, '54': 1.6, '55': 33.8, '56': 14.4, '57': 8.9, '58': 2.9, '59': 24.7, '60': 10.9, '61': 13.2, '62': 3.9, '63': 17.2, '64': 10.4, '65': 9.9, '66': 8.9, '67': 22.0, '68': 9.8, '69': 19.4, '70': 11.3, '71': 17.8, '72': 13.9, '73': 16.9, '74': 39.7, '75': 39.7}
        self.testset_calculations = {'0': "-1 * ['h'] -1 * ['n2o'] +1 * ['n2ohts']",
              '1': "-1 * ['oh'] -1 * ['n2'] +1 * ['n2ohts']",
              '2': "-1 * ['h'] -1 * ['hf'] +1 * ['hfhts']",
              '3': "-1 * ['hf'] -1 * ['h'] +1 * ['hfhts']",
              '4': "-1 * ['h'] -1 * ['hcl'] +1 * ['hclhts']",
              '5': "-1 * ['hcl'] -1 * ['h'] +1 * ['hclhts']",
              '6': "-1 * ['h'] -1 * ['ch3f'] +1 * ['hfch3ts']",
              '7': "-1 * ['hf'] -1 * ['ch3'] +1 * ['hfch3ts']",
              '8': "-1 * ['h'] -1 * ['f2'] +1 * ['hf2ts']",
              '9': "-1 * ['hf'] -1 * ['f'] +1 * ['hf2ts']",
              '10': "-1 * ['ch3'] -1 * ['clf'] +1 * ['ch3fclts']",
              '11': "-1 * ['ch3f'] -1 * ['cl'] +1 * ['ch3fclts']",
              '12': "-1 * ['f-'] -1 * ['ch3f'] +1 * ['fch3fts']",
              '13': "-1 * ['ch3f'] -1 * ['f-'] +1 * ['fch3fts']",
              '14': "-1 * ['fch3fcomp'] +1 * ['fch3fts']",
              '15': "-1 * ['fch3fcomp'] +1 * ['fch3fts']",
              '16': "-1 * ['cl-'] -1 * ['ch3cl'] +1 * ['clch3clts']",
              '17': "-1 * ['ch3cl'] -1 * ['cl-'] +1 * ['clch3clts']",
              '18': "-1 * ['clch3clcomp'] +1 * ['clch3clts']",
              '19': "-1 * ['clch3clcomp'] +1 * ['clch3clts']",
              '20': "-1 * ['f-'] -1 * ['ch3cl'] +1 * ['fch3clts']",
              '21': "-1 * ['cl-'] -1 * ['ch3f'] +1 * ['fch3clts']",
              '22': "-1 * ['fch3clcomp1'] +1 * ['fch3clts']",
              '23': "-1 * ['fch3clcomp2'] +1 * ['fch3clts']",
              '24': "-1 * ['oh-'] -1 * ['ch3f'] +1 * ['hoch3fts']",
              '25': "-1 * ['ch3oh'] -1 * ['f-'] +1 * ['hoch3fts']",
              '26': "-1 * ['hoch3fcomp2'] +1 * ['hoch3fts']",
              '27': "-1 * ['hoch3fcomp1'] +1 * ['hoch3fts']",
              '28': "-1 * ['h'] -1 * ['n2'] +1 * ['hn2ts']",
              '29': "-1 * ['hn2'] +1 * ['hn2ts']",
              '30': "-1 * ['h'] -1 * ['co'] +1 * ['hcots']",
              '31': "-1 * ['hco'] +1 * ['hcots']",
              '32': "-1 * ['h'] -1 * ['c2h4'] +1 * ['c2h5ts']",
              '33': "-1 * ['c2h5'] +1 * ['c2h5ts']",
              '34': "-1 * ['ch3'] -1 * ['c2h4'] +1 * ['c3h7ts']",
              '35': "-1 * ['c3h7'] +1 * ['c3h7ts']",
              '36': "-1 * ['hcn'] +1 * ['hcnts']",
              '37': "-1 * ['hnc'] +1 * ['hcnts']",
              '38': "-1 * ['h'] -1 * ['hcl'] +1 * ['RKT01']",
              '39': "-1 * ['H2'] -1 * ['cl'] +1 * ['RKT01']",
              '40': "-1 * ['oh'] -1 * ['H2'] +1 * ['RKT02']",
              '41': "-1 * ['H2O'] -1 * ['h'] +1 * ['RKT02']",
              '42': "-1 * ['ch3'] -1 * ['H2'] +1 * ['RKT03']",
              '43': "-1 * ['CH4'] -1 * ['h'] +1 * ['RKT03']",
              '44': "-1 * ['oh'] -1 * ['CH4'] +1 * ['RKT04']",
              '45': "-1 * ['H2O'] -1 * ['ch3'] +1 * ['RKT04']",
              '46': "-1 * ['h'] -1 * ['H2'] +1 * ['RKT06']",
              '47': "-1 * ['h'] -1 * ['H2'] +1 * ['RKT06']",
              '48': "-1 * ['oh'] -1 * ['NH3'] +1 * ['RKT07']",
              '49': "-1 * ['H2O'] -1 * ['NH2'] +1 * ['RKT07']",
              '50': "-1 * ['hcl'] -1 * ['ch3'] +1 * ['RKT08']",
              '51': "-1 * ['cl'] -1 * ['CH4'] +1 * ['RKT08']",
              '52': "-1 * ['oh'] -1 * ['C2H6'] +1 * ['RKT09']",
              '53': "-1 * ['H2O'] -1 * ['C2H5'] +1 * ['RKT09']",
              '54': "-1 * ['f'] -1 * ['H2'] +1 * ['RKT10']",
              '55': "-1 * ['hf'] -1 * ['h'] +1 * ['RKT10']",
              '56': "-1 * ['O'] -1 * ['CH4'] +1 * ['RKT11']",
              '57': "-1 * ['oh'] -1 * ['ch3'] +1 * ['RKT11']",
              '58': "-1 * ['h'] -1 * ['PH3'] +1 * ['RKT12']",
              '59': "-1 * ['H2'] -1 * ['PH2'] +1 * ['RKT12']",
              '60': "-1 * ['h'] -1 * ['oh'] +1 * ['RKT14']",
              '61': "-1 * ['H2'] -1 * ['O'] +1 * ['RKT14']",
              '62': "-1 * ['h'] -1 * ['H2S'] +1 * ['RKT16']",
              '63': "-1 * ['H2'] -1 * ['HS'] +1 * ['RKT16']",
              '64': "-1 * ['O'] -1 * ['hcl'] +1 * ['RKT17']",
              '65': "-1 * ['oh'] -1 * ['cl'] +1 * ['RKT17']",
              '66': "-1 * ['NH2'] -1 * ['ch3'] +1 * ['RKT18']",
              '67': "-1 * ['NH'] -1 * ['CH4'] +1 * ['RKT18']",
              '68': "-1 * ['NH2'] -1 * ['C2H5'] +1 * ['RKT19']",
              '69': "-1 * ['NH'] -1 * ['C2H6'] +1 * ['RKT19']",
              '70': "-1 * ['C2H6'] -1 * ['NH2'] +1 * ['RKT20']",
              '71': "-1 * ['C2H5'] -1 * ['NH3'] +1 * ['RKT20']",
              '72': "-1 * ['NH2'] -1 * ['CH4'] +1 * ['RKT21']",
              '73': "-1 * ['NH3'] -1 * ['ch3'] +1 * ['RKT21']",
              '74': "-1 * ['C5H8'] +1 * ['RKT22']",
              '75': "-1 * ['C5H8'] +1 * ['RKT22']"}
        self.charges = {'hcn': -0.0, 'n2': 0.0, 'N2H2': 0.0, 'hfch3ts': 0.0, 'NH3': -0.0, 'hclhts': -0.0, 'fch3clcomp2': -1.0, 'hf2ts': 0.0, 'RKT09': 0.0, 'f': -0.0, 'ch3cl': -0.0, 'fch3fcomp': -1.0, 'RKT06': -0.0, 'c2h4': 0.0, 'RKT04': 0.0, 'RKT21': 0.0, 'RKT05': -0.0, 'hn2ts': 0.0, 'RKT17': -0.0, 'RKT03': 0.0, 'n2o': -0.0, 'c2h5': 0.0, 'oh-': -1.0, 'HS': -0.0, 'O': -0.0, 'RKT18': 0.0, 'cl': -0.0, 'f2': -0.0, 'cl-': -1.0, 'c2h5ts': 0.0, 'H2': 0.0, 'f-': -1.0, 'CH4': -0.0, 'fch3clcomp1': -1.0, 'NH': 0.0, 'hcots': 0.0, 'RKT22': -0.0, 'PH2': -0.0, 'hcnts': 0.0, 'hcl': 0.0, 'ch3': 0.0, 'RKT16': -0.0, 'hnc': 0.0, 'H2O': 0.0, 'C5H8': 0.0, 'hoch3fcomp2': -1.0, 'H2S': -0.0, 'hoch3fts': -1.0, 'ch3f': 0.0, 'hfhts': -0.0, 'c3h7': 0.0, 'RKT15': 0.0, 'fch3clts': -1.0, 'clch3clts': -1.0, 'c3h7ts': 0.0, 'ch3fclts': -0.0, 'hch3clts': -0.0, 'RKT20': -0.0, 'N2H': 0.0, 'RKT11': 0.0, 'RKT19': -0.0, 'C2H6': 0.0, 'RKT02': 0.0, 'RKT14': 0.0, 'hoch3fcomp1': -1.0, 'RKT10': -0.0, 'n2ohts': -0.0, 'PH3': -0.0, 'NH2': -0.0, 'ch3oh': -0.0, 'clf': -0.0, 'RKT07': 0.0, 'C2H5': 0.0, 'oh': 0.0, 'co': 0.0, 'fch3fts': -1.0, 'hf': 0.0, 'h': -0.0, 'RKT13': -0.0, 'clch3clcomp': -1.0, 'CH2OH': -0.0, 'hn2': 0.0, 'RKT01': -0.0, 'RKT12': -0.0, 'hco': 0.0, 'RKT08': 0.0}
    