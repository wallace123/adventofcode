#!/usr/bin/python3

INPUT1 = 'data/day2'
TEST1 = "ULL\nRRDDD\nLURDL\nUUUUD\n"

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    directions = []
    for char in data:
        directions.append(char)
    return directions

def move(s, d):
    if s == 1 and ((d == 'U') or (d == 'L')):
        return 1
    elif s == 1 and d == 'D':
        return 4
    elif s == 1 and d == 'R':
        return 2
    elif s == 2 and d == 'U':
        return 2
    elif s == 2 and d == 'D':
        return 5
    elif s == 2 and d == 'L':
        return 1
    elif s == 2 and d == 'R':
        return 3
    elif s == 3 and ((d == 'U') or (d == 'R')):
        return 3
    elif s == 3 and d == 'D':
        return 6
    elif s == 3 and d == 'L':
        return 2
    elif s == 4 and d == 'U':
        return 1
    elif s == 4 and d == 'D':
        return 7
    elif s == 4 and d == 'R':
        return 5
    elif s == 4 and d == 'L':
        return 4
    elif s == 5 and d == 'U':
        return 2
    elif s == 5 and d == 'D':
        return 8
    elif s == 5 and d == 'R':
        return 6
    elif s == 5 and d == 'L':
        return 4
    elif s == 6 and d == 'U':
        return 3
    elif s == 6 and d == 'D':
        return 9
    elif s == 6 and d == 'R':
        return 6
    elif s == 6 and d == 'L':
        return 5
    elif s == 7 and d == 'U':
        return 4
    elif s == 7 and ((d == 'D') or (d == 'L')):
        return 7
    elif s == 7 and d == 'R':
        return 8
    elif s == 8 and d == 'U':
        return 5
    elif s == 8 and d == 'D':
        return 8
    elif s == 8 and d == 'R':
        return 9
    elif s == 8 and d == 'L':
        return 7
    elif s == 9 and d == 'U':
        return 6
    elif s == 9 and ((d == 'D') or (d == 'R')):
        return 9
    elif s == 9 and d == 'L':
        return 8

def move2(s, d):
    if s == 1 and ((d == 'U') or (d == 'R') or (d == 'L')):
        return 1
    elif s == 1 and d == 'D':
        return 3
    elif s == 2 and ((d == 'U') or (d == 'L')):
        return 2
    elif s == 2 and d == 'R':
        return 3
    elif s == 2 and d == 'D':
        return 6
    elif s == 3 and d == 'U':
        return 1
    elif s == 3 and d == 'D':
        return 7
    elif s == 3 and d == 'R':
        return 4
    elif s == 3 and d == 'L':
        return 2
    elif s == 4 and ((d == 'U') or (d == 'R')):
        return 4
    elif s == 4 and d == 'D':
        return 8
    elif s == 4 and d == 'L':
        return 3
    elif s == 5 and ((d == 'U') or (d == 'D') or (d == 'L')):
        return 5
    elif s == 5 and d == 'R':
        return 6
    elif s == 6 and d == 'U':
        return 2
    elif s == 6 and d == 'D':
        return 'A'
    elif s == 6 and d == 'R':
        return 7
    elif s == 6 and d == 'L':
        return 5
    elif s == 7 and d == 'U':
        return 3
    elif s == 7 and d == 'D':
        return 'B'
    elif s == 7 and d == 'R':
        return 8
    elif s == 7 and d == 'L':
        return 6
    elif s == 8 and d == 'U':
        return 4
    elif s == 8 and d == 'D':
        return 'C'
    elif s == 8 and d == 'R':
        return 9
    elif s == 8 and d == 'L':
        return 7
    elif s == 9 and ((d == 'U') or (d == 'R') or (d == 'D')):
        return 9
    elif s == 9 and d == 'L':
        return 8
    elif s == 'A' and ((d == 'L') or (d == 'D')):
        return 'A'
    elif s == 'A' and d == 'U':
        return 6
    elif s == 'A' and d == 'R':
        return 'B'
    elif s == 'B' and d == 'U':
        return 7
    elif s == 'B' and d == 'D':
        return 'D'
    elif s == 'B' and d == 'R':
        return 'C'
    elif s == 'B' and d == 'L':
        return 'A'
    elif s == 'C' and ((d == 'R') or (d == 'D')):
        return 'C'
    elif s == 'C' and d == 'U':
        return 8
    elif s == 'C' and d == 'L':
        return 'B'
    elif s == 'D' and ((d == 'L') or (d == 'D') or (d == 'R')):
        return 'D'
    elif s == 'D' and d == 'U':
        return 'B'

def star1(data):
    start = 5
    code = []
    for direction in parse1(data):
        if direction == '\n':
            code.append(start)
            continue
        start = move(start, direction)

    print(code)

def star2(data):
    start = 5
    code = []
    for direction in parse1(data):
        if direction == '\n':
            code.append(start)
            continue
        start = move2(start, direction)

    print(code)

star1(data)
star2(data)
