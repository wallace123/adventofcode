#!/usr/bin/python3
import copy

class Bingo:
    def __init__(self):
        self.numbers = []
        self.played_numbers = []
        self.boards = {}
        self.win = {}
        self._parse_input()
        
    def _parse_input(self):
        with open('data/day4.txt', 'r') as infile:
            content = infile.read().rstrip()
            content = content.split('\n\n')
            
        for index in range(len(content)):
            if index == 0:
                self.numbers = content[index].split(',')
            else:
                self.boards[index] = content[index].split('\n')
                tmp_list = []
                for item in self.boards[index]:
                    tmp_list.append(item.lstrip().split())
                self.boards[index] = tmp_list
    
    def column(self, matrix, i):
        return [row[i] for row in matrix]
        
    def winning_numbers(self):
        self.win = copy.deepcopy(self.boards)
        
        for board in self.win.keys():
            for index in range(len(self.boards[board][0])):
                self.win[board].append(self.column(self.boards[board], index))
                
    def play(self):
        cols = len(self.boards[1][0])
        self.winning_numbers()
        keys = self.win.keys()
        for num in self.numbers:
            for board in keys:
                for index in range(cols):
                    if num in self.win[board][index]:
                        self.win[board][index].remove(num)
                        continue
                        
            self.played_numbers.append(num)
            
            for board in keys:
                for row_col in self.win[board]:
                    if len(row_col) == 0:
                        for pnum in self.played_numbers:
                            for index in range(cols):
                                try:
                                    self.boards[board][index].remove(pnum)
                                except:
                                    pass
                        return(board)
                        
    def calc_score(self):
        winner = self.play()
        last_num = self.played_numbers[-1]
        psum = 0
        for row_col in self.boards[winner]:
            for num in row_col:
                psum += int(num)
                
        print(psum * int(last_num))
        

if __name__ == '__main__':
    b = Bingo()
    b.calc_score()