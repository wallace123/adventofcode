#!/usr/bin/python3

INPUT1 = 'data/day2'
TEST1 = '1,0,0,0,99' # 2,0,0,0,99
TEST2 = '2,3,0,3,99' # 2,3,0,6,99
TEST3 = '2,4,4,5,99,0' # 2,4,4,5,99,9801
TEST4 = '1,1,1,4,99,5,6,0,99' # 30,1,1,4,2,5,6,0,99

with open(INPUT1) as f:
    data = f.read()

def parse1(data):
    codes = data.split(',')
    nums =[]
    for item in codes:
        nums.append(int(item.strip()))
    return nums

def comp(data):
    i = 0
    while data[i] != 99:
        if data[i] == 1:
            pos1 = data[i+1]
            pos2 = data[i+2]
            pos3 = data[i+3]
            dsum = data[pos1] + data[pos2]
            data[pos3] = dsum
            i += 4
        elif data[i] == 2:
            pos1 = data[i+1]
            pos2 = data[i+2]
            pos3 = data[i+3]
            dmul = data[pos1] * data[pos2]
            data[pos3] = dmul
            i += 4
    return data
            
def prep1(data):
    data[1] = 12
    data[2] = 2
    return data

def prep2(data, noun, verb):
    data[1] = noun
    data[2] = verb
    return data

def star1(data):
    mydata = parse1(data)
    mydata = prep1(mydata)
    mydata = comp(mydata)
    print(mydata[0])
    

def star2(data):
    mydata = parse1(data)
    found = False
    for i in range(0, 99):
        for j in range(0, 99):
            mydata = prep2(mydata, i, j)
            mydata = comp(mydata)
            if mydata[0] == 19690720:
            #if mydata[0] == 11590668:
                found = True
                print((100*i)+j)
                break
            else:
                mydata = parse1(data)
        if found == True:
            break
        else:
            mydata = parse1(data)
    

star1(data)
star2(data)
