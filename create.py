#!/usr/bin/python3
"""Create file structure"""

import argparse
import os
import sys
import stat


def create_structure(mydir):
    for i in range(1, 26):
        myfile = os.path.join(mydir, 'day'+str(i)+'.py')
        f = open(myfile, 'w+')
        f.write('#!/usr/bin/python3\n')
        f.close()
        os.chmod(myfile, stat.S_IRWXU|stat.S_IRGRP)
    datadir = os.path.join(mydir, 'data')
    os.mkdir(datadir)
    

argparser = argparse.ArgumentParser()
argparser.add_argument("year", help="Advent of Code Year")
args = argparser.parse_args()

cwd = os.getcwd()
mydir = os.path.join(cwd, args.year)

if os.path.isdir(mydir):
    create_structure(mydir)
else:
    os.mkdir(mydir)
    create_structure(mydir)

print("done")

