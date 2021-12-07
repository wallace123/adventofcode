#!/usr/bin/python3
import matplotlib.pyplot as plt

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
    for i in range(256):
        LF.mult_fish(i)
        print(f'Day {i+1} - {len(LF.fish)}')
        LF.fish = Laternfish._parse_input(LF)
        