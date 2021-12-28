#!/usr/bin/python3

class BITS:
    def __init__(self):
        self.packet = ''
        self.version = 0
        self.typeID = 0
        self.lvalue = 0
        self.ltypeID = 0
        self.index = 0
        self.versions = []
        
    def _parse_input(self):
        with open('data/day16.txt', 'r') as infile:
            content = infile.read().rstrip()
        
        for char in content:
            num  = format(int(char, 16), 'b')
            while len(num) % 4 != 0:
                num  = '0' + num
            self.packet += num
            
    def literal(self):
        lead = 1
        tmpstr = ''
        
        while lead:
            lead = int(self.packet[self.index], 2)
            self.index += 1
            tmpstr += self.packet[self.index: self.index+4]
            self.index += 4
            
        self.lvalue = int(tmpstr, 2)
        print(self.lvalue)
        
    def operator(self):
        self.ltypeID = int(self.packet[self.index], 2)
        self.index += 1
        
        if self.ltypeID == 0:
            length = int(self.packet[self.index: self.index+15], 2)
            self.index += 15
            stop = self.index + length
            while self.index < stop:
                self.parse_packet()
        else:
            length = int(self.packet[self.index: self.index+11], 2)
            self.index += 11
            for _ in range(length):
                self.parse_packet()
                
    def parse_packet(self):
        #self._parse_input()
        #print(self.packet)

        self.version = int(self.packet[self.index: self.index+3], 2)
        self.versions.append(self.version)
        self.index += 3
        self.typeID = int(self.packet[self.index: self.index+3], 2)
        self.index += 3
        
        #print(f'index {self.index}, length {len(self.packet[self.index:])}')
        
        if len(self.packet[self.index:]) < 6:
            return
        elif self.typeID == 4:
            self.literal()
        else:
            self.operator()
            
    def add_versions(self):
        total = 0
        for v in self.versions:
            total += v
            
        print(f'Version total: {total}')
        
        
if __name__ == '__main__':
    B = BITS()
    B._parse_input()
    print(B.packet)
    B.parse_packet()
    B.add_versions()