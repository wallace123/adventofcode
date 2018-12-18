#!/usr/bin/python3
"""
"""
import sys
import numpy
from collections import OrderedDict
from operator import itemgetter

INPUT = 'data/day17.txt'
TESTINPUT = 'data/day17test.txt'

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    myinput = TESTINPUT
else:
    myinput = INPUT


claypoints = []
x = 0
y = 0

with open(myinput) as f:
    lines = f.readlines()
    for line in lines:
        first = line.split(',')[0]
        second = line.split(',')[1].strip()
        if 'x' in first:
            x = int(first.split('=')[1])
        elif 'y' in first:
            y = int(first.split('=')[1])
        if 'x' in second:
            rag = second.split('=')[1]
            start = int(rag.split('..')[0])
            end = int(rag.split('..')[1])
            for i in range(start, end+1):
                claypoints.append((i, y))
        elif 'y' in second:
            rag = second.split('=')[1]
            start = int(rag.split('..')[0])
            end = int(rag.split('..')[1])
            for i in range(start, end+1):
                claypoints.append((x, i))

claypoints = list(OrderedDict.fromkeys(claypoints))
min_x = min(claypoints, key=itemgetter(0))[0]
max_x = max(claypoints, key=itemgetter(0))[0]
min_y = min(claypoints, key=itemgetter(1))[1]
max_y = max(claypoints, key=itemgetter(1))[1]

print(claypoints)
print(min_x, max_x, min_y, max_y)

a = numpy.full((max_y+1, max_x+1), 0)

for point in claypoints:
    a[point[1]][point[0]] = 1

a[0][500] = 2

numpy.savetxt('myarray.csv', a, delimiter=',')
