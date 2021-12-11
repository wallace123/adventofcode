#!/usr/bin/python3

class Nav:
    def __init__(self):
        self.puzzle = self._parse_input()
        self.complete = []
        self.start = '<{[('
        self.close = '>}])'
        self.illegals = []
        self.score = 0
        
    def _parse_input(self):
        with open('data/day10.txt', 'r') as infile:
            content = [line.rstrip() for line in infile.readlines()]

        temp = []
        for line in content:
            temp.append([char for char in line])
            
        return temp

    def get_complete(self):
        for line in self.puzzle:
            if line[-1] in self.close:
                self.complete.append(line)            
            
    def is_match(self, close, start):
        if (close == '>') and (start == '<'):
            return True
        elif (close == ')') and (start == '('):
            return True
        elif (close == '}') and (start == '{'):
            return True
        elif (close == ']') and (start == '['):
            return True
        else:
            return False
            
    def has_close(self, line):
        for char in line:
            if char in self.close:
                return True
                
        return False
        
    def remove_easy(self, line):
        remove_index = []
        for index in range(len(line)):
            if line[index] in self.close:
                if self.is_match(line[index], line[index-1]):
                    remove_index.append(index)
        
        remove_index.reverse()        
        for index in remove_index:
            del line[index]
            del line[index-1]

        return line
        
    def illegal_char(self, line):
        for index in range(len(line)):
            if line[index] in self.close:
                if not self.is_match(line[index], line[index-1]):
                    if line[index-1] in self.start:
                        return line[index]
        
        return 0
            
    def illegal(self):
        for line in self.puzzle:
            not_found = 1
            while self.has_close(line) and not_found:
                line = self.remove_easy(line)
                val = self.illegal_char(line)
                if val != 0:
                    self.illegals.append(val)
                    not_found = 0
                    
    def calc_score(self):
        for i in self.illegals:
            if i == ')':
                self.score += 3
            if i == ']':
                self.score += 57
            if i == '}':
                self.score += 1197
            if i == '>':
                self.score += 25137
       

if __name__ == '__main__':
    N = Nav()
    N.illegal()
    N.calc_score()
    print(N.score)