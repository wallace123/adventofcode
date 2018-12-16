#!/usr/bin/python3
"""
"""
import sys

INPUT = 'data/day15.txt'
TEST1 = 'data/day15test1.txt'

if len(sys.argv) > 1 and sys.argv[1] == 'test1':
    myinput = TEST1
else:
    myinput = INPUT

with open(myinput) as f:
    lines = [l.strip() for l in f.readlines()]

