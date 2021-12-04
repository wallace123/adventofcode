#!/usr/bin/python3
from collections import Counter

class Submarine:
    def __init__(self):
        self.puzzle = self._parse_data()
        self.gama = 0
        self.epsilon = 0
        self.power_consuption = 0
        
    def _parse_data(self):
        with open('data/day3.txt', 'r') as ins:
            content = ins.readlines()
            
        return [line.strip() for line in content]
        
    def column(self, matrix, i):
        return [row[i] for row in matrix]
        
    def most_frequent(self, plist):
        occurence_count = Counter(plist)
        return occurence_count.most_common(1)[0][0]
        
    def least_frequent(self, plist):
        occurence_count = Counter(plist)
        return occurence_count.most_common()[1][0]
        
    def calc_gama(self):
        tmp = ''
        for index in range(len(self.puzzle[0])):
            tmp += self.most_frequent(self.column(self.puzzle, index))
            
        self.gama = int(tmp, 2)
        
    def calc_epsilon(self):
        tmp = ''
        for index in range(len(self.puzzle[0])):
            tmp += self.least_frequent(self.column(self.puzzle, index))
            
        self.epsilon = int(tmp, 2)
        
    def calc_powercon(self):
        self.calc_gama()
        self.calc_epsilon()
        self.power_consumption = self.gama * self.epsilon
        

if __name__ == '__main__':
    One = Submarine()
    One.calc_powercon()
    print(One.power_consumption)