#!/usr/bin/python3

class Cave:
    def __init__(self):
        self.puzzle = self._parse_input()
        self.lows = []
        self.risk = 0
        
    def _parse_input(self):
        with open('data/day9.txt', 'r') as infile:
            return [line.rstrip() for line in infile.readlines()]
            
    def get_nums(self, index1, index2):
        test = self.puzzle[index1][index2]
        
        try:
            left = self.puzzle[index1][index2-1]
        except IndexError:
            left = 10
            
        try:
            right = self.puzzle[index1][index2+1]
        except IndexError:
            right = 10       
            
        try:
            up = self.puzzle[index1-1][index2]
        except IndexError:
            up = 10

        try:
            down = self.puzzle[index1+1][index2]
        except IndexError:
            down = 10
            
        return int(test), int(left), int(right), int(up), int(down)
        
    def is_low(self, test, left, right, up, down):
        if (test < left) and (test < right) and (test < up) and (test < down):
            return True
        else:
            return False
            
    def get_lows(self):
        for index1 in range(len(self.puzzle)):
            for index2 in range(len(self.puzzle[0])):
                test, left, right, up, down = self.get_nums(index1, index2)
                if self.is_low(test, left, right, up, down):
                    self.lows.append(test)
                    
    def calc_risk(self):
        for i in self.lows:
            self.risk += (i+1)
            

if __name__ == '__main__':
    C = Cave()
    C.get_lows()
    C.calc_risk()
    print(C.risk)