#!/usr/bin/python3
import io


INPUT1 = 'data/day6'
TEST1 = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L" # 42

with open(INPUT1) as f:
    data = f.read()


def parse1(data):
    items = io.StringIO(data)
    items = items.readlines()

    mylist = []
    for i in items:
        mylist.append((i.split(')')[0].strip(), i.split(')')[1].strip()))
    return mylist


def star1(data):
    mydata = parse1(data)
    print(mydata)


def star2(data):
    pass


star1(TEST1)
star2(data)
