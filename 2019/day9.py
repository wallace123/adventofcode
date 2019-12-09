#!/usr/bin/python3

INPUT1 = 'data/day9'

with open(INPUT1) as f:
    data = f.read()


def parse1(data):
    codes = data.split(',')
    nums = []
    for item in codes:
        nums.append(int(item.strip()))
    return nums


def star1(data):
    mydata = parse1(data)
    print(mydata)


def star2(data):
    pass


star1(data)
star2(data)
