#!/usr/bin/python3

class Laternfish:
    def __init__(self):
        self.fish = self._parse_input()
        
    def _parse_input(self):
        with open('data/day6.txt', 'r') as infile:
            return [int(num) for num in infile.read().rstrip().split(',')]
            
    def mult_fish(self, days):
        for day in range(days):
            new_fish = []
            for index in range(len(self.fish)):
                if self.fish[index] == 0:
                    self.fish[index] = 6
                    new_fish.append(8)
                else:
                    self.fish[index] -= 1
            self.fish += new_fish
            
if __name__ == '__main__':
    LF = Laternfish()
    LF.mult_fish(256)
    print(len(LF.fish))