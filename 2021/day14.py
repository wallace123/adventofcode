#!/usr/bin/python3
from collections import Counter

class Polymer:
    def __init__(self):
        self.template = ''
        self.rules = {}
        self.least = 0
        self.most = 0
        
    def _parse_input(self):
        with open('data/day14.txt', 'r') as infile:
            content = infile.read().rstrip().split('\n\n')
            
        self.template = content[0]
        
        rule = content[1].split('\n')
        for r in rule:
            data = r.rstrip().split(' -> ')
            self.rules[data[0]] = data[1]

    def pairs(self, pstr):
        pair_list = []
        
        for index in range(2, len(pstr)+1):
                pair_list.append(pstr[index-2:index])
                
        return pair_list
        
    def do_rules(self, plist):
        tstr = ''

        for pair in plist:
            tstr += pair[0] + self.rules[pair]
            
        return tstr + plist[-1][1]
        

    def grow(self, steps):
        self._parse_input()
        
        for i in range(steps):
            plist = self.pairs(self.template)
            self.template = self.do_rules(plist)
            
    def calc_ends(self):
        res = Counter(self.template)
        self.least = min(res, key = res.get)
        self.most = max(res, key = res.get)
        print(res[self.most] - res[self.least])
        
        
if __name__ == '__main__':
    P = Polymer()
    P.grow(40)
    print(len(P.template))
    P.calc_ends()