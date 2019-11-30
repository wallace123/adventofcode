#!/usr/bin/python3

INPUT1 = 'data/day1'

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    tmp = []
    directions = data.split(',')
    for item in directions:
        tmp.append(item.strip())
    tmp2 = []
    for item in tmp:
        tmp2.append((item[0], int(item[1:])))
    return tmp2

def walk(start, t):
    if start[0] == 'N' and t[0] == 'R':
        return ('E', (start[1][0], start[1][1]+t[1]))
    elif start[0] == 'N' and t[0] == 'L':
        return ('W', (start[1][0], start[1][1]-t[1]))
    elif start[0] == 'E' and t[0] == 'R':
        return ('S', (start[1][0]-t[1], start[1][1]))
    elif start[0] == 'E' and t[0] == 'L':
        return ('N', (start[1][0]+t[1], start[1][1]))
    elif start[0] == 'W' and t[0] == 'R':
        return ('N', (start[1][0]+t[1], start[1][1]))
    elif start[0] == 'W' and t[0] == 'L':
        return ('S', (start[1][0]-t[1], start[1][1]))
    elif start[0] == 'S' and t[0] == 'R':
        return ('W', (start[1][0], start[1][1]-t[1]))
    elif start[0] == 'S' and t[0] == 'L':
        return ('E', (start[1][0], start[1][1]+t[1]))

test1 = "R2, L3"
test2 = "R2, R2, R2"
test3 = "R5, L5, R5, R3"

def star1(data):
    start = ('N', (0, 0))
    directions = parse1(data)
    for item in directions:
        start = walk(start, item)

    print(start, abs(start[1][0])+abs(start[1][1]))


test4 = "R8, R4, R4, R8"
def star2(data):
    start = ('N', (0, 0))
    directions = parse1(data)
    visit = [(0, 0)]
    for item in directions:
        start = walk(start, item)
        if (visit[-1][0] != start[1][0]) and (start[0] == 'N'):
            for i in range(visit[-1][0]+1, start[1][0]+1):
                coord = (i, visit[-1][1])
                if coord in visit:
                    print(coord, abs(coord[0])+abs(coord[1]))
                    return 
                visit.append((i, visit[-1][1]))
        elif (visit[-1][0] != start[1][0]) and (start[0] == 'S'):
            for i in reversed(range(start[1][0], visit[-1][0])):
                coord = (i, visit[-1][1])
                if coord in visit:
                    print(coord, abs(coord[0])+abs(coord[1]))
                    return 
                visit.append((i, visit[-1][1]))
        if (visit[-1][1] != start[1][1]) and (start[0] == 'E'):
            for i in range(visit[-1][1]+1, start[1][1]+1):
                coord = (visit[-1][0], i)
                if coord in visit:
                    print(coord, abs(coord[0])+abs(coord[1]))    
                    return
                visit.append((visit[-1][0], i))
        if (visit[-1][1] != start[1][1]) and (start[0] == 'W'):
            for i in reversed(range(start[1][1], visit[-1][1])):
                coord = (visit[-1][0], i)
                if coord in visit:
                    print(coord, abs(coord[0])+abs(coord[1]))   
                    return 
                visit.append((visit[-1][0], i))

    print("messed up")

star1(data)
star2(data)
