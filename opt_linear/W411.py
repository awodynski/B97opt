from testsetclass import TestsetClass


class W411(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['hcn', 'n2', 'hocl', 'hcno', 'methanol', 'ch2-trip', 'honc', 'hocn', 'alh', 'p4', 't-hono', 'oxirene', 'hnnn', 'c2h3f', 'c2h2', 'bf', 'alh3', 'co2', 'f', 'c2', 'hcnh', 'cs2', 'ch3nh', 'glyoxal', 'c2h4', 'propane', 's2', 'ch', 'ethanol', 'n2o', 'f2o', 'cf', 'o3', 'becl2', 'alcl', 'hoo', 'ph3', 's2o', 'propyne', 'cl', 'no', 'dioxirane', 'f2', 'bn3pi', 't-n2h2', 'ch2ch', 'cl2', 'bhf2', 'ssh', 'ch3nh2', 'so', 'hof', 'hcl', 'bh3', 'ch4', 'f2co', 'p2', 'ch3', 'ch2nh', 'oclo', 'hnc', 'ocs', 'n2h4', 'nh2', 'bn', 'sif', 'alf', 'clo', 'clcn', 'si', 'alcl3', 'c-hooo', 'ch3f', 'n2h', 'h2o', 'cf4', 'nh', 'c-hcoh', 'oxirane', 'b2h6', 'al', 'cs', 'h2', 'sih3f', 'b', 'ch2nh2', 'h2co', 'n', 'sif4', 'so2', 'hs', 'of', 'hccf', 'cl2o', 's4-c2v', 'cn', 't-hooo', 'allene', 'acetaldehyde', 'cch', 'hno', 'bef2', 'h2s', 'c2h5f', 'propene', 'clf', 'o2', 'o', 's', 'be2', 'nh3', 'oh', 'p', 'b2', 'hnco', 'sih4', 'bh', 'fo2', 'co', 'foof', 'ch2-sing', 'ch2f2', 'hf', 'fccf', 'si2h6', 'h', 's3', 'so3', 'c', 'ccl2', 'sih', 'ketene', 'alf3', 'no2', 'h2cn', 'c-n2h2', 'hooh', 't-hcoh', 'acetic', 'cloo', 'hcof', 'c-hono', 'cf2', 'nccn', 'be', 'bf3', 'ch2c', 'formic', 'sio', 'hco', 'c2h6', 'nh2cl']
        self.exp_values = {'0': 109.493, '1': 213.169, '2': 73.570, '3': 324.945, '4': 281.287, '5': 84.995, '6': 190.745, '7': 73.921, '8': 535.885, '9': 307.870, '10': 420.420, '11': 607.023, '12': 382.753, '13': 242.267, '14': 713.080, '15': 1007.909, '16': 181.456, '17': 84.221, '18': 183.913, '19': 87.731, '20': 721.502, '21': 582.301, '22': 422.959, '23': 861.578, '24': 298.018, '25': 811.241, '26': 474.629, '27': 564.095, '28': 513.501, '29': 107.499, '30': 182.591, '31': 83.096, '32': 482.276, '33': 410.973, '34': 232.974, '35': 141.640, '36': 446.081, '37': 107.208, '38': 705.605, '39': 677.864, '40': 704.100, '41': 577.780, '42': 470.973, '43': 573.892, '44': 651.526, '45': 437.668, '46': 430.967, '47': 309.099, '48': 359.934, '49': 438.281, '50': 439.441, '51': 163.780, '52': 804.017, '53': 405.525, '54': 374.658, '55': 343.749, '56': 182.517, '57': 225.274, '58': 322.477, '59': 312.651, '60': 317.647, '61': 122.618, '62': 533.462, '63': 142.710, '64': 501.899, '65': 336.249, '66': 635.101, '67': 403.743, '68': 248.059, '69': 478.760, '70': 398.472, '71': 313.418, '72': 298.203, '73': 266.163, '74': 279.422, '75': 259.727, '76': 456.072, '77': 420.636, '78': 410.066, '79': 269.089, '80': 296.534, '81': 434.737, '82': 291.135, '83': 258.782, '84': 390.141, '85': 386.087, '86': 410.029, '87': 132.721, '88': 165.128, '89': 166.229, '90': 502.037, '91': 228.485, '92': 224.864, '93': 335.747, '94': 193.052, '95': 285.447, '96': 175.533, '97': 364.971, '98': 350.149, '99': 205.890, '100': 158.653, '101': 312.219, '102': 312.649, '103': 280.778, '104': 331.785, '105': 172.218, '106': 181.350, '107': 346.943, '108': 177.357, '109': 105.815, '110': 260.621, '111': 152.745, '112': 126.465, '113': 270.849, '114': 233.089, '115': 104.251, '116': 290.578, '117': 59.750, '118': 120.824, '119': 39.042, '120': 233.297, '121': 208.781, '122': 117.593, '123': 62.800, '124': 227.882, '125': 65.447, '126': 168.364, '127': 101.457, '128': 234.348, '129': 53.075, '130': 147.023, '131': 128.120, '132': 93.780, '133': 67.459, '134': 134.721, '135': 126.385, '136': 152.369, '137': 147.428, '138': 105.239, '139': 2.669}
        self.testset_calculations = {'0': "-1 * ['h2'] +2 * ['h']",
              '1': "-1 * ['alh3'] +1 * ['al'] +3 * ['h']",
              '2': "-1 * ['alh'] +1 * ['al'] +1 * ['h']",
              '3': "-1 * ['sih4'] +1 * ['si'] +4 * ['h']",
              '4': "-1 * ['bh3'] +1 * ['b'] +3 * ['h']",
              '5': "-1 * ['bh'] +1 * ['b'] +1 * ['h']",
              '6': "-1 * ['ch2-trip'] +1 * ['c'] +2 * ['h']",
              '7': "-1 * ['sih'] +1 * ['si'] +1 * ['h']",
              '8': "-1 * ['si2h6'] +2 * ['si'] +6 * ['h']",
              '9': "-1 * ['ch3'] +1 * ['c'] +3 * ['h']",
              '10': "-1 * ['ch4'] +1 * ['c'] +4 * ['h']",
              '11': "-1 * ['b2h6'] +2 * ['b'] +6 * ['h']",
              '12': "-1 * ['sih3f'] +1 * ['si'] +3 * ['h'] +1 * ['f']",
              '13': "-1 * ['ph3'] +1 * ['p'] +3 * ['h']",
              '14': "-1 * ['c2h6'] +2 * ['c'] +6 * ['h']",
              '15': "-1 * ['propane'] +3 * ['c'] +8 * ['h']",
              '16': "-1 * ['ch2-sing'] +1 * ['c'] +2 * ['h']",
              '17': "-1 * ['ch'] +1 * ['c'] +1 * ['h']",
              '18': "-1 * ['h2s'] +2 * ['h'] +1 * ['s']",
              '19': "-1 * ['hs'] +1 * ['h'] +1 * ['s']",
              '20': "-1 * ['c2h5f'] +2 * ['c'] +5 * ['h'] +1 * ['f']",
              '21': "-1 * ['ch3nh2'] +1 * ['c'] +1 * ['n'] +5 * ['h']",
              '22': "-1 * ['ch3f'] +1 * ['c'] +1 * ['f'] +3 * ['h']",
              '23': "-1 * ['propene'] +3 * ['c'] +6 * ['h']",
              '24': "-1 * ['nh3'] +1 * ['n'] +3 * ['h']",
              '25': "-1 * ['ethanol'] +2 * ['c'] +1 * ['o'] +6 * ['h']",
              '26': "-1 * ['ch3nh'] +1 * ['c'] +1 * ['n'] +4 * ['h']",
              '27': "-1 * ['c2h4'] +2 * ['c'] +4 * ['h']",
              '28': "-1 * ['methanol'] +1 * ['c'] +1 * ['o'] +4 * ['h']",
              '29': "-1 * ['hcl'] +1 * ['h'] +1 * ['cl']",
              '30': "-1 * ['nh2'] +1 * ['n'] +2 * ['h']",
              '31': "-1 * ['nh'] +1 * ['n'] +1 * ['h']",
              '32': "-1 * ['ch2nh2'] +1 * ['c'] +1 * ['n'] +4 * ['h']",
              '33': "-1 * ['bhf2'] +1 * ['b'] +1 * ['h'] +2 * ['f']",
              '34': "-1 * ['h2o'] +2 * ['h'] +1 * ['o']",
              '35': "-1 * ['hf'] +1 * ['h'] +1 * ['f']",
              '36': "-1 * ['ch2ch'] +2 * ['c'] +3 * ['h']",
              '37': "-1 * ['oh'] +1 * ['o'] +1 * ['h']",
              '38': "-1 * ['propyne'] +3 * ['c'] +4 * ['h']",
              '39': "-1 * ['acetaldehyde'] +2 * ['c'] +1 * ['o'] +4 * ['h']",
              '40': "-1 * ['allene'] +3 * ['c'] +4 * ['h']",
              '41': "-1 * ['sif4'] +1 * ['si'] +4 * ['f']",
              '42': "-1 * ['bf3'] +1 * ['b'] +3 * ['f']",
              '43': "-1 * ['c2h3f'] +2 * ['c'] +1 * ['f'] +3 * ['h']",
              '44': "-1 * ['oxirane'] +2 * ['c'] +1 * ['o'] +4 * ['h']",
              '45': "-1 * ['ch2f2'] +1 * ['c'] +2 * ['f'] +2 * ['h']",
              '46': "-1 * ['alf3'] +1 * ['al'] +3 * ['f']",
              '47': "-1 * ['bef2'] +1 * ['be'] +2 * ['f']",
              '48': "-1 * ['ch2c'] +2 * ['c'] +2 * ['h']",
              '49': "-1 * ['n2h4'] +4 * ['h'] +2 * ['n']",
              '50': "-1 * ['ch2nh'] +1 * ['c'] +1 * ['n'] +3 * ['h']",
              '51': "-1 * ['alf'] +1 * ['al'] +1 * ['f']",
              '52': "-1 * ['acetic'] +2 * ['c'] +2 * ['o'] +4 * ['h']",
              '53': "-1 * ['c2h2'] +2 * ['c'] +2 * ['h']",
              '54': "-1 * ['h2co'] +2 * ['h'] +1 * ['c'] +1 * ['o']",
              '55': "-1 * ['h2cn'] +2 * ['h'] +1 * ['c'] +1 * ['n']",
              '56': "-1 * ['bf'] +1 * ['b'] +1 * ['f']",
              '57': "-1 * ['becl2'] +1 * ['be'] +2 * ['cl']",
              '58': "-1 * ['t-hcoh'] +1 * ['c'] +1 * ['o'] +2 * ['h']",
              '59': "-1 * ['alcl3'] +1 * ['al'] +3 * ['cl']",
              '60': "-1 * ['c-hcoh'] +1 * ['c'] +1 * ['o'] +2 * ['h']",
              '61': "-1 * ['alcl'] +1 * ['al'] +1 * ['cl']",
              '62': "-1 * ['ketene'] +2 * ['c'] +1 * ['o'] +2 * ['h']",
              '63': "-1 * ['sif'] +1 * ['si'] +1 * ['f']",
              '64': "-1 * ['formic'] +1 * ['c'] +2 * ['o'] +2 * ['h']",
              '65': "-1 * ['hcnh'] +1 * ['c'] +1 * ['n'] +2 * ['h']",
              '66': "-1 * ['glyoxal'] +2 * ['c'] +2 * ['o'] +2 * ['h']",
              '67': "-1 * ['hcof'] +1 * ['c'] +1 * ['o'] +1 * ['f'] +1 * ['h']",
              '68': "-1 * ['nh2cl'] +1 * ['n'] +1 * ['cl'] +2 * ['h']",
              '69': "-1 * ['cf4'] +1 * ['c'] +4 * ['f']",
              '70': "-1 * ['hccf'] +2 * ['c'] +1 * ['f'] +1 * ['h']",
              '71': "-1 * ['hcn'] +1 * ['h'] +1 * ['c'] +1 * ['n']",
              '72': "-1 * ['hnc'] +1 * ['h'] +1 * ['c'] +1 * ['n']",
              '73': "-1 * ['cch'] +2 * ['c'] +1 * ['h']",
              '74': "-1 * ['hco'] +1 * ['h'] +1 * ['c'] +1 * ['o']",
              '75': "-1 * ['co'] +1 * ['c'] +1 * ['o']",
              '76': "-1 * ['oxirene'] +2 * ['c'] +1 * ['o'] +2 * ['h']",
              '77': "-1 * ['f2co'] +1 * ['c'] +1 * ['o'] +2 * ['f']",
              '78': "-1 * ['hocn'] +1 * ['c'] +1 * ['o'] +1 * ['n'] +1 * ['h']",
              '79': "-1 * ['hooh'] +2 * ['h'] +2 * ['o']",
              '80': "-1 * ['t-n2h2'] +2 * ['h'] +2 * ['n']",
              '81': "-1 * ['hnco'] +1 * ['c'] +1 * ['o'] +1 * ['n'] +1 * ['h']",
              '82': "-1 * ['c-n2h2'] +2 * ['h'] +2 * ['n']",
              '83': "-1 * ['cf2'] +1 * ['c'] +2 * ['f']",
              '84': "-1 * ['co2'] +1 * ['c'] +2 * ['o']",
              '85': "-1 * ['fccf'] +2 * ['c'] +2 * ['f']",
              '86': "-1 * ['dioxirane'] +1 * ['c'] +2 * ['o'] +2 * ['h']",
              '87': "-1 * ['cf'] +1 * ['c'] +1 * ['f']",
              '88': "-1 * ['ssh'] +2 * ['s'] +1 * ['h']",
              '89': "-1 * ['hocl'] +1 * ['h'] +1 * ['o'] +1 * ['cl']",
              '90': "-1 * ['nccn'] +2 * ['n'] +2 * ['c']",
              '91': "-1 * ['n2'] +2 * ['n']",
              '92': "-1 * ['n2h'] +2 * ['n'] +1 * ['h']",
              '93': "-1 * ['ocs'] +1 * ['o'] +1 * ['c'] +1 * ['s']",
              '94': "-1 * ['sio'] +1 * ['si'] +1 * ['o']",
              '95': "-1 * ['clcn'] +1 * ['cl'] +1 * ['c'] +1 * ['n']",
              '96': "-1 * ['hoo'] +1 * ['h'] +2 * ['o']",
              '97': "-1 * ['hcno'] +1 * ['c'] +1 * ['o'] +1 * ['n'] +1 * ['h']",
              '98': "-1 * ['honc'] +1 * ['c'] +1 * ['o'] +1 * ['n'] +1 * ['h']",
              '99': "-1 * ['hno'] +1 * ['h'] +1 * ['n'] +1 * ['o']",
              '100': "-1 * ['hof'] +1 * ['h'] +1 * ['o'] +1 * ['f']",
              '101': "-1 * ['c-hono'] +1 * ['h'] +1 * ['n'] +2 * ['o']",
              '102': "-1 * ['t-hono'] +1 * ['h'] +1 * ['n'] +2 * ['o']",
              '103': "-1 * ['cs2'] +1 * ['c'] +2 * ['s']",
              '104': "-1 * ['hnnn'] +1 * ['h'] +3 * ['n']",
              '105': "-1 * ['cs'] +1 * ['c'] +1 * ['s']",
              '106': "-1 * ['cn'] +1 * ['c'] +1 * ['n']",
              '107': "-1 * ['so3'] +1 * ['s'] +3 * ['o']",
              '108': "-1 * ['ccl2'] +1 * ['c'] +2 * ['cl']",
              '109': "-1 * ['bn3pi'] +1 * ['b'] +1 * ['n']",
              '110': "-1 * ['so2'] +1 * ['s'] +2 * ['o']",
              '111': "-1 * ['no'] +1 * ['n'] +1 * ['o']",
              '112': "-1 * ['so'] +1 * ['s'] +1 * ['o']",
              '113': "-1 * ['n2o'] +2 * ['n'] +1 * ['o']",
              '114': "-1 * ['c-hooo'] +1 * ['h'] +3 * ['o']",
              '115': "-1 * ['s2'] +2 * ['s']",
              '116': "-1 * ['p4'] +4 * ['p']",
              '117': "-1 * ['cl2'] +2 * ['cl']",
              '118': "-1 * ['o2'] +2 * ['o']",
              '119': "-1 * ['f2'] +2 * ['f']",
              '120': "-1 * ['t-hooo'] +1 * ['h'] +3 * ['o']",
              '121': "-1 * ['s2o'] +2 * ['s'] +1 * ['o']",
              '122': "-1 * ['p2'] +2 * ['p']",
              '123': "-1 * ['clf'] +1 * ['cl'] +1 * ['f']",
              '124': "-1 * ['no2'] +1 * ['n'] +2 * ['o']",
              '125': "-1 * ['clo'] +1 * ['cl'] +1 * ['o']",
              '126': "-1 * ['s3'] +3 * ['s']",
              '127': "-1 * ['cl2o'] +2 * ['cl'] +1 * ['o']",
              '128': "-1 * ['s4-c2v'] +4 * ['s']",
              '129': "-1 * ['of'] +1 * ['o'] +1 * ['f']",
              '130': "-1 * ['c2'] +2 * ['c']",
              '131': "-1 * ['oclo'] +2 * ['o'] +1 * ['cl']",
              '132': "-1 * ['f2o'] +2 * ['f'] +1 * ['o']",
              '133': "-1 * ['b2'] +2 * ['b']",
              '134': "-1 * ['fo2'] +1 * ['f'] +2 * ['o']",
              '135': "-1 * ['cloo'] +1 * ['cl'] +2 * ['o']",
              '136': "-1 * ['foof'] +2 * ['f'] +2 * ['o']",
              '137': "-1 * ['o3'] +3 * ['o']",
              '138': "-1 * ['bn'] +1 * ['b'] +1 * ['n']",
              '139': "-1 * ['be2'] +2 * ['be']"}
        self.charges = {'hcn': 0.0, 'n2': 0.0, 'hocl': 0.0, 'hcno': 0.0, 'methanol': 0.0, 'ch2-trip': 0.0, 'honc': -0.0, 'hocn': -0.0, 'alh': -0.0, 'p4': -0.0, 't-hono': 0.0, 'oxirene': 0.0, 'hnnn': -0.0, 'c2h3f': 0.0, 'c2h2': 0.0, 'bf': 0.0, 'alh3': -0.0, 'co2': -0.0, 'f': -0.0, 'c2': 0.0, 'hcnh': 0.0, 'cs2': 0.0, 'ch3nh': 0.0, 'glyoxal': 0.0, 'c2h4': 0.0, 'propane': 0.0, 's2': -0.0, 'ch': -0.0, 'ethanol': 0.0, 'n2o': -0.0, 'f2o': -0.0, 'cf': 0.0, 'o3': -0.0, 'becl2': -0.0, 'alcl': 0.0, 'hoo': 0.0, 'ph3': -0.0, 's2o': 0.0, 'propyne': -0.0, 'cl': -0.0, 'no': 0.0, 'dioxirane': -0.0, 'f2': -0.0, 'bn3pi': 0.0, 't-n2h2': 0.0, 'ch2ch': 0.0, 'cl2': -0.0, 'bhf2': 0.0, 'ssh': -0.0, 'ch3nh2': 0.0, 'so': 0.0, 'hof': -0.0, 'hcl': -0.0, 'bh3': -0.0, 'ch4': -0.0, 'f2co': 0.0, 'p2': -0.0, 'ch3': 0.0, 'ch2nh': 0.0, 'oclo': -0.0, 'hnc': 0.0, 'ocs': -0.0, 'n2h4': 0.0, 'nh2': -0.0, 'bn': 0.0, 'sif': -0.0, 'alf': -0.0, 'clo': -0.0, 'clcn': 0.0, 'si': -0.0, 'alcl3': 0.0, 'c-hooo': 0.0, 'ch3f': 0.0, 'n2h': 0.0, 'h2o': -0.0, 'cf4': 0.0, 'nh': -0.0, 'c-hcoh': 0.0, 'oxirane': 0.0, 'b2h6': 0.0, 'al': 0.0, 'cs': -0.0, 'h2': 0.0, 'sih3f': 0.0, 'b': -0.0, 'ch2nh2': -0.0, 'h2co': 0.0, 'n': -0.0, 'sif4': 0.0, 'so2': -0.0, 'hs': -0.0, 'of': -0.0, 'hccf': -0.0, 'cl2o': 0.0, 's4-c2v': -0.0, 'cn': 0.0, 't-hooo': 0.0, 'allene': 0.0, 'acetaldehyde': -0.0, 'cch': -0.0, 'hno': 0.0, 'bef2': 0.0, 'h2s': -0.0, 'c2h5f': 0.0, 'propene': 0.0, 'clf': -0.0, 'o2': 0.0, 'o': -0.0, 's': -0.0, 'be2': 0.0, 'nh3': -0.0, 'oh': 0.0, 'p': -0.0, 'b2': 0.0, 'hnco': -0.0, 'sih4': -0.0, 'bh': 0.0, 'fo2': 0.0, 'co': -0.0, 'foof': 0.0, 'ch2-sing': -0.0, 'ch2f2': 0.0, 'hf': 0.0, 'fccf': -0.0, 'si2h6': -0.0, 'h': 0.0, 's3': -0.0, 'so3': -0.0, 'c': -0.0, 'ccl2': -0.0, 'sih': -0.0, 'ketene': -0.0, 'alf3': -0.0, 'no2': -0.0, 'h2cn': 0.0, 'c-n2h2': 0.0, 'hooh': -0.0, 't-hcoh': 0.0, 'acetic': -0.0, 'cloo': -0.0, 'hcof': 0.0, 'c-hono': 0.0, 'cf2': 0.0, 'nccn': 0.0, 'be': 0.0, 'bf3': 0.0, 'ch2c': 0.0, 'formic': 0.0, 'sio': -0.0, 'hco': 0.0, 'c2h6': 0.0, 'nh2cl': 0.0}
    