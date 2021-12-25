#!/usr/bin/python3

class Dirac:
    def __init__(self):
        self.p1_space = 4
        self.p2_space = 8
        self.p1_score = 0
        self.p2_score = 0
        self.rolls = 0
        self.dice = 0
        self.turn = 1
        
    def roll(self):
        one = 0
        two = 0
        three = 0
        if self.dice + 1 < 100:
            one = self.dice + 1
            self.dice += 1
        else:
            self.dice = 1
            one = self.dice
            
        if self.dice + 1 < 100:
            two = self.dice + 1
            self.dice += 1
        else:
            self.dice = 1
            two = self.dice
            
        if self.dice + 1 < 100:
            three = self.dice + 1
            self.dice += 1
        else:
            self.dice = 1
            three = self.dice
            
        self.rolls += 1
            
        return one + two + three
            
        
    def game(self):
        move = 0
        while (self.p1_score < 1000) or (self.p2_score < 1000):
            move = self.roll()
            if (self.turn % 2) == 0:
                self.p2_space += move
                if (self.p2_space % 10) == 0:
                    self.p2_space = 10
                else:
                    self.p2_space %= 10
                self.p2_score += self.p2_space
            else:
                self.p1_space += move
                if (self.p1_space % 10) == 0:
                    self.p1_space = 10
                else:
                    self.p1_space %= 10
                self.p1_score += self.p2_space
            self.turn += 1
            
        

if __name__ == '__main__':
    D = Dirac()
    D.game()
    print(D.p1_score)
    print(D.p2_score)    
    print(D.rolls)
        
        