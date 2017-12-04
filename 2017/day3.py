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

board_max = 10
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

def myfunc(input):
    steps = 0
    board = odd_sqr()
    for k,v in board.items():
        print(list(v[1]))
    return steps

#print(myfunc(test1) == answer1)
#print(myfunc(test2) == answer2)
#print(myfunc(test3) == answer3)
#print(myfunc(test4) == answer4)
print(myfunc(mypuz))
