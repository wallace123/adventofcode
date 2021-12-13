#!/usr/bin/python3

class Paper:
    def __init__(self):
        self.dots = []
        self.folds = []
        
    def _parse_input(self):
        with open('data/day13.txt', 'r') as infile:
            content = infile.read().split('\n\n')
            
        temp = [line.rstrip() for line in content[0].split('\n')]
        for coord in temp:
            vals = coord.split(',')
            self.dots.append((int(vals[0]), int(vals[1])))
            
        temp = [line.rstrip() for line in content[1].split('\n')]
        #del temp[-1]
        for coord in temp:
            vals = coord.split('=')
            self.folds.append((vals[0][-1], int(vals[1])))
            
    def calc_fold(self, d, val):
        temp = []
        for coord in self.dots:
            if d == 'y':
                if coord[1] > val:
                    diff = coord[1] - val
                    new_val = val - diff
                    new_coord = (coord[0], new_val)
                    if new_coord not in self.dots:
                        temp.append(new_coord)
                else:
                    temp.append(coord)
            if d == 'x':
                if coord[0] > val:
                    diff = coord[0] - val
                    new_val = val - diff
                    new_coord = (new_val, coord[1])
                    if new_coord not in self.dots:
                        temp.append(new_coord)
                else:
                    temp.append(coord)
                        
        return temp
        
    def fold(self, times):
        self._parse_input()
        for index in range(times):
            ins = self.folds[index]
            d = ins[0]
            val = ins[1]
            temp = self.calc_fold(d, val)
            
            self.dots = []
            for coord in temp:
                self.dots.append(coord)
                
        self.dots.sort()
        
    def print_paper(self):
        line = ''
        for y in range(self.dots[-1][1]+1):
            for x in range(self.dots[-1][0]+1):
                if (x, y) in self.dots:
                    line += '#'
                else:
                    line += ' '
            print(line)
            line = ''
            

if __name__ == '__main__':
    P = Paper()
    P.fold(12)
    P.print_paper()
    print(len(P.dots))