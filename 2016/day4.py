#!/usr/bin/python3
import re
from collections import OrderedDict, Counter

INPUT1 = 'data/day4'
TEST1 = 'aaaaa-bbb-z-y-x-123[abxyz]\n' # Real
TEST2 = 'a-b-c-d-e-f-g-h-987[abcde]\n' # Real
TEST3 = 'not-a-real-room-404[oarel]\n' # Real
TEST4 = 'totally-real-room-200[decoy]\n' # Not Real

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    rooms = data.split('\n')
    del rooms[-1]
    return rooms

def rr(room):
    m = re.search(r"\[([a-z]+)\]", room)
    checksum = m.group(1)

    m = re.search(r"\-([0-9]+)\[", room)
    secid = m.group(1)

    lets = room.split('-')
    del lets[-1]
    str1 = ""
    str1 = str1.join(lets)

    c1 = Counter(str1)
    cs = c1.keys()
    cs = sorted(cs)
    cs = sorted(cs, key=lambda x: -c1[x])
    if ''.join(cs[:5]) == checksum:
        return int(secid)
    else:
        return 0

def star1(data):
    mydata = parse1(data)
    total = 0
    for item in mydata:
        total += rr(item)

    print(total)

def star2(data):
    pass

star1(data)
star2(data)    
    
