#!/usr/bin/env python3

from Squasher import squash
import re
import sys
import subprocess


args = sys.argv

# Add one file and commit/commit and push 
if args[1] == '-f' and args[2] != '-p':
    index = args.index('-f')
    squash.addFileAndCommit(args, index)

elif (re.search('-fp', arg) for arg in args) or (re.search('pf', arg) for arg in args):
    for arg in args:
        match1 = re.findall('-fp', arg)
        match2 = re.findall('-pf', arg)
    
    if match1:
        index1= args.index('-pf')
        squash.addFileAndCommit(args, index1)
        squash.push()
    elif match2:
        index2 = args.index('-fp')
        squash.addFileAndCommit(args, index2)
        

# Add all files and commit/commit and push
if args[1] == '-a':
    index = args.index('-a')
    squash.addAllAndCommit(args, index)

elif (re.search('-ap', arg) for arg in args) or (re.search('pa', arg) for arg in args):
    for arg in args:
        match1 = re.findall('-ap', arg)
        match2 = re.findall('-pa', arg)
    
    if match1:
        index1= args.index('-pa')
        squash.addFileAndCommit(args, index1)
        squash.push()
    elif match2:
        index2 = args.index('-ap')
        squash.addFileAndCommit(args, index2)
        squash.push()
            