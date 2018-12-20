#!/usr/bin/python3
"""
"""
import sys
import time
from collections import defaultdict

INPUT = 'data/day19.txt'
TESTINPUT = 'data/day19test.txt'

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    myinput = TESTINPUT
else:
    myinput = INPUT

with open(myinput) as f:
    lines = f.readlines()
    data = [item.split() for item in lines[1:]]

#print(data)

d = defaultdict(list)

for i in range(len(lines)-1):
    d[i] = data[i]

#print(d)

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

ip = 1
ip_val = 0
#start = [0, 0, 0, 0, 0, 0]
start = [1, 0, 0, 0, 0, 0]
tmp = []
dispatcher = {'addr':addr, 'addi':addi, 'mulr':mulr, 'muli':muli,
              'banr':banr, 'bani':bani, 'borr':borr, 'bori':bori,
              'setr':setr, 'seti':seti, 'gtir':gtir, 'gtrr':gtrr,
              'eqir':eqir, 'eqri':eqri, 'eqrr':eqrr}

while ip < len(lines)-1:
    function = dispatcher[d[ip_val][0]]
    a, b, c = int(d[ip_val][1]), int(d[ip_val][2]), int(d[ip_val][3])
    tmp = function(start, a, b, c)
    print('ip={} {} {} {} {} {} {}'.format(ip_val, start, d[ip_val][0], a, b, c, tmp))
    ip_val = tmp[ip]+1
    start = tmp[:]
    start[1] = ip_val
    #time.sleep(5)
