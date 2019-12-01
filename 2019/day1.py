#!/usr/bin/python3
import math

INPUT1 = 'data/day1'
TEST1 = '14\n'
TEST2 = '1969\n'
TEST3 = '100756\n'

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    mass = []
    mydata = data.split('\n')
    del mydata[-1]
    for line in mydata:
        #print(line)
        mass.append(int(line.strip()))
    return mass
  

def calcmass(mass):
    return (math.floor(mass/3))-2

def calcfuel(mass):
    fuel = 0
    mass = calcmass(mass)
    while mass > 0:
        fuel = fuel + mass
        mass = calcmass(mass)

    return fuel

def star1(data):
    mass = parse1(data)
    sum = 0
    for item in mass:
        sum = sum + calcmass(item)

    print(sum)


def star2(data):
    mass = parse1(data)
    sum = 0
    for item in mass:
        sum = sum + calcfuel(item)

    print(sum)

star1(data)
star2(data)
