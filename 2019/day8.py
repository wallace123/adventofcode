#!/usr/bin/python3

from collections import Counter

INPUT1 = 'data/day8'

with open(INPUT1) as f:
    data = f.read()


def parse1(data):
    nums = data.strip()
    r = []
    for c in nums:
        r.append(int(c))

    return r


def star1(data):
    v = parse1(data)
    datasize = len(v)
    pix = 25*6
    layer = []
    d = {0: 10000000}

    for i in range(0, datasize+1):
        if (i == 0) or (i%pix != 0):
            layer.append(v[i])
        else:
            dc = Counter(layer)
            if dc[0] < d[0]:
                d = dc
            if i < datasize:
                layer = [v[i]]

    print(d[1]*d[2])
            


def star2(data):
    pass


star1(data)
star2(data)
