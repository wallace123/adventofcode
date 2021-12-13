#!/usr/bin/python3
from collections import defaultdict

class Cave:
    def __init__(self):
        self.puzzle = defaultdict(list)
        self.count = 0
        
    def _parse_input(self):
        with open('data/day12.txt', 'r') as infile:
            content = infile.read().rstrip().split('\n')
            
        for con in content:
            data = con.split('-')
            self.puzzle[data[0]] = []
            self.puzzle[data[1]] = []
            
        for con in content:
            data = con.split('-')
            self.puzzle[data[0]].append(data[1])
            self.puzzle[data[1]].append(data[0])
            
    def printAllPathsUtil(self, u, d, visited, path):
        if u.islower():
            visited[u] = True
        path.append(u)
        
        if u == d:
            print(path)
            self.count += 1
        else:
            for i in self.puzzle[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
                    
        path.pop()
        visited[u] = False
        
    def printAllPaths(self, s, d):
        self._parse_input()
        visited = {}
        for key in self.puzzle.keys():
            visited[key] = False
        path = []
        self.printAllPathsUtil(s, d, visited, path)
        
        
if __name__ == '__main__':
    C = Cave()
    C.printAllPaths('start', 'end')
    print(C.count)