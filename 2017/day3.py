"""
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 312051.
"""
import math

board_max = 700
test1 = 1
test2 = 12
test3 = 23
test4 = 1024
mypuz = 312051

answer1 = 0
answer2 = 3
answer3 = 2
answer4 = 31

def odd_sqr():
    sqr_dict = {}
    cell = 0
    for i in range(1, board_max, 2):
        sqr = i*i
        sqr_dict[sqr] = [(cell, -cell), range((sqr+1) - (8*cell) , sqr+1)]
        cell += 1

    return sqr_dict

board = odd_sqr()

def find_cell(num, key, value):
    sqr_cell = value[0]
    mov = int(math.sqrt(key)) - 1
    bot = range((key-mov)+1, key+1)
    #print(list(bot))
    left = range((key-(2*mov))+1, (key-mov)+1)
    #print(list(left))
    top = range((key-(3*mov))+1, (key-(2*mov))+1)
    #print(list(top))
    right = range((key-(4*mov))+1, (key-(3*mov))+1)
    #print(list(right))
    x = 0
    y = 0

    if num in bot:
        print("%d in bot" % num)
        pos = bot[int(len(bot)/2):]
        neg = bot[:int(len(bot)/2)]
        if num in pos:
            print("%d in pos" % num)
        elif num in neg:
            print("%d in neg" % num)
            print(list(neg))
            y = value[0][1]
            rev_neg = list(reversed(list(neg)))
            print(rev_neg)
            x = -(rev_neg.index(num))
    elif num in left:
        print("%d in left" % num)
        print(len(left))
    elif num in top:
        print("%d in top" % num)
        print(len(top))
    elif num in right:
        print("%d in right" % num)
        print(len(right))

    return x, y

def myfunc(input):
    steps = 0
    x = 0
    y = 0
    for k,v in board.items():
        if input in list(v[1]):
            (x,y)  = find_cell(input, k, v)
            print((x,y))
    steps = abs(x) + abs(y)
    print(steps)
    return steps

#print(myfunc(test1) == answer1)
#print(myfunc(test2) == answer2)
print(myfunc(test3) == answer3)
#print(myfunc(test4) == answer4)
print(myfunc(mypuz))
