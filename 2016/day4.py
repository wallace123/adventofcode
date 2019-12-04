#!/usr/bin/python3
import re
import string
from collections import OrderedDict, Counter

INPUT1 = 'data/day4'
TEST1 = 'aaaaa-bbb-z-y-x-123[abxyz]\n' # Real
TEST2 = 'a-b-c-d-e-f-g-h-987[abcde]\n' # Real
TEST3 = 'not-a-real-room-404[oarel]\n' # Real
TEST4 = 'totally-real-room-200[decoy]\n' # Not Real
TEST5 = 'qzmt-zixmtkozy-ivhz-343[nothh]\n' # very encrypted name

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

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def decrypt(room):
    code = ""
    for c in room:
        if c.isdigit():
            break
        code += c

    m = re.search(r"\-([0-9]+)\[", room)
    secid = int(m.group(1))

    shift = secid % 26

    d = caesar(code, shift)
    return d, secid


def star1(data):
    mydata = parse1(data)
    total = 0
    for item in mydata:
        total += rr(item)

    print(total)

def star2(data):
    mydata = parse1(data)
    for item in mydata:
        if 'north' in decrypt(item)[0]:
            print(decrypt(item))


star1(data)
star2(data)    
    
