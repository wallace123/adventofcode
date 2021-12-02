#!/usr/bin/python3

class Submarine:
    def __init__(self):
        self.position = [0, 0]
        self.instructions = []
        
    def forward(self, val):
        self.position[0] += val
        
    def backward(self, val):
        self.position[0] -= val
        
    def up(self, val):
        self.position[1] -= val
        
    def down(self, val):
        self.position[1] += val
        
    def result(self):
        print(self.position[0] * self.position[1])
        
    def _parse_instructions(self, infile):
        with open(infile, 'r') as ins:
            lines = ins.readlines()
            
        for line in lines:
            coord = line.split(' ')
            direction = coord[0]
            val = int(coord[1].strip())
            self.instructions.append((direction, val))
            
    def move(self, infile):
        self._parse_instructions(infile)
        for coord in self.instructions:
            code = 'self.' + coord[0] + '(%s)' % coord[1]
            eval(code)
            
class Submarine2(Submarine):
    def __init__(self):
        self.position = [0, 0]
        self.instructions = []
        self.aim = 0
        
    def forward(self, val):
        self.position[0] += val
        self.position[1] += (val * self.aim)
        
    def down(self, val):
        self.aim += val
        
    def up(self, val):
        self.aim -= val

            
if __name__ == "__main__":
    One = Submarine()
    One.move('data/day2.txt')
    One.result()
    
    Two = Submarine2()
    Two.move('data/day2.txt')
    Two.result()