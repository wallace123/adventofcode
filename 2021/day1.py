#!/usr/bin/python3
with open('data/day1.txt') as input:
    data = input.readlines()
    
puzzle = []
for line in data:
    puzzle.append(int(line.strip()))
    
count = 0
for num in range(len(puzzle)):
    try:
        if puzzle[num] < puzzle[num+1]:
            count += 1
    except:
        pass
        
print(count)

count = 0
for num in range(len(puzzle)):
    try:
        first = puzzle[num] + puzzle[num+1] + puzzle[num+2]
        second = puzzle[num+1] + puzzle[num+2] + puzzle[num+3]
        if first < second:
            count += 1
        first = 0
        second = 0
    except:
        pass

print(count)