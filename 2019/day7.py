#!/usr/bin/python3
from itertools import permutations

INPUT1 = 'data/day7'
TEST1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0' # 43210, 4,3,2,1,0
TEST2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0' # 54321, 0,1,2,3,4
TEST3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0' # 65210, 1,0,4,3,2

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
        print("Error in mode 0 add")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error in mode 1 add")

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
        print("Error in mode 0 mul")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error in mode 1 mul")

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
    try:
        out = data[p1]
    except IndexError:
        print(eip, modes, p1)

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
        print("Error in mode 0 jit")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error in mode 1 jit")

    if p1 != 0:
        return p2
    else:
        return eip+3


#opcode = 6
def jif(eip, data, modes):
    p1 = data[eip+1]
    p2 = data[eip+2]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error in mode 0 jif")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error in mode 1 jif")

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
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error in mode 0 lt")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error in mode 1 lt")

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
    elif modes[0] == 1:
        p1 = p1
    else:
        print("Error in mode 0 eq")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    else:
        print("Error in mode 1 eq")

    if p1 == p2:
        data[p3] = 1
    else:
        data[p3] = 0

    return eip+4, data    



def comp(data, f, s):
    eip = 0
    count = 0
    saved = data
    while count <= 2:
        #eip = 0
        #data = saved
        while data[eip] != 99:
            op, modes = getmodes(data[eip])
            if op == 1:
                eip, data = add(eip, data, modes)
            elif op == 2:
                eip, data = mul(eip, data, modes)
            elif op == 3:
                count += 1
                if count == 1:
                    eip, data = inp(eip, f, data, modes)
                elif count == 2:
                    eip, data = inp(eip, s, data, modes)
                else:
                    print("Third input?")
            elif op == 4:
                eip, out = getout(eip, data, modes)
                #print(out)
                return out
            elif op == 5:
                eip = jit(eip, data, modes)
            elif op == 6:
                eip = jif(eip, data, modes)
            elif op == 7:
                eip, data = lt(eip, data, modes)
            elif op == 8:
                eip, data = eq(eip, data, modes) 

    #return data
    return out


def star1(data):
    mydata = parse1(data)
    perm = permutations([0,1,2,3,4])
    sig = 0
    for i in perm:
        # A
        nsig = comp(mydata, i[0], 0)
        print("A: ", nsig)
        # B
        nsig = comp(mydata, i[1], nsig)
        print("B: ", nsig)
        # C
        nsig = comp(mydata, i[2], nsig)
        print("C: ", nsig)
        # D
        nsig = comp(mydata, i[3], nsig)
        print("D: ", nsig)
        # E
        nsig = comp(mydata, i[4], nsig)
        print("E: ", nsig)

        if nsig > sig:
            sig = nsig

    print(sig)
        


def star2(data):
    #mydata = parse1(data)
    #mydata = comp(mydata, 5)
    pass


star1(data)
star2(data)
