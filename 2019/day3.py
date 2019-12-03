#!/usr/bin/python3
import operator

INPUT1 = 'data/day3'
TEST1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\n'\
        'U62,R66,U55,R34,D71,R55,D58,R83' # 159, 610
TEST2 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n'\
        'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7' # 135, 410

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    w1 = []
    w2 = []
    t1 = data.split('\n')[0].split(',')
    t2 = data.split('\n')[1].split(',')

    for d in t1:
        w1.append((d[0], int(d[1:])))
   
    for d in t2:
        w2.append((d[0], int(d[1:])))
    return w1, w2

def getpoints(wire):
    s = (0, 0)
    p = []
    for d in wire:
        if d[0] == 'U':
            dis = s[1]+d[1]
            for i in range(s[1], dis+1):
                p.append((s[0], i))
            s = (s[0], dis)
        elif d[0] == 'D':
            dis = s[1]-d[1]
            for i in reversed(range(dis, s[1]+1)):
                p.append((s[0], i))
            s = (s[0], dis)
        elif d[0] == 'R':
            dis = s[0]+d[1]
            for i in range(s[0], dis+1):
                p.append((i, s[1]))
            s = (dis, s[1])
        elif d[0] == 'L':
            dis = s[0]-d[1]
            for i in reversed(range(dis, s[0]+1)):
                p.append((i, s[1]))
            s = (dis, s[1])

    return p

def md(p):
    return abs(p[0]) + abs(p[1])

def getintersection(p1, p2):
    return set(p1) & set(p2)

def steps(wire, inter):
    s = (0, 0)
    p = {}
    count = 0
    for d in wire:
        if d[0] == 'U':
            dis = s[1]+d[1]
            for i in range(s[1], dis+1):
                count += 1
                if ((s[0], i) in inter) and ((s[0], i) not in p.keys()):
                    p[(s[0], i)] = count
            s = (s[0], dis)
            count -= 1
        elif d[0] == 'D':
            dis = s[1]-d[1]
            for i in reversed(range(dis, s[1]+1)):
                count += 1
                if ((s[0], i) in inter) and ((s[0], i) not in p.keys()):
                    p[(s[0], i)] = count
            s = (s[0], dis)
            count -= 1
        elif d[0] == 'R':
            dis = s[0]+d[1]
            for i in range(s[0], dis+1):
                count += 1
                if ((i, s[1]) in inter) and ((i, s[1]) not in p.keys()):
                    p[(i, s[1])] = count
            s = (dis, s[1])
            count -= 1
        elif d[0] == 'L':
            dis = s[0]-d[1]
            for i in reversed(range(dis, s[0]+1)):
                count += 1
                if ((i, s[1]) in inter) and ((i, s[1]) not in p.keys()):
                    p[(i, s[1])] = count
            s = (dis, s[1])
            count -= 1

    return p

def md(p):
    return abs(p[0]) + abs(p[1])

def getintersection(p1, p2):
    return set(p1) & set(p2)


def star1(data):
    mydata = parse1(data)
    points1 = getpoints(mydata[0])
    points1 = list(set(points1))
    points2 = getpoints(mydata[1])
    points2 = list(set(points2))

    dups = set(points1) & set(points2)
   
    dis = [] 
    for p in dups:
        if p == (0, 0):
            continue
        else:
            dis.append(md(p))

    dis.sort()
    print(dis[0])   


def star2(data):
    mydata = parse1(data)
    points1 = getpoints(mydata[0])
    points1 = list(set(points1))
    points2 = getpoints(mydata[1])
    points2 = list(set(points2))

    intersects = getintersection(points1, points2)
    intersects.remove((0, 0))

    step1 = steps(mydata[0], intersects)
    step2 = steps(mydata[1], intersects)

    step_list = []
    for i in intersects:
        step_list.append((i, step1[i] + step2[i]))

    step_list.sort(key = operator.itemgetter(1))
    print(step_list[0][1]-2) # unsure why off by 2
    

star1(data)
star2(data) 
