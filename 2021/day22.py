#!/usr/bin/python3

class Reactor:
    def __init__(self):
        self.puzzle = []
        self.on = []
        
    def _parse_input(self):
        with open('data/day22.txt', 'r') as infile:
            content = infile.read().rstrip()
            
        self.puzzle = [line.rstrip() for line in content.split('\n')]
        
    def parse_inst(self, inst):
        cmd = inst.split(' ')[0]
        coords = inst.split(' ')[1]
        x = coords.split(',')[0].split('=')[1].split('..')
        y = coords.split(',')[1].split('=')[1].split('..')
        z = coords.split(',')[2].split('=')[1].split('..')
        
        x = [int(x[0]), int(x[1])]
        y = [int(y[0]), int(y[1])]
        z = [int(z[0]), int(z[1])]
        
        return cmd, x, y, z
        
    def check_limit(self, coord):
        if (coord[0] <= 50) and (coord[0] >= -50) and (coord[1] <= 50) and (coord[1] >= -50):
            return True
        else:
            print(f'coord out of range: {coord}')
            return False
            
    def get_cubes(self, x, y, z):
        cubes = []
        if not (self.check_limit(x) and (self.check_limit(y)) and self.check_limit(z)):
            print('not getting cubes')
            return cubes
        
        for ix in range(x[0], x[1]+1):
            for iy in range(y[0], y[1]+1):
                for iz in range(z[0], z[1]+1):
                    cubes.append((ix,iy,iz))
                    
        return cubes
        
    def turn_on(self, cubes):
        self.on = list(set(cubes + self.on))
        
    def turn_off(self, cubes):
        self.on = list(set(self.on) - set(cubes))
        
    def reboot(self):
        self._parse_input()
        
        for inst in self.puzzle:
            cmd, x, y, z = self.parse_inst(inst)
            cubes = self.get_cubes(x, y, z)
            if cmd == 'on':
                self.turn_on(cubes)
            elif cmd == 'off':
                self.turn_off(cubes)
            else:
                print('Something wrong with cmd: {cmd}')
                
                
if __name__ == '__main__':
    R = Reactor()
    R.reboot()
    print(len(R.on))