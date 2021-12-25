#!/usr/bin/python3
from itertools import cycle

class Dirac:
    def __init__(self):
        self.p1_space = cycle(range(1, 11))
        self.p2_space = cycle(range(1, 11))
        self.p1_score = 0
        self.p2_score = 0
        self.rolls = 0
        self.dice = cycle(range(1, 101))
        self.turn = 1
        
    def initial_space(self):
        with open('data/day21.txt', 'r') as infile:
            content = infile.readlines()

        nums = []
        for line in content:
            nums.append(int(line.split(':')[1].strip()))
            
        for _ in range(nums[0]):
            next(self.p1_space)
            
        for _ in range(nums[1]):
            next(self.p2_space)
    
    def roll(self):
        self.rolls += 3
        return next(self.dice) + next(self.dice) + next(self.dice)
            
        
    def game(self):
        self.initial_space()
        move = 0
        while (self.p1_score < 1000) and (self.p2_score < 1000):
            move = self.roll()
            if (self.turn % 2) == 0:
                for _ in range(move):
                    val = next(self.p2_space)
                self.p2_score += val
                #print(f'P2 {self.p2_score}')
            else:
                for _ in range(move):
                    val = next(self.p1_space)
                self.p1_score += val
                #print(f'P1 {self.p1_score}')
            self.turn += 1

        if self.p1_score < self.p2_score:
            print(self.p1_score * self.rolls)
        else:
            print(self.p2_score * self.rolls)        
        

if __name__ == '__main__':
    D = Dirac()
    D.game()
    print(D.p1_score)
    print(D.p2_score)
    print(D.rolls)
    
        
        