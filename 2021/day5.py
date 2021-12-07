#!/usr/bin/python3
from collections import Counter

class Hydrovents:
    def __init__(self):
        self.puzzle = self._parse_input()
        self.hvlines = []
        self.line_coords = []
        
    def _parse_input(self):
        with open('data/day5.txt', 'r') as infile:
            lines = infile.readlines()
            
        lines = [line.rstrip() for line in lines]
        lines = [line.split(' -> ') for line in lines]
        lines = [item for item in lines]
        
        tmp_list = []
        for coords in lines:
            x1 = int(coords[0].split(',')[0])
            x2 = int(coords[1].split(',')[0])
            y1 = int(coords[0].split(',')[1])
            y2 = int(coords[1].split(',')[1])
            tmp_list.append([(x1, y1), (x2, y2)])
        return tmp_list
        
    def get_horizontal_vertical(self):
        for coords in self.puzzle:
            x1 = coords[0][0]
            x2 = coords[1][0]
            y1 = coords[0][1]
            y2 = coords[1][1]
            if (x1 == x2) or (y1 == y2):
                self.hvlines.append(coords)
                
    def get_line_coords(self):
        self.get_horizontal_vertical()
        for coords in self.hvlines:
            x1 = coords[0][0]
            x2 = coords[1][0]
            y1 = coords[0][1]
            y2 = coords[1][1]
            dx = x2 - x1
            dy = y2 - y1
            inc = 0
            new_coord = coords[0]
            if dx != 0:
                if dx < 0:
                    step = -1
                else:
                    step = 1
                for index in range(0, dx, step):
                    new_coord = (x1+index, y1)
                    self.line_coords.append(new_coord)
            if dy != 0:
                if dy < 0:
                    step = -1
                else:
                    step = 1
                for index in range(0, dy, step):
                    new_coord = (x1, y1+index)
                    self.line_coords.append(new_coord)
            self.line_coords.append(coords[1])
            
if __name__ == '__main__':
    HV = Hydrovents()
    HV.get_line_coords()
    print(HV.hvlines)
    count = Counter(HV.line_coords)
    #print(count)
    mto = 0
    #print(count.values())
    for num in count.values():
        if num > 1:
            mto += 1
            
    print(mto)