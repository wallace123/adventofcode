#!/usr/bin/python3
from collections import Counter

class Trench:
    def __init__(self):
        self.target_area = []
        self.x_range = (0, 0)
        self.y_range = (0, 0)
        self.hits = []
        self.heights = []
        
    def _parse_input(self):
        with open('data/day17.txt', 'r') as infile:
            content = infile.read().rstrip()
            
        content = content.split(':')
        vals = content[1].strip().split(',')
        x = vals[0].split('=')[1]
        y = vals[1].split('=')[1]
        xr = x.split('..')
        yr = y.split('..')
        self.x_range = (int(xr[0]), int(xr[1]))
        self.y_range = (int(yr[0]), int(yr[1]))
        
        for xi in range(self.x_range[0], self.x_range[1]+1):
            for yi in range(self.y_range[0], self.y_range[1]+1):
                self.target_area.append((xi, yi))

    def step(self, position, velocity):
        x = velocity[0]
        y = velocity[1]
        
        new_position = (position[0] + x, position[1] + y)
        
        if x > 0:
            new_x = x - 1
        elif x < 0:
            new_x = x + 1
        else:
            new_x = x

        new_y = y - 1
        
        new_velocity = (new_x, new_y)
        
        return new_position, new_velocity
        
    def hit(self, coord):
        if coord in self.target_area:
            return True
        else:
            return False
            
    def over(self, coord):
        x = coord[0]
        y = coord[1]
        
        if y < self.y_range[0]:
            return True
        
    def shoot(self, velocity):
        position = (0, 0)
        while 1:
            position, velocity = self.step(position, velocity)
            if self.hit(position):
                return True
            elif self.over(position):
                #print('over!')
                return False

    def get_height(self, velocity):
        position = (0, 0)
        prev_y = 0
        y = 1
        while y > prev_y:
            prev_y = position[1]
            position, velocity = self.step(position, velocity)
            y = position[1]
            self.heights.append(y)                    


if __name__ == '__main__':
    T = Trench()
    T._parse_input()
    for x in range(75):
        for y in range(-250, 350):
            if T.shoot((x, y)):
                T.hits.append((x, y))
    
    #day 1    
    #print(T.hits)
    #for hit in T.hits:
    #    T.get_height(hit)
    #print(max(Counter(T.heights)))
    
    # day 2
    print(len(T.hits))