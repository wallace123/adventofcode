#!/usr/bin/python3
"""
"""

INPUT1 = 'data/day16_1.txt'

with open(INPUT1) as f:
    data = f.read()

def parseday1(data):
    step1 = data.split('\n\n')
    step2 = [d.split('\n') for d in step1]
    data = []

    for item in step2:
        data.append(([int(d) for d in item[0] if d.isdigit()],
                     [int(d) for d in item[1].split()[1:]],
                     [int(d) for d in item[2] if d.isdigit()]))

    return data

def parseday2(data):
    step1 = data.split('\n\n')
    step2 = [d.split('\n') for d in step1]
    data = []

    for item in step2:
        data.append(([int(d) for d in item[0] if d.isdigit()],
                     [int(d) for d in item[1].split()],
                     [int(d) for d in item[2] if d.isdigit()]))

    return data

def addr(regs, a, b, c):
    # reg = [op, a, b, c]
    result = regs[:]
    result[c] = result[a] + result[b]
    return result

def addi(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] + b
    return result

def mulr(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] * result[b]
    return result

def muli(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] * b
    return result

def banr(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] & result[b]
    return result

def bani(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] & b
    return result

def borr(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] | result[b]
    return result

def bori(regs, a, b, c):
    result = regs[:]
    result[c] = result[a] | b
    return result

def setr(regs, a, b, c):
    result = regs[:]
    result[c] = result[a]
    return result

def seti(regs, a, b, c):
    result = regs[:]
    result[c] = a
    return result

def gtir(regs, a, b, c):
    result = regs[:]
    result[c] = int(bool(a > result[b]))
    return result

def gtri(regs, a, b, c):
    result = regs[:]
    result[c] = int(bool(result[a] > b))
    return result

def gtrr(regs, a, b, c):
    result = regs[:]
    result[c] = int(bool(result[a] > result[b]))
    return result

def eqir(regs, a, b, c):
    result = regs[:]
    result[c] = int(bool(a == result[b]))
    return result

def eqri(regs, a, b, c):
    result = regs[:]
    result[c] = int(bool(result[a] == b))
    return result

def eqrr(regs, a, b, c):
    result = regs[:]
    result[c] = int(bool(result[a] == result[b]))
    return result

ops = [addr, addi, mulr, muli, banr, bani, borr, bori,
       setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

mydata = parseday1(data)
success = 0
match = 0

for test in mydata:
    before = test[0]
    a, b, c = test[1][0], test[1][1], test[1][2]
    after = test[2]
    for op in ops:
        if op(before, a, b, c) == after:
            match += 1

    if match >= 3:
        success += 1
    match = 0

print("Part 1: {}".format(success))

#ops2 = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
#        'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

"""
used this code to get opcode mapping
mydata = parseday2(data)
opdict = {}

for op in ops:
    opdict[op] = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                  9, 10, 11, 12, 13, 14, 15]

for test in mydata:
    before = test[0]
    opcode = test[1][0]
    a, b ,c = test[1][1], test[1][2], test[1][3]
    after = test[2]
    for op in ops:
        if op(before, a, b, c) != after:
            if opcode in opdict[op]:
                opdict[op].remove(opcode)

for k, v in opdict.items():
    print(k, v)
"""

opdict = {}
opdict[0] = bani
opdict[1] = banr
opdict[2] = muli
opdict[3] = setr
opdict[4] = bori
opdict[5] = eqrr
opdict[6] = gtir
opdict[7] = mulr
opdict[8] = gtrr
opdict[9] = seti
opdict[10] = gtri
opdict[11] = eqri
opdict[12] = addi
opdict[13] = borr
opdict[14] = eqir
opdict[15] = addr

INPUT2 = 'data/day16_2.txt'
with open(INPUT2) as f:
    step1 = f.readlines()
    step2 = [d.split() for d in step1]
    mydata = []
    for item in step2:
        mydata.append(list(map(int, item)))
    
regs = [0, 0, 0, 0]

for line in mydata:
    opcode, a, b, c = line[0], line[1], line[2], line[3]
    regs = opdict[opcode](regs, a, b, c)

print("Part 2: {}".format(regs[0]))
