#!/usr/bin/python3

import pandas

INPUT1 = 'data/day3'
TEST1 = ' 5 10 25\n'
TEST2 = ' 101 301 501 \n 102 302 502 \n 103 303 503 \n 201 401 601 \n 202 402 602 \n 203 403 603 \n'

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    sides = []
    lines = data.split('\n')
    del lines[-1]
    for line in lines:
        line = line.split()
        sides.append((int(line[0].strip()), int(line[1].strip()), int(line[2].strip())))

    return sides

def parse2(data):
    rows = parse1(data)
    tmp = {
        'col1': [],
        'col2': [],
        'col3': []
    }
    for row in rows:
        tmp['col1'].append(row[0])
        tmp['col2'].append(row[1])
        tmp['col3'].append(row[2])

    return tmp
        

def istrig(data):
    #print(data)
    if data[0] + data[1] <= data[2]:
        return False
    elif data[1] + data[2] <= data[0]:
        return False
    elif data[2] + data[0] <= data[1]:
        return False
    else:
        return True

def star1(data):
    count = 0
    data = parse1(data)
    for item in data:
        if istrig(item):
            count += 1
    print(count)

def star2(data):
    count = 0
    data = parse2(data)
    mul = 0
    trip = []
    for key, val in data.items():
        mul = 0
        trip.clear()
        for item in val:
            if mul < 3:
                trip.append(item)
                mul += 1
            if mul == 3:
                if istrig(trip):
                    count += 1
                mul = 0
                trip.clear()

    print(count)

star1(data)
star2(data)
