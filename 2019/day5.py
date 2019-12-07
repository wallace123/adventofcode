#!/usr/bin/python3

INPUT1 = 'data/day5'

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    codes = data.split(',')
    nums = []
    for item in codes:
        nums.append(int(item.strip()))
    return nums


def getmodes(op):
    op = str(op)
    c = []
    for i in op:
        c.append(int(i))

    for i in range(len(c), 5):
        c.insert(0, 0)

    c.reverse()
    opcode = int(str(c[1]) + str(c[0]))
    c.pop(0)
    c.pop(0)
    return opcode, c

#opcode = 1
def add(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error")

    data[p3] = p1+p2

    return eip+4, data

#opcode = 2
def mul(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error")

    data[p3] = p1*p2

    return eip+4, data

#opcode = 3
def inp(eip, myin, data, modes):
    p1 = data[eip+1]
    data[p1] = myin

    return eip+2, data

#opcode = 4
def getout(eip, data, modes):
    p1 = data[eip+1]
    out = data[p1]

    return eip+2, out


#opcode = 5
def jit(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error")

    if modes[1] == 0:
        p2 == data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error")

    if p1 == 0:
        return eip+3
    else:
        return p2


#opcode = 6
def jif(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error")

    if modes[1] == 0:
        p2 == data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error")

    if p1 == 0:
        return p2
    else:
        return eip+3


#opcode = 7
def lt(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[1] == 1:
        p1 = p1
    else:
        print("Error")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1
        p2 = p2
    else:
        print("Error")

    if p1 < p2:
        data[p3] = 1
    else:
        data[p3] = 0

    return eip+4, data    


#opcode = 8
def eq(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[1] == 1:
        p1 = p1
    else:
        print("Error")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1
        p2 = p2
    else:
        print("Error")

    if p1 == p2:
        data[p3] = 1
    else:
        data[p3] = 0

    return eip+4, data    


def comp(data, myin):
    eip = 0
    while data[eip] != 99:
        op, modes = getmodes(data[eip])
        if op == 1:
            eip, data = add(eip, data, modes)
        elif op == 2:
            eip, data = mul(eip, data, modes)
        elif op == 3:
            eip, data = inp(eip, myin, data, modes)
        elif op == 4:
            eip, out = getout(eip, data, modes)
            print(out)
        elif op == 5:
            eip = 

    return data


def star1(data):
    mydata = parse1(data)
    mydata = comp(mydata, 1)


def star2(data):
    pass


star1(data)
star2(data)
