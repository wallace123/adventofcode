#!/usr/bin/python3
"""
"""
import sys
import copy

INPUT = 'data/day18.txt'
TESTINPUT = 'data/day18test.txt'

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    myinput = TESTINPUT
else:
    myinput = INPUT

with open(myinput) as f:
    data = [list(line.strip()) for line in f.readlines()]

TR = '|' # TREE
OA = '.' # Open Acre
LY = '#' # Lumberyard

def oa2tr(y, x, grid):
    count = 0
    
    if y - 1 >= 0 and x - 1 >= 0:
        if grid[y-1][x-1] == TR:
            count += 1
    if y - 1 >= 0:
        if grid[y-1][x] == TR:
            count += 1
    if y - 1 >= 0 and x + 1 <= len(grid[0])-1:
        if grid[y-1][x+1] == TR:
            count += 1
    if x + 1 <= len(grid[0])-1:
        if grid[y][x+1] == TR:
            count += 1
    if y + 1 <= len(grid)-1 and x + 1 <= len(grid[0])-1:
        if grid[y+1][x+1] == TR:
            count += 1
    if y + 1 <= len(grid)-1:
        if grid[y+1][x] == TR:
            count += 1
    if y + 1 <= len(grid)-1 and x - 1 >= 0:
        if grid[y+1][x-1] == TR:
            count += 1
    if x - 1 >= 0:
        if grid[y][x-1] == TR:
            count += 1

    if count >= 3:
        return True
    else:
        return False

def tr2ly(y, x, grid):
    count = 0

    if y - 1 >= 0 and x - 1 >= 0:
        if grid[y-1][x-1] == LY:
            count += 1
    if y - 1 >= 0:
        if grid[y-1][x] == LY:
            count += 1
    if y - 1 >= 0 and x + 1 <= len(grid[0])-1:
        if grid[y-1][x+1] == LY:
            count += 1
    if x + 1 <= len(grid[0])-1:
        if grid[y][x+1] == LY:
            count += 1
    if y + 1 <= len(grid)-1 and x + 1 <= len(grid[0])-1:
        if grid[y+1][x+1] == LY:
            count += 1
    if y + 1 <= len(grid)-1:
        if grid[y+1][x] == LY:
            count += 1
    if y + 1 <= len(grid)-1 and x - 1 >= 0:
        if grid[y+1][x-1] == LY:
            count += 1
    if x - 1 >= 0:
        if grid[y][x-1] == LY:
            count += 1

    if count >= 3:
        return True
    else:
        return False

def ly2ly(y, x, grid):
    lycount = 0
    trcount = 0

    if y - 1 >= 0 and x - 1 >= 0:
        if grid[y-1][x-1] == LY:
            lycount += 1
        if grid[y-1][x-1] == TR:
            trcount += 1
    if y - 1 >= 0:
        if grid[y-1][x] == LY:
            lycount += 1
        if grid[y-1][x] == TR:
            trcount += 1
    if y - 1 >= 0 and x + 1 <= len(grid[0])-1:
        if grid[y-1][x+1] == LY:
            lycount += 1
        if grid[y-1][x+1] == TR:
            trcount += 1
    if x + 1 <= len(grid[0])-1:
        if grid[y][x+1] == LY:
            lycount += 1
        if grid[y][x+1] == TR:
            trcount += 1
    if y + 1 <= len(grid)-1 and x + 1 <= len(grid[0])-1:
        if grid[y+1][x+1] == LY:
            lycount += 1
        if grid[y+1][x+1] == TR:
            trcount += 1
    if y + 1 <= len(grid)-1:
        if grid[y+1][x] == LY:
            lycount += 1
        if grid[y+1][x] == TR:
            trcount += 1
    if y + 1 <= len(grid)-1 and x - 1 >= 0:
        if grid[y+1][x-1] == LY:
            lycount += 1
        if grid[y+1][x-1] == TR:
            trcount += 1
    if x - 1 >= 0:
        if grid[y][x-1] == LY:
            lycount += 1
        if grid[y][x-1] == TR:
            trcount += 1

    if lycount >= 1 and trcount >= 1:
        return True
    else:
        return False

def printgrid(grid):
    for item in grid:
        print(''.join(item))


for i in range(1000000000):
    tmp = copy.deepcopy(data)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if tmp[y][x] == OA:
                if oa2tr(y, x, tmp):
                    data[y][x] = TR
            if tmp[y][x] == TR:
                if tr2ly(y, x, tmp):
                    data[y][x] = LY
            if tmp[y][x] == LY:
                if not ly2ly(y, x, tmp):
                    data[y][x] = OA

trcount = 0
lycount = 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == TR:
            trcount += 1
        elif data[y][x] == LY:
            lycount += 1

print('TR = {}, LY = {}\nResource Value = {}'.format(trcount, lycount, trcount*lycount))
