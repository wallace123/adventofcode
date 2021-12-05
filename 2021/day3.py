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
        most_common = occurence_count.most_common()
        if (len(most_common) > 1) and (most_common[0][1] == most_common[1][1]):
            return '1'
        else:
            return occurence_count.most_common(1)[0][0]
        
    def least_frequent(self, plist):
        occurence_count = Counter(plist)
        most_common = occurence_count.most_common()
        if (len(most_common) > 1) and (most_common[0][1] == most_common[1][1]):
            return '0'
        else:
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
        
        
class Submarine2(Submarine):
    def __init__(self):
        self.puzzle = self._parse_data()
        self.oxygen = 0
        self.co2 = 0
        self.lifesupport = 0
        
    def calc_oxygen(self):
        tmp_list = self.puzzle.copy()
        del_list = []
        for index in range(len(self.puzzle[0])):
            mf = self.most_frequent(self.column(tmp_list, index))
            for item in tmp_list:
                if item[index] != mf:
                    del_list.append(item)
            for item in del_list:
                tmp_list.remove(item)
            del_list = []
            if len(tmp_list) == 1:
                break
                
        self.oxygen = int(tmp_list[0], 2)
        
    def calc_co2(self):
        tmp_list = self.puzzle.copy()
        del_list = []
        for index in range(len(self.puzzle[0])):
            lf = self.least_frequent(self.column(tmp_list, index))
            for item in tmp_list:
                if item[index] != lf:
                    del_list.append(item)
            for item in del_list:
                tmp_list.remove(item)
            del_list = []
            if len(tmp_list) == 1:
                break
   
        self.co2 = int(tmp_list[0], 2)
        
    def calc_lifesupport(self):
        self.calc_oxygen()
        self.calc_co2()
        self.lifesupport = self.oxygen * self.co2
        

if __name__ == '__main__':
    One = Submarine()
    One.calc_powercon()
    print(One.power_consumption)
    
    Two = Submarine2()
    Two.calc_lifesupport()
    print(Two.lifesupport)