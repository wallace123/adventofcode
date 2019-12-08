#!/usr/bin/python3

from collections import Counter

INPUT1 = 'data/day8'
TEST1 = '0222112222120000'

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
    v = parse1(data)
    datasize = len(v)
    pix = 25*6
    #pix = 2*2
    layer = []
    layers = []
    tmp = []
    image = []

    for i in range(0, datasize+1):
        if (i==0) or (i%pix != 0):
            layer.append(v[i])
        else:
            layers.append(layer)
            if i < datasize:
                layer = [v[i]]

    for i in range(0, len(layers[0])):
        for l in layers:
            tmp.append(l[i])
        image.append(tmp)
        tmp = []

    decode = []
    for i in image:
        for p in i:
            if p == 0 or p == 1:
                decode.append(p)
                break

    #print(decode)
    out = ""
    for i in range(0, len(decode)):
        if (i==0) or (i%25 != 0):
            if decode[i] == 1:
                out += ' '
            else:
                out += '*'
        else:
            print(out)
            if i < len(decode):
                if decode[i] == 1:
                    out = ' '
                else:
                    out = '*'


star1(data)
star2(data)
