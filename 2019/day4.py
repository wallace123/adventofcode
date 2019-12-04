#!/usr/bin/python3
from collections import Counter

INPUT1 = '387638-919123'
TEST1 = '111111'  # TRUE
TEST2 = '223450'  # FALSE
TEST3 = '123789'  # FALSE
TEST4 = '122345'  # TRUE

def parse1(data):
    nums = data.split('-')
    tmp = []
    if len(nums) == 2:
        for i in range(int(nums[0]), int(nums[1])+1):
            tmp.append(str(i))
    else:
        tmp = nums

    return tmp

def ispass(p):
    # check length 6
    if len(p) != 6:
        #print('Failed length test: ', p)
        return False
    
    # check double
    doub = False
    digcount = Counter(p)
    for i in digcount.values():
        if i > 1:
            doub = True
            break

    if not doub:
        #print('Failed double check: ', p)
        return False

    # check adjacent
    adj = False
    for i in range(0, len(p)+1):
        try:
            if p[i] == p[i+1]:
                adj = True
                break
        except IndexError:
            pass

    if not adj:
        #print('Failed adjacent check: ', p)
        return False

    # check never decrease
    for i in range(0, len(p)+1):
        try:
            if p[i] > p[i+1]:
                #print('Failed decrease check: ', p)
                return False
        except IndexError:
            pass

    return True


def ispass2(p):
    # check length 6
    if len(p) != 6:
        #print('Failed length test: ', p)
        return False
    
    # contains double
    doub = False
    digcount = Counter(p)
    for i in digcount.values():
        if i == 2:
            doub = True
            break

    if not doub:
        #print('Failed double check: ', p)
        return False

    # check adjacent
    adj = False
    for i in range(0, len(p)+1):
        try:
            if p[i] == p[i+1]:
                adj = True
                break
        except IndexError:
            pass

    if not adj:
        #print('Failed adjacent check: ', p)
        return False

    # check never decrease
    for i in range(0, len(p)+1):
        try:
            if p[i] > p[i+1]:
                #print('Failed decrease check: ', p)
                return False
        except IndexError:
            pass

    return True


def star1(data):
    mydata = parse1(data)
    count = 0
    for item in mydata:
        if ispass(item):
            count += 1

    print(count)

def star2(data):
    mydata = parse1(data)
    count = 0
    for item in mydata:
        if ispass2(item):
            count += 1

    print(count)

star1(INPUT1)
star2(INPUT1)
