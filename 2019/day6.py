#!/usr/bin/python3

INPUT1 = 'data/day6'
TEST1 = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L" # 42

with open(INPUT1) as f:
    data = f.read()


def parse1(data):
    items = data.split('\n')
    return items


def star1(data):
    mydata = parse1(data)
    print(mydata)


def star2(data):
    pass


star1(data)
star2(data)
