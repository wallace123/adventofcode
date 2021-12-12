#!/usr/bin/python3

class Octopus:
    def __init__(self):
        self.puzzle = self._parse_input()
        self.flashes = 0
        
    def _parse_input(self):
        with open('data/day11.txt', 'r') as infile:
            content = [line.rstrip() for line in infile]
        
        temp2 = []
        for line in content:
            temp = [int(num) for num in line]
            temp2.append(temp)
            
        return temp2
            
    def flash(self, index1, index2):
        #up
        try:
            if (index1-1) >= 0:
                self.puzzle[index1-1][index2] += 1
        except:
            pass
        
        #down     
        try:
            self.puzzle[index1+1][index2] += 1
        except:
            pass
        
        #left      
        try:
            if (index2-1) >= 0:
                self.puzzle[index1][index2-1] += 1
        except:
            pass

        #right       
        try:
            self.puzzle[index1][index2+1] += 1
        except:
            pass
       
        #up-left       
        try:
            if ((index1-1) >= 0) and ((index2-1) >= 0):
                self.puzzle[index1-1][index2-1] += 1
        except:
            pass
            
        #up-right      
        try:
            if (index1-1) >= 0:
                self.puzzle[index1-1][index2+1] += 1
        except:
            pass
            
        #down-left       
        try:
            if (index2-1) >= 0:
                self.puzzle[index1+1][index2-1] += 1
        except:
            pass
            
        #down-right     
        try:
            self.puzzle[index1+1][index2+1] += 1
        except:
            pass
                
    def step(self, i):
        for index1 in range(len(self.puzzle)):
            for index2 in range(len(self.puzzle[0])):
                self.puzzle[index1][index2] += 1
                
        flash_list = []
        before = -1
        
        while before < len(flash_list): 
            before = len(flash_list)        
            for index1 in range(len(self.puzzle)):
                for index2 in range(len(self.puzzle[0])):
                    if self.puzzle[index1][index2] > 9:
                        if (index1, index2) in flash_list:
                            pass
                        else:
                            flash_list.append((index1, index2))
                            self.flash(index1, index2)
        
        for index1 in range(len(self.puzzle)):
            for index2 in range(len(self.puzzle[0])):
                if self.puzzle[index1][index2] > 9:
                    self.puzzle[index1][index2] = 0
                    self.flashes += 1


if __name__ == '__main__':
    O = Octopus()
    for i in range(100):
        print(f'step {i+1}')
        O.step(i+1)
        for line in O.puzzle:
            nums = ''.join(str(e) for e in line)
            print(nums)
        print('\n')

    print(O.flashes)
    
    all_flash = '0000000000'
    count = 0
    O = Octopus()
    for i in range(300):
        O.step(i+1)
        for line in O.puzzle:
            nums = ''.join(str(e) for e in line)
            if nums == all_flash:
                count += 1
            if count == 10:
                print(f'All flash on step {i+1}!!!!!!!!!!!!!!!!')
        count = 0
        