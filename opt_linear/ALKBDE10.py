from testsetclass import TestsetClass


class ALKBDE10(TestsetClass):
    def __init__(self):
        self.weak = 1.0
        self.molecules = ['cao', 'be', 'lio', 'mg', 'na', 'lif', 'ca', 'nao', 's', 'f', 'o', 'h', 'mgo', 'mgs', 'hf', 'kf', 'beo', 'bef', 'li', 'k']
        self.exp_values = {'0': 138.7, '1': 106.6, '2': 96.2, '3': 142.1, '4': 117.5, '5': 139.2, '6': 82.5, '7': 62.2, '8': 56.7, '9': 65.2}
        self.testset_calculations = {'0': "-1 * ['bef'] +1 * ['be'] +1 * ['f']",
              '1': "-1 * ['beo'] +1 * ['be'] +1 * ['o']",
              '2': "-1 * ['cao'] +1 * ['ca'] +1 * ['o']",
              '3': "-1 * ['hf'] +1 * ['h'] +1 * ['f']",
              '4': "-1 * ['kf'] +1 * ['k'] +1 * ['f']",
              '5': "-1 * ['lif'] +1 * ['li'] +1 * ['f']",
              '6': "-1 * ['lio'] +1 * ['li'] +1 * ['o']",
              '7': "-1 * ['mgo'] +1 * ['mg'] +1 * ['o']",
              '8': "-1 * ['mgs'] +1 * ['mg'] +1 * ['s']",
              '9': "-1 * ['nao'] +1 * ['na'] +1 * ['o']"}
        self.charges = {'cao': 0.0, 'be': 0.0, 'lio': -0.0, 'mg': -0.0, 'na': -0.0, 'lif': 0.0, 'ca': 0.0, 'nao': 0.0, 's': -0.0, 'f': -0.0, 'o': -0.0, 'h': -0.0, 'mgo': -0.0, 'mgs': -0.0, 'hf': 0.0, 'kf': -0.0, 'beo': 0.0, 'bef': 0.0, 'li': -0.0, 'k': 0.0}
    