#!/usr/bin/python3

class Crabs:
    def __init__(self):
        self.puzzle = self._parse_input()
        self.fuel_list = []
        self.min_fuel = 0
        
    def _parse_input(self):
        with open('data/day7.txt', 'r') as infile:
            content = infile.read().rstrip()
            
        return [int(num) for num in content.split(',')]
        
    def find_pos(self):
        sum = 0
        for i in range(min(self.puzzle), max(self.puzzle)):
            for num in self.puzzle:
                sum += abs(num - i)
            self.fuel_list.append(sum)
            sum=0
            
        self.min_fuel = min(self.fuel_list)
        
    def find_pos2(self):
        sum = 0
        for i in range(min(self.puzzle), max(self.puzzle)):
            for num in self.puzzle:
                steps = abs(num - i)+1
                fuel = 0
                for f in range(steps):
                    fuel += f
                sum += fuel
            self.fuel_list.append(sum)
            sum = 0
            
        self.min_fuel = min(self.fuel_list)

        
if __name__ == '__main__':
    Crab1 = Crabs()
    Crab1.find_pos()
    print(Crab1.min_fuel)
    Crab2 = Crabs()
    Crab2.find_pos2()
    print(Crab2.min_fuel)