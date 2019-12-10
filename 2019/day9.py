#!/usr/bin/python3

INPUT1 = 'data/day9'
TEST1 = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
TEST2 = '1102,34915192,34915192,7,4,7,99,0'
TEST3 = '104,1125899906842624,99'

with open(INPUT1) as f:
    data = f.read()


def parse1(data):
    codes = data.split(',')
    nums = []
    for item in codes:
        nums.append(int(item.strip()))
    for i in range(0, 9999999):
        nums.append(0)
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
def add(eip, data, modes, base):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 add")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    elif modes[1] == 2:
        p2 = data[base+p2]
    else:
        print("Error in mode 1 add")

    if modes[2] == 0:
        data[p3] = p1+p2
    elif modes[2] == 2:
        data[base+p3] = p1+p2
    else:
        print('Error in modes 2 add')

    return eip+4, data


#opcode = 2
def mul(eip, data, modes, base):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 mul")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    elif modes[1] == 2:
        p2 = data[base+p2]
    else:
        print("Error in mode 1 mul")

    if modes[2] == 0:
        data[p3] = p1*p2
    elif modes[2] == 2:
        data[base+p3] = p1*p2
    else:
        print("Error in modes 2 mul")

    return eip+4, data


#opcode = 3
def inp(eip, myin, data, modes, base):
    p1 = data[eip+1]
    if modes[0] == 0:
        data[p1] = myin
    elif modes[0] == 2:
        data[base+p1] = myin
    else:
        print("Error in mode 0 inp")

    return eip+2, data


#opcode = 4
def getout(eip, data, modes, base):
    p1 = data[eip+1]
    print(modes[0])
    try:
        if modes[0] == 0:
            out = data[p1]
        elif modes[0] == 1:
            out = p1
        elif modes[0] == 2:
            out = data[base+p1]
        else:
            print("Error in mode 0 getout")
    except IndexError:
        print(eip, modes, p1)

    return eip+2, out


#opcode = 5
def jit(eip, data, modes, base):
    p1 = data[eip+1]
    p2 = data[eip+2]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 jit")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    elif modes[1] == 2:
        p2 = data[base+p2]
    else:
        print("Error in mode 1 jit")

    if p1 != 0:
        return p2
    else:
        return eip+3


#opcode = 6
def jif(eip, data, modes, base):
    p1 = data[eip+1]
    p2 = data[eip+2]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 jif")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    elif modes[1] == 2:
        p2 = data[base+p2]
    else:
        print("Error in mode 1 jif")

    if p1 == 0:
        return p2
    else:
        return eip+3


#opcode = 7
def lt(eip, data, modes, base):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 lt")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    elif modes[1] == 2:
        p2 = data[base+p2]
    else:
        print("Error in mode 1 lt")

    if p1 < p2:
        if modes[2] == 0:
            data[p3] = 1
        elif modes[2] == 2:
            data[base+p3] = 1
        else:
            print("Error in mode 2 lt")
    else:
        if modes[2] == 0:
            data[p3] = 0
        elif modes[2] == 2:
            data[base+p3] = 0
        else:
            print("Error in mode 2 lt")

    return eip+4, data    


#opcode = 8
def eq(eip, data, modes, base):
    p1 = data[eip+1]
    p2 = data[eip+2]
    p3 = data[eip+3]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 eq")

    if modes[1] == 0:
        p2 = data[p2]
    elif modes[1] == 1:
        p2 = p2
    elif modes[1] == 2:
        p2 = data[base+p2]
    else:
        print("Error in mode 1 eq")

    if p1 == p2:
        if modes[2] == 0:
            data[p3] = 1
        elif modes[2] == 2:
            data[base+p3] = 1
        else:
            print("Error in mode 2 eq")
    else:
        if modes[2] == 0:
            data[p3] = 0
        elif modes[2] == 2:
            data[base+p3] = 0
        else:
            print("Error in mode 2 eq")

    return eip+4, data


#opcode = 9
def arbase(eip, data, modes, base):
    p1 = data[eip+1]

    if modes[0] == 0:
        p1 = data[p1]
    elif modes[0] == 1:
        p1 = p1
    elif modes[0] == 2:
        p1 = data[base+p1]
    else:
        print("Error in mode 0 arbase")

    return eip+2, base+p1


def comp(data, s):
    eip = 0
    saved = data
    base = 0

    while data[eip] != 99:
        op, modes = getmodes(data[eip])
        if op == 1:
            eip, data = add(eip, data, modes, base)
        elif op == 2:
            eip, data = mul(eip, data, modes, base)
        elif op == 3:
            eip, data = inp(eip, s, data, modes, base)
        elif op == 4:
            eip, out = getout(eip, data, modes, base)
            print(out)
            #return out
        elif op == 5:
            eip = jit(eip, data, modes, base)
        elif op == 6:
            eip = jif(eip, data, modes, base)
        elif op == 7:
            eip, data = lt(eip, data, modes, base)
        elif op == 8:
            eip, data = eq(eip, data, modes, base)
        elif op == 9:
            eip, base = arbase(eip, data, modes, base)

    #return data
    return out


def star1(data):
    mydata = parse1(data)
    #print(comp(mydata, 1))
    comp(mydata, 1)


def star2(data):
    mydata = parse1(data)
    comp(mydata, 2)


#star1(data)
star2(data)
